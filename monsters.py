# defaults

monster_constants = [
    ['name',                    'dimension', 'variety' ],
    ['Byakhee',                  0,          'standard'],
    ['Chthonian',                1,          'standard'],
    ['Cultist',                  5,          'standard'],
    ['Dark Young',               4,          'standard'],
    ['Dhole',                    0,          'standard'],
    ['Dimensional Shambler',     2,          'standard'],
    ['Elder Thing',              3,          'standard'],
    ['Fire Vampire',             6,          'standard'],
    ['Flying Polyp',             4,          'standard'],
    ['Formless Spawn',           4,          'standard'],
    ['Ghost',                    5,          'standard'],
    ['Ghoul',                    4,          'standard'],
    ['Gug',                      7,          'standard'],
    ['High Priest',              8,          'standard'],
    ['Hound of Tindalos',        2,          'standard'],
    ['Maniac',                   5,          'standard'],
    ['Mi-Go',                    0,          'standard'],
    ['Nightgaunt',               7,          'standard'],
    ['Shoggoth',                 3,          'standard'],
    ['Star Spawn',               8,          'standard'],
    ['Vampire',                  5,          'standard'],
    ['Warlock',                  0,          'standard'],
    ['Witch',                    0,          'standard'],
    ['Zombie',                   5,          'standard'],
    ['God of the Bloody Tongue', 1,          'mask'    ],
    ['Haunter of the Dark',      2,          'mask'    ],
    ['The Black Man',            5,          'mask'    ],
    ['The Bloated Woman',        4,          'mask'    ],
    ['The Dark Pharaoh',         7,          'mask'    ]
]

monster_defaults = [
    ['name',                     'rulesets',    'abilities',                'stats'                  ],
    ['Byakhee',                  [ 3, 0, 0 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -2, 1, -1, 1, 0, 1 ]   ],
    ['Chthonian',                [ 4, 0, 0 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ 1, 3, -2, 2, -3, 3 ]   ],
    ['Cultist',                  [ 0, 0, 0 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -3, 1, 0, 0, 1, 1 ]    ],
    ['Dark Young',               [ 2, 0, 0 ],   [ 0, 0, 0, 0.5, 1, 1, 0 ],  [ -2, 3, 0, 3, -1, 3 ]   ],
    ['Dhole',                    [ 0, 0, 0 ],   [ 0, 0, 0, 0.5, 0.5, 1, 1], [ -1, 3, -1, 4, -3, 4 ]  ],
    ['Dimensional Shambler',     [ 1, 0, 1 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -3, 1, -2, 1, -2, 0 ]  ],
    ['Elder Thing',              [ 0, 1, 2 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -2, 2, -3, 2, 0, 1 ]   ],
    ['Fire Vampire',             [ 3, 0, 0 ],   [ 1, 0, 0, 0, 1, 0, 0],     [ 0, 1, 0, 0, -2, 2 ]    ],
    ['Flying Polyp',             [ 3, 0, 0 ],   [ 0, 0, 0, 0.5, 1, 1, 1 ],  [ 0, 3, -2, 4, -3, 3 ]   ],
    ['Formless Spawn',           [ 0, 0, 0 ],   [ 0, 0, 0, 0, 1, 0, 0 ],    [ 0, 2, -1, 2, -2, 2 ]   ],
    ['Ghost',                    [ 2, 0, 0 ],   [ 0, 0, 1, 0, 1, 0, 0 ],    [ -3, 1, -2, 2, -2, 2 ]  ],
    ['Ghoul',                    [ 0, 0, 0 ],   [ 1, 0, 0, 1, 1, 0, 0, ],   [ -3, 1, 0, 1, -1, 1 ]   ],
    ['God of the Bloody Tongue', [ 0, 0, 0 ],   [ 0, 1, 0, 1, 1, 0, 1 ],    [ 1, 4, -3, 3, -4, 4 ]   ],
    ['Gug',                      [ 0, 0, 0 ],   [ 0, 0, 0, 1, 1, 0, 1],     [ -2, 3, -1, 2, -2, 4 ]  ],
    ['Haunter of the Dark',      [ 3, 0, 0 ],   [ 0, 1, 0, 1, 1, 0, 0 ],    [ -3, 2, -2, 2, -2, 2 ]  ],
    ['High Priest',              [ 0, 0, 0 ],   [ 0, 0, 0, 1, 0, 0, 0 ],    [ -2, 2, 1, 1, -1, 2 ]   ],
    ['Hound of Tindalos',        [ 5, 0, 0 ],   [ 0, 0, 0, 0, 1, 0, 0 ],    [ -1, 2, -2, 4,  -1, 3 ] ],
    ['Maniac',                   [ 0, 0, 0 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -1, 1, 0, 0, 1, 1 ]    ],
    ['Mi-Go',                    [ 3, 0, 3 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -2, 1, -1, 2, 0, 1 ]   ],
    ['Nightgaunt',               [ 3, 2, 4 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -2, 2, -1, 1, -2, 0 ]  ],
    ['Shoggoth',                 [ 1, 0, 0 ],   [ 0, 0, 0, 0.5, 1, 1, 0 ],  [ -1, 3, -1, 3, -1, 3 ]  ],
    ['Star Spawn',               [ 0, 0, 0 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -1, 3, -3, 2, -3, 3 ]  ],
    ['The Black Man',            [ 0, 0, 5 ],   [ 0, 1, 0, 1, 1, 0, 0 ],    [ -3, 1, 0, 0, 0, 0 ]    ],
    ['The Bloated Woman',        [ 0, 0, 6 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -1, 2, -1, 2, -2, 2 ]  ],
    ['The Dark Pharaoh',         [ 0, 0, 7 ],   [ 0, 0, 0, 1, 1, 0, 0 ],    [ -1, 2, -1, 1, -3, 3 ]  ],
    ['Vampire',                  [ 0, 0, 0 ],   [ 0, 0, 1, 0.5, 1, 0, 0 ],  [ -3, 1, 0, 2, -3, 3 ]   ],
    ['Warlock',                  [ 2, 0, 8 ],  [ 0, 0, 0, 1, 0, 0, 0 ],    [ -3, 2, -1, 1, -3, 1 ]  ],
    ['Witch',                    [ 0, 0, 0 ] ,  [ 0, 0, 0, 1, 0.5, 0, 0 ],  [ -1, 1, 0, 0, -3, 2]    ],
    ['Zombie',                   [ 0, 0, 0 ],   [ 0, 0, 1, 1, 1, 0, 0 ],    [ 1, 1, -1, 1, -1, 2]    ],
]
 
monster_cup_defaults = {
        'Byakhee' : 3,
        'Chthonian' : 2,
        'Cultist' : 6,
        'Dark Young' : 3,
        'Dhole' : 1,
        'Dimensional Shambler' : 2,
        'Elder Thing' : 2,
        'Fire Vampire' : 2,
        'Flying Polyp' : 1, 
        'Formless Spawn' : 2, 
        'Ghost' : 3,
        'Ghoul' : 3,
        'God of the Bloody Tongue' : 0,
        'Gug' : 2,
        'Haunter of the Dark' : 0,
        'High Priest' : 1,
        'Hound of Tindalos' : 2,
        'Maniac' : 3,
        'Mi-Go' : 3,
        'Nightgaunt' : 2,
        'Shoggoth' : 2,
        'Star Spawn' : 2,
        'The Black Man' : 0,
        'The Bloated Woman' : 0,
        'The Dark Pharaoh' : 0,
        'Vampire' : 1, 
        'Warlock' : 2,
        'Witch' : 2,
        'Zombie' : 3
    }

# transforms history

monster_transforms = [
    ['name',                     'rulesets',    'abilities',  'stats'  ],
    ['Byakhee',                  [  ],          [  ],         [  ]     ],
    ['Cultist',                  [  ],          [  ],         [  ]     ],
    ['Dark Young',               [  ],          [  ],         [  ]     ],
    ['Chthonian',                [  ],          [  ],         [  ]     ],
    ['Dhole',                    [  ],          [  ],         [  ]     ],
    ['Dimensional Shambler',     [  ],          [  ],         [  ]     ],
    ['Elder Thing',              [  ],          [  ],         [  ]     ],
    ['Fire Vampire',             [  ],          [  ],         [  ]     ],
    ['Flying Polyp',             [  ],          [  ],         [  ]     ],
    ['Formless Spawn',           [  ],          [  ],         [  ]     ],
    ['Ghost',                    [  ],          [  ],         [  ]     ],
    ['Ghoul',                    [  ],          [  ],         [  ]     ],
    ['God of the Bloody Tongue', [  ],          [  ],         [  ]     ],
    ['Gug',                      [  ],          [  ],         [  ]     ],
    ['Haunter of the Dark',      [  ],          [  ],         [  ]     ],
    ['High Priest',              [  ],          [  ],         [  ]     ],
    ['Hound of Tindalos',        [  ],          [  ],         [  ]     ],
    ['Maniac',                   [  ],          [  ],         [  ]     ],
    ['Mi-Go',                    [  ],          [  ],         [  ]     ],
    ['Nightgaunt',               [  ],          [  ],         [  ]     ],
    ['Shoggoth',                 [  ],          [  ],         [  ]     ],
    ['Star Spawn',               [  ],          [  ],         [  ]     ],
    ['The Black Man',            [  ],          [  ],         [  ]     ],
    ['The Bloated Woman',        [  ],          [  ],         [  ]     ],
    ['The Dark Pharaoh',         [  ],          [  ],         [  ]     ],
    ['Vampire',                  [  ],          [  ],         [  ]     ],
    ['Warlock',                  [  ],          [  ],         [  ]     ],
    ['Witch',                    [  ],          [  ],         [  ]     ],
    ['Zombie',                   [  ],          [  ],         [  ]     ],
]

monster_cup_transforms = [ ]

# transformers

def set_movement_rules( rulset_vector, movement_rule ):
    return [ movement_rule, rulset_vector[1], rulset_vector[2] ]

def set_evade_rules( rulset_vector, evade_rule ):
    return [ rulset_vector[0], evade_rule, rulset_vector[2] ]

def set_combat_rules( rulset_vector, combat_rule ):
    return [ rulset_vector[0], rulset_vector[1], combat_rule ]

def add_ambush( abilities_vector ):
    return [ a + 1 if i == 0 else a for i,a in enumerate( abilities_vector ) ]

def remove_ambush( abilities_vector ):
    return [ a - 1 if i == 0 else a for i,a in enumerate( abilities_vector ) ]

def add_endless( abilities_vector ):
    return [ a + 1 if i == 1 else a for i,a in enumerate( abilities_vector ) ]

def remove_endless( abilities_vector ):
    return [ a - 1 if i == 1 else a for i,a in enumerate( abilities_vector ) ]

def add_undead( abilities_vector ):
    return [ a + 1 if i == 2 else a for i,a in enumerate( abilities_vector ) ]

def remove_undead( abilities_vector ):
    return [ a - 1 if i == 2 else a for i,a in enumerate( abilities_vector ) ]

def add_physical_resistance( abilities_vector ):
    return [ a + 0.5 if i == 3 else a for i,a in enumerate( abilities_vector ) ]

def remove_physical_resistance( abilities_vector ):
    return [ a - 0.5 if i == 3 else a for i,a in enumerate( abilities_vector ) ]

def add_physical_immunity( abilities_vector ):
    return [ a + 1 if i == 3 else a for i,a in enumerate( abilities_vector ) ]

def remove_physical_immunity( abilities_vector ):
    return [ a - 1 if i == 3 else a for i,a in enumerate( abilities_vector ) ]

def add_magical_resistance( abilities_vector ):
    return [ a + 0.5 if i == 4 else a for i,a in enumerate( abilities_vector ) ]

def remove_magical_resistance( abilities_vector ):
    return [ a - 0.5 if i == 4 else a for i,a in enumerate( abilities_vector ) ]

def add_magical_immunity( abilities_vector ):
    return [ a + 1 if i == 4 else a for i,a in enumerate( abilities_vector ) ]

def remove_magical_immunity( abilities_vector ):
    return [ a - 1 if i == 4 else a for i,a in enumerate( abilities_vector ) ]

def inc_nightmarish( abilities_vector ):
    return [ a + 1 if i == 5 else a for i,a in enumerate( abilities_vector ) ]

def dec_nightmarish( abilities_vector ):
    return [ a - 1 if i == 5 else a for i,a in enumerate( abilities_vector ) ]

def inc_overwhelming( abilities_vector ):
    return [ a + 1 if i == 6 else a for i,a in enumerate( abilities_vector ) ]

def dec_overwhelming( abilities_vector ):
    return [ a - 1 if i == 6 else a for i,a in enumerate( abilities_vector ) ]

def inc_awareness( stats_vector ):
    return [ s - 1 if i == 0 else s for i,s in enumerate( stats_vector ) ]

def dec_awareness( stats_vector ):
    return [ s + 1 if i == 0 else s for i,s in enumerate( stats_vector ) ]

def inc_toughness( stats_vector ):
    return [ s + 1 if i == 1 else s for i,s in enumerate( stats_vector ) ]

def dec_toughness( stats_vector ):
    return [ s - 1 if i == 1 else s for i,s in enumerate( stats_vector ) ]

def inc_horror_rating( stats_vector ):
    return [ s - 1 if i == 2 else s for i,s in enumerate( stats_vector ) ]

def dec_horror_rating( stats_vector ):
    return [ s + 1 if i == 2 else s for i,s in enumerate( stats_vector ) ]

def inc_horror_damage( stats_vector ):
    return [ s - 1 if i == 3 else s for i,s in enumerate( stats_vector ) ]

def dec_horror_damage( stats_vector ):
    return [ s + 1 if i == 3 else s for i,s in enumerate( stats_vector ) ]

def inc_combat_rating( stats_vector ):
    return [ s - 1 if i == 4 else s for i,s in enumerate( stats_vector ) ]

def dec_combat_rating( stats_vector ):
    return [ s + 1 if i == 4 else s for i,s in enumerate( stats_vector ) ]

def inc_combat_damage( stats_vector ):
    return [ s - 1 if i == 5 else s for i,s in enumerate( stats_vector ) ]

def dec_combat_damage( stats_vector ):
    return [ s + 1 if i == 5 else s for i,s in enumerate( stats_vector ) ]

def inc_freq( dictionary, monster ):
    return { m:f+1 if m.upper() == monster.upper() else f for m,f in dictionary.items() }

def dec_freq( dictionary, monster ):
    return { m:f-1 if m.upper() == monster.upper() else f for m,f in dictionary.items() }


def current_stats( vector, transformations ):
    s = vector
    for transformation in transformations:
        s = transformation( s )
    return s

current_rules = current_abilities = current_stats

def current_frequencies( dictionary, transformations ):
    f = dictionary
    for transformation in transformations:
        f = transformation[0]( f, transformation[1] )
    return f


# validators

def movement_rules_constraint( vector, next_transform, prev_transforms ):
    """
        MONSTER MOVEMENT RULESETS
        Monsters will move when the Mythos procedure calls for it. "Movement" looks different
            for different monsters.
        0. Normal Movement
            This monster will move 1 adjacent space in the direction supplied by the Mythos.
        1. Fast Movement
            This monster will move 2 adjacent spaces in the direction supplied by the Mythos.
        2. Stationary
            This monster will not be moved, even if called for by the Mythos.
        3. Flying
            This monsters will move to
                - from a location/street area to an adjacent street area if an Investigator is present
                - from a location/street area to the sky if an Investigator is not present
                - from the sky to a street area if an Investigator is present 
            This monster will not move if no Investigator is in any street area.
        4. Chthonian
            This monster will not change location. Instead it will 'roll a 2-sided die', and add 1 damage 
            to every investigator in Arkham on a 1 and nothing on a 2.
        5. Hound of Tindalos
            This monster will move to the Investigator in the nearest location to it, barring the Hospital
            and Asylum.

        This validator returns True if the proposed ruleset is one of these. Otherwise, False. 
    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if transformed_vector[0] not in { 0, 1, 2, 3, 4, 5 }:
        return False
    else:
        return True
    
def evade_rules_constraint( vector, next_transform, prev_transforms ):
    """
        MONSTER EVASION RULESETS
        When an Investigator performs an Evade check against monster, the monster's evade ruleset
            is invoked.
        0. Standard Evade 
            On a failure, the Investigator immediately receives the appropriate Horror and combat
            begins. 
            On a success, the Investigator returns to moving as they were.
        1. Elder Thing 
            On a failure, in addition to immediately receiving Horror and beginning combat, the 
                Investigator must also discard a Weapon or Spell.
            On a success, the Investigator returns to moving as they were.
        2. Nightgaunt
            On a failure, the Investigator is moved to the nearest gate if in Arkham, or to the corresponding
                gate in Arkham if in an Other World.
            On a success, the Investigator returns to moving as they were.

        This validator returns True if the proposed ruleset is one of these. Otherwise, False.
    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if transformed_vector[0] not in { 0, 1 }:
        return False
    else:
        return True

def combat_rules_constraint( vector, next_transform, prev_transforms ):
    """
        MONSTER COMBAT RULESETS
        When an Investigator performs a Combat check against a monster, the monster's combat
            ruleset is invoked.
        0. Standard Combat
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, the Investigator receives the appropriate amount of Damage, and, if conscious,
                must begin the combat cycle again. 
        1. Dimensional Shambler
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, the Investigator is now lost in time & space.
        2. Elder Thing
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, in addition to receiving the appropriate amount of Damage, and, if conscious,
                beginning the combat cycle again, the Investigator must discard a Weapon or Spell.
        3. Mi-Go
            On a success, the Investigator earns a random Unique Item, but does not get to collect any
                monster trophies. In addition, the Mi-Go is not returned to the Monster Cup, but is 
                removed from Arkham.
            On a failure, the Investigator receives the appropriate amount of Damage, and, if conscious,
                must begin the combat cycle again.
        4. Nightgaunt
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, the Investigator is moved to the nearest gate if in Arkham, or to the corresponding
                gate in Arkham if in an Other World.
        5. The Black Man
            Instead of performing a Combat check, the Investigator must pass a Luck(-1) check or be devoured. If
                passed, the Investigator earns 2 clues. In either case, the Black Man is removed from Arkham.
        6. The Bloated Woman
            Before the Horror check during Combat, the Investigator must pass a Will(-2) check or immediately fail 
                both the Horror and Combat checks.
        7. The Dark Pharaoh
            Lore is used in Combat instead of Fight
        8. Warlock
            On a success, the Investigator earns 2 clues tokens, but does not collect any monster trophies. In 
                addition, this monster is not returned to the Monster Cup, but is removed from Arkham.
            On a failure, the Investigator receives the appropriate amount of Damage, and, if conscious,
                must begin the combat cycle again.

        This validator returns True if the proposed rulelset is one of these. Otherwise, False.
    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if transformed_vector[0] not in { 0, 1, 2, 3, 4, 5, 6, 7, 8 }:
        return False
    else:
        return True
    
def ambush_constraint( vector, next_transform, prev_transforms ):
    """
        AMBUSH

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[0] <= 1:
        return True
    else:
        return False
    
def endless_constraint( vector, next_transform, prev_transforms ):
    """
        ENDLESS

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[1] <= 1:
        return True
    else:
        return False
    
def undead_constraint( vector, next_transform, prev_transforms ):
    """
        UNDEAD

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[2] <= 1:
        return True
    else:
        return False
    
def phsyical_constraint( vector, next_transform, prev_transforms ):
    """
        PHYSICAL RESISTANCE AND IMMUNITY

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[3] <= 1:
        return True
    else:
        return False
    
def magical_constraint( vector, next_transform, prev_transforms ):
    """
        MAGICAL RESISTANCE AND IMMUNITY

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[4] <= 1:
        return True
    else:
        return False
    
def nightmarish_constraint( vector, next_transform, prev_transforms ):
    """
        NIGHTMARISH

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[5] <= 1:
        return True
    else:
        return False
    
def overwhelming_constraint( vector, next_transform, prev_transforms ):
    """
        OVERWHELMING

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if 0 <= transformed_vector[6] <= 1:
        return True
    else:
        return False

def toughness_constraint( vector, next_transform, prev_transforms ):
    """
        TOUGHNESS

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if transformed_vector[1] > 0:
        return True
    else:
        return False
    
def toughness_constraint( vector, next_transform, prev_transforms ):
    """
        TOUGHNESS

    """
    transformed_vector = next_transform( current_rules( vector, prev_transforms ) )
    if transformed_vector[1] > 0:
        return True
    else:
        return False