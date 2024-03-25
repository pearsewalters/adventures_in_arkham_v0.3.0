import transformers, currency, constraints
from tools import debugger as db
from phase_funcs import upkeep_funcs, mythos_funcs
from params import DEBUG_LVL
from context import Context
from icecream import ic

def mythos( context: Context ):
    """ Performs Mythos phase bookkeeping """
    db( 1 )
    print( f"\n\n\x1b[1;38;5;191m{'*'*50}  MYTHOS  {'*'*50}\x1b[22;38;5;70m\n\n")

    # spawn gate

    new_gate =  mythos_funcs.choose_gate_location( context ) 
    gate_to =  mythos_funcs.choose_gate_to( context ) 
    new_clue = mythos_funcs.choose_clue_location( context, exclusion=new_gate )

    # check gate constraints
    spawn_gate = mythos_funcs.spawn_gate( 
        constraints.location_gate_constraint( 
            context.locations.defaults.row( new_gate ).status, 
            transformers.add_gate, 
            context.locations.transforms.row( new_gate ).status 
        )
    )
    too_many_gates = constraints.too_many_gates_constraint(
        context.board.defaults['gates_in_arkham'],
        transformers.inc_gates_in_arkham,
        context.board.transforms['gates_in_arkham']
    )
        
    if too_many_gates:
        # too many gates in arkham
        mythos_funcs.awaken_the_ancient_one( context )
        return None
    
    if spawn_gate:
        # add gate to location
        spawn_gate( context, new_gate, gate_to )
        # do doom things
        mythos_funcs.doom_factory( 
            context, 
            mythos_funcs.monster_factory, 1, [ new_gate ] 
        )
        # do clue things
        mythos_funcs.clue_factory(
            context,
            new_clue
        )
    else:
        # gate tried to open on another gate
        mythos_funcs.monster_surge( context, mythos_funcs.monster_factory )
    
    # move monsters
    mythos_funcs.move_monsters( context )

    return None

def upkeep( context: Context ):
    """ Performs Upkeep phase bookkeeping """    
    db( 1 )
    print( f"\n\n\x1b[1;38;5;191m{'*'*50}  UPKEEP  {'*'*50}\x1b[22;38;5;70m\n")
    # remind the player to refresh items manually
    print( '\x1b[3;38;5;250mRemember to refresh your items...\x1b[23;38;5;70m\n\n' )

    conditions = context.investigator.conditions 
    
    # check if not delayed and lost in time & space 

    lost = upkeep_funcs.lost_in_time_space( conditions )

    if lost:
        lost( context )

    # check for blessing/curse and 1/6 chance
        
    blessed_cursed = upkeep_funcs.blessing_curse( conditions )

    if blessed_cursed:
        blessed_cursed( context )
    
    # check for retainer, then check for loss ( 1/6 chance )
    
    retainer = upkeep_funcs.retainer( conditions )

    if retainer:
        retainer( context )

    # check for bankruptcy/loan, in arkham and 1/2 chance
    
    bank_loan = upkeep_funcs.bank_loan( conditions, context.investigator.location.in_arkham )

    if bank_loan:
        bank_loan( context )

    ## update context reflect any changes
    context.investigator.possessions = currency.investigator_possessions( context.investigator.defaults.possessions, context.investigator.transforms.possessions ) 
    context.investigator.conditions = currency.investigator_conditions( context.investigator.defaults.conditions, context.investigator.transforms.conditions ) 

    # announce focus point count
    print( f'\x1b[3;38;5;250m{context.investigator.nickname} has {currency.investigator_focus( context.investigator.defaults.focus, context.investigator.transforms.focus )[1]} focus point(s). Increase or decrease your skills with focus points.\x1b[23;38;5;250m' )
    
    # set bookkeeping flag to false
    context.board.transforms['bookkeeping'] += [ transformers.toggle_bookkeeping ]

def movement( context ):

    # set bookkeeping flag to false
    context.board.transforms['bookkeeping'] += [ transformers.toggle_bookkeeping ]

def encounters( context ):

    # set bookkeeping flag to false
    context.board.transforms['bookkeeping'] += [ transformers.toggle_bookkeeping ]
     
phase_funcs = [ mythos, upkeep, movement, encounters ]
