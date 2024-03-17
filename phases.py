import tools, transformers, currency, constraints, commands, upkeep_funcs
from params import DEBUG, DEBUG_LVL, BLESS_CURSE_DIE, RETAINER_DIE, BANK_LOAN_DIE

## debugging
if not DEBUG or DEBUG_LVL < 0:
    ic.disable()

def mythos( context ):
    """ Performs Mythos phase bookkeeping """

    print( f'\n\n\x1b[1;38;5;191m{'*'*50}  MYTHOS  {'*'*50}\x1b[22;38;5;70m\n\n')

    gate_distro = {}
    clue_distro = {}

    for loc_const, loc_descs in zip( context['locations']['constants'][1:], context['locations']['currents'][1:] ):

        instability = context['locations']['constants'][0].index( 'instability' )
        mystery = context['locations']['constants'][0].index( 'mystery' )
        current_clues = loc_descs[2][0]
        historical_clues = loc_descs[2][1]
        # gate likelihood := instability ** ( 1 + current clues ) * historical clues 
        gate_distro[ loc_const[0] ] = ( loc_const[ instability ] ** ( 1+ current_clues ) ) * historical_clues
        # clue likelihood := mystery ** historical clues * (1 + current clues )
        clue_distro[ loc_const[0] ] = ( loc_const[ mystery ] ** historical_clues ) * current_clues 

    
    new_gate = tools.rand_from_distro( gate_distro )
    new_gate_desc =  {
        'index' : [ row[0] for row in context['locations']['constants'] ].index( new_gate ),
        'defaults' : [ row for row in context['locations']['defaults'][1:] if row[0] ==  new_gate ][0],
        'transforms' : [ row for row in context['locations']['transforms'][1:] if row[0] ==  new_gate ][0]   
    }
   
    new_clue = tools.rand_from_distro( { k:v for k,v in clue_distro.items() if k != new_gate } )
    new_clue_desc =  {
        'index' : [ row[0] for row in context['locations']['constants'] ].index( new_clue ),
        'defaults' : [ row for row in context['locations']['defaults'][1:] if row[0] ==  new_clue ][0],
        'transforms' : [ row for row in context['locations']['transforms'][1:] if row[0] ==  new_clue ][0]   
    }

    draw_gate = constraints.location_gate_constraint( new_gate_desc['defaults'][2], transformers.add_gate, new_gate_desc['transforms'][2] )
    gate_limit = constraints.too_many_gates_constraint( context['board']['defaults']['gates_open'], transformers.inc_gates_open, context['board']['transforms']['gates_open'] )
    clue_limit = constraints.location_clues_constraint( new_clue_desc['defaults'][2], transformers.inc_clue, new_clue_desc['transforms'][2] )
    doom_limit = constraints.doom_track_constraint( context['board']['defaults']['doom_track'], transformers.inc_doom_track, context['board']['transforms']['doom_track'] )

    if draw_gate == 1:
        if gate_limit == 1:
            # add doom
            if doom_limit == 1:
                # add gate to location
                context['locations']['transforms'][ new_gate_desc['index'] ][2].append( transformers.add_gate )
                # remove all clues from that location:
                for n in range( currency.location_status( new_gate_desc['defaults'][2], new_gate_desc['transforms'][2] )[0] ):
                    context['locations']['transforms'][ new_gate_desc['index'] ][2].append( transformers.dec_clue )
                # increase gates on board
                context['board']['transforms']['gates_open'].append( transformers.inc_gates_open )
                # announce new gate
                print( f'Something strange has occurred at {new_gate}!' )
                
                # add monster
                # add_monster( new_gate )
                # move monsters
                # move_monsters()
            
                # add clue to new location if it doesn't have a gate on it
                if clue_limit == 1:
                    context['locations']['transforms'][ new_clue_desc['index'] ][2].append( transformers.inc_clue )
                    # announce clue
                    print( f'Something interesting has turned up at {new_clue}...')
                # increase historical clues no matter what
                context['locations']['transforms'][ new_clue_desc['index'] ][2].append( transformers.inc_historical_clues )
        elif gate_limit == 2:
            # awaken_the_ancient_one()
            ...
    elif draw_gate == 2:
        print( 'A monster surge!' )

    print( "\x1b[3;38;5;250mType 'next phase' to move on to UPKEEP...\x1b[23;38;5;70m\n\n" )

    # set bookkeeping flag to false
    context['board']['transforms']['bookkeeping'].append( transformers.toggle_bookkeeping )


def upkeep( context ):
    """ Performs Upkeep phase bookkeeping """    

    print( f'\n\n\x1b[1;38;5;191m{'*'*50}  UPKEEP  {'*'*50}\x1b[22;38;5;70m\n')
    # remind the player to refresh items manually
    print( '\x1b[3;38;5;250mRemember to refresh your items...\x1b[23;38;5;70m\n\n' )

    conditions = ic( context['investigator']['conditions'] )
    
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
    
    bank_loan = upkeep_funcs.bank_loan( conditions )

    if bank_loan:
        bank_loan( context )


    ## update context reflect any changes
    context['investigator']['possessions'] = ic( currency.possessions( context['investigator']['defaults'][12], context['investigator']['transforms'][12] ) )
    context['investigator']['conditions'] = ic( currency.condtions( context['investigator']['defaults'][3], context['investigator']['transforms'][3] ) )

    # announce focus point count
    print( f'\x1b[3;38;5;250m{context['investigator']['nickname']} has {currency.skill( context['investigator']['defaults'][4], context['investigator']['transforms'][4] )[1]} focus point(s). Increase or decrease your skills with focus points.\x1b[23;38;5;250m' )
    
    # set bookkeeping flag to false
    context['board']['transforms']['bookkeeping'].append( transformers.toggle_bookkeeping )

    
def movement( context ):

    # set bookkeeping flag to false
    context['board']['transforms']['bookkeeping'].append( transformers.toggle_bookkeeping )

def encounters( context ):

    # set bookkeeping flag to false
    context['board']['transforms']['bookkeeping'].append( transformers.toggle_bookkeeping )

        
    

phase_funcs = [ mythos, upkeep, movement, encounters ]