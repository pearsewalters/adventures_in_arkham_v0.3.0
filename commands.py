import time, transformers, constraints, phases, investigator

from icecream import ic

def animate_ellipsis( keyframes, speed ):
    anim_str = ''
    for n in range( keyframes ):
        print( f'\x1b[A \x1b[0J{anim_str}')
        anim_str += '.'
        time.sleep( 1 / speed )
        if len( anim_str ) == 4:
            anim_str = ''

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


def show( context, view ):
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

def show_possessions( context: dict ):
    """ Displays investigator possessions """

    nickname = context['investigator']['nickname']
    possessions = context['investigator']['possessions']
    equipment = context['investigator']['equipped_items']
    exhausted = context['investigator']['exhausted_items']
    weapons = context['weapons']

    display = f'{nickname}\'s Current Possessions\n{'+'*20}\n'

    display += f'${possessions['money']} {'.'*5} CLUES: {possessions['clues']}\n'
    display += f'EQUIPPED: [{','.join(equipment)}]\n'
    display += f'EXHAUSTED: [{','.join(exhausted)}]\n'

    def add_weapon_details( weapon, spacer ):
        d = []
        w_constants= [ row for row in weapons['constants'] if row[0] == weapon ][0]
        w_defaults = [ row for row in weapons['defaults'] if row[0] == weapon ][0][1]
        # modality
        if w_defaults[0]:
            d.append( 'magical' )
        else:
            d.append( 'physical' ) 
        # bonus
        d.append( f'+{w_defaults[1]}' )
        # rarity
        d.append( w_constants[1] ) 
        # uses
        if w_constants[2] == float('inf'):
            d.append( '∞ uses' )
        else:
            d.append( str(w_constants[2]) + ' use(s)' ) 
        # hands
        d.append( str(w_constants[3]) + '-handed' ) 

        return f'{spacer}{w_constants[4]}\n{spacer}( {" / ".join( d )} )'


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
            d += f'{header}: \n '
            d += f'{' '*len(header)}   {item}\n'
        return d
    

    display += add_poss_to_disp( possessions['weapons'],'WEAPONS',add_weapon_details)
    display += add_poss_to_disp( possessions['consumables'],'CONSUMABLES')
    display += add_poss_to_disp( possessions['tomes'],'TOMES')
    display += add_poss_to_disp( possessions['passive_buffs'],'PASSIVE BUFFS')
    display += add_poss_to_disp( possessions['active_buffs'],'ACTIVE BUFFS')
    display += add_poss_to_disp( possessions['spells'],'SPELLS')
    display += add_poss_to_disp( possessions['allies'],'ALLIES')
    display += add_poss_to_disp( possessions['gate_trophies'], 'GATE TROPHIES' )
    display += add_poss_to_disp( possessions['monster_trophies'], 'MONSTER TROPHIES' )

    return display + '\n'

def show_status( context ):
    """ Displays investigator health, location, and conditions """
    nickname = context['investigator']['nickname']
    
    display = f'{nickname}\'s Current Status\n{'+'*20}\n'

    # health status
    max_damage = context['investigator']['damage'][0]
    current_damage = context['investigator']['damage'][1]
    consciousness = 'unconscious' if context['investigator']['damage'][2] else 'conscious'
    display_damage = f'{current_damage}/{max_damage}'

    max_horror = context['investigator']['horror'][0]
    current_horror = context['investigator']['horror'][1]
    sanity = 'insane' if context['investigator']['horror'][2] else 'sane'
    display_horror = f'{current_horror}/{max_horror}'

    display += f'DAMAGE: {display_damage} {'.'*5} HORROR: {display_horror}\n'
    display += f'{nickname} is currently {consciousness} and {sanity}\n\n'

    # location 
    location_id = context['investigator']['location'][0]
    location_name = context['locations']['constants'][ location_id ][0]
    location_neighborhood = context['locations']['constants'][ location_id][1]

    display += f'LOCATION: {location_name}, in the {location_neighborhood} neighborhood\n\n'

    # conditions 
    conditions = context['investigator']['conditions']
    display_conditions = ''

    if conditions[1]:
        if conditions[0]:
            display_conditions += f'{nickname} is currently arrested\n'
        elif conditions[2]:
            display_conditions += f'{nickname} is currently lost in time & space\n'
        else:
            display_conditions += f'{nickname} is currently delayed\n'
    if conditions[3]:
        display_conditions += f'{nickname} is earning money from a retainer\n'
    if conditions[4]:
        display_conditions += f'{nickname} currently has a loan from the Bank of Arkham\n'
    if conditions[5]:
        display_conditions += f'{nickname} is a member of the Silver Twilight Lodge\n'
    if conditions[6]:
        display_conditions += f'{nickname} is the Deputy of Arkham. Monsters beware!\n'
    if not conditions[7] + 1:
        display_conditions += f'{nickname} is cursed!'
    if not conditions[7] - 1:
        display_conditions += f'{nickname} is blessed!'

    display += display_conditions

    return display + '\n'

def show_skills( context ):
    """ Displays investigator skills"""

    nickname = context['investigator']['nickname']
    
    focus = context['investigator']['focus'][1]
    mvmt = context['investigator']['location'][1]
    
    speed = context['investigator']['speed'][1]
    sneak = context['investigator']['sneak']

    fight = context['investigator']['fight'][1]
    will = context['investigator']['will']

    lore = context['investigator']['lore'][1]
    luck = context['investigator']['luck']

    display = f'{nickname}\'s Current Skills\n{'+'*20}\nFOCUS: {focus} {'.'*5} MVMT:  {mvmt}\nSPEED: {speed} {'.'*5} SNEAK: {sneak}\nFIGHT: {fight} {'.'*5} WILL:  {will}\nLORE:  {lore} {'.'*5} LUCK:  {luck}\n'

    return display


def equip( context, *args ):
    """ Equips a weapon on the investigator in context """
    weapon = ' '.join( [w.upper() for w in args] )

    nickname = context['investigator']['nickname']

    weapon_desc = [ row for row in context['weapons']['constants'] if row[0] == weapon ][0]
    equipment = context['investigator']['equipped_items']
    hands = context['investigator']['hands']
    inv_weapons = context['investigator']['possessions']['weapons']

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

    
    for hand in range( weapon_desc[3] ):
        context['investigator']['transforms'][10].append( transformers.dec_hands )
    context['investigator']['transforms'][10].append( ( transformers.equip_item, weapon ) )

    return f'{nickname} has equipped {weapon}\n'

def dequip( context, *args ):

    weapon = ' '.join( [w.upper() for w in args] )

    nickname = context['investigator']['nickname']

    weapon_desc = [ row for row in context['weapons']['constants'] if row[0] == weapon ][0]
    equipment = context['investigator']['equipped_items']
    inv_weapons = context['investigator']['possessions']['weapons']

    if not len(equipment) and weapon != 'args':
        return f'{nickname} has nothing equipped'
    if weapon == 'args':
        return f"Try following 'dequip' with one of these: {','.join(inv_weapons)}"
    if weapon not in inv_weapons:
        return f'{nickname} does not own {weapon}, and as such cannot dequip it'
    if weapon not in equipment:
        return f'{nickname} does not have {weapon} equipped'
    
    for hand in range( weapon_desc[3] ):
        context['investigator']['transforms'][10].append( transformers.inc_hands )
    context['investigator']['transforms'][10].append( ( transformers.unequip, weapon ) )

    return f'{nickname} has dequipped {weapon}\n'

def move( context ):

    if not constraints.movement_pts_constraint( context['investigator']['defaults'][8], transformers.dec_movement, context['investigator']['transforms'][8]):
        return f'{context['investigator']['nickname']} no longer has any movement points.\n'

    # get current location of investigator
    current_location = context['investigator']['location'][0]

    # get neighbors for that location
    neighbors = [ (context['locations']['graph'][0][i], i) for i,v in enumerate( context['locations']['graph'][current_location]) if v == 1 ]

    prompt = 'Where would you like to move to? (Enter a number)\n\n'
    prompt += f'0. Stay where you are ({context['locations']['constants'][ context['investigator']['location'][0] ][0] })\n'

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
        for name, desc in location_desc( context['locations']['currents'][1:] ):
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
        return f'{context['investigator']['nickname']} is staying where they are\n'
    else:
        # new location is neighbor's num_id
        new_loc = neighbors[ reply-1 ][ 1 ]
        context['investigator']['transforms'][8].append( (transformers.change_loc, new_loc) )
        context['investigator']['transforms'][8].append( transformers.dec_movement )
        return f'{context['investigator']['nickname']} has moved to {neighbors[ reply-1 ][0]}\n'

def refresh( context ):

    context['investigator']['transforms'][11].append( transformers.refresh_items )

    return f'{context['investigator']['nickname']} has refreshed their items'

def next_phase( context, *args ):
    """ Moves into the next phase of play """
    arg = ' '.join( [w.upper() for w in args] )

    phase_funcs = {
        0 : phases.mythos,
        1 : None,
        2 : None,
        3 : None
    }

    if arg != 'PHASE':
        return "Please say 'next phase' to advance to next phase. \x1b[1;38;5;191mHave you done everything for this phase before moving on?\x1b[22;38;5;70m\n"
    
    phase_names = [ 'MYTHOS', 'UPKEEP', 'MOVEMENT', 'ENCOUNTERS' ]

    # advance next phase
    context['board']['transforms']['current_phase'].append( transformers.advance_current_phase )
    
    # inform the player
    print( f'Beginning the { phase_names[ (context['board']['phase'] + 1) % 4 ] } phase' ) 
    # animate ellipsis in terminal
    # animate_ellipsis( 12, 4 )

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
        'refresh' : (refresh, "Readies any exhausted items")
    },
    2 : {
        'move' : (move, "Bring up the move dialog to change locations")
    },
    3 : {

    }
}