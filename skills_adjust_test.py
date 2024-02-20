from icecream import ic

# base transformation functions
def inc_skill( matrix ):
    return [ matrix[0], matrix[1]+1, matrix[2] ]
def dec_skill( matrix ):
    return [ matrix[0], matrix[1]-1, matrix[2] ]
def get_current_skill( matrix: list , transformations: list ) -> int:
    m = matrix
    for transformation in transformations:
        m = transformation( m )
    return m
def get_current_complement_skill( matrix: list, transformations: list ) -> int:
    return matrix[2] - get_current_skill( matrix, transformations )[1]

# wrappers for ease of use and better logging
def inc_focus( matrix ):
    return inc_skill( matrix )
def dec_focus( matrix ):
    return dec_skill( matrix )
def inc_speed( matrix ):
    return inc_skill( matrix )
def dec_speed( matrix ):
    return dec_skill( matrix )
def inc_fight( matrix ):
    return inc_skill( matrix )
def dec_fight( matrix ):
    return dec_skill( matrix )
def inc_lore( matrix ):
    return inc_skill( matrix )
def dec_lore( matrix ):
    return dec_skill( matrix )
def inc_sneak( matrix ):
    return dec_skill( matrix )
def dec_sneak( matrix ):
    return inc_skill( matrix )
def inc_will( matrix ):
    return dec_skill( matrix )
def dec_will( matrix ):
    return inc_skill( matrix )
def inc_luck( matrix ):
    return dec_skill( matrix )
def dec_luck( matrix ):
    return inc_skill( matrix )


get_current_focus = get_current_speed = get_current_fight = get_current_lore = get_current_skill
get_current_sneak = get_current_will = get_current_luck = get_current_complement_skill



# rules validation
def skills_rule( matrix, next_transform, prev_transforms ):
    transformed_matrix = next_transform( get_current_skill( matrix, prev_transforms) )
    # skill must be inside the range defined on the investigator sheets
    if transformed_matrix[0] - 3 <= transformed_matrix[1] <= transformed_matrix[0]:
        return True
    else:
        return False

def focus_rule( matrix, next_transform, prev_transforms ):
    transformed_matrix = next_transform( get_current_skill( matrix, prev_transforms) )
    # focus can't be less than 0 or greater than the max
    if 0 <= transformed_matrix[1] <= transformed_matrix[0]:
        return True
    else:
        return False


#########################################################################################
## This will have to be worked in. The interface below does not accomodate such tables ##
#########################################################################################
# skill defaults
skills_defaults = [
    [ 'name',           'focus',        'speed',        'fight',        'lore'      ],
    [ 'Amanda Sharpe',  [ 2, 2, 0 ],    [ 4, 4, 5 ],    [ 4, 4, 5 ],    [ 4, 4, 5 ] ],
    [ 'Harvey Walters', [ 2, 2, 0 ],    [ 3, 3, 5 ],    [ 3, 3, 3 ],    [ 6, 6, 7 ] ]
]
skills_transforms = [
    [ 'name',           'focus',        'speed',        'fight',        'lore'      ],
    [ 'Amanda Sharpe',  [  ],           [  ],           [  ],           [  ]        ],
    [ 'Harvey Walters', [  ],           [  ],           [  ],           [  ]        ]
]




# default character 
skills = { 
    'focus' : [ 999, 999, 0 ]
}
skills['speed'] = skills['sneak'] = [ 4, 4, 5 ]
skills['fight'] = skills['will'] = [ 4, 4, 5 ]
skills['lore'] = skills['luck'] = [ 4, 4, 5 ]
    
transforms = { 
    'focus' : [ ]
}
transforms['speed'] = transforms['sneak'] = [  ]
transforms['fight'] = transforms['will'] = [  ]
transforms['lore'] = transforms['luck'] = [  ]

# interface 
valid_commands = { 'show', 'increase', 'decrease' }
command_funcs = {
    'show' : {
        'focus' : get_current_focus,
        'speed' : get_current_speed,
        'sneak' : get_current_sneak,
        'fight' : get_current_fight,
        'will' : get_current_will,
        'lore' : get_current_lore,
        'luck' : get_current_luck
    },
    'increase' : {
        'speed' : inc_speed,
        'sneak' : inc_sneak,
        'fight' : inc_fight,
        'will' : inc_will,
        'lore' : inc_lore,
        'luck' : inc_luck
    },
    'decrease' : {
        'speed' : dec_speed,
        'sneak' : dec_sneak,
        'fight' : dec_fight,
        'will' : dec_will,
        'lore' : dec_lore,
        'luck' : dec_luck
    }
}

log = []

while True:
    output = input( '>>> ' ).lower()
    if output == 'bye':
        print( 'bye!' )
        break
    elif len( set( output.split() ) & valid_commands ) != 1:
        print( 'Try again with a valid command.' )
    elif len( set( output.split() ) & valid_commands ) == 1:
        command = list(set( output.split() ) & valid_commands)[0]
        argument = list(set( output.split() ) - valid_commands)[0]
        if command != 'show' and focus_rule( skills['focus'], dec_focus, transforms['focus'] ):
            if skills_rule( skills[argument], command_funcs[command][argument], transforms[argument] ):
                transforms['focus'].append( dec_focus )
                transforms[argument].append( command_funcs[command][argument] )
                log.append( command_funcs[command][argument].__name__ )
                ic( log )
            else: 
                print( 'Can\'t adjust your skill level like that. ' )
        elif command != 'show' and not focus_rule( skills['focus'], dec_focus, transforms['focus'] ):
            print( 'You\'ve run out of focus. Move on to casting spells or using items? (y/n)' )
        else:
            show = command_funcs[command][argument]( skills[argument], transforms[argument] )
            print( show )