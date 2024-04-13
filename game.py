import math, traceback, phases, transformers, commands, params
from tools import adjacencies, currentLocationsDesc, debugger, setLimit
from classes.table import Table
from classes.context import Context
from tables import constants, defaults, transformations
import currency
import ancientOnes

from icecream import ic


phaseBookkeeping = {
    0 : phases.mythos,
    1 : phases.upkeep,
    2 : phases.movement,
    3 : phases.encounters
}

graph, leftGraph, rightGraph = adjacencies( 'locations.csv' )

def nextFrame() -> Context:
    debugger( 0 )
    return Context( **{
            'board' : {
            'phase' : currency.boardCurrentPhase( defaults.board['currentPhase'], transformations.board['currentPhase'] ),
            'bookkeeping' : currency.boardBookkeeping( defaults.board['bookkeeping'], transformations.board['bookkeeping'] ),
            'win' : currency.boardWinCond( defaults.board['winCond'], transformations.board['winCond'] ),
            'gatesOpen' : currency.boardGatesInArkham( defaults.board['gatesInArkham'], transformations.board['gatesInArkham'] ),
            'defs' : defaults.board,
            'trans' : transformations.board
        },
        'mythos' : {
            'headline' : currency.mythosHeadline( defaults.mythosEffects['headline'], transformations.mythosEffects['headline'] ),
            'mystic' : currency.mythosMystic( defaults.mythosEffects['mystic'], transformations.mythosEffects['mystic'] ),
            'urban' : currency.mythosUrban( defaults.mythosEffects['urban'], transformations.mythosEffects['urban'] ),
            'weather' : currency.mythosWeather( defaults.mythosEffects['weather'], transformations.mythosEffects['weather'] ),
            'mvmtPoints' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).mvmtPoints,
            'speed' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).speed,
            'sneak' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).sneak,
            'fight' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).fight,
            'will' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).will,
            'lore' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).lore,
            'luck' : currency.mythosModifiers( defaults.mythosEffects['modifiers'], transformations.mythosEffects['modifiers'] ).luck,
            'resolution' : currency.mythosResolution( defaults.mythosEffects['resolution'],transformations.mythosEffects['resolution'] ),
            'cons' : constants.mythosEffects,
            'defs' : defaults.mythosEffects,
            'trans' : transformations.mythosEffects,
            'deckDefaults' : defaults.mythosDeck,
            'deckTransforms' : transformations.mythosDeck
        },
        'briefs' : {
            'names' : currency.boardInvestigators( defaults.board['investigators'], transformations.board['investigators'] ),
             'cons' : Table( [constants.investigators.table[0]] + [ constants.investigators.row( inv, bundled=False ) for inv in INVESTIGATORS ] ), 
             'defs' : Table( [defaults.investigators.table[0]] + [ defaults.investigators.row( inv, bundled=False ) for inv in INVESTIGATORS ] ),
            'trans' : Table( [transformations.investigators.table[0]] + [ transformations.investigators.row( inv, bundled=False ) for inv in INVESTIGATORS ] ),
             'locs' : [ currency.investigatorLocation( defaults.investigators.row( inv ).location, transformations.investigators.row( inv ).location ) for inv in INVESTIGATORS ]
        },
        'locations' : {
                  'cons' : constants.locations,
                  'defs' : defaults.locations,
                 'trans' : transformations.locations,
              'currents' : currentLocationsDesc( defaults.locations, transformations.locations ),
                 'graph' : graph,
             'leftGraph' : leftGraph,
            'rightGraph' : rightGraph
        },
        'graph' : {
                   'graphDefaults' : defaults.graph,
               'leftGraphDefaults' : defaults.leftGraph,
              'rightGraphDefaults' : defaults.rightGraph,
                 'graphTransforms' : transformations.graph,
             'leftGraphTransforms' : transformations.leftGraph,
            'rightGraphTransforms' : transformations.rightGraph
        },
        'monsters' : {
            'cons' : constants.monsters,
            'defs' : defaults.monsters,
            'trans' : transformations.monsters,
            'deckDefaults' : defaults.monsterCup,
            'deckTransforms' : transformations.monsterCup
        },
        'weapons' : {
            'cons' : constants.weapons,
            'defs' : defaults.weapons,
            'trans' : transformations.weapons,
            'deckDefaults' : defaults.weaponsDeck,
            'deckTransforms' : transformations.weaponsDeck
        },
        'consumables' : {
            'cons' : constants.consumables,
            'defs' : defaults.consumables,
            'trans' : transformations.consumables,
            'deckDefaults' : defaults.consumablesDeck,
            'deckTransforms' : transformations.consumablesDeck
        },
        'tomes' : {
            'cons' : constants.tomes,
            'defs' : defaults.tomes,
            'trans' : transformations.tomes,
            'deckDefaults' : defaults.tomesDeck,
            'deckTransforms' : transformations.tomesDeck
        },
        'passiveBuffs' : {
            'cons' : constants.passiveBuffs,
            'defs' : defaults.passiveBuffs,
            'trans' : transformations.passiveBuffs,
            'deckDefaults' : defaults.passiveBuffsDeck,
            'deckTransforms' : transformations.passiveBuffsDeck
        },
        'activeBuffs' : {
            'cons' : constants.activeBuffs,
            'defs' : defaults.activeBuffs,
            'trans' : transformations.activeBuffs,
            'deckDefaults' : defaults.activeBuffsDeck,
            'deckTransforms' : transformations.activeBuffsDeck
        },
        'oddities' : {
            'cons' : constants.oddities,
            'defs' : defaults.oddities,
            'trans' : transformations.oddities,
            'deckDefaults' : defaults.odditiesDeck,
            'deckTransforms' : transformations.odditiesDeck
        },
        'spells' : {
            'cons' : constants.spells,
            'defs' : None,
            'trans' : None,
            'deckDefaults' : defaults.spellsDeck,
            'deckTransforms' : transformations.spellsDeck
        },
        'allies' : {
            'cons' : constants.allies,
            'defs' : None,
            'trans' : None,
            'deckDefaults' : defaults.alliesDeck,
            'deckTransforms' : transformations.alliesDeck
        },
        'gates' : {
            'cons' : constants.gates,
            'defs' : defaults.gates,
            'trans' : transformations.gates,
            'deckDefaults' : defaults.gatesDeck,
            'deckTransforms' : transformations.gatesDeck
        },
        'investigator' : {
            'name'  : currency.boardInvestigators( defaults.board['investigators'], transformations.board['investigators'] )[ currency.boardCurrentPlayer( defaults.board['currentPlayer'], transformations.board['currentPlayer'] ) ],
            'cons'  : constants.investigators.row( currency.boardInvestigators( defaults.board['investigators'], transformations.board['investigators'] )[ currency.boardCurrentPlayer( defaults.board['currentPlayer'], transformations.board['currentPlayer'] ) ] ),
            'defs'  : defaults.investigators.row( currency.boardInvestigators( defaults.board['investigators'], transformations.board['investigators'] )[ currency.boardCurrentPlayer( defaults.board['currentPlayer'], transformations.board['currentPlayer'] ) ] ),
            'trans' : transformations.investigators.row( currency.boardInvestigators( defaults.board['investigators'], transformations.board['investigators'] )[ currency.boardCurrentPlayer( defaults.board['currentPlayer'], transformations.board['currentPlayer'] ) ] )
        }
    })


# game defaults

INVESTIGATORS = [ "Sister Mary", "Vincent Lee", "Jenny Barnes", "Harvey Walters" ]
# INVESTIGATORS = ["Vincent Lee", "Carolyn Fern"]
ANCIENT_ONE = "AZATHOTH"

# set investigators
for inv in INVESTIGATORS:
    transformations.board['investigators'].append( ( transformers.addInvestigator, inv ) )
    transformations.locations.row( 
        constants.investigators.row( inv ).home
    ).investigators += [ ( transformers.addOccupant, inv ) ]
    # set win condition
    transformations.board['winCond'].append( transformers.incGatesClosedToWin )
    

# set ancient one and apply rules
transformations.board['ancientOne'].append( ( transformers.setAncientOne, ANCIENT_ONE ) )
    
ancientOnes.RULES[ ANCIENT_ONE ]( nextFrame() )

# set gate limit
setLimit( transformations.board['gatesInArkham'], transformers.decGatesInArkham, params.GATE_LIMIT, x=len( INVESTIGATORS ) )

# set monster limit
setLimit( transformations.board['monstersInArkham'], transformers.decMonsterCount,  params.MONSTER_LIMIT, x=len( INVESTIGATORS ) )

# set outskirts limit
setLimit( transformations.board['monstersInOutskirts'], transformers.decMonsterCount,  params.OUTSKIRTS_LIMIT, x=len( INVESTIGATORS ) )
 
# begin game loop

# if currency.boardAwakened( defaults.board['awakened'], transformations.board['awakened'] ):
#     print( 'The Ancient One has risen!' )
# else:
#     phases.mythos( nextFrame() )

# phases.mythos( nextFrame() )
# phases.upkeep( nextFrame() )
# phases.movement( nextFrame() )
# phases.encounters( nextFrame() )


def gameLoop():

    while True:

        ## set new context for loop
        context = nextFrame()

        ## check for win condition
        if context.board.win[0] == 0 and context.board.gatesOpen == 0:
            print(f'\x1b[38;5;70m\n\n{" "*20}The ancient one is banished! You\'ve saved Arkham and the world!\n\n' )
            break

        ## phase bookkeeping
        if context.board.bookkeeping and phaseBookkeeping[ context.board.phase ]:
            phaseBookkeeping[ context.board.phase ]( context )

        # build command dictionary 
        valCom = { k:v for k,v in commands.phaseCommands[ context.board.phase ].items() }
        valCom.update( commands.anytimeCommands )

        # receive and process command
        sentence = input( f'\x1b[38;5;70m>>> ' ).strip().lower().split(' ')
        print('\n')
        command = ic( sentence[0] )
        arguments = ic( sentence[1:] )

        if command not in valCom:
            print( 'Hmm...unsure what you want. Try again. Type "commands" to see a list of valid commands.' )
        elif command == 'quit':
            if commands.quitGame():
                break 
        elif command == 'commands':
            print( commands.showCommands( valCom ) )
        else:
            try:
                if len( arguments ):
                    msg = valCom[command][0]( context, *arguments ) 
                else:
                    msg = valCom[command][0]( context )
                # if command returns a message, print it 
                if msg:
                    print( f'\x1b[38;5;70m{msg}' )
            except TypeError as error:
                traceback.printTb( None )
                print( f'ERROR: {error}' )