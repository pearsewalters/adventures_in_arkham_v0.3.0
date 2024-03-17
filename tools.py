# odds and ends that help 

import random, csv
from icecream import ic, install
install()


def adjacencies( map_data_csv ):
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
    all_neighbors, left_neighbors, right_neighbors = [ [ None ] ], [ [ None ] ], [ [ None ] ]

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

    all_neighbors = assign_neighbors( create_matrix( all_neighbors, neighbors ), neighbors, 1 )
    left_neighbors = assign_neighbors( create_matrix( left_neighbors, neighbors ), neighbors, 2 )
    right_neighbors = assign_neighbors( create_matrix( right_neighbors, neighbors ), neighbors, 3 )

    return all_neighbors, left_neighbors, right_neighbors


def rand_from_distro( distro: dict ) -> str:
    """Returns a random key using the values to determine likelihood"""
    total = sum( distro.values() )
    v, r = 0, random.uniform(0,1)
    for k in distro:
        v += distro[k]/total
        if v >= r:
            return k
        
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

def search_table( table: list, search_term, search_column, result_column="row", skip_header_row=True, gen=False):
    
    search_t = table[1:] if skip_header_row else table
    
    search_col_index = table[0].index( search_column )
    result_col_index = table[0].index( result_column ) if result_column != "row" else None

    result_table = []

    for row in search_t:
        if row[ search_col_index ] == search_term:
            if result_col_index != None:
                result_table.append( row[ result_col_index ] )
            else:
                result_table.append( row )
    
    return result_table
    
def search_gen( table: list, search_terms: list, search_column, result_column="row", skip_header_row=True, negate=False):
    
    search_t = table[1:] if skip_header_row else table
    
    search_col_index = table[0].index( search_column )
    result_col_index = table[0].index( result_column ) if result_column != "row" else None

    result = None
    
    for row in search_t:
        if not negate and row[ search_col_index ] in search_terms:
            result = row[ result_col_index ] if result_col_index != None else row
            yield result
        elif negate and row[ search_col_index ] not in search_terms:
            result = row[ result_col_index ] if result_col_index != None else row
            yield result

class Table:
    def __init__( self, table, header_row=True, header_col=True ):
        self.table = table
        if header_row:
            self._header_row = 0 
            self._rows = self.table[1:]
        if header_col:
            self._header_col = 0
            self._cols = self.table[ 0 ]
    
    def row_num( self, row_n ):
        if hasattr( self, '_header_row' ):
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
    
    def row( self, row_name ):
        if hasattr( self, '_header_row' ):
            for row in self._rows:
                if row[ self._header_col ] == row_name:
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
            for row in self.table:
                if eval( f'"{ str( row[ col_index ] ) }"' + cond + f'"{ str( val ) }"' ):
                    yield row
