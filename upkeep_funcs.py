import constraints, params, tools, transformers
from icecream import ic

if not params.DEBUG or params.DEBUG_LVL < 1:
    ic.disable()


def lost_in_time_space( conditions ):
    """ Checks if lost in time & space on upkeep; returns a protocol or None """
    ic()
    def lost_protocol( context ):
        ic()
        # remove lost in time & space flag
        context['investigator']['transforms'][3].append( transformers.remove_lost )
        # relocate investigator 
        home = context['investigator']['defaults'][8][0]
        context['investigator']['transforms'][8].append( (transformers.change_loc, home ))
        # set investigator 'in arkham' flag
        context['investigator']['transforms'][8].append( transformers.set_in_arkham )
        print( f'{context['investigator']['nickname']} has been transported back to Arkham! What a sigh of relief that must be....\n')

    if not conditions[0] and conditions[1]:
        ic()
        return lost_protocol

    return None

def blessing_curse( conditions ):
    """ Checks for blessing/curse on upkeep; return a protocol or None """
    ic()
    def first_after_curse( context ):
        ic()
        # first round after being cursed...
        context['investigator']['transforms'][3].append( transformers.add_blessing )
    
    def first_after_blessing( context ):
        ic()
        # first round after being blessed
        context['investigator']['transforms'][3].append( transformers.add_curse )

    def blessing_curse_protocol( context ):
        ic()
        # if blessed
        if conditions[7] == 1:
            context['investigator']['transforms'][3].append( transformers.remove_blessing )
            print( f'{context['investigator']['nickname']} has lost their blessing! Blast this uncareful cosmos!\n' )
        # if cursed
        if conditions[7] == -1:
            context['investigator']['transforms'][3].append( transformers.remove_curse )
            print( f'{context['investigator']['nickname']} is no longer cursed! Thank their lucky stars!' )
        

    # if first round after being blessed or cursed
    if (conditions[7] % 4) == 2:
        # if blessed
        if conditions[7] == 1:
            return first_after_blessing
        # if cursed
        elif conditions[7] == -1:
            return first_after_curse
    # if after first round
    elif (conditions[7] % 2) == 1 and tools.roll_die( params.BLESS_CURSE_DIE ):
        return blessing_curse_protocol
    
    return None

def retainer( conditions ):
    """ Checks for retainer on upkeep; return a protocol or None """
    ic()
    def retainer_payout( context ):
        """ Pay out retainer amount """
        ic()
        context['investigator']['transforms'][12] += [ transformers.inc_money for n in range(params.RETAINER_PAYOUT ) ]
        print( f'{context['investigator']['nickname']}\'s retainer has kicked in. They now have two more dollars' )

    def first_after_retainer( context ):
        ic()
        # first round after gaining retainer
        retainer_payout( context )
        context['investigator']['transforms'][3].append( transformers.remove_retainer )

    def retainer_protocol( context ):
        ic()
        retainer_payout( context )
        if tools.roll_die( params.RETAINER_DIE ):
            context['investigator']['transforms'][3].append( transformers.remove_retainer )
            print( f'{context['investigator']['nickname']} has been fired from their job! In \x1b[3mthis\x1b[23m economy? With all of these \x1b[3mmonsters??\x1b[23m' )

    # first round after retainer
    if conditions[3] == 2:
        return first_after_retainer
    # subsequent rounds after
    elif conditions[3] == 1:
        return retainer_protocol
    
    return None

def bank_loan( conditions, in_arkham ):
    """ Checks for bank loan on upkeep; return a protocol or None """
    ic()
    def first_after_loan( context ):
        """ Investigator does not have to roll; reset flag to 1 """
        ic()
        context['investigator']['transforms'][3].append( transformers.remove_bank_loan )

    def repo_dequip( context ):
        """ Bank dequips investigator """
        ic()
        if len( context['investigator']['equipped_items'] ):
            for equipped in context['investigator']['equipped_items']:
                weapon = context['weapons']['constants'].row( equipped )
                if weapon != None:
                    for hand in range( weapon[3] ):
                        context['investigator']['transforms'][10].append( transformers.inc_hands )
                context['investigator']['transforms'][10].append( ( transformers.unequip, weapon ) )

    def repo_items( variety, remove_func, context ):
        """ Generalized repo for any item type """
        ic()
        for item in context['investigator']['possessions'][variety]:
            # remove from investigator
            context['investigator']['transforms'][12].append( (remove_func, item) )
            # add back to deck
            context[variety]['deck_tranforms'].append( ( transformers.inc_freq, item ) )
            print( f'The bank has repossessed {context['investigator']['nickname']}\'s {item}')

    def repo_buffs( variety, remove_func, context ):
        """ Bank repos select buffs """
        ic()
        for buff in context[variety]['constants'].filter( 'rarity', 'learned', cond='!=' ):
            if buff[0] in context['investigator']['possessions'][variety]:
                # remove buff from investigator
                context['investigator']['transforms'][12].append( ( remove_func, buff[0] ) )
                # add back to deck
                context[variety]['deck_transforms'].append( (transformers.inc_freq), buff[0] )
                print( f'The bank has repossessed {context['investigator']['nickname']}\'s {buff[0]}\n')

    def bank_loan_protocol( context ):
        """ If the investigator can't pay interest, the bank repos all their items """
        ic()
        enough_cash = constraints.money_constraint( context['investigator']['defaults'][12], transformers.dec_money, context['investigator']['transforms'][12] )
        
        if enough_cash:
            context['investigator']['transforms'][12].append( transformers.dec_money )
            print( f'Interest payment due! {context['investigator']['nickname']} has paid a dollar to keep the bank away.' )
        else:
            print( f'Time to pay back the loan! The Bank of Arkham has found you\n')
            # ensure bank loan cannot be given out in the future
            context['investigator']['transforms'][3].append( transformers.set_bankrupt )
            # dequip items
            repo_dequip( context )
            # lose weapons
            repo_items( 'weapons', transformers.remove_weapon_item, context )
            # lose cnosumables
            repo_items( 'consumables', transformers.remove_consumable_item, context )
            # lose tomes
            repo_items( 'tomes', transformers.remove_tome_item, context )
            # lose passive buffs
            repo_buffs( 'passive_buffs', transformers.remove_passive_buff, context )
            # lose active buffs
            repo_buffs( 'active_buffs', transformers.remove_active_buff, context )
            # lose oddities
            repo_items( 'oddities', transformers.remove_oddity_item, context )
    
    # first round after receiving loan
    if conditions[4] == 2:
        return first_after_loan
    # subsequent rounds; investigator has to be in arkham
    elif conditions[4] == 1 and in_arkham and tools.roll_die( params.BANK_LOAN_DIE ):
        return bank_loan_protocol

    return None