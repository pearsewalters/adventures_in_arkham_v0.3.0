import board, investigator, monsters, locations, tools
from icecream import ic

# game defaults

INVESTIGATOR = "Sister Mary"
ANCIENT_ONE = "Azathoth"

def azathoth_rules():
    """Apply ancient one rules for Azathoth"""
    # maniacs have their toughness increased by 1
    for row in monsters.monster_transforms[1:]:
        if row[0] == 'Maniac':
            row[ 3 ].append( monsters.inc_toughness )
            break
    # doom track is set to 14
    doom_track = 14
    while doom_track:
        board.board_transforms['doom_track'].append( board.dec_doom_track )
        doom_track -= 1


# apply ancient one rules

ancient_one_rules = {
    'Azathoth' : azathoth_rules
}

# set investigator
board.board_transforms['investigators'].append( ( board.add_investigator, INVESTIGATOR ) )
# set ancient one and apply rules
board.board_transforms['ancient_one'].append( ( board.set_ancient_one, ANCIENT_ONE ) )
ancient_one_rules[ ANCIENT_ONE ]()




# select random unstable location to draw the first gate
    
def unstable_locations( locs ):
    for row in locs[1:]:
        if row[ locs[0].index( 'instability' ) ] > 0:
            yield row

def location_defs_trans( loc, locs ):
    location = {}
    for l in enumerate( locs ):
        if loc == l[1][0][0]:
            location['id'] = l[0]
            location['defaults'] = l[1][0]
            location['transforms'] = l[1][1]
    return location

def monster_defs_trans( mon, mons ):
    return location_defs_trans( mon, mons )

def monster_dimension( monster ):
    for mon in monsters.monster_constants:
        if mon[0] == monster:
            return mon[1]
        

def awaken_the_ancient_one():
    print( 'The ancient one awakens!' )
    print( 'Game over!' )
    return False

def add_doom():
    if board.current_doom_track( board.board_defaults['doom_track'], board.board_transforms['doom_track'] ) + 1 == 0:
        return awaken_the_ancient_one()
    else:
        board.board_transforms['doom_track'].append( board.inc_doom_track )
        return True
    
        
def increase_terror_track():

    board.board_transforms['terror_track'].append( board.inc_terror_track )
    terror_track = board.current_terror_track( board.board_defaults['terror_track'], board.board_transforms['terror_track'] )

    print( 'The terror has increased!' )

    magick_shoppe = location_defs_trans( 'YE OLDE MAGICK SHOPPE' )
    curiositie = location_defs_trans( 'CURIOSITIE SHOPPE' )
    general = location_defs_trans( 'GENERAL STORE' )

    if terror_track >= 11:
        add_doom()
    elif terror_track >= 10:
        # remove the monster limit
        board.board_transforms['monster_limit'].append( board.remove_monster_limit )
    elif terror_track >= 9 and locations.location_closed_constraint( magick_shoppe['defaults'][2], locations.mark_closed, magick_shoppe['transforms'][2] ):
        # close ye olde magick shoppe
        magick_shoppe['transforms'][2].append( locations.mark_closed )
    elif terror_track >= 6 and locations.location_closed_constraint( curiositie['defaults'][2], locations.mark_closed, curiositie['transforms'][2] ):
        # close curiositie shoppe
        curiositie['transforms'][2].append( locations.mark_closed )
    elif terror_track >= 3 and locations.location_closed_constraint( general['defaults'][2], locations.mark_closed, general['transforms'][2] ):
        # close general store
        general['transforms'][2].append( locations.mark_closed )

    # no matter what, remove an ally from the game
    print( 'Margie, pack your bags!' )


def add_monster( location ):

    new_monster = tools.rand_from_distro( monsters.current_frequencies( monsters.monster_cup_defaults, monsters.monster_cup_transforms ) )

    too_many_monsters = board.too_many_monsters_constraint( board.board_defaults['monster_limit'], board.inc_monster_count, board.board_transforms['monster_limit'] )

    if too_many_monsters == 1:
        print( f'A {new_monster} has appeared!' )
        # add monster to location
        location['transforms'][1].append( ( locations.add_occupant, new_monster ) )
        # update monster cup frequency
        monsters.monster_cup_transforms.append( ( monsters.dec_freq, new_monster ) )
        # update monster count on board
        board.board_transforms['monster_limit'].append( board.inc_monster_count )
        
    elif too_many_monsters == 2:
        # announce
        print( 'Too many monsters!' )
        # write over the location
        location = location_defs_trans( 'OUTSKIRTS', zip( locations.location_defaults, locations.location_transforms ) )
        # check outskirts constraint
        outskirts_full = board.outskirts_full_constraint( board.board_defaults['outskirts_limit'], board.inc_outskirts_count, board.board_transforms['outskirts_limit'] )
        if outskirts_full == 1:
            # add monster to outskirts
            location['transforms'][1].append( ( locations.add_occupant, new_monster ) )
            # increase outskirts count
            board.board_transforms['outskirts_limit'].append( board.inc_outskirts_count )
        elif outskirts_full == 2:
            print( 'The outskirts are teeming with monsters!' )
            # empty the outskirts
            for mon in locations.current_location_occupants( location['defaults'][1], location['transforms'][1] ):
                # remove monster
                location['transforms'].append( (locations.remove_occupant, mon ) )
                # update monster cup frequency
                monsters.monster_cup_transforms.append( ( monsters.inc_freq, mon ) )
            # increase terror track
            increase_terror_track()
        
    # update monster locations by dimension
    board.board_transforms['monster_locations'].append( ( board.add_monster_location, monster_dimension( new_monster ), location['id'] ) ) 

def arkham_locations( locs ):
    for loc in locs:
        if loc != 38:
            yield loc

def location_occupants_of_dimension( loc_id, dim ):
    for occupant in locations.current_location_occupants( locations.location_defaults[loc_id][1], locations.location_transforms[loc_id][1] ):
        if monster_dimension( occupant ) == dim:
            yield occupant

def arkham_location_occupants_of_dimension( locs, dim ):
    for loc in arkham_locations( locs ):
        for occupant in location_occupants_of_dimension( loc, dim ):
            yield occupant, loc

def normal_monster_move( monster, adj_matrix, dim, loc ):
    # find adjacency
    adj = adj_matrix[loc].index( 1 )
    # remove current location from index
    board.board_transforms['monster_locations'].append( (board.remove_monster_location, dim, loc ) )
    # add future location to index
    board.board_transforms['monster_locations'].append( (board.add_monster_location, dim, adj ) )
    print( f'{monster} has moved from {locations.all_neighbors[loc][0]} to {locations.all_neighbors[adj][0]}.')
    
def fast_monster_move( monster, adj_matrix, dim, loc ):
    """This is normal monster movement with the square of the adjacency matrix"""

    squared_adj = tools.matrix_square( [ row[1:] for row in adj_matrix[1:] ] )
    # put the labels back in
    for a,b in zip( squared_adj, adj_matrix[1:] ):
        a.insert( 0, b[0] )
    squared_adj.insert( 0, adj_matrix[0] )

    normal_monster_move( monster, squared_adj, dim, loc )

def stationary_monster_move( *args ):
    """This doesn't move the monster, but receives args for compatibility."""
    return None

def flying_monster_move( monster, adj_matrix, dim, loc ):
    """This will one day have implementation..."""
    ...
    return NotImplemented

def chthonian_monster_move( monster, adj_matrix, dim, loc ):
    """This will one day have implementation..."""
    ...
    return NotImplemented

def hound_monster_move( monster, adj_matrix, dim, loc ):
    """This will one day have implementation..."""
    ...
    return NotImplemented

def move_monsters():
    # monsters move in groups based on their dimension
    groups = [ (0,), (4,), (5,), (8,), (2,3), (1,6,7) ]
    # each group has likelihood of appearing, i do this so i can use rand_from_distro 
    distros = [ 11, 11, 11, 11, 11, 11 ]
    # randomly select a group to move left...
    move_left = tools.rand_from_distro( dict(zip( groups, distros )) )
    # ...and of the remaining groups randomly select one to go right
    move_right = tools.rand_from_distro( { k:v for k,v in dict(zip( groups, distros )).items() if k != move_left } )

    rules = {
        0 : normal_monster_move,
        1 : fast_monster_move,
        2 : stationary_monster_move,
        3 : flying_monster_move,
        4 : chthonian_monster_move,
        5 : hound_monster_move
    }

    def move_by_rule( rule, *args ):
        rules = {
            0 : normal_monster_move,
            1 : fast_monster_move,
            2 : stationary_monster_move,
            3 : flying_monster_move,
            4 : chthonian_monster_move,
            5 : hound_monster_move
        }
        return rules[rule]( *args )

    for dim, locs in enumerate( board.current_monst_locs_by_dim( board.board_defaults['monster_locations'], board.board_transforms['monster_locations' ] ) ): 
        if dim in move_left and len( locs ):
            for occupant, loc_id in arkham_location_occupants_of_dimension( locs, dim ):
                # check monster movement rule
                monster_in_situ = monster_defs_trans( occupant, zip( monsters.monster_defaults, monsters.monster_transforms ) )
                mvmt_rule = monsters.current_rules( monster_in_situ['defaults'][1], monster_in_situ['transforms'][1] )[0]
                rules[mvmt_rule](occupant, locations.left_neighbors, dim, loc_id )   
        elif dim in move_right and len( locs ):
            for occupant, loc_id in arkham_location_occupants_of_dimension( locs, dim ):
                # check monster movement rule
                monster_in_situ = monster_defs_trans( occupant, zip( monsters.monster_defaults, monsters.monster_transforms ) )
                mvmt_rule = monsters.current_rules( monster_in_situ['defaults'][1], monster_in_situ['transforms'][1] )[0]
                rules[mvmt_rule](occupant, locations.right_neighbors, dim, loc_id )

def mythos():

    gate_distro = {}
    clue_distro = {}

    for loc in zip( locations.location_constants[1:], locations.location_defaults[1:], locations.location_transforms[1:] ):
        # gate likelihood := instability * ( 1 + current clues ) * historical clues 
        gate_distro[ loc[0][0] ] = loc[0][ locations.location_constants[0].index( 'instability' ) ] # * ( locations.current_location_status( loc[1][2], loc[2][2] )[0] + 1 ) * ( locations.current_location_status( loc[1][2], loc[2][2] )[1] )
        # clue likelihood := mystery * (1 + current clues ) * historical clues
        clue_distro[ loc[0][0] ] = loc[0][ locations.location_constants[0].index( 'mystery' ) ] # * ( locations.current_location_status( loc[1][2], loc[2][2] )[0] + 1 ) * ( locations.current_location_status( loc[1][2], loc[2][2] )[1] )

    
    new_gate = location_defs_trans( tools.rand_from_distro( gate_distro ), zip( locations.location_defaults, locations.location_transforms ) )
    new_clue = location_defs_trans( tools.rand_from_distro( { k:v for k,v in clue_distro.items() if k != new_gate['defaults'][0] } ), zip( locations.location_defaults, locations.location_transforms ) )

    draw_gate = locations.location_gate_constraint( new_gate['defaults'][2], locations.add_gate, new_gate['transforms'][2] )
    too_many_gates = board.too_many_gates_constraint( board.board_defaults['gates_open'], board.inc_gates_open, board.board_transforms['gates_open'] )
    loc_already_has_clue = locations.location_clues_constraint( new_clue['defaults'][2], locations.inc_clue, new_clue['transforms'][2] )

    if draw_gate == 1:
        if too_many_gates == 1:
            # add doom
            if add_doom():
                # add gate to location
                new_gate['transforms'][2].append( locations.add_gate )
                # remove all clues from that location:
                for n in range( locations.current_location_status( new_gate['defaults'][2], new_gate['transforms'][2] )[0] ):
                    new_gate['transforms'][2].append( locations.dec_clue )
                # increase gates on board
                board.board_transforms['gates_open'].append( board.inc_gates_open )
                # announce new gate
                print( f'A new gate has appeared at {new_gate["defaults"][0]}!' )
                
                # add monster
                add_monster( new_gate )
                # move monsters
                move_monsters()
            
                # add clue to new location if it doesn't have a gate on it
                if loc_already_has_clue == 1:
                    new_clue['transforms'][2].append( locations.inc_clue )
                    # announce clue
                    print( f'A clue has appeared at {new_clue["defaults"][0]}')
                # increase historical clues no matter what
                new_clue['transforms'][2].append( locations.inc_historical_clues )
        elif too_many_gates == 2:
            awaken_the_ancient_one()
    elif draw_gate == 2:
        print( 'A monster surge!' )
        
def investigator_defs_trans( inv ):
    return location_defs_trans( inv, zip( investigator.investigator_defaults, investigator.investigator_transforms ) )

def inv_constants( inv ):
    return [ row for row in investigator.investigator_constants if row[0] == inv ][0]

def show_skills():
    """ Displays investigator skills"""

    inv_constants( INVESTIGATOR )

    nickname = 'TEST' # inv_constants( INVESTIGATOR )[1]
    investigator_desc = investigator_defs_trans( INVESTIGATOR )
    
    focus = investigator.current_skill( investigator_desc['defaults'][4], investigator_desc['transforms'][4] )[1]
    mvmt = investigator.current_skill( investigator_desc['defaults'][4], investigator_desc['transforms'][4] )[2]
    
    speed = investigator.current_skill( investigator_desc['defaults'][5], investigator_desc['transforms'][5] )[1]
    sneak = investigator.current_complement_skill( investigator_desc['defaults'][5], investigator_desc['transforms'][5] )

    fight = investigator.current_skill( investigator_desc['defaults'][6], investigator_desc['transforms'][6] )[1]
    will = investigator.current_complement_skill( investigator_desc['defaults'][6], investigator_desc['transforms'][6] )

    lore = investigator.current_skill( investigator_desc['defaults'][7], investigator_desc['transforms'][7] )[1]
    luck = investigator.current_complement_skill( investigator_desc['defaults'][7], investigator_desc['transforms'][7] )

    display = f'{nickname}\'s Current Skills\n{'~'*20}\nFOCUS: {focus} {'.'*5} MVMT:  {mvmt}\nSPEED: {speed} {'.'*5} SNEAK: {sneak}\nFIGHT: {fight} {'.'*5} WILL:  {will}\nLORE:  {lore} {'.'*5} LUCK:  {luck}\n'

    return display
    
def show_status():
    """ Displays investigator health, location, and conditions """
    nickname = inv_constants( INVESTIGATOR )[1]
    investigator_desc = investigator_defs_trans( INVESTIGATOR )

    display = f'{nickname}\'s Current Status\n{'~'*20}\n'

    # health status
    max_damage = investigator.current_stat( investigator_desc['defaults'][1], investigator_desc['transforms'][1] )[0]
    current_damage = investigator.current_stat( investigator_desc['defaults'][1], investigator_desc['transforms'][1] )[1]
    consciousness = 'unconscious' if investigator.current_stat( investigator_desc['defaults'][1], investigator_desc['transforms'][1] )[2] else 'conscious'
    display_damage = f'{current_damage}/{max_damage}'

    max_horror = investigator.current_stat( investigator_desc['defaults'][2], investigator_desc['transforms'][2] )[0]
    current_horror = investigator.current_stat( investigator_desc['defaults'][2], investigator_desc['transforms'][2] )[1]
    sanity = 'insane' if investigator.current_stat( investigator_desc['defaults'][2], investigator_desc['transforms'][2] )[2] else 'sane'
    display_horror = f'{current_horror}/{max_horror}'

    display += f'DAMAGE: {display_damage} {'.'*5} HORROR: {display_horror}\n'
    display += f'{nickname} is currently {consciousness} and {sanity}\n\n'

    # location 
    location_id = investigator.current_location( investigator_desc['defaults'][8], investigator_desc['transforms'][8] )[0]
    location_name = locations.location_constants[ location_id ][0]
    location_neighborhood = locations.location_constants[ location_id][1]

    display += f'LOCATION: {location_name}, in the {location_neighborhood} neighborhood\n\n'

    # conditions 
    conditions = investigator.current_condtions( investigator_desc['defaults'][3], investigator_desc['transforms'][3] )
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

    return display

def show_possessions():
    """ Displays investigator possessions """

    nickname = inv_constants( INVESTIGATOR )[1]
    investigator_desc = investigator_defs_trans( INVESTIGATOR )

    possessions = investigator.current_possessions( investigator_desc['defaults'][12], investigator_desc['transforms'][12] )

    display = f'{nickname}\'s Current Possessions\n{'~'*20}\n'

    display += f'MONEY: {possessions['money']} {'.'*5} CLUES: {possessions['clues']}\n'

    def add_poss_to_disp( poss, header ):
        d = ''
        if len( poss ):
            d += f'{header}: \n '
            for item in poss:
                d += f'{' '*len(header)} - {item}\n'
            return d + '\n'
        return d
    
    display += add_poss_to_disp( possessions['common'],'COMMON ITEMS')
    display += add_poss_to_disp( possessions['unique'],'UNIQUE ITEMS')
    display += add_poss_to_disp( possessions['spells'],'SPELLS')
    display += add_poss_to_disp( possessions['buffs'],'LEARNED SKILLS')
    display += add_poss_to_disp( possessions['allies'],'ALLIES')

    return display + '\n'

def quit():
    ask = input( 'Are you sure you want to quit? (y/n) ' ).strip().lower()
    if ask == 'y':
        return True
    return False

def begin( phase ):
    phases = { 
        'upkeep' : None, 
        'movement' : None,
        'encounters' : None,
        'mythos' : mythos 
    }
    if phase not in phases:
        print( 'That is not a valid phase. Try again.' )
        return False
    return phases[phase]()
    
def show( view ):
    """ Dispatch for show_view functions """
    views = {
        'skills' : show_skills,
        'status' : show_status,
        'possessions' : show_possessions
    }
    if view not in views:
        return 'That is not a valid view. Try again.' 
    return views[view]()


valid_commands = {
    'quit' : quit,
    'begin': begin,
    'show' : show
}

while True:
    sentence = input( f'\x1b[38;5;70m>>> ' ).strip().lower().split(' ')
    print('\n')
    command = sentence[0]
    arguments = sentence[1:]
    if command not in valid_commands:
        print( 'Hmm...unsure what you want. Try again. Type "help" to see a list of valid commands.' )
    elif command == 'quit':
        if quit():
            break
    else:
        try:
            if len( arguments ):
                msg = valid_commands[command]( *arguments )
                # if command return a message, print it 
                if msg:
                    print( msg )
            else:
                valid_commands[command]()
        except TypeError as error:
            print( error )