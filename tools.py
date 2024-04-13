# odds and ends that help 

import math, random, csv, inspect, time
from classes.table import Table
from classes.context import Context
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

def randFromDistro( distro: dict ) -> str:
    """Returns a random key using the values to determine likelihood"""
    total = sum( distro.values() )
    if total:
        v, r = 0, random.uniform(0,1)
        for k in distro:
            v += distro[k]/total
            if v >= r:
                return k
    return None

def bound( x ):
    """ Used to convert -2 or 2 to -1 or 1 for skill check purposes """
    def sign( y ):
        if 0 <= y:
            return 1
        return -1
    t = type( x )
    s = sign( x )
    m = abs( x ) * 10
    if 5 <= m%10 <= 9:
        return s * t( ( m - m%10 + 10)/10 )
    elif 1 <= m%10 <= 4:
        return s * t( ( m - m%10 - 10)/10 )
    return x

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

def currentLocationsDesc( defaults, transforms ):
    """ Returns a Table with current location descriptions """
    current_descs = [ defaults.table[0] ]
    for index,row in enumerate(defaults.table[1:]):
        current_descs.append([
            row[0],
            currency.location_investigators( row[1], transforms.table[index+1][1] ),
            currency.location_occupants( row[2], transforms.table[index+1][2] ),
            currency.location_gate_to( row[3], transforms.table[index+1][3]),
            currency.locationStatus( row[4], transforms.table[index+1][4] )
        ])
    return Table( current_descs )

def setLimit( trans_record, transform, n, x=None ):

    """ Used for setting gate limit, monsters limits, and doom limit """
    if eval( str( n ) ):
        trans_record += [ transform ]
        return setLimit( trans_record, transform, eval( str( n ) ) - 1, x )
    
def clobber( context: Context, filter, column="rarity" ) -> dict:
    """ Returns a deck of items that passes the filter provided """

    deck = {}

    def miniClobber( itemType: str ):
        for item in getattr( context, itemType ).constants.filter( column, filter ):
            yield item.name, currency.deckFrequency( getattr( context, itemType ).deckDefaults, getattr( context, itemType ).deckTransforms )[item.name]

    for weapon, freq in miniClobber( "weapons" ):
        deck[weapon] = freq

    for tome, freq in miniClobber( "tomes" ):
        deck[tome] = freq

    for consumable, freq in miniClobber( "consumables" ):
        deck[consumable] = freq

    for passiveBuff, freq in miniClobber( "passiveBuffs" ):
        deck[passiveBuff] = freq

    for activeBuff, freq in miniClobber( "activeBuffs" ):
        deck[activeBuff] = freq

    for oddity, freq in miniClobber( "oddities" ):
        deck[oddity] = freq

    return deck

