import params, transformers
from classes.context import Context
from classes.data import Investigator
from tools import roll_die, debugger as db
from icecream import ic

def lostInTimeSpace( conditions: Investigator.conditions ):
    """ Checks if lost in time & space on upkeep; returns a protocol or None """
    
    def lost_protocol( context: Context ):
        db( 2 )
        # remove lost in time & space flag
        context.investigator.transforms.conditions += [ transformers.removeLostInTimeAndSpace ]
        # relocate investigator 
        context.investigator.transforms.location += [ ( transformers.change_loc, context.investigator.constants.home ) ]
        # set investigator 'in arkham' flag
        context.investigator.transforms.location += [ transformers.addInArkham ]

        print( f'{context.investigator.nickname} has been transported back to Arkham! What a sigh of relief that must be....\n')

    if not conditions.delayed and conditions.lostInTimeAndSpace:
        return lost_protocol

    return None

def blessingCurse( conditions: Investigator.conditions ):
    """ Checks for blessing/curse on upkeep; return a protocol or None """
    
    def first_after_curse( context ):
        db( 2 )
        # first round after being cursed...
        context.investigator.transforms.conditions += [ transformers.addBlessing ]
    
    def first_after_blessing( context ):
        db( 2 )
        # first round after being blessed
        context.investigator.transforms.conditions += [ transformers.add_curse ]

    def blessing_curse_protocol( context ):
        db( 2 )
        # if blessed
        if conditions.blessedCursed == 1:
            context.investigator.transforms.conditions += [ transformers.remove_blessing ]
            print( f'{context.investigator.nickname} has lost their blessing! Blast this uncareful cosmos!\n' )
        # if cursed
        if conditions.blessedCursed == -1:
            context.investigator.transforms.conditions += [ transformers.remove_curse ]
            print( f'{context.investigator.nickname} is no longer cursed! Thank their lucky stars!' )

    # if first round after being blessed or cursed
    if (conditions.blessedCursed % 4) == 2:
        # if blessed
        if conditions.blessedCursed == 1:
            return first_after_blessing
        # if cursed
        elif conditions.blessedCursed == -1:
            return first_after_curse
    # if after first round
    elif (conditions.blessedCursed % 2) == 1 and roll_die( params.BLESS_CURSE_DIE ):
        return blessing_curse_protocol
    
    return None

def retainer( conditions: Investigator.conditions ):
    """ Checks for retainer on upkeep; return a protocol or None """
    
    def retainer_payout( context: Context ):
        """ Pay out retainer amount """
        db( 2 )
        context.investigator.transforms.possessions += [ transformers.incMoney for n in range(params.RETAINER_PAYOUT ) ]
        print( f'{context.investigator.nickname}\'s retainer has kicked in. They now have two more dollars' )

    def first_after_retainer( context: Context ):
        db( 2 )
        # first round after gaining retainer
        retainer_payout( context )
        context.investigator.transforms.conditions += [ transformers.removeRetainer ]

    def retainer_protocol( context: Context ):
        db( 2 )
        retainer_payout( context )
        if roll_die( params.RETAINER_DIE ):
            context.investigator.transforms.conditions += [ transformers.removeRetainer ]
            print( f'{context.investigator.nickname} has been fired from their job! In \x1b[3mthis\x1b[23m economy? With all of these \x1b[3mmonsters??\x1b[23m' )

    # first round after retainer
    if conditions.retainer == 2:
        return first_after_retainer
    # subsequent rounds after
    elif conditions.retainer == 1:
        return retainer_protocol
    
    return None

def bankLoan( conditions: Investigator.conditions, in_arkham: int ):
    """ Checks for bank loan on upkeep; return a protocol or None """
    
    def firstAfterLoan( context: Context ):
        """ Investigator does not have to roll; reset flag to 1 """
        db( 2 )
        context.investigator.transforms.conditions += [ transformers.remove_bank_loan ]

    def repoDequip( context: Context ):
        """ Bank dequips investigator """
        db( 2 )
        if len( context.investigator.equipped_items ):
            for equipped in context.investigator.equipped_items:
                weapon = context.weapons.constants.row( equipped )
                if weapon != None:
                    for hand in range( weapon[3] ):
                        context.investigator.transforms.equipped_items += [ transformers.incHands ] 
                context.investigator.transforms.equipped_items += [ ( transformers.unequip, weapon ) ] 

    def repoItems( variety, remove_func, context: Context ):
        """ Generalized repo for any item type """
        db( 2 )
        for item in context.investigator.possessions[variety]:
            # remove from investigator
            context.investigator.transforms.possessions += [ (remove_func, item) ]
            # add back to deck
            getattr( context, variety ).deck_transforms += [ ( transformers.incFreq, item ) ]
            
            print( f'The bank has repossessed {context.investigator.nickname}\'s {item}')

    def repoBuffs( variety, remove_func, context: Context ):
        """ Bank repos select buffs """
        db( 2 )
        for buff in getattr( context, variety ).constants.filter( 'rarity', 'learned', cond='!=' ):
            if buff.name in context.investigator.possessions[variety]:
                # remove buff from investigator
                context.investigator.transforms.possessions += [ ( remove_func, buff.name ) ]
                # add back to deck
                getattr( context, variety ).deck_transforms += [ (transformers.incFreq, buff.name ) ]
                print( f'The bank has repossessed {context.investigator.nickname}\'s {buff.name}\n')

    def bankLoanProtocol( context: Context ):
        """ If the investigator can't pay interest, the bank repos all their items """
        db( 2 )
        enough_cash = True if context.investigator.possessions['money'] >= 1 else False
        
        if enough_cash:
            context.investigator.transforms.possessions += [ transformers.decMoney ]
            print( f'Interest payment due! {context.investigator.nickname} has paid a dollar to keep the bank away.' )
        else:
            print( f'Time to pay back that loan! The Bank of Arkham has found you\n')
            # ensure bank loan cannot be given out in the future
            context.investigator.transforms.conditions += [ transformers.set_bankrupt ]
            # dequip items
            repoDequip( context )
            # lose weapons
            repoItems( 'weapons', transformers.removeWeaponItem, context )
            # lose cnosumables
            repoItems( 'consumables', transformers.removeConsumableItem, context )
            # lose tomes
            repoItems( 'tomes', transformers.removeTomeItem, context )
            # lose passive buffs
            repoBuffs( 'passive_buffs', transformers.removePassiveBuff, context )
            # lose active buffs
            repoBuffs( 'active_buffs', transformers.removeActiveBuff, context )
            # lose oddities
            repoItems( 'oddities', transformers.removeOddityItem, context )
    
    # first round after receiving loan
    if conditions.bankLoan == 2:
        return firstAfterLoan
    # subsequent rounds; investigator has to be in arkham
    elif conditions.bankLoan == 1 and in_arkham and roll_die( params.BANK_LOAN_DIE ):
        return bankLoanProtocol

    return None