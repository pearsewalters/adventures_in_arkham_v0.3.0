
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
    return matrix[:matrix.index(item)] + matrix[matrix.index(item)+1:]

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
        'spells' : [ k for k in possessions['spells'] ],
        'buffs' : [ l for l in possessions['buffs'] ],
        'allies' : [ m for m in possessions['allies'] ]
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



