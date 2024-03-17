import traceback, phases, currency, transformers, weapons, commands, tools, constraints
from params import DEBUG, DEBUG_LVL
from tables import constants, defaults, transformations
from tools import Table, adjacencies

from icecream import ic

## debugging
if not DEBUG or DEBUG_LVL < 0:
    ic.disable()


# game defaults

INVESTIGATORS = [ "Sister Mary" ]
ANCIENT_ONE = "Azathoth"

# location matrix
locations = {}
locations['all_neighbors'], locations['left_neighbors'], locations['right_neighbors'] = adjacencies( 'locations.csv' )

def azathoth_rules():
    """Apply ancient one rules for Azathoth"""
    # maniacs have their toughness increased by 1
    for row in transformations.monsters[1:]:
        if row[0] == 'Maniac':
            row[ 3 ].append( transformers.inc_toughness )
            break
    # doom track is set to 14
    doom_track = 14
    while doom_track:
        transformations.board['doom_track'].append( transformers.dec_doom_track )
        doom_track -= 1


# apply ancient one rules

ancient_one_rules = {
    'Azathoth' : azathoth_rules
}

# set investigators
for inv in INVESTIGATORS:
    transformations.board['investigators'].append( ( transformers.add_investigator, inv ) )
    # set win condition
    transformations.board['win_cond'].append( transformers.inc_gates_closed_to_win )
    

# set ancient one and apply rules
transformations.board['ancient_one'].append( ( transformers.set_ancient_one, ANCIENT_ONE ) )

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
            currency.location_occupants( value[1], transforms[index+1][1] ),
            currency.location_status( value[2], transforms[index+1][2] )
        ])
    return loc_descs


def monster_defs_trans( mon, mons ):
    return location_defs_trans( mon, mons )

def monster_dimension( monster ):
    for mon in constants.monsters:
        if mon[0] == monster:
            return mon[1]
        
def awaken_the_ancient_one():
    print( 'The ancient one awakens!' )
    print( 'Game over!' )
    return False

def add_doom():
    if currency.doom_track( defaults.board['doom_track'], transformations.board['doom_track'] ) + 1 == 0:
        return awaken_the_ancient_one()
    else:
        transformations.board['doom_track'].append( transformers.inc_doom_track )
        return True
    
        
def increase_terror_track():

    transformations.board['terror_track'].append( transformers.inc_terror_track )
    terror_track = currency.terror_track( defaults.board['terror_track'], transformations.board['terror_track'] )

    print( 'The terror has increased!' )

    magick_shoppe = location_defs_trans( 'YE OLDE MAGICK SHOPPE' )
    curiositie = location_defs_trans( 'CURIOSITIE SHOPPE' )
    general = location_defs_trans( 'GENERAL STORE' )

    if terror_track >= 11:
        add_doom()
    elif terror_track >= 10:
        # remove the monster limit
        transformations.board['monster_limit'].append( transformers.remove_monster_limit )
    elif terror_track >= 9 and constraints.location_closed_constraint( magick_shoppe['defaults'][2], transformers.mark_closed, magick_shoppe['transforms'][2] ):
        # close ye olde magick shoppe
        magick_shoppe['transforms'][2].append( transformers.mark_closed )
    elif terror_track >= 6 and constraints.location_closed_constraint( curiositie['defaults'][2], transformers.mark_closed, curiositie['transforms'][2] ):
        # close curiositie shoppe
        curiositie['transforms'][2].append( transformers.mark_closed )
    elif terror_track >= 3 and constraints.location_closed_constraint( general['defaults'][2], transformers.mark_closed, general['transforms'][2] ):
        # close general store
        general['transforms'][2].append( transformers.mark_closed )

    # no matter what, remove an ally from the game
    print( 'Margie, pack your bags!' )


def add_monster( location ):

    new_monster = tools.rand_from_distro( currency.frequencies( defaults.monster_cup, transformations.monster_cup ) )

    too_many_monsters = constraints.too_many_monsters_constraint( defaults.board['monster_limit'], transformers.inc_monster_count, transformations.board['monster_limit'] )

    if too_many_monsters == 1:
        print( f'A {new_monster} has appeared!' )
        # add monster to location
        location['transforms'][1].append( ( transformers.add_occupant, new_monster ) )
        # update monster cup frequency
        transformations.monster_cup.append( ( transformers.dec_freq, new_monster ) )
        # update monster count on board
        transformations.board['monster_limit'].append( transformers.inc_monster_count )
        
    elif too_many_monsters == 2:
        # announce
        print( 'Too many monsters!' )
        # write over the location
        location = location_defs_trans( 'OUTSKIRTS', zip( defaults.locations, transformations.locations ) )
        # check outskirts constraint
        outskirts_full = constraints.outskirts_full_constraint( defaults.board['outskirts_limit'], transformers.inc_outskirts_count, transformations.board['outskirts_limit'] )
        if outskirts_full == 1:
            # add monster to outskirts
            location['transforms'][1].append( ( transformers.add_occupant, new_monster ) )
            # increase outskirts count
            transformations.board['outskirts_limit'].append( transformers.inc_outskirts_count )
        elif outskirts_full == 2:
            print( 'The outskirts are teeming with monsters!' )
            # empty the outskirts
            for mon in currency.location_occupants( location['defaults'][1], location['transforms'][1] ):
                # remove monster
                location['transforms'].append( (transformers.remove_occupant, mon ) )
                # update monster cup frequency
                transformations.monster_cup.append( ( transformers.inc_freq, mon ) )
            # increase terror track
            increase_terror_track()
        
    # update monster locations by dimension
    transformations.board['monster_locations'].append( ( transformers.add_monster_location, monster_dimension( new_monster ), location['id'] ) ) 

def arkham_locations( locs ):
    for loc in locs:
        if loc != 38:
            yield loc

def location_occupants_of_dimension( loc_id, dim ):
    for occupant in currency.location_occupants( defaults.locations[loc_id][1], transformations.locations[loc_id][1] ):
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
    transformations.board['monster_locations'].append( (transformers.remove_monster_location, dim, loc ) )
    # add future location to index
    transformations.board['monster_locations'].append( (transformers.add_monster_location, dim, adj ) )
    print( f'{monster} has moved from {locations['all_neighbors'][loc][0]} to {locations['all_neighbors'][adj][0]}.')
    
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

    for dim, locs in enumerate( currency.monst_locs_by_dim( defaults.board['monster_locations'], transformations.board['monster_locations' ] ) ): 
        if dim in move_left and len( locs ):
            for occupant, loc_id in arkham_location_occupants_of_dimension( locs, dim ):
                # check monster movement rule
                monster_in_situ = monster_defs_trans( occupant, zip( defaults.monsters, transformations.monsters ) )
                mvmt_rule = currency.monster_rules( monster_in_situ['defaults'][1], monster_in_situ['transforms'][1] )[0]
                rules[mvmt_rule](occupant, locations['left_neighbors'], dim, loc_id )   
        elif dim in move_right and len( locs ):
            for occupant, loc_id in arkham_location_occupants_of_dimension( locs, dim ):
                # check monster movement rule
                monster_in_situ = monster_defs_trans( occupant, zip( defaults.monsters, transformations.monsters ) )
                mvmt_rule = currency.monster_rules( monster_in_situ['defaults'][1], monster_in_situ['transforms'][1] )[0]
                rules[mvmt_rule](occupant, locations['right_neighbors'], dim, loc_id )
        
def investigator_dict( inv ):
    index = [ row[0] for row in constants.investigators ].index( inv )
    return {
        'name' : inv,
        'nickname' : constants.investigators[index][1],
        'occupation' : constants.investigators[index][2],
        'home' : constants.investigators[index][3],
        'ability_name' : constants.investigators[index][4],
        'ability_desc' : constants.investigators[index][5],
        'story' : constants.investigators[index][6],
        'damage' : currency.stat( defaults.investigators[index][1], transformations.investigators[index][1] ),
        'horror' : currency.stat( defaults.investigators[index][2], transformations.investigators[index][2] ),
        'conditions' : currency.condtions( defaults.investigators[index][3], transformations.investigators[index][3] ),
        'focus' : currency.skill( defaults.investigators[index][4], transformations.investigators[index][4] ),
        'speed' : currency.skill( defaults.investigators[index][5], transformations.investigators[index][5] ),
        'sneak' : currency.complement_skill( defaults.investigators[index][5], transformations.investigators[index][5] ),
        'fight' : currency.skill( defaults.investigators[index][6], transformations.investigators[index][6] ),
        'will' : currency.complement_skill( defaults.investigators[index][6], transformations.investigators[index][6] ),
        'lore' : currency.skill( defaults.investigators[index][7], transformations.investigators[index][7] ),
        'luck' : currency.complement_skill( defaults.investigators[index][7], transformations.investigators[index][7] ),
        'location' : currency.inv_location( defaults.investigators[index][8], transformations.investigators[index][8] ),
        'hands' : currency.equipment( defaults.investigators[index][10], transformations.investigators[index][10] )[0],
        'equipped_items' : currency.equipment( defaults.investigators[index][10], transformations.investigators[index][10] )[1],
        'exhausted_items' : currency.exhausted( defaults.investigators[index][11], transformations.investigators[index][11]),
        'possessions' : currency.possessions( defaults.investigators[index][12], transformations.investigators[index][12] ),
        'constants' : constants.investigators[index],
        'defaults' : defaults.investigators[index],
        'transforms' : transformations.investigators[index]
    }

# create context for the game frames
mythos_context = {
    'board' : {
        'phase' : 0,
        'defaults' : defaults.board,
        'transforms' : transformations.board
    },
    'locations' : {
        'constants' : constants.locations,
        'defaults' : defaults.locations,
        'transforms' : transformations.locations,
        'currents' : current_locations_desc( defaults.locations, transformations.locations ),
    }
}

phase_bookkeeping = {
    0 : phases.mythos,
    1 : phases.upkeep,
    2 : phases.movement,
    3 : phases.encounters
}




# begin game loop

while True:


    ## set context for loop
    context = {
        'board' : {
            'phase' : currency.phase( defaults.board['current_phase'], transformations.board['current_phase'] ),
            'bookkeeping' : currency.bookkeeping( defaults.board['bookkeeping'], transformations.board['bookkeeping'] ),
            'win' : currency.win_condition( defaults.board['win_cond'], transformations.board['win_cond'] ),
            'gates_open' : currency.gates_open( defaults.board['gates_open'], transformations.board['gates_open'] ),
            'defaults' : defaults.board,
            'transforms' : transformations.board
        },
        'locations' : {
            'constants' : constants.locations,
            'defaults' : defaults.locations,
            'transforms' : transformations.locations,
            'currents' : current_locations_desc( defaults.locations, transformations.locations ),
            'graph' : locations['all_neighbors'],
        },
        'investigator' : investigator_dict( currency.investigators(
            defaults.board['investigators'], transformations.board['investigators']
        )[ currency.player( defaults.board['current_player'], transformations.board['current_player'] ) ] ),
        'weapons' : {
            'constants' : constants.weapons,
            'defaults' : defaults.weapons,
            'transforms' : transformations.weapons,
            'deck_defaults' : defaults.weapons_deck,
            'deck_transforms' : transformations.weapons_deck
        },
        'consumables' : {
            'constants' : weapons.constants,
            'defaults' : weapons.defaults,
            'transforms' : weapons.transforms,
            'deck_defaults' : weapons.deck_defaults,
            'deck_transforms' : weapons.deck_transforms
        },
        'tomes' : {
            'constants' : weapons.constants,
            'defaults' : weapons.defaults,
            'transforms' : weapons.transforms,
            'deck_defaults' : weapons.deck_defaults,
            'deck_transforms' : weapons.deck_transforms
        },
        'passive_buffs' : {
            'constants' : weapons.constants,
            'defaults' : weapons.defaults,
            'transforms' : weapons.transforms,
            'deck_defaults' : weapons.deck_defaults,
            'deck_transforms' : weapons.deck_transforms
        },
        'active_buffs' : {
            'constants' : weapons.constants,
            'defaults' : weapons.defaults,
            'transforms' : weapons.transforms,
            'deck_defaults' : weapons.deck_defaults,
            'deck_transforms' : weapons.deck_transforms
        },
        'oddites' : {
            'constants' : weapons.constants,
            'defaults' : weapons.defaults,
            'transforms' : weapons.transforms,
            'deck_defaults' : weapons.deck_defaults,
            'deck_transforms' : weapons.deck_transforms
        }
    }
    

    ## check for win condition
    if context['board']['win'][0] == 0 and context['board']['gates_open'] == 0:
        print(f'\x1b[38;5;70m\n\n{" "*20}The ancient one is banished! You\'ve saved Arkham and the world!\n\n' )
        break

    ## phase bookkeeping
    if context['board']['bookkeeping'] and phase_bookkeeping[ context['board']['phase'] ]:
        phase_bookkeeping[ context['board']['phase'] ]( context )

    val_com = { k:v for k,v in commands.phase_commands[ context['board']['phase'] ].items() }
    val_com.update( commands.anytime_commands )

    sentence = input( f'\x1b[38;5;70m>>> ' ).strip().lower().split(' ')
    print('\n')
    command = ic( sentence[0] )
    arguments = ic( sentence[1:] )

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
            traceback.print_tb( None )
            print( f'ERROR: {error}' )
