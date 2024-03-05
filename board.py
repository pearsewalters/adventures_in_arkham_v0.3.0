# defaults

board_defaults = {
    'investigators' : [  ],
    'ancient_one' : [ ],
    'doom_track' : 0,
    'terror_track' : 0,
    'gates_open' : 0,
    'gates_sealed' : 0,
    'clues_to_seal' : 5,
    'win_cond' : [ 1, 6 ],
    'monster_limit' : 4,
    'outskirts_limit' : 7,
    'monster_locations' : [ [],[],[],[],[],[],[],[],[] ]
}

# transforms

board_transforms = {
    'investigators' : [  ],
    'ancient_one' : [ ],
    'doom_track' : [ ],
    'terror_track' : [ ],
    'gates_open' : [ ],
    'gates_sealed' : [ ],
    'clues_to_seal' : [ ],
    'win_cond' : [ ],
    'monster_limit' : [ ],
    'outskirts_limit' : [ ],
    'monster_locations' : [  ]
}


def add_investigator( vector, investigator ):
    return vector + [ investigator ]

def remove_investigator( vector, investigator ):
    return vector[:vector.index(investigator)] + vector[vector.index(investigator)+1:] 

def set_ancient_one( vector, ancient_one ):
    return vector + [ ancient_one ]

def inc_doom_track( integer ):
    return integer + 1

def dec_doom_track( integer ):
    return integer - 1

def inc_terror_track( integer ):
    return integer + 1

def dec_terror_track( integer ):
    return integer - 1

def inc_gates_open( integer ):
    return integer + 1

def dec_gates_open( integer ):
    return integer - 1

def inc_gates_sealed( integer ):
    return integer + 1

def dec_gates_sealed( integer ):
    return integer - 1

def inc_clues_to_seal( integer ):
    return integer + 1

def dec_clues_to_seal( integer ):
    return integer - 1

def inc_gates_closed_to_win( vector ):
    return [ vector[0] + 1, vector[1] ]

def dec_gates_closed_to_win( vector ):
    return [ vector[0] - 1, vector[1] ]

def inc_seals_to_win( vector ):
    return [ vector[0], vector[1] + 1 ]

def dec_seals_to_win( vector ):
    return [ vector[0], vector[1] -1 ]

def inc_monster_count( integer ):
    """Decrements the monster limit in Arkham"""
    return integer - 1

def dec_monster_count( integer ):
    """Increments the monster limit in Arkham"""
    return integer + 1

def remove_monster_limit( integer ):
    """Intended for removing the monster limit"""
    return float('inf')

def inc_outskirts_count( integer ):
    """Decrements the outskirts limit"""
    return integer - 1

def dec_outskirts_count( integer ):
    """Increments the outskirts limit"""
    return integer + 1

def add_monster_location( vector, dimension, location ):
    return [ locs + [location] if dim == dimension else locs for dim, locs in enumerate( vector ) ]

def remove_monster_location( vector, dimension, location ):
    return [ locs[:locs.index(location)] + locs[locs.index(location)+1:] if dim == dimension else locs for dim, locs in enumerate( vector ) ]

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

current_gates_open = current_monster_count = current_terror_track = current_doom_track 

def current_monst_locs_by_dim( matrix, transformations ):
    m = matrix
    for transformation, dimension, location in transformations:
        m = transformation( m, dimension, location )
    return m

# validators

def too_many_gates_constraint( integer, next_transform, prev_transforms ):
    """
        TOO MANY GATES
        There is such a limit to the number of gates that can be open at once.
        For 1-2 players, this is 8. Since I don't have a way to play with more than
            one Investigator right now, this constraint will be hardcoded at 8 gates.
        This function returns 0 if passed a bad transform, 1 if passed a good transform,
        or 2 if passed a transform that surpasses the gate limit.
    """
    transformed_integer = next_transform( current_gates_open( integer, prev_transforms ) )
    # has to be between 0 and 8 
    if 0 <= transformed_integer <= 8:
        return 1
    elif 8 < transformed_integer:
        return 2
    else:
        return 0

def too_many_monsters_constraint( integer, next_transform, prev_transforms ):
    """
        TOO MANY MONSTERS
        The monster limit is set at the beginning of the game at according to how
            many investigators there are. The monster limit is the number of Investigators
            plus 3. For a one-Investigator game, that makes 4.
        The way the monster limit is handled is decrementing the monster limit whenever a 
            monster is added to Arkham. If the proposed monster limit is ever 0, the limit 
            has been reached.
        This function returns 0 if passed a bad transform, 1 if passed a good
            transform, and 2 if the monster limit has been reached.
    """
    transformed_integer = next_transform( current_gates_open( integer, prev_transforms ) )
    if 4 < transformed_integer:
        return 0
    elif 0 <= transformed_integer <= 4:
        return 1
    else:
        return 2
    
def outskirts_full_constraint( integer, next_transform, prev_transforms ):
    """
        OUTSKIRTS ARE FULL
        When there are too many monsters in the outskirts, the terror level increases. 
        The limit to the number of monsters in the outskirts is 8 minus the number of
            investigators. For a single player game, that's 7.
        This function returns 0 when passed a bad transform, 1 when passed a good 
            transform, and 2 if the outskirts are full.
    """
    transformed_integer = next_transform( current_gates_open( integer, prev_transforms ) )
    if 0 <= transformed_integer <= 7:
        return 1
    elif 7 < transformed_integer:
        return 2
    else:
        return 0