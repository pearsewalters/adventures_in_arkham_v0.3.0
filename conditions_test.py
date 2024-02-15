# condition data

condition_defaults = [
    [ 'name',           'conditions'   ],
    [ 'Amanda Sharpe',  [ 0, 0, 0, 0 ] ],
    [ 'Harvey Walters', [ 0, 0, 0, 0 ] ],
    ...
]

condition_transforms = [
    [ 'name',           'transforms'   ],
    [ 'Amanda Sharpe',  [ ]            ],
    [ 'Harvey Walters', [ ]            ],
    ...
]

# condition transformers
def add_delay( matrix ):
    return [ matrix[0]+1, matrix[1], matrix[2], matrix[3] ]
def remove_delay( matrix ):
    return [ matrix[0]-1, matrix[1], matrix[2], matrix[3] ]
def add_arrest( matrix ):
    return [ matrix[0], matrix[1]+1, matrix[2], matrix[3] ]
def remove_arrest( matrix ):
    return [ matrix[0], matrix[1]-1, matrix[2], matrix[3] ]
def add_lost( matrix ):
    return [ matrix[0], matrix[1], matrix[2]+1, matrix[3] ]
def remove_lost( matrix ):
    return [ matrix[0], matrix[1], matrix[2]-1, matrix[3] ]
def add_blessing( matrix ):
    return [ matrix[0], matrix[1], matrix[2], matrix[3]+1 ]
def remove_blessing( matrix):
    return [ matrix[0], matrix[1], matrix[2], matrix[3]-1 ]

get_current_conditions = get_current_stat

def add_curse( matrix ):
    return remove_blessing( matrix )
def remove_curse( matrix ):
    return add_blessing( matrix )



# condition validators
def delay_constraint( matrix, next_transform, prev_transforms ):
    """
        DELAYED
        A Character becomes delayed for a number of reasons. If delayed, a Character cannot take their turn until they 
            become undelayed during the following Upkeep phase.
        This stat exists in {0,1} where 0 is undelayed, and 1 is delayed.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[0] <= 1:
        return True
    else:
        return False
    
def arrest_constraint( matrix, next_transform, prev_transforms ):
    """
        ARRESTED
        A Character can be arrested because of certain in-game events. If arrested, a Character becomes DELAYED.
        This stat exists in {0,1} where 0 is un-arrested, and 1 is arrested.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[1] <= 1:
        return True
    else:
        return False
    
def lost_constraints( matrix, next_transform, prev_transforms ):
    """
        LOST IN TIME & SPACE
        A Character becomes lost in time & space for a number of reasons. If lost in time & space, a Character becomes DELAYED.
        A Character remains lost in time & space after becoming undelayed until the following Upkeep phase.
        This stat exists in {0,1} where 0 is not lost in time & space, and 1 is lost in time & space.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[2] <= 1:
        return True
    else:
        return False
    
def blessed_cursed_constraints( matrix, next_transform, prev_transforms ):
    """
        BLESSED & CURSED
        A Character can receive a blessing or a curse for a number of reasons. This status affects the outcome of skill checks.
        If a Character is cursed and becomes blessed, their condition is now normal (the effects cancel). Similarly, if a Character
            is blessed and becomes cursed, their condition is normal.
        This stat exists in {-1,0,1} where -1 is cursed, 0 is normal, and 1 is blessed.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    if not -1 <= transformed_matrix[3] <= 1:
        return 0 # invalid transform
    elif transformed_matrix[3] == -1:
        return 1 # cursed
    elif transformed_matrix[3] == 0:
        return 2 # normal
    elif transformed_matrix[3] == 1:
        return 3 # blessed