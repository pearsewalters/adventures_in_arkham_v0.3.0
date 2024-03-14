
# locations 

def add_occupant( vector, occupant ):
    return vector + [ occupant ]

def remove_occupant( vector, occupant ):
    return vector[:vector.index(occupant)] + vector[vector.index(occupant)+1:]

def inc_clue( vector ):
    return [ v + 1 if n == 0 else v for n,v in enumerate(vector) ]

def dec_clue( vector ):
    return [ v - 1 if n == 0 else v for n,v in enumerate(vector) ]

def inc_historical_clues( vector ):
    return [ v + 1 if n == 1 else v for n,v in enumerate(vector) ]

def add_seal( vector ):
    return [ v + 1 if n == 2 else v for n,v in enumerate(vector) ]

def remove_seal( vector ):
    return [ v - 1 if n == 2 else v for n,v in enumerate(vector) ]

def add_gate( vector ):
    return [ v + 1 if n == 3 else v for n,v in enumerate(vector) ]

def remove_gate( vector ):
    return [ v - 1 if n == 3 else v for n,v in enumerate(vector) ]

def mark_explored( vector ):
    return [ v + 1 if n == 4 else v for n,v in enumerate(vector) ]

def mark_unexplored( vector ):
    return [ v - 1 if n == 4 else v for n,v in enumerate(vector) ]

def mark_closed( vector ):
    return [ v + 1 if n == 5 else v for n,v in enumerate(vector) ]

def mark_open( vector ):
    return [ v + 1 if n == 5 else v for n,v in enumerate(vector) ]


# investigators

# health

def inc_health_stat( matrix ):
    return [ matrix[0], matrix[1] + 1, matrix[2] ]

def dec_health_stat( matrix ):
    return [ matrix[0], matrix[1] - 1, matrix[2] ]

def inc_damage( matrix ):
    return [ matrix[0], matrix[1] + 1, matrix[2] ]

def dec_damage( matrix ):
    return [ matrix[0], matrix[1] - 1, matrix[2] ]

def inc_max_damage( matrix ):
    return [ matrix[0] + 1, matrix[1], matrix[2] ]

def dec_max_damage( matrix ):
    return [ matrix[0] - 1, matrix[1], matrix[2] ]

def inc_horror( matrix ):
    return inc_damage( matrix )

def dec_horror( matrix ):
    return dec_damage( matrix )

def inc_max_horror( matrix ):
    return inc_max_damage( matrix )

def dec_max_horror( matrix ):
    return dec_max_damage( matrix )

def set_uncon( matrix ):
    return [ matrix[0], matrix[1], matrix[2] + 1 ]

def set_con( matrix ):
    return [ matrix[0], matrix[1], matrix[2] - 1 ]

def set_insane( matrix ):
    return set_uncon( matrix )

def set_sane( matrix ):
    return set_con( matrix )

# conditions

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

def add_curse( matrix ):
    return remove_blessing( matrix )

def remove_curse( matrix ):
    return add_blessing( matrix )

# skills

def inc_skill( matrix ):
    return [ matrix[0], matrix[1]+1, matrix[2] ]

def dec_skill( matrix ):
    return [ matrix[0], matrix[1]-1, matrix[2] ]

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

# locational

def change_loc( matrix, new_loc ):
    return [ new_loc, matrix[1], matrix[2] ]

def move_to_CURIOSITIE_SHOPPE( matrix ):
    return change_loc( matrix, 1 )

def move_to_NEWSPAPER( matrix ):
    return change_loc( matrix, 2 )

def move_to_TRAIN_STATION( matrix ):
    return change_loc( matrix, 3 )

def move_to_NORTHSIDE_STREETS( matrix ):
    return change_loc( matrix, 29 )

def move_to_ARKHAM_ASYLUM( matrix ):
    return change_loc( matrix, 4 )

def move_to_BANK_OF_ARKHAM( matrix ):
    return change_loc( matrix, 5 )

def move_to_INDEPENDENCE_SQUARE( matrix ):
    return change_loc( matrix, 6)

def move_to_DOWNTOWN_STREETS( matrix ):
    return change_loc( matrix, 30)

def move_to_HIBBS_ROADHOUSE( matrix ):
    return change_loc( matrix, 7 )

def move_to_POLICE_STATION( matrix ):
    return change_loc( matrix, 8 )

def move_to_JAIL( matrix ):
    return change_loc( matrix, 9)

def move_to_VELMAS_DINER( matrix ):
    return change_loc( matrix, 10)

def move_to_DOWNTOWN_STREETS( matrix ):
    return change_loc( matrix, 31)

def move_to_RIVER_DOCKS( matrix ):
    return change_loc( matrix, 11 )

def move_to_THE_UNNAMEABLE( matrix ):
    return change_loc( matrix, 12 )

def move_to_UNVISITED_ISLE( matrix ):
    return change_loc( matrix, 13)

def move_to_MERCHANT_DISTRICT_STREETS( matrix ):
    return change_loc( matrix, 32)

def move_to_BLACK_CAVE( matrix ):
    return change_loc( matrix, 14 )

def move_to_GENERAL_STORE( matrix ):
    return change_loc( matrix, 15 )

def move_to_GRAVEYARD( matrix ):
    return change_loc( matrix, 16)

def move_to_RIVERTOWN_STREETS( matrix ):
    return change_loc( matrix, 33)

def move_to_ADMINISTRATION( matrix ):
    return change_loc( matrix, 17 )

def move_to_SCIENCE_BUILDING( matrix ):
    return change_loc( matrix, 18 )

def move_to_LIBRARY( matrix ):
    return change_loc( matrix, 19)

def move_to_MISKATONIC_UNIVERSITY_STREETS( matrix ):
    return change_loc( matrix, 34)

def move_to_THE_WITCH_HOUSE( matrix ):
    return change_loc( matrix, 20 )

def move_to_THE_SILVER_TWILIGHT_LODGE( matrix ):
    return change_loc( matrix, 21 )

def move_to_THE_INNER_SANCTUM( matrix ):
    return change_loc( matrix, 22)

def move_to_FRENCH_HILL_STREETS( matrix ):
    return change_loc( matrix, 35)

def move_to_ST_MARYS_HOSPITAL( matrix ):
    return change_loc( matrix, 23 )

def move_to_WOODS( matrix ):
    return change_loc( matrix, 24 )

def move_to_YE_OLDE_MAGICK_SHOPPE( matrix ):
    return change_loc( matrix, 25)

def move_to_UPTOWN_STREETS( matrix ):
    return change_loc( matrix, 36)

def move_to_MAS_BOARDING_HOUSE( matrix ):
    return change_loc( matrix, 26 )

def move_to_HISTORICAL_SOCIETY( matrix ):
    return change_loc( matrix, 27 )

def move_to_SOUTH_CHURCH( matrix ):
    return change_loc( matrix, 28)

def move_to_SOUTHSIDE_STREETS( matrix ):
    return change_loc( matrix, 37)

def inc_movement( matrix ):
    return [ matrix[0], matrix[1]+1, matrix[2] ]

def dec_movement( matrix ):
    return [ matrix[0], matrix[1]-1, matrix[2] ]

def set_in_arkham( matrix ):
    return [ matrix[0], matrix[1], matrix[2]+1 ]

def set_in_other_world( matrix ):
    return [ matrix[0], matrix[1], matrix[2]-1 ]


# equipment

def inc_hands( matrix ):
    return [ matrix[0]+1, matrix[1] ]

def dec_hands( matrix ):
    return [ matrix[0]-1, matrix[1] ]

def equip_item( matrix, item ):
    return [ matrix[0], matrix[1]+[item] ]

def unequip( matrix, item ):
    return [ matrix[0], matrix[1][:matrix[1].index(item)] + matrix[1][matrix[1].index(item)+1:] ]

# exhausted items

def exhaust_item( matrix, item ):
    return matrix + [item]

def refresh_items( matrix ):
    return matrix[:0]


# possessions

def inc_money( dictionary ):
    return { k:(v+1 if k == 'money' else v) for k,v in dictionary.items() }

def dec_money( dictionary ):
    return { k:(v-1 if k == 'money' else v) for k,v in dictionary.items() }

def inc_clues( dictionary ):
    return { k:(v+1 if k == 'clues' else v) for k,v in dictionary.items() }

def dec_clues( dictionary ):
    return { k:(v-1 if k == 'clues' else v) for k,v in dictionary.items() }

def inc_gate_trophies( dictionary ):
    return { k:(v+1 if k == 'gate_trophies' else v) for k,v in dictionary.items() }

def dec_gate_trophies( dictionary ):
    return { k:(v-1 if k == 'gate_trophies' else v) for k,v in dictionary.items() }

def inc_monster_trophies( dictionary ):
    return { k:(v+1 if k == 'monster_trophies' else v) for k,v in dictionary.items() }

def dec_monster_trophies( dictionary ):
    return { k:(v-1 if k == 'monster_trophies' else v) for k,v in dictionary.items() }

def add_item( dictionary, variety, item ):
    return { k:(v+[item] if k == variety else v) for k,v in dictionary.items() }

def remove_item( dictionary, variety, item ):
    return { k:( v[:v.index(item)] + v[v.index(item)+1:] if k == variety else v) for k,v in dictionary.items() }

def add_common_item( dictionary, item ):
    return add_item( dictionary, 'common', item )

def remove_common_item( dictionary, item ):
    return remove_item( dictionary, 'common', item )

def add_unique_item( dictionary, item ):
    return add_item( dictionary, 'unique', item )

def remove_unique_item( dictionary, item ):
    return remove_item( dictionary, 'unique', item )

def add_spell( dictionary, spell ):
    return add_item( dictionary, 'spells', spell )

def remove_spell( dictionary, spell ):
    return remove_item( dictionary, 'spells', spell )

def add_buff( dictionary, buff  ):
    return add_item( dictionary, 'buffs', buff )

def remove_buff( dictionary, buff ):
    return remove_item( dictionary, 'buffs', buff )

def add_ally( dictionary, ally ):
    return add_item( dictionary, 'allies', ally )

def remove_ally( dictionary, ally ):
    return remove_item( dictionary, 'allies', ally )

# board

def add_investigator( vector, investigator ):
    return vector + [ investigator ]

def remove_investigator( vector, investigator ):
    return vector[:vector.index(investigator)] + vector[vector.index(investigator)+1:] 

def advance_current_phase( integer ):
    return (integer + 1) % 4

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
