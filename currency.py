from icecream import ic

def __current_stat__( vector, transforms ):
    v = vector
    for transform in transforms:
        v = transform[0]( v, *transform[1:]) if type( transform ) == tuple  else transform(v)
    return v

# board

def boardInvestigators( investigators, transformations ):
    return __current_stat__( investigators, transformations )

def boardCurrentPlayer( current_player: int, transformations: list ) -> int:
    return __current_stat__( current_player, transformations )

def boardCurrentPhase( current_phase, transformations ):
    return __current_stat__( current_phase, transformations )

def boardBookkeeping( bookkeeping, transformations ):
    return __current_stat__( bookkeeping, transformations )

def board_ancient_one( ancient_one, transformations ):
    return __current_stat__( ancient_one, transformations )

def board_awakened( awakened, transformations ):
    return __current_stat__( awakened, transformations )

def board_doom_track( doom_track, transformations ):
    return __current_stat__( doom_track, transformations )

def board_terror_track( terror_track, transformations ):
    return __current_stat__( terror_track, transformations )

def boardGatesInArkham( gates_in_arkham, transformations ):
    return __current_stat__( gates_in_arkham, transformations )

def board_gates_sealed( gates_sealed, transformations ):
    return __current_stat__( gates_sealed, transformations )

def board_clues_to_seal( clues_to_seal, transformations ):
    return __current_stat__( clues_to_seal, transformations )

def boardWinCond( win_cond, transformations ):
    return __current_stat__( win_cond, transformations )

def board_monsters_in_arkham( monster_limit, transformations ):
    return __current_stat__( monster_limit, transformations )

def board_monsters_in_outskirts( outskirts_limit, transformations ):
    return __current_stat__( outskirts_limit, transformations )

def board_monster_locations( monster_locations, transformations ):
    return __current_stat__( monster_locations, transformations )

# mythos

def mythosHeadline( headline, transformations ):
    return __current_stat__( headline, transformations )

def mythosMystic( mystic, transformations ):
    return __current_stat__( mystic, transformations )

def mythosUrban( urban, transformations ):
    return __current_stat__( urban, transformations )

def mythosWeather( weather, transformations ):
    return __current_stat__( weather, transformations )

def mythosModifiers( modifiers, transformations ):
    return __current_stat__( modifiers, transformations )

def mythosBannedMonster( bannedMonster, transformations ):
    return __current_stat__( bannedMonster, transformations )

def mythosResolution( resolution, transformations ):
    return __current_stat__( resolution, transformations )

# decks 

def deckFrequency( deck, transformations ):
    return __current_stat__( deck, transformations )

# locations 

def location_investigators( location, transformations ):
    return __current_stat__( location, transformations )

def location_occupants( location, transformations):
    return __current_stat__( location, transformations )

def location_gate_to( location, transformations ):
    return __current_stat__( location, transformations )

def locationStatus( location, transformations ):
    return __current_stat__( location, transformations )

def graph( graph, transformations ):
    return __current_stat__( graph, transformations )

# monsters

def monster_rulesets( rulesets, transformations ):
    return __current_stat__( rulesets, transformations )

def monster_abilities( abilities, transformations ):
    return __current_stat__( abilities, transformations )

def monster_stats( stats, transformations ):
    return __current_stat__( stats, transformations )

# investigators

def investigatorDamage( damage, transformations ):
    return __current_stat__( damage, transformations )

def investigatorHorror( horror, transformations ):
    return __current_stat__( horror, transformations )

def investigatorConditions( conditions, transformations ):
    return __current_stat__( conditions, transformations )

def investigatorFocus( focus, transformations ):
    return __current_stat__( focus, transformations )

def investigatorSkill( skill, transformations ):
    return __current_stat__( skill, transformations )

def investigatorComplementSkill( skill, transformations ):
    return skill[2] - investigatorSkill( skill, transformations )[1]

def investigatorLocation( location, transformations ):
    return __current_stat__( location, transformations )

def investigatorEquippedItems( equipped_items, transformations ):
    return __current_stat__( equipped_items, transformations )

def investigatorExhaustedItems( exhausted_items, transformations ):
    return __current_stat__( exhausted_items, transformations )

def investigatorPossessions( possessions, transformations ):
    return __current_stat__( possessions, transformations )

# items

def item_stats( stats, transformations ):
    return __current_stat__( stats, transformations )

# gates

def gateFreqs( gates_deck, transformations ):
    return __current_stat__( gates_deck, transformations )