
# locations 

def current_location_occupants( vector, transformations):
    location = vector
    for transformation, occupant in transformations:
        location = transformation( location, occupant )
    return location

def current_location_status( vector, transformations ):
    location = vector
    for transformation in transformations:
        location = transformation( location )
    return location

# investigators

def current_stat( matrix, transformations ):
    stat = matrix
    for transformation in transformations:
        stat = transformation( stat )
    return stat

current_condtions = current_stat

def current_skill( matrix, transformations ):
    return current_stat( matrix, transformations)

def current_complement_skill( matrix, transformations):
    return matrix[2] - current_skill( matrix, transformations )[1]

current_exhausted = current_skill

def current_possessions( dictionary, transformations ):
    d = dictionary
    for transformation in transformations:
        d = transformation[0]( d, transformation[1] ) if hasattr( transformation, '__iter__' ) else transformation( d )
    return d

current_equipment = current_inv_location = current_possessions

# board

def current_investigators( vector, transformations ):
    i = vector
    for transformation in transformations:
        i = transformation[0]( i, transformation[1] )
    return i

current_ancient_one = current_investigators

def current_doom_track( integer, transformations ):
    d = integer
    for transformation in transformations:
        d = transformation( d )
    return d

current_player = current_phase = current_gates_open = current_monster_count = current_terror_track = current_win_condition = current_doom_track 

def current_monst_locs_by_dim( matrix, transformations ):
    m = matrix
    for transformation, dimension, location in transformations:
        m = transformation( m, dimension, location )
    return m

