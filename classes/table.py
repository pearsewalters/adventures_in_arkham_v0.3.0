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
    
    def index( self, name ):
        for i, v in enumerate( self.table[1:] ):
            if v[0] == name:
                return i+1
    
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