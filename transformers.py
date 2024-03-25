from icecream import ic
from params import DEBUG_LVL
from tools import debugger as db


# generalizable functions
def increase( vector, dimension ):
    """ Increases a dimension in a vector by 1 """
    return vector._replace(**{ dimension: getattr(vector,dimension) + 1} )

def decrease( vector, dimension ):
    """ Decreases a dimension in a vector by 1 """
    return vector._replace(**{ dimension: getattr(vector,dimension) - 1} )

def cycle_int( integer, mod ):
    """ Cycles an integer up, 0 thru mod-1 """
    return (integer + 1) % mod

def cycle( vector, dimension, mod ):
    """ Cycles a dimension in a vector from 0 through mod-1 """
    return vector._replace( **{ dimension : (getattr( vector, dimension) + 1) % mod } )

def add_to_list( l, element ):
    return l + [ element ]

def remove_from_list( l, element ):
    return l[ :l.index(element) ] + l[ l.index(element)+1: ]

def inc_freq( dictionary, key ):
    return { m:f+1 if m.upper() == key.upper() else f for m,f in dictionary.items() }

def dec_freq( dictionary, key ):
    return { m:f-1 if m.upper() == key.upper() else f for m,f in dictionary.items() }

def inc_max_skill( skill ):
    db( 3 )
    return increase( skill, 'max_'+skill )

def dec_max_skill( skill ):
    db( 3 )
    return decrease( skill, 'max_'+skill )

def inc_current_skill( skill ):
    db( 3 )
    return increase( skill, 'current_'+skill )

def dec_current_skill( skill ):
    db( 3 )
    return decrease( skill, 'current_'+skill )

# board

def add_investigator( vector, investigator ):
    return add_to_list( vector, investigator )

def remove_investigator( vector, investigator ):
    return remove_from_list( vector, investigator )

def advance_current_phase( integer ):
    return cycle_int( integer, 4 )

def toggle_bookkeeping( integer ):
    return cycle_int( integer, 2 )

def set_ancient_one( vector, ancient_one ):
    return add_to_list( vector, ancient_one )

def set_awakened( awakened ):
    return awakened + 1

def inc_doom_track( integer ):
    return integer + 1

def dec_doom_track( integer ):
    return integer - 1

def inc_terror_track( integer ):
    return integer + 1

def dec_terror_track( integer ):
    return integer - 1

def inc_gates_in_arkham( integer ):
    return integer + 1

def dec_gates_in_arkham( integer ):
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
    return integer + 1

def dec_monster_count( integer ):
    return integer - 1

def remove_monster_limit( integer ):
    """Intended for removing the monster limit"""
    return float('-inf')

def inc_outskirts_count( integer ):
    return integer + 1

def dec_outskirts_count( integer ):
    return integer - 1

def add_monster_location( vector, dimension, location ):
    return [ locs + [location] if dim == dimension else locs for dim, locs in enumerate( vector ) ]

def remove_monster_location( vector, dimension, location ):
    return [ locs[:locs.index(location)] + locs[locs.index(location)+1:] if dim == dimension else locs for dim, locs in enumerate( vector ) ] 

# locations

def add_occupant( location_occupants, new_occupant ):
    db( 3 )
    return add_to_list( location_occupants, new_occupant )

def remove_occupant( location_occupants, old_occupant ):
    db( 3 )
    return remove_from_list( location_occupants, old_occupant )

def add_gate_to( location_gate_to, new_gate ):
    db( 3 )
    return add_to_list( location_gate_to, new_gate )

def remove_gate_to( location_gate_to, old_gate ):
    db( 3 )
    return remove_from_list( location_gate_to, old_gate )
    
def inc_loc_clues( location ):
    db( 3 )
    return increase( location, 'clues' )

def dec_loc_clues( location ):
    db( 3 )
    return decrease( location, 'clues' )

def inc_historical_clues( location ):
    db( 3 )
    return increase( location, 'historical_clues' )

def dec_historical_clues( location ):
    db( 3 )
    return decrease( location, 'historical_clues' )

def add_seal( location ):
    db( 3 )
    return increase( location, 'sealed' )

def remove_seal( location ):
    db( 3 )
    return decrease( location, 'sealed' )

def add_gate( location ):
    db( 3 )
    return increase( location, 'gate' )

def remove_gate( location ):
    db( 3 )
    return decrease( location, 'gate' )

def inc_historical_gates( location ):
    db( 3 )
    return increase( location, 'historical_gates' )

def dec_historical_gates( location ):
    db( 3 )
    return decrease( location, 'historical_gates' )

def add_explored( location ):
    db( 3 )
    return increase( location, 'explored' )

def remove_explored( location ):
    db( 3 )
    return decrease( location, 'explored' )

def add_closed( location ):
    db( 3 )
    return increase( location, 'closed' ) 

def remove_closed( location ):
    db( 3 )
    return decrease( location, 'closed' )

# monsters

def set_movement( rulesets, move_rules ):
    db( 3 )
    return rulesets._replace( movement=move_rules )

def set_combat( rulesets, combat_rules ):
    db( 3 )
    return rulesets._replace( combat=combat_rules )

def set_evade( rulesets, evade_rules ):
    db( 3 )
    return rulesets._replace( evade=evade_rules )

def add_ambush( abilities ):
    db( 3 )
    return increase( abilities, 'ambush' )

def remove_ambush( abilities ):
    db( 3 )
    return decrease( abilities, 'ambush' )

def add_endless( abilities ):
    db( 3 )
    return increase( abilities, 'endless' )

def remove_endless( abilities ):
    db( 3 )
    return decrease( abilities, 'endless' )

def add_undead( abilities ):
    db( 3 )
    return increase( abilities, 'undead' )

def remove_undead( abilities ):
    db( 3 )
    return decrease( abilities, 'undead' )

def set_physical_immunity( abilities ):
    db( 3 )
    return abilities._replace( physical=0 )

def set_physical_resistance( abilities ):
    db( 3 )
    return abilities._replace( physical=0.5 )

def remove_physical( abilities ):
    db( 3 )
    return abilities._replace( physical=1 )

def set_magical_immunity( abilities ):
    db( 3 )
    return abilities._replace( magical=0 )

def set_magical_resistance( abilities ):
    db( 3 )
    return abilities._replace( magical=0.5 )

def remove_magical( abilities ):
    db( 3 )
    return abilities._replace( magical=1 )

def inc_nightmarish( abilities ):
    db( 3 )
    return increase( abilities, 'nightmarish' )

def dec_nightmarish( abilities ):
    db( 3 )
    return decrease( abilities, 'nightmarish' )

def inc_overwhelming( abilities ):
    db( 3 )
    return increase( abilities, 'overwhelming' )

def dec_overwhelming( abilities ):
    db( 3 )
    return decrease( abilities, 'overwhelming' )

def inc_awareness( stats ):
    db( 3 )
    return increase( stats, 'awareness' )

def dec_awareness( stats ):
    db( 3 )
    return decrease( stats, 'awareness' )

def inc_toughness( stats ):
    db( 3 )
    return increase( stats, 'toughness' )

def dec_toughness( stats ):
    db( 3 )
    return decrease( stats, 'toughness' )

def inc_horror_mod( stats ):
    db( 3 )
    return increase( stats, 'horror_mod' )

def dec_horror_mod( stats ):
    db( 3 )
    return decrease( stats, 'horror_mod' )

def inc_horror_received( stats ):
    db( 3 )
    return increase( stats, 'horror' )

def dec_horror_received( stats ):
    db( 3 )
    return decrease( stats, 'horror' )

def inc_combat_mod( stats ):
    db( 3 )
    return increase( stats, 'combat_mod' )

def dec_combat_mod( stats ):
    db( 3 )
    return decrease( stats, 'combat_mod' )

def inc_damage_received( stats ):
    db( 3 )
    return increase( stats, 'damage' )

def dec_damage_received( stats ):
    db( 3 )
    return decrease( stats, 'damage' )

# investigators

def inc_max_damage( damage ):
    db( 3 )
    return increase( damage, 'max_damage' )

def dec_max_damage( damage ):
    db( 3 )
    return decrease( damage, 'max_damage' )

def inc_current_damage( damage ):
    db( 3 )
    return increase( damage, 'current_damage' )

def dec_current_damage( damage ):
    db( 3 )
    return decrease( damage, 'current_damage' )

def set_unconscious( damage ):
    db( 3 )
    return increase( damage, 'unconscious' )

def set_conscious( damage ):
    db( 3 )
    return decrease( damage, 'unconscious' )

def inc_max_horror( horror ):
    db( 3 )
    return increase( horror, 'max_horror' )

def dec_max_horror( horror ):
    db( 3 )
    return decrease( horror, 'max_horror' )

def inc_current_horror( horror ):
    db( 3 )
    return increase( horror, 'current_horror' )

def dec_current_horror( horror ):
    db( 3 )
    return decrease( horror, 'current_horror' )

def set_insane( horror ):
    db( 3 )
    return increase( horror, 'insane' )

def set_sane( horror ):
    db( 3 )
    return decrease( horror, 'insane' )

def add_lost_in_time_and_space( conditions ):
    db( 3 )
    return increase( conditions, 'lost_in_time_and_space' )

def remove_lost_in_time_and_space( conditions ):
    db( 3 )
    return decrease( conditions, 'lost_in_time_and_space' )

def add_delayed( conditions ):
    db( 3 )
    return increase( conditions, 'delayed' )

def remove_delayed( conditions ):
    db( 3 )
    return decrease( conditions, 'delayed' )

def add_arrested( conditions ):
    db( 3 )
    return increase( conditions, 'arrested' )

def remove_arrested( conditions ):
    db( 3 )
    return decrease( conditions, 'arrested' )

def add_retainer( conditions ):
    db( 3 )
    return increase( conditions, 'retainer' )

def remove_retainer( conditions ):
    db( 3 )
    return decrease( conditions, 'retainer' )

def add_bank_loan( conditions ):
    db( 3 )
    return increase( conditions, 'bank_loan' )

def remove_bank_loan( conditions ):
    db( 3 )
    return decrease( conditions, 'bank_loan' )

def set_bankrupt( conditions ):
    db( 3 )
    return conditions._replace( bank_loan=float('inf') )

def add_stl_membership( conditions ):
    db( 3 )
    return increase( conditions, 'stl_membership' )

def remove_stl_membership( conditions ):
    db( 3 )
    return decrease( conditions, 'stl_membership' )

def add_deputized( conditions ):
    db( 3 )
    return increase( conditions, 'deputized' )

def remove_deputized( conditions ):
    db( 3 )
    return decrease( conditions, 'deputized' )

def add_blessing( conditions ):
    db( 3 )
    return increase( conditions, 'blessed_cursed' )

def remove_blessing( conditions ):
    db( 3 )
    return decrease( conditions, 'blessed_cursed' )

def add_curse( conditions ):
    db( 3 )
    return add_blessing( conditions )

def remove_curse( conditions ):
    db( 3 )
    return remove_blessing( conditions )

# skills

def inc_max_focus( focus ):
    db( 3 )
    return increase( focus, 'max_focus' )

def dec_max_focus( focus ):
    db( 3 )
    return decrease( focus, 'max_focus' )

def inc_current_focus( focus ):
    db( 3 )
    return increase( focus, 'current_focus' )

def dec_current_focus( focus ):
    db( 3 )
    return decrease( focus, 'current_focus' )

def inc_max_speed( speed ):
    db( 3 )
    return increase( speed, 'max_speed' )

def dec_max_speed( speed ):
    db( 3 )
    return decrease( speed, 'max_speed' )

def inc_current_speed( speed ):
    db( 3 )
    return increase( speed, 'current_speed' )

def dec_current_speed( speed ):
    db( 3 )
    return decrease( speed, 'current_speed' )

def inc_current_sneak( speed ):
    db( 3 )
    return decrease( speed, 'current_speed' )

def dec_current_sneak( speed ):
    db( 3 )
    return increase( speed, 'current_speed' )

def inc_sum_speed_sneak( speed ):
    db( 3 )
    return increase( speed, 'speed_sneak_sum' )

def dec_sum_speed_sneak( speed ):
    db( 3 )
    return decrease( speed, 'speed_sneak_sum' )

def inc_max_fight( fight ):
    db( 3 )
    return increase( fight, 'max_fight' )

def dec_max_fight( fight ):
    db( 3 )
    return decrease( fight, 'max_fight' )

def inc_current_fight( fight ):
    db( 3 )
    return increase( fight, 'current_fight' )

def dec_current_fight( fight ):
    db( 3 )
    return decrease( fight, 'current_fight' )

def inc_current_will( fight ):
    db( 3 )
    return decrease( fight, 'current_fight' )

def dec_current_will( fight ):
    db( 3 )
    return increase( fight, 'current_fight' )

def inc_sum_fight_will( fight ):
    db( 3 )
    return increase( fight, 'fight_will_sum' )

def dec_sum_fight_will( fight ):
    db( 3 )
    return decrease( fight, 'fight_will_sum' )

def inc_max_lore( lore ):
    db( 3 )
    return increase( lore, 'max_lore' )

def dec_max_lore( lore ):
    db( 3 )
    return decrease( lore, 'max_lore' )

def inc_current_lore( lore ):
    db( 3 )
    return increase( lore, 'current_lore' )

def dec_current_lore( lore ):
    db( 3 )
    return decrease( lore, 'current_lore' )

def inc_current_luck( fight ):
    db( 3 )
    return decrease( fight, 'current_fight' )

def dec_current_luck( fight ):
    db( 3 )
    return increase( fight, 'current_fight' )

def inc_sum_lore_luck( lore ):
    db( 3 )
    return increase( lore, 'lore_luck_sum' )

def dec_sum_lore_luck( lore ):
    db( 3 )
    return decrease( lore, 'lore_luck_sum' )

def change_location( location, new_loc_id ):
    db( 3 )
    return location._replace( current_location=new_loc_id )

def inc_mvmt_points( location ):
    db( 3 )
    return increase( location, 'mvmt_points' )

def dec_mvmt_points( location ):
    db( 3 )
    return decrease( location, 'mvmt_points' )

def add_in_arkham( location ):
    db( 3 )
    return increase( location, 'in_arkham' )

def remove_in_arkham( location ):
    db( 3 )
    return decrease( location, 'in_arkham' )

def inc_hands( equipped_items ):
    db( 3 )
    return increase( equipped_items, 'hands' )

def dec_hands( equipped_items ):
    db( 3 )
    return decrease( equipped_items, 'hands' )

def equip_item( equipped_items, item ):
    db( 3 )
    return equipped_items._replace( equipment = add_to_list( equipped_items, item ) )

def dequip_item( equipped_items, item ):
    db( 3 )
    return equipped_items._replace( equipment = remove_from_list( equipped_items, item ) )

def exhaust_item( exhausted_items, item ):
    db( 3 )
    return add_to_list( exhausted_items, item )

def refresh_exhausted( exhausted_items ):
    db( 3 )
    return exhausted_items[:0] 

# possessions

def inc_money( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'money' else v) for k,v in possessions.items() }

def dec_money( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'money' else v) for k,v in possessions.items() }

def inc_inv_clues( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'clues' else v) for k,v in possessions.items() }

def dec_inv_clues( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'clues' else v) for k,v in possessions.items() }

def inc_gate_trophies( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'gate_trophies' else v) for k,v in possessions.items() }

def dec_gate_trophies( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'gate_trophies' else v) for k,v in possessions.items() }

def inc_monster_trophies( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'monster_trophies' else v) for k,v in possessions.items() }

def dec_monster_trophies( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'monster_trophies' else v) for k,v in possessions.items() }

def add_item( possessions, variety, item ):
    db( 3 )
    return { k:(v+[item] if k == variety else v) for k,v in possessions.items() }

def remove_item( possessions, variety, item ):
    db( 3 )
    return { k:( v[:v.index(item)] + v[v.index(item)+1:] if k == variety else v) for k,v in possessions.items() }

def add_weapon( possessions, item ):
    db( 3 )
    return add_item( possessions, 'weapons', item )
    
def remove_weapon_item( possessions, item ):
    db( 3 )
    return remove_item( possessions, 'weapons', item )

def add_consumable_item( possessions, item ):
    db( 3 )
    return add_item( possessions, 'consumables', item )

def remove_consumable_item( possessions, item ):
    db( 3 )
    return remove_item( possessions, 'consumables', item )

def add_tome_item( possessions, item ):
    db( 3 )
    return add_item( possessions, 'tomes', item )

def remove_tome_item( possessions, item ):
    db( 3 )
    return remove_item( possessions, 'tomes', item )

def add_passive_buff( possessions, item ):
    db( 3 )
    return add_item( possessions, 'passive_buffs', item )

def remove_passive_buff( possessions, item ):
    db( 3 )
    return remove_item( possessions, 'passive_buffs', item )

def add_active_buff( possessions, item ):
    db( 3 )
    return add_item( possessions, 'active_buffs', item )

def remove_active_buff( possessions, item ):
    db( 3 )
    return remove_item( possessions, 'active_buffs', item )

def add_oddity_item( possessions, item ):
    db( 3 )
    return add_item( possessions, 'oddities', item )

def remove_oddity_item( possessions, item ):
    db( 3 )
    return remove_item( possessions, 'oddities', item )

def add_spell( possessions, spell ):
    db( 3 )
    return add_item( possessions, 'spells', spell )

def remove_spell( possessions, spell ):
    db( 3 )
    return remove_item( possessions, 'spells', spell )

def add_ally( possessions, ally ):
    db( 3 )
    return add_item( possessions, 'allies', ally )

def remove_ally( possessions, ally ):
    db( 3 )
    return remove_item( possessions, 'allies', ally )

# non-specific item transforms

def inc_price( item ):
    """ Increases the item price """
    db( 3 )
    return increase( item, 'price' )

def dec_price( item ):
    """ Decreases the item price """
    db( 3 )
    return decrease( item, 'price' )

def inc_bonus( item ):
    """ Increases item bonus """
    db( 3 )
    return increase( item, 'bonus' )

def dec_bonus( item ):
    """ Decreases item bonus """
    db( 3 )
    return decrease( item, 'bonus' )

def inc_sanity_cost( item ):
    """ Increases item sanity cost """
    db( 3 )
    return increase( item, 'sanity_cost' )

def dec_sanity_cost( item ):
    """ Decrease item sanity cost """
    db( 3 )
    return decrease( item, 'sanity_cost' )

# weapons-specific transforms

def change_modality( weapon ):
    """ Changes a physical weapon in a magical one, a magical into physical """
    db( 3 )
    return cycle( weapon, 'modality', 2 )

def change_exhaustable( weapon ):
    """ Makes a non-exhaustible weapon exhaustable, exhaustible to non """
    db( 3 )
    return cycle( weapon, 'exhaustable', 2 )

def change_losable( weapon ):
    """ Makes a non-losable weapon losable, losable to non """
    db( 3 )
    return cycle( weapon, 'losable', 2 )

# gates

def inc_gate_modifier( gate ):
    db( 3 )
    return increase( gate, 'modifier' )

def dec_gate_modifier( gate ):
    db( 3 )
    return decrease( gate, 'modifier' )
