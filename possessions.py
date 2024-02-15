
# possessions data

possession_defaults = [
    ['name',           'random_possessions', 'equipped_items', 'exhausted_items', 'possessions' ]
    ['Amanda Sharpe',  [ 1,1,1,2 ],          [ 2, [] ],        [],                   { 'money' : 1,
    'clues' : 1,
    'gate_trophies' : 0,
    'monster_trophies' : 0, 
    'common' : [],
    'unique' : [],
    'spells' : [],
    'buffs' : [] } ] ,
    ['Harvey Walters', [ 0,2,2,1 ],          [ 2, [] ],        [],                   { 'money' : 5,
    'clues' : 1,
    'gate_trophies' : 0,
    'monster_trophies' : 0, 
    'common' : [],
    'unique' : [],
    'spells' : [],
    'buffs' : [] } ] 
]

possession_transforms = [
    ['name',           'random_possessions', 'equipped_items', 'possessions' ]
    ['Amanda Sharpe',  [],                   [],               []            ],
    ['Harvey Walters', [],                   [],               []            ],
]

def inc_hands( matrix ):
    return [ matrix[0]+1, matrix[2] ]

def dec_hands( matrix ):
    return [ matrix[0]-1, matrix[2] ]

def equip_item( matrix, item ):
    return [ matrix[0], matrix[1]+[item] ]

def unequip( matrix, item ):
    equipment = [ i for i in matrix[1] ]
    for i in range( len( equipment ) ):
        if equipment[i] == item:
            del equipment[i]
            break
    return [ matrix[0], equipment ]

def exhaust_item( matrix, item ):
    return matrix + [item]

def refresh_items( matrix ):
    return matrix[:0]

def copy_of_possessions( possessions ):
    return { 
        'money' : possessions['money'],
        'clues' : possessions['clues'],
        'gate_trophies' : possessions['gate_trophies'],
        'monster_trophies' : possessions['monster_trophies'], 
        'common' : [ i for i in possessions['common'] ],
        'unique' : [ j for j in possessions['unique'] ],
        'spells' : [ k for k in possessions['spells'] ]
    }

def inc_money( possessions ):
    p = copy_of_possessions( possessions )
    p['money'] += 1
    return p

def dec_money( possessions ):
    p = copy_of_possessions( possessions )
    p['money'] -= 1
    return p

def inc_clues( possessions ):
    p = copy_of_possessions( possessions )
    p['clues'] += 1
    return p

def dec_clues( possessions ):
    p = copy_of_possessions( possessions )
    p['clues'] -= 1
    return p

def inc_gate_trophies( possessions ):
    p = copy_of_possessions( possessions )
    p['gate_trophies'] += 1
    return p

def dec_gate_trophies( possessions ):
    p = copy_of_possessions( possessions )
    p['gate_trophies'] -= 1
    return p

def inc_monster_trophies( possessions ):
    p = copy_of_possessions( possessions )
    p['monster_trophies'] += 1
    return p

def dec_monster_trophies( possessions ):
    p = copy_of_possessions( possessions )
    p['monster_trophies'] -= 1
    return p

def add_item( possessions, variety, item ):
    p = copy_of_possessions( possessions )
    p[variety] += [item]
    return p

def remove_item( possessions, variety, item ):
    p = copy_of_possessions( possessions )
    for i in range( len( p[variety] ) ):
        if p[variety][i] == item:
            del p[variety][i]
            break
    return p

def add_common_item( dictionary, item ):
    return add_item( dictionary, 'common', item )

def remove_common_item( dictionary, item ):
    return remove_item( dictionary, 'common', item )

def add_unique_item( dictionary, item ):
    return add_item( dictionary, 'unique', item )

def remove_unique_item( dictionary, item ):
    return remove_item( dictionary, 'unique', item )

def add_spell( dictionary, spell ):
    return add_item( dictionary, 'spell', spell )

def remove_spell( dictionary, spell ):
    return remove_item( dictionary, 'spell', spell )

def add_buff( dictionary, buff  ):
    return add_item( dictionary, 'buff', buff )

def remove_buff( dictionary, buff ):
    return remove_item( dictionary, 'buff', buff )

def get_current_possessions( dictionary, transformations ):
    d = dictionary
    for transformation in transformations:
        d = transformation[0]( d, transformation[1] ) if hasattr( transformation, '__iter__' ) else transformation( d )
    return d

get_current_equipment = get_current_possessions

# validators    

def hands_constraint( matrix, next_transform, prev_transforms ):
    """
        HANDS
        Investigators have a standard 2 hands available. Reducing this to less than 0 is illegal.
        Some items or spells may increase the number of hands, but this constraint gives no upper limit.

        Returns True if the proposed transform is 0 <= hands, else returns False
    """
    transformed_matrix = next_transform( get_current_equipment( matrix, prev_transforms ) )
    # can't be less than 0
    if 0 <= transformed_matrix[0]:
        return True
    else:
        return False
    
def money_constraint( dictionary, next_transform, prev_transforms ):
    """
        MONEY
        Money exists in [0,inf). While the analog game has a finite amount of money tokens, 
            right now there is no rule regarding what happens when that pool of tokens runs out.
            Since this is the case, I am assuming there's no reason to believe the money should 
            run out for any reason.
    """
    transformed_dictionary = next_transform( get_current_possessions( dictionary, prev_transforms ) )
    # can't be less than 0
    if 0 <= transformed_dictionary['money']:
        return True
    else:
        return False

def clues_constraint( dictionary, next_transform, prev_transforms ):
    """
        CLUES
        Clues exists in [0,inf), and so 'negative clues' is illegal. The analog game may have something to 
            say about running out of clue tokens, but I'm choosing to treat clue tokens as an infinite resource.
    """
    transformed_dictionary = next_transform( get_current_possessions( dictionary, prev_transforms ) )
    # can't be less than 0
    if 0 <= transformed_dictionary['clues']:
        return True
    else:
        return False
    
def gate_trophy_constraint( dictionary, next_transform, prev_transforms ):
    """
        GATE TROPHIES
        Gate trophies exist in [0,num_gates] where num_gates is the number of gate tokens in the game.
        Base game includes 16 gate tokens. Rewrite this constraint when including expansions.
    """
    transformed_dictionary = next_transform( get_current_possessions( dictionary, prev_transforms ) )
    if 0 <= transformed_dictionary['gate_trophies'] <= 16:
        return True
    else:
        return False
    
def monster_trophy_constraint( dictionary, next_transform, prev_transforms ):
    """
        MONSTER TROPHIES
        Monster trophies exist in [0,num_monsters] where num_monsters is the number of monster tokens in the game.
        Base game includes 55 regular monsters. 
        Rewrite this constraint whenever additional monsters are added, such as Nyarlathotep's masks or including 
            expansions.
    """
    transformed_dictionary = next_transform( get_current_possessions( dictionary, prev_transforms ) )
    if 0 <= transformed_dictionary['monster_trophies'] <= 55:
        return True
    else:
        return False

