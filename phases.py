from classes.context import Context
import transformers, currency, constraints
from tools import debugger as db
from phaseFuncs import mythosFuncs, upkeepFuncs, movementFuncs, encountersFuncs
from params import DEBUG_LVL
from icecream import ic

def mythos( context ):
    """ Performs Mythos phase bookkeeping """
    db( 1 )
    print( f"\n\n\x1b[1;38;5;191m{'*'*50}  MYTHOS  {'*'*50}\x1b[22;38;5;70m\n\n")

    # spawn gate

    new_gate =  mythosFuncs.chooseGateLocation( context ) 
    gate_to =  mythosFuncs.chooseGateTo( context ) 
    new_clue = mythosFuncs.chooseClueLocation( context, exclusion=new_gate )

    # check gate constraints
    spawn_gate = mythosFuncs.spawnGate( 
        constraints.gateAtLocation( 
            context.locations.defaults.row( new_gate ).status, 
            transformers.addGate, 
            context.locations.transforms.row( new_gate ).status 
        )
    )
    too_many_gates = constraints.boardGateLimit(
        context.board.defaults['gatesInArkham'],
        transformers.incGatesInArkham,
        context.board.transforms['gatesInArkham']
    )
        
    if too_many_gates:
        # too many gates in arkham
        mythosFuncs.awakenTheAncientOne( context )
        return None
    
    if spawn_gate:
        # add gate to location
        spawn_gate( context, new_gate, gate_to )
        # do doom things
        mythosFuncs.doomFactory( 
            context, 
            mythosFuncs.monsterFactory, 1, [ new_gate ] 
        )
        # do clue things
        mythosFuncs.clueFactory(
            context,
            new_clue
        )
    else:
        # gate tried to open on another gate
        mythosFuncs.monsterSurge( context, mythosFuncs.monsterFactory )
    
    # move monsters
    mythosFuncs.moveMonsters( context )

    # resolve last mythos phase's effect
    if context.mythos.resolution:
        context.mythos.resolution( context )

    # finally activate mythos effects
    resolution = ic( mythosFuncs.activateEffect( context ) )
    context.mythos.transforms[ 'resolution' ] += [ ( transformers.setResolution, resolution ) ]

    return None

def upkeep( context: Context ):
    """ Performs Upkeep phase bookkeeping """    
    db( 1 )
    print( f"\n\n\x1b[1;38;5;191m{'*'*50}  UPKEEP  {'*'*50}\x1b[22;38;5;70m\n")
    # remind the player to refresh items manually
    print( '\x1b[3;38;5;250mRemember to refresh your items...\x1b[23;38;5;70m\n\n' )

    conditions = context.investigator.conditions 
    
    # check if not delayed and lost in time & space 

    lost = upkeepFuncs.lostInTimeSpace( conditions )

    if lost:
        lost( context )

    # check for blessing/curse and 1/6 chance
        
    blessedCursed = upkeepFuncs.blessingCurse( conditions )

    if blessedCursed:
        blessedCursed( context )
    
    # check for retainer, then check for loss ( 1/6 chance )
    
    retainer = upkeepFuncs.retainer( conditions )

    if retainer:
        retainer( context )

    # check for bankruptcy/loan, in arkham and 1/2 chance
    
    bankLoan = upkeepFuncs.bankLoan( conditions, context.investigator.location.inArkham )

    if bankLoan:
        bankLoan( context )

    ## update context reflect any changes
    context.investigator.possessions = currency.investigatorPossessions( context.investigator.defaults.possessions, context.investigator.transforms.possessions ) 
    context.investigator.conditions = currency.investigatorConditions( context.investigator.defaults.conditions, context.investigator.transforms.conditions ) 

    # announce focus point count
    print( f'\x1b[3;38;5;250m{context.investigator.nickname} has {currency.investigatorFocus( context.investigator.defaults.focus, context.investigator.transforms.focus )[1]} focus point(s). Increase or decrease your skills with focus points.\x1b[23;38;5;250m' )
    
    # set bookkeeping flag to false
    context.board.transforms['bookkeeping'] += [ transformers.toggleBookkeeping ]

def movement( context: Context ):

    print( f"\n\n\x1b[1;38;5;191m{'*'*50}  MOVEMENT  {'*'*50}\x1b[22;38;5;70m\n\n")

    conditions = context.investigator.conditions
    location = context.investigator.location

    # check if investigator is delayed

    delayed = movementFuncs.delayed( conditions )

    if delayed:
        delayed( context )
        # set bookkeeping flag to false and end movement bookkeeping
        context.board.transforms['bookkeeping'] += [ transformers.toggleBookkeeping ]
        return None
    
    # check if investigator is in arkham 

    inArkham = movementFuncs.inArkham( location )

    if inArkham:
        # assign mvmt points
        inArkham( context )
         # announce mvmt point count
        print( f'\x1b[3;38;5;250m{context.investigator.nickname} has {currency.investigatorLocation( context.investigator.defaults.location, context.investigator.transforms.location ).mvmtPoints} movement point(s).\x1b[23;38;5;250m' )
        # set bookkeeping flag to false and end movement bookkeeping 
        context.board.transforms['bookkeeping'] += [ transformers.toggleBookkeeping ]
        return None
    
    # investigator is neither delayed nor in arkham

    movementFuncs.inOtherWorld( context )

    # set bookkeeping flag to false and end movement bookkeeping 
    context.board.transforms['bookkeeping'] += [ transformers.toggleBookkeeping ]
    return None
    
def encounters( context: Context ):

    print( f"\n\n\x1b[1;38;5;191m{'*'*50}  ENCOUNTERS  {'*'*50}\x1b[22;38;5;70m\n\n")

    location = context.investigator.location

    # if investigator is standing on a gate, immediately move them into the other world

    onGate = encountersFuncs.onGate( location )
    if onGate:
        onGate( context )

    # if investigator is on location with a special encounter type
    if context.locations.constants[ location.currentLocation ].special:

        # the special might return a function that the investigator should be able to call from the text user interface
        interfaceCommand = context.locations.constants[ location.currentLocation ].special( context )

    
    # set bookkeeping flag to false
    context.board.transforms['bookkeeping'] += [ transformers.toggleBookkeeping ]
     
phase_funcs = [ mythos, upkeep, movement, encounters ]
