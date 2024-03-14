import traceback, phases, currency, transformers, board, investigator, monsters, locations, weapons, commands, tools

from icecream import ic

# game defaults

INVESTIGATORS = [ "Sister Mary" ]
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
        board.board_transforms['doom_track'].append( transformers.dec_doom_track )
        doom_track -= 1


# apply ancient one rules

ancient_one_rules = {
    'Azathoth' : azathoth_rules
}

# set investigators
for inv in INVESTIGATORS:
    board.board_transforms['investigators'].append( ( transformers.add_investigator, inv ) )
    # set win condition
    board.board_transforms['win_cond'].append( transformers.inc_gates_closed_to_win )
    

# set ancient one and apply rules
board.board_transforms['ancient_one'].append( ( transformers.set_ancient_one, ANCIENT_ONE ) )

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

def current_locations_desc( defaults, transforms ):
    loc_descs = [ defaults[0] ]
    for index,value in enumerate(defaults[1:]):
        loc_descs.append([
            value[0],
            currency.current_location_occupants( value[1], transforms[index+1][1] ),
            currency.current_location_status( value[2], transforms[index+1][2] )
        ])
    return loc_descs


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
        
def investigator_dict( inv ):
    index = [ row[0] for row in investigator.investigator_constants ].index( inv )
    return {
        'name' : inv,
        'nickname' : investigator.investigator_constants[index][1],
        'occupation' : investigator.investigator_constants[index][2],
        'home' : investigator.investigator_constants[index][3],
        'ability_name' : investigator.investigator_constants[index][4],
        'ability_desc' : investigator.investigator_constants[index][5],
        'story' : investigator.investigator_constants[index][6],
        'damage' : currency.current_stat( investigator.investigator_defaults[index][1], investigator.investigator_transforms[index][1] ),
        'horror' : currency.current_stat( investigator.investigator_defaults[index][2], investigator.investigator_transforms[index][2] ),
        'conditions' : currency.current_condtions( investigator.investigator_defaults[index][3], investigator.investigator_transforms[index][3] ),
        'focus' : currency.current_skill( investigator.investigator_defaults[index][4], investigator.investigator_transforms[index][4] ),
        'speed' : currency.current_skill( investigator.investigator_defaults[index][5], investigator.investigator_transforms[index][5] ),
        'sneak' : currency.current_complement_skill( investigator.investigator_defaults[index][5], investigator.investigator_transforms[index][5] ),
        'fight' : currency.current_skill( investigator.investigator_defaults[index][6], investigator.investigator_transforms[index][6] ),
        'will' : currency.current_complement_skill( investigator.investigator_defaults[index][6], investigator.investigator_transforms[index][6] ),
        'lore' : currency.current_skill( investigator.investigator_defaults[index][7], investigator.investigator_transforms[index][7] ),
        'luck' : currency.current_complement_skill( investigator.investigator_defaults[index][7], investigator.investigator_transforms[index][7] ),
        'location' : currency.current_inv_location( investigator.investigator_defaults[index][8], investigator.investigator_transforms[index][8] ),
        'hands' : currency.current_equipment( investigator.investigator_defaults[index][10], investigator.investigator_transforms[index][10] )[0],
        'equipped_items' : currency.current_equipment( investigator.investigator_defaults[index][10], investigator.investigator_transforms[index][10] )[1],
        'exhausted_items' : currency.current_exhausted( investigator.investigator_defaults[index][11], investigator.investigator_transforms[index][11]),
        'possessions' : currency.current_possessions( investigator.investigator_defaults[index][12], investigator.investigator_transforms[index][12] ),
        'constants' : investigator.investigator_constants[index],
        'defaults' : investigator.investigator_defaults[index],
        'transforms' : investigator.investigator_transforms[index]
    }

# create context for the game frames
mythos_context = {
    'board' : {
        'phase' : 0,
        'defaults' : board.board_defaults,
        'transforms' : board.board_transforms
    },
    'locations' : {
        'constants' : locations.location_constants,
        'defaults' : locations.location_defaults,
        'transforms' : locations.location_transforms,
        'currents' : current_locations_desc( locations.location_defaults, locations.location_transforms ),
    }
}


# initiate game with first mythos phase

phases.mythos( mythos_context )
commands.next_phase( mythos_context, "phase" )

# begin game loop

while True:
    
    ## pull context into loop
    context = {
        'board' : {
            'phase' : currency.current_phase( board.board_defaults['current_phase'], board.board_transforms['current_phase'] ),
            'win' : currency.current_win_condition( board.board_defaults['win_cond'], board.board_transforms['win_cond'] ),
            'gates_open' : currency.current_gates_open( board.board_defaults['gates_open'], board.board_transforms['gates_open'] ),
            'defaults' : board.board_defaults,
            'transforms' : board.board_transforms
        },
        'locations' : {
            'constants' : locations.location_constants,
            'defaults' : locations.location_defaults,
            'transforms' : locations.location_transforms,
            'currents' : current_locations_desc( locations.location_defaults, locations.location_transforms ),
            'graph' : locations.all_neighbors,
        },
        'investigator' : investigator_dict( currency.current_investigators(
            board.board_defaults['investigators'], board.board_transforms['investigators']
        )[ currency.current_player( board.board_defaults['current_player'], board.board_transforms['current_player'] ) ] ),
        'weapons' : {
            'constants' : weapons.constants,
            'defaults' : weapons.defaults,
        }
    }

    ## check for win condition
    if context['board']['win'][0] == 0 and context['board']['gates_open'] == 0:
        print(f'\x1b[38;5;70m\n\n{" "*20}The ancient one is banished! You\'ve saved Arkham and the world!\n\n' )
        break

    val_com = { k:v for k,v in commands.phase_commands[ context['board']['phase'] ].items() }
    val_com.update( commands.anytime_commands )

    sentence = input( f'\x1b[38;5;70m>>> ' ).strip().lower().split(' ')
    print('\n')
    command = sentence[0]
    arguments = sentence[1:]

    if command not in val_com:
        print( 'Hmm...unsure what you want. Try again. Type "commands" to see a list of valid commands.' )
    elif command == 'quit':
        if commands.quit_game():
            break 
    elif command == 'commands':
        print( commands.show_commands( val_com ) )
    else:
        try:
            if len( arguments ):
                msg = val_com[command][0]( context, *arguments )
            else:
                msg = val_com[command][0]( context )
            # if command returns a message, print it 
            if msg:
                print( f'\x1b[38;5;70m{msg}' )
        except TypeError as error:

            traceback.print_tb(  )
            
            print( f'ERROR: {error}' )
