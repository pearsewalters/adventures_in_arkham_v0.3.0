def __current_stat__( vector, transforms ):
    v = vector
    for transform in transforms:
        v = transform[0]( v, transform[1]) if type( transform ) == tuple  else transform(v)
    return v

# board

def board_investigators( investigators, transformations ):
    return __current_stat__( investigators, transformations )

def board_current_player( current_player, transformations ):
    return __current_stat__( current_player, transformations )

def board_current_phase( current_phase, transformations ):
    return __current_stat__( current_phase, transformations )

def board_bookkeeping( bookkeeping, transformations ):
    return __current_stat__( bookkeeping, transformations )

def board_ancient_one( ancient_one, transformations ):
    return __current_stat__( ancient_one, transformations )

def board_awakened( awakened, transformations ):
    return __current_stat__( awakened, transformations )

def board_doom_track( doom_track, transformations ):
    return __current_stat__( doom_track, transformations )

def board_terror_track( terror_track, transformations ):
    return __current_stat__( terror_track, transformations )

def board_gates_in_arkham( gates_in_arkham, transformations ):
    return __current_stat__( gates_in_arkham, transformations )

def board_gates_sealed( gates_sealed, transformations ):
    return __current_stat__( gates_sealed, transformations )

def board_clues_to_seal( clues_to_seal, transformations ):
    return __current_stat__( clues_to_seal, transformations )

def board_win_cond( win_cond, transformations ):
    return __current_stat__( win_cond, transformations )

def board_monsters_in_arkham( monster_limit, transformations ):
    return __current_stat__( monster_limit, transformations )

def board_monsters_in_outskirts( outskirts_limit, transformations ):
    return __current_stat__( outskirts_limit, transformations )

def board_monster_locations( monster_locations, transformations ):
    return __current_stat__( monster_locations, transformations )

# decks 

def deck_frequency( deck, transformations ):
    return __current_stat__( deck, transformations )

# locations 

def location_investigators( location, transformations ):
    return __current_stat__( location, transformations )

def location_occupants( location, transformations):
    return __current_stat__( location, transformations )

def location_gate_to( location, transformations ):
    return __current_stat__( location, transformations )

def location_status( location, transformations ):
    return __current_stat__( location, transformations )

# monsters

def monster_rulesets( rulesets, transformations ):
    return __current_stat__( rulesets, transformations )

def monster_abilities( abilities, transformations ):
    return __current_stat__( abilities, transformations )

def monster_stats( stats, transformations ):
    return __current_stat__( stats, transformations )

# investigators

def investigator_damage( damage, transformations ):
    return __current_stat__( damage, transformations )

def investigator_horror( horror, transformations ):
    return __current_stat__( horror, transformations )

def investigator_conditions( conditions, transformations ):
    return __current_stat__( conditions, transformations )

def investigator_focus( focus, transformations ):
    return __current_stat__( focus, transformations )

def investigator_skill( skill, transformations ):
    return __current_stat__( skill, transformations )

def investigator_complement_skill( skill, transformations ):
    return skill[2] - investigator_skill( skill, transformations )[1]

def investigator_location( location, transformations ):
    return __current_stat__( location, transformations )

def investigator_equipped_items( equipped_items, transformations ):
    return __current_stat__( equipped_items, transformations )

def investigator_exhausted_items( exhausted_items, transformations ):
    return __current_stat__( exhausted_items, transformations )

def investigator_possessions( possessions, transformations ):
    return __current_stat__( possessions, transformations )

# items

def item_stats( stats, transformations ):
    return __current_stat__( stats, transformations )

# gates

def gate_freqs( gates_deck, transformations ):
    return __current_stat__( gates_deck, transformations )