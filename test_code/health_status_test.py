


# health status data
health_status_defaults = [ 
    [ 'name',           'damage',     'horror',   ],
    [ 'Amanda Sharpe',  [ 5, 0, 0 ],  [ 5, 0, 0 ] ],
    [ 'Harvey Walters', [ 3, 0, 0 ],  [ 7, 0, 0 ] ]
]

health_status_transforms = [
    [ 'name',           'damage_transforms', 'horror_transforms' ],
    [ 'Amanda Sharpe',  [],                  []                  ],
    [ 'Harvey Walters', [],                  []                  ]
]


# transformers
def inc_stat( matrix ):
    return [ matrix[0], matrix[1] + 1, matrix[2] ]
def dec_stat( matrix ):
    return [ matrix[0], matrix[1] - 1, matrix[2] ]
def get_current_stat( matrix, transformations ):
    stat = matrix
    for transformation in transformations:
        stat = transformation( stat )
    return stat

def inc_damage( matrix ):
    return inc_stat( matrix )
def dec_damage( matrix ):
    return dec_stat( matrix )
def inc_max_damage( matrix ):
    return inc_stat( matrix )
def dec_max_damage( matrix ):
    return dec_stat( matrix )
def inc_horror( matrix ):
    return inc_stat( matrix )
def dec_horror( matrix ):
    return dec_stat( matrix )
def inc_max_horror( matrix ):
    return inc_stat( matrix )
def dec_max_horror( matrix ):
    return dec_stat( matrix )
def set_insane( matrix ):
    return inc_stat( matrix )
def set_sane( matrix ):
    return dec_stat( matrix )
def set_uncon( matrix ):
    return inc_stat( matrix )
def set_con( matrix ):
    return dec_stat( matrix )

get_damage = get_horror = get_max_damage = get_max_horror = get_insane = get_uncon = get_current_stat


# validators

def damage_constraint( matrix, next_transform, prev_transforms ):
    """
        DAMAGE:
        A Character who receives greater than or equal to their max_damage becomes unconscious. 
        A Character cannot remove damage to less than 0. 

        This validator returns 0 if the Character's damage is on the interval (-inf, 0)
                               1 if the Character's damage is on the interval [0, max), or
                               2 if the Character's damage is on the interval [max, inf) 

        SANITY:
        A Character who receives greater than or equal to their max_horror becomes insane. 
        A Character cannot remove horror to less than 0. 

        This validator returns 0 if the Character's horror is on the interval (-inf, 0)
                               1 if the Character's horror is on the interval [0, max), or
                               2 if the Character's horror is on the interval [max, inf) 
    """
    transformed_matrix = next_transform( get_current_stat( matrix, prev_transforms ) )
    # damage can't less than 0 or greater than max
    if 0 <= transformed_matrix[1] < transformed_matrix[0]:
        return 1
    # character is unconscious if max damage is reached
    elif transformed_matrix[0] >= transformed_matrix[1]:
        return 2
    # otherwise, invalid transform
    else:
        return 0

horror_constraint = damage_constraint

def unconscious_constraint( matrix, next_transform, prev_transforms ):
    """
        UNCONCIOUS:
        A Character becomes unconscious if they receive total damage of at least their max damage.
        This stat exists in {0,1}, where 0 is conscious and 1 is unconscious.

        INSANE:
        A Character becomes insane if they receive total horror of at least their max horror.
        This stat exists in {0,1}, where 0 is sane and 1 is insane.
    """
    transformed_matrix = next_transform( get_current_stat( matrix, prev_transforms ) )
    # unconscious can only be 0 or 1 
    if 0 <= transformed_matrix[1] <= 1:
        return True
    else:
        return False




    

    
