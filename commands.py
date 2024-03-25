import time, transformers, constraints, phases, tools
from context import Context
from params import DEBUG_LVL
from icecream import ic

def quit_game():
    """ Will exit the game loop """
    confirm = input( 'Are you sure you want to quit? (y/n) ' ).strip().lower()
    if confirm == 'y':
        return True
    return False

def show_args( args ):
    if args:
        msg = ''
        for k,v in args.items():
            msg += f' - {k}{" "*(12-len(k))} \x1b[3m{v[1]}\x1b[23m\n'
        return msg
    return "No available args\n"

def show_commands( commands ):
    """ Displays list of commands """
    if commands:
        msg = 'Available commands: \n'
        msg += show_args( commands )
        msg += '\nTo see what arguments a command can receive, type \'[command] args\''
        return msg
    return "No available commands\n"

def show( context: Context, view ):
    """ Dispatch for show_view functions """
    views = {
        'status' : ( show_status, "Display investigator health and conditions"),
        'possessions' : (show_possessions, "Display investigator inventory, equipped and exhausted items"),
        'skills' : (show_skills, "Display current skill levels")
    }
    if view == 'args':
        return show_args( views )
    elif view not in views:
        return 'That is not a valid view. Try again.' 
    return views[view][0]( context )

def show_possessions( context: Context ):
    """ Displays investigator possessions """

    nickname = context.investigator.nickname
    possessions = context.investigator.possessions
    equipment = context.investigator.equipment
    exhausted = context.investigator.exhausted_items

    display = f'{nickname}\'s Current Possessions\n{"+"*20}\n'

    display += f"${possessions['money']} {'.'*5} CLUES: {possessions['clues']}\n"
    display += f"EQUIPPED: [{','.join(equipment)}]\n"
    display += f"EXHAUSTED: [{','.join(exhausted)}]\n"
    display += f"MONSTER TROPHIES: {possessions['monster_trophies']} {'.'*5} GATE TROPHIES: {possessions['gate_trophies']}\n'"
    display += '\x1b[3;38;5;250mYou can exchange trophies for various things around town...\x1b[23;38;5;70m\n'

    def add_weapon_details( weapon, spacer ):
        d = []
        constants = context.weapons.constants.row( weapon )
        stats = context.weapons.defaults.row( weapon ).stats
        # modality
        if stats.modality == 1:
            d.append( 'magical' )
        elif stats.modality == 0:
            d.append( 'physical' ) 
        # bonus
        d.append( f'+{stats.bonus}' )
        # rarity
        d.append( constants.rarity ) 
        # uses
        if constants.uses == float('inf'):
            d.append( '∞ uses' )
        else:
            d.append( str(constants.uses) + ' use(s)' ) 
        # hands
        d.append( str(constants.hands) + '-handed' ) 

        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'
    
    def add_consumable_details( consumable, spacer ):
        d = []
        constants = context.consumables.constants.row( consumable )
        stats = context.consumables.defaults.row( consumable ).stats
        # bonus 
        if constants.stat:
            d.append( f'{stats.bonus} {constants.stat.upper()}' )
        # rarity
        d.append( constants.rarity )
        
        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'

    def add_tome_details( tome, spacer ):
        d = []
        constants = context.tomes.constants.row( tome )
        stats = context.tomes.defaults.row( tome ).stats
        # rarity
        d.append( constants.rarity )
        # mvmt points
        d.append( f'{stats.mvmt_cost} MVMT to read' )
        # horror
        if stats.sanity_cost == 0:
            how_many_horrors = 'not many'
        elif stats.sanity_cost == 1:
            how_many_horrors = 'several'
        elif stats.sanity_cost >= 2:
            how_many_horrors = 'many'
        d.append( f'contains {how_many_horrors} horrors' )
        # uses
        if constants.uses == float('inf'):
            d.append( '∞ uses' )
        else:
            d.append( str(constants.uses) + ' use(s)' ) 

        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'
    
    def add_passive_details( buff, spacer ):
        d = []
        constants = context.passive_buffs.constants.row( buff )
        stats = context.passive_buffs.defaults.row( buff ).stats
        # rarity
        d.append( constants.rarity )
        # bonus
        if constants.stat:
            d.append( f'+{stats.bonus} {constants.stat.upper()}' )
        elif constants.check:
            d.append( f'+{stats.bonus} {constants.check.upper()}' )
        
        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'

    def add_active_details( buff, spacer ):
        d = []
        constants = context.active_buffs.constants.row( buff )
        stats = context.active_buffs.defaults.row( buff ).stats
        # rarity
        d.append( constants.rarity )
        # available phase
        phases = []
        if '1' in str(constants.phase):
            phases.append('UPKEEP')
        elif '2' in str(constants.phase):
            phases.append('MOVEMENT')
        elif '3' in str(constants.phase):
            phases.append('ENCOUNTERS')
        d.append( f"available during {','.join(phases)} phases")
        # bonus
        if stats.bonus:
            d.append( f"exhaust for +{stats.bonus} {constants.stat.upper()}")
        # reroll
        if constants.check:
            d.append( f"exhaust to reroll a failed {constants.check} CHECK")

        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'

    def add_oddity_details( oddity, spacer ):
        d = []
        constants = context.oddities.constants.row( oddity )

        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'

    def add_spell_details( spell, spacer ):
        d = []
        constants = context.spells.constants.row( spell )
        # modifier
        if 1 < constants.modifier:
            d.append( 'elementary' )
        elif -1 <= constants.modifier <= 1:
            d.append( 'complicated' )
        elif constants.modifier < -1:
            d.append( 'intricate' )
        # sanity
        if constants.sanity_cost == 0:
            d.append( 'will not affect sanity' )
        if constants.sanity_cost == 1:
            d.append( 'slight affect on your sanity' )
        if constants.sanity_cost == 2:
            d.append( 'noticeable affect on your sanity' )
        # phase
        phases = []
        if '1' in str(constants.phase):
            phases.append('UPKEEP')
        elif '2' in str(constants.phase):
            phases.append('MOVEMENT')
        elif '3' in str(constants.phase):
            phases.append('ENCOUNTERS')
        d.append( f"available during {','.join(phases)} phases")
        # hands
        d.append( str(constants.hands) + '-handed' ) 

        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'
    
    def add_ally_details( ally, spacer ):
        d = []
        constants = context.allies.constants.row( ally )

        return f'{spacer}{constants.description}\n{spacer}( {" / ".join( d )} )'

    def add_poss_to_disp( poss, header, detail_func=None ):
        d = ''
        if type( poss ) == list and len(poss):
            d += f'{header}: \n '
            spacer = ' '*len(header)
            for item in poss:
                d += f'{spacer} - {item}\n'
                if detail_func != None:
                    d += detail_func( item, spacer ) + '\n\n'
                else:
                    d += '\n'
            return d + '\n'
        elif type( poss ) == int and poss > 0:
            d += f"{header}: \n "
            d += f"{' '*len(header)}   {item}\n"
        return d
    

    display += add_poss_to_disp( possessions['weapons'],'WEAPONS',add_weapon_details)
    display += add_poss_to_disp( possessions['consumables'],'CONSUMABLES',add_consumable_details)
    display += add_poss_to_disp( possessions['tomes'],'TOMES',add_tome_details)
    display += add_poss_to_disp( possessions['passive_buffs'],'PASSIVE BUFFS',add_passive_details)
    display += add_poss_to_disp( possessions['active_buffs'],'ACTIVE BUFFS',add_active_details)
    display += add_poss_to_disp( possessions['oddities'],'ODDITIES',add_oddity_details)
    display += add_poss_to_disp( possessions['spells'],'SPELLS',add_spell_details)
    display += add_poss_to_disp( possessions['allies'],'ALLIES',add_ally_details)

    return display + '\n'

def show_status( context: Context ):
    """ Displays investigator health, location, and conditions """
    nickname = context.investigator.nickname
    
    display = f"{nickname}\'s Current Status\n{'+'*20}\n"

    # health status
    max_damage = context.investigator.damage.max_damage
    current_damage = context.investigator.damage.current_damage
    consciousness = 'unconscious' if context.investigator.damage.unconscious else 'conscious'
    display_damage = f'{current_damage}/{max_damage}'

    max_horror = context.investigator.horror.max_horror
    current_horror = context.investigator.horror.current_horror
    sanity = 'insane' if context.investigator.horror.insane else 'sane'
    display_horror = f'{current_horror}/{max_horror}'

    display += f"DAMAGE: {display_damage} {'.'*5} HORROR: {display_horror}\n"
    display += f'{nickname} is currently {consciousness} and {sanity}\n\n'

    # location 
    location_id = context.investigator.location.current_location
    location_name = context.locations.constants.row_num( location_id ).name
    location_neighborhood = context.locations.constants.row_num( location_id ).neighborhood

    display += f'LOCATION: {location_name}, in the {location_neighborhood} neighborhood\n\n'

    # conditions 
    conditions = context.investigator.conditions
    display_conditions = ''

    if conditions.lost_in_time_and_space:
        display_conditions += f'{nickname} is currently lost in time & space\n'
    if conditions.delayed:
        display_conditions += f'{nickname} is currently delayed\n'
    if conditions.arrested:
        display_conditions += f'{nickname} is currently arrested\n'
    if conditions.retainer:
        display_conditions += f'{nickname} is earning money from a retainer\n'
    if 0 < conditions.bank_loan < float('inf'):
        display_conditions += f'{nickname} currently has a loan from the Bank of Arkham\n'
    if conditions.bank_loan == float('inf'):
        display_conditions += f'{nickname} bankrupted and is never again allowed to receive a loan from the Bank of Arkham\n'
    if conditions.stl_membership:
        display_conditions += f'{nickname} is a member of the Silver Twilight Lodge\n'
    if conditions.deuptized:
        display_conditions += f'{nickname} is a Deputy of Arkham. Monsters beware!\n'
    if conditions.blessed_cursed < 0:
        display_conditions += f'{nickname} is cursed!'
    if 0 < conditions.blessed_cursed:
        display_conditions += f'{nickname} is blessed!'

    display += display_conditions

    return display + '\n'

def show_skills( context: Context ):
    """ Displays investigator skills"""

    nickname = context.investigator.nickname
    
    focus = context.investigator.focus.current_focus
    mvmt = context.investigator.location.mvmt_points
    
    max_speed = context.investigator.speed.max_speed
    current_speed = context.investigator.speed.current_speed
    
    max_sneak = context.investigator.speed.speed_sneak_sum - max_speed + 3
    current_sneak = context.investigator.sneak
    
    max_fight = context.investigator.fight.max_fight
    current_fight = context.investigator.fight.current_fight
    
    max_will = context.investigator.fight.fight_will_sum - max_fight + 3
    current_will = context.investigator.will

    max_lore = context.investigator.lore.max_lore
    current_lore = context.investigator.lore.current_lore
    
    max_luck = context.investigator.lore.lore_luck_sum - max_lore + 3
    current_luck = context.investigator.luck

    
    display = f"{nickname}\'s Current Skills\n{'+'*20}\n"
    display += f"FOCUS: {focus} {'.'*5} MVMT:  {mvmt}\n"
    display += f"SPEED: {current_speed}/{max_speed} {'.'*5} SNEAK: {current_sneak}/{max_sneak}\n"
    display += f"FIGHT: {current_fight}/{max_fight} {'.'*5}  WILL: {current_will}/{max_will}\n"
    display += f" LORE: {current_lore}/{max_lore} {'.'*5}  LUCK: {current_luck}/{max_luck}\n"

    return display

def equip( context: Context, *args ):
    """ Equips a weapon on the investigator in context """
    weapon = ' '.join( [w.upper() for w in args] )

    nickname = context.investigator.nickname

    weapon_desc = context.weapons.constants.row( weapon )
    equipment = context.investigator.equipment
    hands = context.investigator.hands
    inv_weapons = context.investigator.possessions['weapons']

    if not len(inv_weapons) and weapon != 'args':
        return f'{nickname} has nothing to equip. Try finding a weapon'
    if weapon == 'args':
        return f"Try following 'equip' with one of these: {','.join(inv_weapons)}"
    if weapon not in inv_weapons:
        return f'{nickname} does not possess {weapon}, and as such cannot equip it'
    if weapon in equipment:
        return f'{nickname} has already equipped {weapon}'
    if hands - weapon_desc[3] < 0:
        return f'{nickname} doesn\'t have enough hands to equip {weapon}'

    
    for hand in range( weapon_desc.hands ):
        context.investigator.transforms.equipped_items += [ transformers.dec_hands ]
    context.investigator.transforms.equipped_items += [ ( transformers.equip_item, weapon ) ]

    return f'{nickname} has equipped {weapon}\n'

def dequip( context: Context, *args ):

    weapon = ' '.join( [w.upper() for w in args] )

    nickname = context.investigator.nickname

    weapon_desc = context.weapons.constants.row( weapon )
    equipment = context.investigator.equipment
    inv_weapons = context.investigator.possessions['weapons']

    if not len(equipment) and weapon != 'args':
        return f'{nickname} has nothing equipped'
    if weapon == 'args':
        return f"Try following 'dequip' with one of these: {','.join(inv_weapons)}"
    if weapon not in inv_weapons:
        return f'{nickname} does not own {weapon}, and as such cannot dequip it'
    if weapon not in equipment:
        return f'{nickname} does not have {weapon} equipped'
    
    for hand in range( weapon_desc.hands ):
        context.investigator.transforms.equipped_items += [ transformers.inc_hands ]
    context.investigator.transforms.equipped_items += [ ( transformers.unequip, weapon ) ]

    return f'{nickname} has dequipped {weapon}\n'

def move( context: Context ):

    if not constraints.movement_pts_constraint( context.investigator.defaults.location, transformers.dec_mvmt_points, context.investigator.transforms.location ):
        return f'{context.investigator.nickname} no longer has any movement points.\n'

    # get current location of investigator
    current_location = context.investigator.location.current_location

    # get neighbors for that location
    neighbors = [ (context.locations.graph[0][i], i) for i,v in enumerate( context.locations.graph[current_location] ) if v == 1 ]

    prompt = 'Where would you like to move to? (Enter a number)\n\n'
    prompt += f'0. Stay where you are ({context.locations.constants.row_num( context.investigator.location ).name})\n'

    def location_desc( locs ):
        for loc in locs: 

            name = loc[0]
            desc = f'{name} \x1b[3m'
            occupants = ','.join(loc[1])
            clues = loc[2][0]
            gate = loc[2][3]
            closed = loc[2][5]

            desc += f'| {occupants} |' if len( occupants ) else ''
            desc += f'| {clues} clues |' if clues else ''
            desc += '| there is a strange portal here! |' if gate else ''
            desc += '| closed for business! |' if closed else ''

            desc += '\x1b[23m'

            yield name, desc
            
    for index, neighbor in enumerate( neighbors ):
        for name, desc in location_desc( context.locations.currents.table[1:] ):
            if name == neighbor[0]:
                prompt += f'{index+1}. {desc}\n'

    print( prompt )

    while True:
        try:
            reply = int( input( '>>> ' ).strip() )
            break
        except ValueError:
            print( 'Please enter one of the numbers\n' )

    if not reply:
        return f'{context.investigator.nickname} is staying where they are\n'
    else:
        # new location is neighbor's num_id
        new_loc = neighbors[ reply-1 ][ 1 ]
        context.investigator.transforms.location += [ (transformers.change_location, new_loc) ]
        context.investigator.transforms.location += [ transformers.dec_mvmt_points ]

        return f'{context.investigator.nickname} has moved to {neighbors[ reply-1 ][0]}\n'

def refresh( context: Context ):

    context.investigator.transforms.exhausted_items += [ transformers.refresh_exhausted ]

    return f'{context.investigator.nickname} has refreshed their items'

def increase( context: Context, skill ):

    skill_funcs = {
        'speed' : ( transformers.inc_current_speed, "Speed is your overall quickness. It informs your movement points, as well as speed-based skill checks" ),
        'sneak' : ( transformers.inc_current_sneak, "Sneak is your overall stealthiness. It informs how well you evade Monsters, as well as stealth-based skill checks" ),
        'fight' : ( transformers.inc_current_fight, "Fight is your overall physical fitness. It informs how well you combat Monsters, as well as physical skill checks" ),
        'will' : ( transformers.inc_current_will, "Will is your overall constitution. It informs how well you stomach the horror of each Monster, as well as will mental skill checks" ),
        'lore' : ( transformers.inc_current_lore, "Lore is your overall undesrstanding of the Mythos. It informs how well you cast Spells, as well as other occult skill checks"),
        'luck' : ( transformers.inc_current_luck , "Luck is how fortunate you are. It informs everything that wouldn't be covered by another skill. " )
    }

    if skill.lower() == 'args':
        return show_args( skill_funcs )

    enough_focus = constraints.focus_constraint( context.investigator.defaults.focus, transformers.dec_current_focus, context.investigator.transforms.focus )

    if not enough_focus:
        return f"{context.investigator.nickname} doesn't have enough focus to adjust their skills" 

    if skill not in skill_funcs:
        return "Oops! That's not a real skill. Try again"
    
    if skill == 'speed' or skill == 'sneak':
        can_inc = constraints.skills_constraint( context.investigator.defaults.speed, skill_funcs[skill][0], context.investigator.transforms.speed )
        if can_inc:
            context.investigator.transforms.speed += [ skill_funcs[skill][0] ]
        else:
            return f"{context.investigator.nickname} can't increase their {skill} beyond the maximum"

    if skill == 'fight' or skill == 'will':
        can_inc = constraints.skills_constraint( context.investigator.defaults.fight, skill_funcs[skill][0], context.investigator.transforms.fight )
        if can_inc:
            context.investigator.transforms.fight += [ skill_funcs[skill][0] ]
        else:
            return f"{context.investigator.nickname} can't increase their {skill} beyond the maximum"

    if skill == 'lore' or skill == 'luck':
        can_inc = constraints.skills_constraint( context.investigator.defaults.lore, skill_funcs[skill][0], context.investigator.transforms.lore )
        if can_inc:
            context.investigator.transforms.lore += [ skill_funcs[skill][0] ]
        else:
            return f"{context.investigator.nickname} can't increase their {skill} beyond the maximum"

    # decrease focus
    context.investigator.transforms.focus [ transformers.dec_current_focus ]
    return f"{context.investigator.nickname} has increased their {skill}"

def decrease( context: Context, skill ):

    skill_funcs = {
        'speed' : ( transformers.dec_current_speed, "Speed is your overall quickness. It informs your movement points, as well as speed-based skill checks" ),
        'sneak' : ( transformers.dec_current_sneak, "Sneak is your overall stealthiness. It informs how well you evade Monsters, as well as stealth-based skill checks" ),
        'fight' : ( transformers.dec_current_fight, "Fight is your overall physical fitness. It informs how well you combat Monsters, as well as physical skill checks" ),
        'will' : ( transformers.dec_current_will, "Will is your overall constitution. It informs how well you stomach the horror of each Monster, as well as will mental skill checks" ),
        'lore' : ( transformers.dec_current_lore, "Lore is your overall understanding of the Mythos. It informs how well you cast Spells, as well as other occult skill checks"),
        'luck' : ( transformers.dec_current_luck , "Luck is how fortunate you are. It informs everything that wouldn't be covered by another skill. " )
    }

    if skill.lower() == 'args':
        return show_args( skill_funcs )

    enough_focus = constraints.focus_constraint( context.investigator.defaults.focus, transformers.dec_current_focus, context.investigator.transforms.focus )

    if not enough_focus:
        return f"{context.investigator.nickname} doesn't have enough focus to adjust their skills" 

    if skill not in skill_funcs:
        return "Oops! That's not a real skill. Try again"
    
    if skill == 'speed' or skill == 'sneak':
        can_inc = constraints.skills_constraint( context.investigator.defaults.speed, skill_funcs[skill][0], context.investigator.transforms.speed )
        if can_inc:
            context.investigator.transforms.speed += [ skill_funcs[skill][0] ]
        else:
            return f"{context.investigator.nickname} can't decrease their {skill} beyond the minimum"

    if skill == 'fight' or skill == 'WILL':
        can_inc = constraints.skills_constraint( context.investigator.defaults.fight, skill_funcs[skill][0], context.investigator.transforms.fight )
        if can_inc:
            context.investigator.transforms.fight += [ skill_funcs[skill][0] ]
        else:
            return f"{context.investigator.nickname} can't decrease their {skill} beyond the minimum"

    if skill == 'lore' or skill == 'luck':
        can_inc = constraints.skills_constraint( context.investigator.defaults.lore, skill_funcs[skill][0], context.investigator.transforms.lore )
        if can_inc:
            context.investigator.transforms.lore += [ skill_funcs[skill][0] ]
        else:
            return f"{context.investigator.nickname} can't decrease their {skill} beyond the minimum"

    context.investigator.transforms.focus += [ transformers.dec_current_focus ]
    return f"{context.investigator.nickname} has decreased their {skill}"

def next_phase( context, *args ):
    """ Moves into the next phase of play """
    arg = ' '.join( [w.upper() for w in args] )

    if arg != 'PHASE':
        return "Please say 'next phase' to advance to next phase. \x1b[1;38;5;191mHave you done everything for this phase before moving on?\x1b[22;38;5;70m\n"
    
    phase_names = [ 'MYTHOS', 'UPKEEP', 'MOVEMENT', 'ENCOUNTERS' ]

    # advance next phase
    context.board.transforms['current_phase'] += [ transformers.advance_current_phase ]
    # set bookkeeping flag to true
    context.board.transforms['bookkeeping'] += [ transformers.toggle_bookkeeping ]
    
    # inform the player
    print( f'Beginning the { phase_names[ (context.board.phase + 1) % 4 ] } phase\n' )
    # animate ellipsis in terminal
    # tools.animate_ellipsis( 24, 4 )

    return None

anytime_commands = {
    'commands' : (show_commands, "Shows this list of commands"),
    'show' : (show, "Use to display a view. Try 'show status' or 'show possessions'"),
    'equip' : (equip, "Equips an item. Try 'equip item'"),
    'dequip' : (dequip, "Dequips and item. Try 'dequip item'"),
    'next' : (next_phase, "Advance the next phase of play"),
    'quit' : (quit_game, "Quits out of the game. No savesies, though!")
}

phase_commands = {
    0 : {},
    1 : {
        'refresh' : (refresh, "Readies any exhausted items"),
        'increase' : (increase, "Increase skill by one point"),
        'decrease' : (decrease, "Decrease skill by one point") 
    },
    2 : {
        'move' : (move, "Bring up the move dialog to change locations")
    },
    3 : {

    }
}


# for debugging 
def debug( context, *args ):
        try:
            if args[0] == 'phase':
                phases.phase_funcs[ int(args[1]) ]( context )
            else:
                ic()
                val = eval( args[0] )
                ic( args[0], val )
        except Exception as error:
            print( error )
        return None

if DEBUG_LVL >= 0:
    anytime_commands.update( { 'debug' : (debug, "Debugger") } )