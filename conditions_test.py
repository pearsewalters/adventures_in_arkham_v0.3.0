# condition data

condition_defaults = [
    [ 'name',           'conditions'   ],
    [ 'Amanda Sharpe',  [ 0, 0, 0, 0, 0, 0, 0, 0 ] ],
    [ 'Harvey Walters', [ 0, 0, 0, 0, 0, 0, 0, 0 ] ],
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
    return [ c+1 if matrix.index(c) == 0 else c for c in matrix if matrix ]
def remove_delay( matrix ):
    return [ c-1 if matrix.index(c) == 0 else c for c in matrix if matrix ]
def add_arrest( matrix ):
    return [ c+1 if matrix.index(c) == 1 else c for c in matrix if matrix ]
def remove_arrest( matrix ):
    return [ c-1 if matrix.index(c) == 1 else c for c in matrix if matrix ]
def add_lost( matrix ):
    return [ c+1 if matrix.index(c) == 2 else c for c in matrix if matrix ]
def remove_lost( matrix ):
    return [ c-1 if matrix.index(c) == 2 else c for c in matrix if matrix ]
def add_retainer( matrix ):
    return [ c+1 if matrix.index(c) == 3 else c for c in matrix if matrix ]
def remove_retainer( matrix ):
    return [ c-1 if matrix.index(c) == 3 else c for c in matrix if matrix ]
def add_bank_loan( matrix ):
    return [ c+1 if matrix.index(c) == 4 else c for c in matrix if matrix ]
def remove_bank_loan( matrix ):
    return [ c-1 if matrix.index(c) == 4 else c for c in matrix if matrix ]
def add_stl_membership( matrix ):
    return [ c+1 if matrix.index(c) == 5 else c for c in matrix if matrix ]
def remove_stl_membership( matrix ):
    return [ c-1 if matrix.index(c) == 5 else c for c in matrix if matrix ]
def add_deputy( matrix ):
    return [ c+1 if matrix.index(c) == 6 else c for c in matrix if matrix ]
def remove_deputy( matrix ):
    return [ c-1 if matrix.index(c) == 6 else c for c in matrix if matrix ]
def add_blessing( matrix ):
    return [ c+1 if matrix.index(c) == 7 else c for c in matrix if matrix ]
def remove_blessing( matrix):
    return [ c-1 if matrix.index(c) == 7 else c for c in matrix if matrix ]

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
    
def retainer_constraints( matrix, next_transform, prev_transforms ):
    """
        RETAINER
        A Character gains a retainer likely from the Newspaper. If a Character has a retainer, they gain $1 every Upkeep.
        After gaining their dollar, there is a chance the Character loses their retainer.
        This stat exists in {0,1} where 0 is 'has no retainer', and 1 is 'has retainer'.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[3] <= 1:
        return True
    else:
        return False
    
def bank_loan_constraints( matrix, next_transform, prev_transforms ):
    """
        BANK LOAN
        A Character gains a loan from the Bank of Arkham. When a Character gets the loan, 
        they immediately gain $10. If a Character has a loan, there is a chance they must pay 
        $1 or, if unable, lose half their items. If this occurs, the Character may not take
        out another loan.`
        This stat exists in {0,1,inf} where 0 is 'has no bank loan', 1 is 'has bank loan', 
        and inf is 'may not receive a bank loan.
        This constraint check returns 0 if passed a bad transform, 1 if a good transform, and
        2 if a transform on a loan that can't be given.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0, 1, or inf
    if 0 <= transformed_matrix[4] <= 1:
        return 1
    elif transformed_matrix[4] == float('inf'):
        return 2
    else:
        return 0
    
def twilight_constraints( matrix, next_transform, prev_transforms ):
    """
        SILVER TWILIGHT LODGE MEMBERSHIP
        A Character gains a lodge membership from the Silver Twilight Lodge. If a Character has 
        a lodge membership, they can optionally have an encounter in the Inner Sanctum.
        This stat exists in {0,1} where 0 is 'has no lodge membership', and 1 is 'has lodge membership'.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[5] <= 1:
        return True
    else:
        return False

def deputy_constraints( matrix, next_transform, prev_transforms ):
    """
        RETAINER
        A Character is deputized for certain heroic acts. If a Character is a deputy, they 
        immediately gain a Patrol Wagon and a Deputy's Revolver, and they gain $1 every Upkeep.
        This stat exists in {0,1} where 0 is 'not deputized', and 1 is 'deputized'.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[6] <= 1:
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
        This constraint check returns 0 if given a bad transform, 1 if cursed, 2 if normal, and 3 if blessed.
    """
    transformed_matrix = next_transform( get_current_conditions( matrix, prev_transforms) )
    if not -1 <= transformed_matrix[7] <= 1:
        return 0 # invalid transform
    elif transformed_matrix[7] == -1:
        return 1 # cursed
    elif transformed_matrix[7] == 0:
        return 2 # normal
    elif transformed_matrix[7] == 1:
        return 3 # blessed