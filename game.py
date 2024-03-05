import board, investigator, monsters, locations, tools
from icecream import ic

# game defaults

INVESTIGATOR = "Amanda Sharpe"
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

def normal_monster_move( adj_matrix, dim, loc ):
    if loc != 38: # ignore the outskirts
        # find adjacency
        adj = adj_matrix[loc].index( 1 )
        # remove current location from index
        board.board_transforms['monster_locations'].append( (board.remove_monster_location, dim, loc ) )
        # add future location to index
        board.board_transforms['monster_locations'].append( (board.add_monster_location, dim, adj ) )
        return adj
    
def move_monsters():
    groups = [ (0,), (4,), (5,), (8,), (2,3), (1,6,7) ]
    distros = [ 11, 11, 11, 11, 11, 11 ]

    move_left = tools.rand_from_distro( dict(zip( groups, distros )) )
    move_right = tools.rand_from_distro( { k:v for k,v in dict(zip( groups, distros )).items() if k != move_left } )

    for dim, locs in enumerate( board.current_monst_locs_by_dim( board.board_defaults['monster_locations'], board.board_transforms['monster_locations' ] ) ): 
        if dim in move_left and len( locs ):
            for occupant, loc_id in arkham_location_occupants_of_dimension( locs, dim ):
                # check monster movement rule
                monster_in_situ = monster_defs_trans( occupant, zip( monsters.monster_defaults, monsters.monster_transforms ) )
                mvmt_rule = monsters.current_rules( monster_in_situ['defaults'][1], monster_in_situ['transforms'][1] )[0]
                if mvmt_rule == 0:
                    adj = normal_monster_move( locations.left_graph, dim, loc_id )
                    print( f'{monster_in_situ["defaults"][0]} has moved from {locations.neighbors_graph[loc_id][0]} to {locations.neighbors_graph[adj][0]}.')
        elif dim in move_right and len( locs ):
            for occupant, loc_id in arkham_location_occupants_of_dimension( locs, dim ):
                # check monster movement rule
                monster_in_situ = monster_defs_trans( occupant, zip( monsters.monster_defaults, monsters.monster_transforms ) )
                mvmt_rule = monsters.current_rules( monster_in_situ['defaults'][1], monster_in_situ['transforms'][1] )[0]
                if mvmt_rule == 0:
                    adj = normal_monster_move( locations.right_graph, dim, loc_id )
                    print( f'{monster_in_situ["defaults"][0]} has moved from {locations.neighbors_graph[loc_id][0]} to {locations.neighbors_graph[adj][0]}.')

def mythos_gate():

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

    


# simulate 10 mythos phases
for m in range(10):
    mythos_gate()
    print()

# for loc in zip( locations.location_defaults[1:], locations.location_transforms[1:] ):
#     name = loc[0][0]
#     occupants = locations.current_location_occupants( loc[0][1], loc[1][1] )
#     status_values = locations.current_location_status( loc[0][2], loc[1][2] )
#     status_labels = [ 'clues', 'historical clues', 'sealed', 'gate', 'explored', 'closed' ]
#     status = dict( zip( status_labels, status_values ) )
#     ic( name, occupants, status )
 
ic( board.current_monst_locs_by_dim( board.board_defaults['monster_locations'], board.board_transforms['monster_locations' ] ) )