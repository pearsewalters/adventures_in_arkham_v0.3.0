# locations 

def location_occupants( vector, transformations):
    location = vector
    for transformation, occupant in transformations:
        location = transformation( location, occupant )
    return location

def location_status( vector, transformations ):
    location = vector
    for transformation in transformations:
        location = transformation( location )
    return location

# investigators

def stat( matrix, transformations ):
    stat = matrix
    for transformation in transformations:
        stat = transformation( stat )
    return stat

condtions = stat

def skill( matrix, transformations ):
    return stat( matrix, transformations)

def complement_skill( matrix, transformations):
    return matrix[2] - skill( matrix, transformations )[1]

exhausted = skill

def possessions( dictionary, transformations ):
    d = dictionary
    for transformation in transformations:
        d = transformation[0]( d, transformation[1] ) if type( transformation ) == tuple else transformation( d )
    return d

equipment = inv_location = possessions

# board

def investigators( vector, transformations ):
    i = vector
    for transformation in transformations:
        i = transformation[0]( i, transformation[1] )
    return i

ancient_one = investigators

def doom_track( integer, transformations ):
    d = integer
    for transformation in transformations:
        d = transformation( d )
    return d

player = phase = bookkeeping = gates_open = monster_count = terror_track = win_condition = doom_track 

def monst_locs_by_dim( matrix, transformations ):
    m = matrix
    for transformation, dimension, location in transformations:
        m = transformation( m, dimension, location )
    return m

def monster_stats( vector, transformations ):
    s = vector
    for transformation in transformations:
        s = transformation( s )
    return s

monster_rules = abilities = monster_stats

def frequencies( dictionary, transformations ):
    f = dictionary
    for transformation in transformations:
        f = transformation[0]( f, transformation[1] )
    return f