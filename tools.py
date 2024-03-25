# odds and ends that help 

import random, csv, inspect, functools, time, math
from collections import namedtuple
from params import DEBUG_LVL
from icecream import ic
import currency

ic.configureOutput( prefix='' )

def debugger( threshold, *args ):
    if DEBUG_LVL < threshold and args:
        return args
    elif threshold <= DEBUG_LVL:
        if not args:
            caller = inspect.stack()[2][3]
            called = inspect.stack()[1][3]
            debug = f'{caller} -> {called}'
            ic( debug )
            return None
        return ic( args )
    
def animate_ellipsis( keyframes, speed ):
    anim_str = ''
    for n in range( keyframes ):
        print( f'\x1b[A \x1b[0J{anim_str}')
        anim_str += '.'
        time.sleep( 1 / speed )
        if len( anim_str ) == 4:
            anim_str = ''

def adjacencies( map_data_csv ):
    """ Provides adjacency matrices of the full graph, as well as left and right graphs; all matrices returned as Tables """
    neighbors = [  ]

    with open( map_data_csv ) as file:
        table = csv.reader( file, delimiter="," )
        headers = next( table )
        for row in table:
            neighbors.append( [ row[0], row[3], row[4], row[5] ] )

    # add other worlds
    other_worlds = [ 'R\'LYEH','PLATEAU OF LENG','THE DREAMLANDS','GREAT HALL OF CELEANO','YUGGOTH','CITY OF THE GREAT RACE','ABYSS','ANOTHER DIMENSION']
    for world in other_worlds:
        neighbors.append( [ world, 'null', 'null', 'null' ] )

    # initialize matrices
    all_neighbors, left_neighbors, right_neighbors = [ [ 'name' ] ], [ [ 'name' ] ], [ [ 'name' ] ]

    def create_matrix( blank, reference ):
        """Creates a labeled 0-matrix from a blank"""
        num_locations = len( reference )

        for location in reference:
            # add column headers 
            blank[0].append( location[0] )
            # add rows with row headers
            blank.append( [ location[0] ] + [ 0 for n in range( num_locations ) ] )

        return blank

    def assign_neighbors( matrix, reference, direction ):
        """Fills out matrix using reference data"""
        for a,b in zip( matrix[1:], reference ):
            ref = [ w.strip() for w in b[ direction ].split(',') ]
            for index, val in enumerate( matrix[0][1:] ):
                if val in ref:
                    a[index+1] = 1
        return matrix

    all_neighbors = Table( assign_neighbors( create_matrix( all_neighbors, neighbors ), neighbors, 1 ) )
    left_neighbors = Table( assign_neighbors( create_matrix( left_neighbors, neighbors ), neighbors, 2 ) )
    right_neighbors = Table( assign_neighbors( create_matrix( right_neighbors, neighbors ), neighbors, 3 ) )

    return all_neighbors, left_neighbors, right_neighbors


def rand_from_distro( distro: dict ) -> str:
    """Returns a random key using the values to determine likelihood"""
    total = sum( distro.values() )
    if total:
        v, r = 0, random.uniform(0,1)
        for k in distro:
            v += distro[k]/total
            if v >= r:
                return k
    return None

def dot_product( a, b ):
    """The dot product of two vectors"""
    return sum( [ a_n * b_n for a_n, b_n in zip( a, b) ] )

def matrix_multiply( A, B ):
    result = [ [] for row in A ]
    for i, r in enumerate( A ):
        for j, element in enumerate( r ):
            result[i].append( dot_product( r, [ s[j] for s in B ] ) )
    return result

def matrix_square( A ):
    return matrix_multiply( A, A )

def roll_die( p ):
    """ Roll die of n sides, return result """
    if random.uniform(0,1) <= p:
        return True
    return False

def current_locations_desc( defaults, transforms ):
    """ Returns a Table with current location descriptions """
    current_descs = [ defaults.table[0] ]
    for index,row in enumerate(defaults.table[1:]):
        current_descs.append([
            row[0],
            currency.location_investigators( row[1], transforms.table[index+1][1] ),
            currency.location_occupants( row[2], transforms.table[index+1][2] ),
            currency.location_gate_to( row[3], transforms.table[index+1][3]),
            currency.location_status( row[4], transforms.table[index+1][4] )
        ])
    return Table( current_descs )

def current_investigators_dec( defaults, transforms ):
    """ Returns a Table with current investigator descriptions """
    current_descs = [ defaults.table[0] ]
    for index,row in enumerate( defaults.table[1:] ):
        current_descs.append([
            row[0],
            currency.investigator_damage( row[1], transforms.table[index+1][1] ),
            currency.investigator_horror( row[2], transforms.table[index+1][2] ),
            currency.investigator_conditions( row[3], )
        ])


class Table:

    class Row:
        def __init__( self, row_data, header_data=None ):
            self._row_data = row_data
            if header_data:
                if len( row_data ) != len( header_data ):
                    msg = f'row_data length: {len(row_data)}    row_data: {row_data}\nheader_data length: {len(header_data)}    header_data: {header_data}'
                    raise IndexError( 'row_data and header_data must be same length', msg )
                self._header_data = header_data

                for h,v in zip( header_data, row_data ):
                    setattr( self, h, v )

        def __iter__( self ):
            yield from self._row_data

        def __getitem__( self, index ):
            return self._row_data[ index ]
        
        def index( self, n ):
            for i, v in enumerate( self._row_data ):
                if v == n:
                    return i

        def contents( self  ):
            return self.__dict__

    def __init__( self, table, header_row=True, header_col=True ):
        self.table = table
        self.headless = [ row[1:] for row in self.table[1:] ]
        if header_row:
            self._header_row = 0 
            self._rows = self.table[1:]
        if header_col:
            self._header_col = 0
            self._cols = self.table[ 0 ]
        

    def __iter__( self ):
        for row in self.table[1:]:
            yield self.Row( row, self.table[0] )

    def __getitem__( self, index ):
        return self.row_num( index )
    
    def row_num( self, row_n, bundled=True ):
        if hasattr( self, '_header_row' ):
            if bundled:
                return self.Row( self._rows[ row_n - 1 ], self.table[ self._header_row ] )
            return self._rows[ row_n - 1 ]
        return self.table[ row_n ]
    
    def col_num( self, col_n ):
        col = []
        if hasattr( self, '_header_col' ):
            for row in self._rows:
                col.append( row[ col_n -1 ] )
            return col
        for row in self.table:
            col.append( col_n )
        return col
    
    def row( self, row_name, bundled=True ):
        if hasattr( self, '_header_row' ):
            for row in self._rows:
                if row[ self._header_col ] == row_name:
                    if bundled:
                        return self.Row( row, self.table[ self._header_row ])
                    return row
        return None
    
    def col( self, col_name ):
        if hasattr( self, '_header_col' ):
            col = []
            if col_name not in self._cols:
                return None
            col_index = self._cols.index( col_name )
            for row in self._rows:
                col.append( row[ col_index] )
            return col
        return None
    
    def find( self, row_name, col_name ):
        if hasattr( self, '_header_row' ):
            row = self.row( row_name )
            col_index = None
            if self.col( col_name ) != None:
                col_index = self._cols.index( col_name )
            if row != None and col_index != None:
                return row[ col_index ]
        return None
    
    def filter( self, col_name, val, cond="==" ):
        """ generator; yields rows with matching val in col_name """
        if hasattr( self, '_header_row' ):
            col_index = self._cols.index( col_name )
            for row in self.table[1:]:
                if eval( f'"{ str( row[ col_index ] ) }"' + cond + f'"{ str( val ) }"' ):
                    yield self.Row( row, self.table[ self._header_row ] )

class Location:

    status = namedtuple( "location_status", ["clues", "historical_clues", "sealed", "gate", "historical_gates", "explored", "closed" ] )

class Monster:

    rulesets = namedtuple( "rulesets", ["movement", "combat", "evade"] )
    abilities = namedtuple( "abilities", ["ambush","endless","undead","physical","magical","nightmarish","overwhelming"] )
    stats = namedtuple( "stats", ["awareness","toughness","horror_mod","horror","combat_mod","damage"] )


class Investigator:

    damage = namedtuple( "damage_stats", ["max_damage", "current_damage", "unconscious" ] )
    horror = namedtuple( "horror_stats", ["max_horror", "current_horror", "insane" ] )

    conditions = namedtuple( "conditions", [
        "lost_in_time_and_space",
        "delayed",
        "arrested",
        "retainer",
        "bank_loan",
        "stl_membership",
        "deputized",
        "blessed_cursed"
    ])

    focus = namedtuple( "focus_stats", ["max_focus", "current_focus" ] )
    speed = namedtuple( "speed_stats", ["max_speed", "current_speed", "speed_sneak_sum" ] )
    fight = namedtuple( "fight_stats", ["max_fight", "current_fight", "fight_will_sum" ] )
    lore = namedtuple( "lore_stats", ["max_lore", "current_lore", "lore_luck_sum" ] )

    location = namedtuple( "location_stats", ["current_location", "mvmt_points", "in_arkham"] )

    random_possessions = namedtuple( "random_possessions", ["common_items", "unique_items", "spells", "skills"] )
    equipped_items = namedtuple( "equipped_items", [ "hands", "equipment"] )


class Items:

    weapon = namedtuple( "weapon_stats", ["modality", "bonus", "sanity_cost", "exhaustable", "losable", "price"] )
    consumable = namedtuple( "consumable_stats", ["bonus", "price"] )
    tome = namedtuple( "tome_stats", ["mvmt_cost", "sanity_cost", "modifier", "price"] )
    passive_buff = namedtuple( "passive_buff_stats", ["bonus", "price"] )
    active_buff = namedtuple( "active_buff_stats", ["bonus","price"] )
    oddity = namedtuple( "oddity_stats", "price" )

def set_limit( trans_record, transform, n, x=None ):
    """ Used for setting gate limit, monsters limits, and doom limit """
    if eval( str( n ) ):
        trans_record += [ transform ]
        return set_limit( trans_record, transform, eval( str( n ) ) - 1, x )