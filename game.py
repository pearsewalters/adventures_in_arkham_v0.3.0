import math, traceback, phases, currency, transformers, commands, tools, constraints, params
from tables import constants, defaults, transformations
from tools import Table, adjacencies, debugger
from context import Context
import ancient_ones

from icecream import ic

# create location matrix
graph, left_graph, right_graph = adjacencies( 'locations.csv' )

phase_bookkeeping = {
    0 : phases.mythos,
    1 : phases.upkeep,
    2 : phases.movement,
    3 : phases.encounters
}

def next_frame() -> Context:
    debugger( 0 )
    return Context(**{
        'board' : {
            'phase' : currency.board_current_phase( defaults.board['current_phase'], transformations.board['current_phase'] ),
            'bookkeeping' : currency.board_bookkeeping( defaults.board['bookkeeping'], transformations.board['bookkeeping'] ),
            'win' : currency.board_win_cond( defaults.board['win_cond'], transformations.board['win_cond'] ),
            'gates_open' : currency.board_gates_in_arkham( defaults.board['gates_in_arkham'], transformations.board['gates_in_arkham'] ),
            'defs' : defaults.board,
            'trans' : transformations.board
        },
        'briefs' : {
            'names' : currency.board_investigators( defaults.board['investigators'], transformations.board['investigators'] ),
            'defs' : defaults.investigators,
            'trans' : transformations.investigators
        },
        'locations' : {
            'cons' : constants.locations,
            'defs' : defaults.locations,
            'trans' : transformations.locations,
            'currents' : tools.current_locations_desc( defaults.locations, transformations.locations ),
            'graph' : graph,
            'left_graph' : left_graph,
            'right_graph' : right_graph
        },
        'monsters' : {
            'cons' : constants.monsters,
            'defs' : defaults.monsters,
            'trans' : transformations.monsters,
            'deck_defaults' : defaults.monster_cup,
            'deck_transforms' : transformations.monster_cup
        },
        'weapons' : {
            'cons' : constants.weapons,
            'defs' : defaults.weapons,
            'trans' : transformations.weapons,
            'deck_defaults' : defaults.weapons_deck,
            'deck_transforms' : transformations.weapons_deck
        },
        'consumables' : {
            'cons' : constants.consumables,
            'defs' : defaults.consumables,
            'trans' : transformations.consumables,
            'deck_defaults' : defaults.consumables_deck,
            'deck_transforms' : transformations.consumables_deck
        },
        'tomes' : {
            'cons' : constants.tomes,
            'defs' : defaults.tomes,
            'trans' : transformations.tomes,
            'deck_defaults' : defaults.tomes_deck,
            'deck_transforms' : transformations.tomes_deck
        },
        'passive_buffs' : {
            'cons' : constants.passive_buffs,
            'defs' : defaults.passive_buffs,
            'trans' : transformations.passive_buffs,
            'deck_defaults' : defaults.passive_buffs_deck,
            'deck_transforms' : transformations.passive_buffs_deck
        },
        'active_buffs' : {
            'cons' : constants.active_buffs,
            'defs' : defaults.active_buffs,
            'trans' : transformations.active_buffs,
            'deck_defaults' : defaults.active_buffs_deck,
            'deck_transforms' : transformations.active_buffs_deck
        },
        'oddities' : {
            'cons' : constants.oddities,
            'defs' : defaults.oddities,
            'trans' : transformations.oddities,
            'deck_defaults' : defaults.oddities_deck,
            'deck_transforms' : transformations.oddities_deck
        },
        'spells' : {
            'cons' : constants.spells,
            'defs' : None,
            'trans' : None,
            'deck_defaults' : defaults.spells_deck,
            'deck_transforms' : transformations.spells_deck
        },
        'allies' : {
            'cons' : constants.allies,
            'defs' : None,
            'trans' : None,
            'deck_defaults' : defaults.allies_deck,
            'deck_transforms' : transformations.allies_deck
        },
        'gates' : {
            'cons' : constants.gates,
            'defs' : defaults.gates,
            'trans' : transformations.gates,
            'deck_defaults' : defaults.gates_deck,
            'deck_transforms' : transformations.gates_deck
        },
        'investigator' : currency.board_investigators( defaults.board['investigators'], transformations.board['investigators'] )[ currency.board_current_player( defaults.board['current_player'], transformations.board['current_player'] ) ],
    })


# game defaults

INVESTIGATORS = [ "Sister Mary", "Vincent Lee", "Jenny Barnes", "Harvey Walters" ]
ANCIENT_ONE = "AZATHOTH"

# set investigators
for inv in INVESTIGATORS:
    transformations.board['investigators'].append( ( transformers.add_investigator, inv ) )
    transformations.locations.row( 
        constants.investigators.row( inv ).home
    ).investigators += [ ( transformers.add_occupant, inv ) ]
    # set win condition
    transformations.board['win_cond'].append( transformers.inc_gates_closed_to_win )
    

# set ancient one and apply rules
transformations.board['ancient_one'].append( ( transformers.set_ancient_one, ANCIENT_ONE ) )
    
ancient_ones.RULES[ ANCIENT_ONE ]( next_frame() )

# set gate limit
tools.set_limit( transformations.board['gates_in_arkham'], transformers.dec_gates_in_arkham, params.GATE_LIMIT, x=len( INVESTIGATORS ) )

# set monster limit
tools.set_limit( transformations.board['monsters_in_arkham'], transformers.dec_monster_count,  params.MONSTER_LIMIT, x=len( INVESTIGATORS ) )

# set outskirts limit
tools.set_limit( transformations.board['monsters_in_outskirts'], transformers.dec_monster_count,  params.OUTSKIRTS_LIMIT, x=len( INVESTIGATORS ) )
 
# begin game loop

if currency.board_awakened( defaults.board['awakened'], transformations.board['awakened'] ):
    print( 'The Ancient One has risen!' )
else:
    phases.mythos( next_frame() )

for location in tools.current_locations_desc( defaults.locations, transformations.locations ).filter( 'occupants', [], "!="):
    ic( location.name, location.occupants )

# phases.upkeep( next_frame() )

# phases.mythos_funcs.move_monsters( next_frame() )



def game_loop():

    while True:

        ## set new context for loop
        context = next_frame()

        ## check for win condition
        if context.board.win[0] == 0 and context.board.gates_open == 0:
            print(f'\x1b[38;5;70m\n\n{" "*20}The ancient one is banished! You\'ve saved Arkham and the world!\n\n' )
            break

        ## phase bookkeeping
        if context.board.bookkeeping and phase_bookkeeping[ context.board.phase ]:
            phase_bookkeeping[ context.board.phase ]( context )

        # build command dictionary 
        val_com = { k:v for k,v in commands.phase_commands[ context.board.phase ].items() }
        val_com.update( commands.anytime_commands )

        # receive and process command
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