from tools import bound, math
import transformers
from math import factorial
from random import uniform
from collections import namedtuple
from classes.context import Context, currency
from classes.table import Table

from icecream import ic 

SkillRollMsg = namedtuple( "skill_roll_message", ["result", "msg"] )

def relocateInvestigator( context: Context, invDefaults: Table.Row, invTransforms: Table.Row, newLocID: int ) -> Table.Row:
    """ Removes investigator from their current location and installs them in new_loc_id """
    # remove investigator from their current location
    context.locations.transforms[ 
        currency.investigatorLocation( 
            invDefaults.location, 
            invTransforms.location ).currentLocation 
        ].investigators += [ (transformers.removeInvestigator, invDefaults.name) ]
    # add investigator to new location
    context.locations.transforms[ newLocID ].investigators += [ (transformers.addInvestigator, invDefaults.name) ]
    # change investigator's current location
    invTransforms.location += [ (transformers.changeLocation, newLocID) ]

    return context.locations.constants[ newLocID ]


def skillCheck( context: Context, inv: str, modifier: int, difficulty: int, skill: str, comp: bool=False ) -> bool: 

    # a skill check is an answer to the binomial distro formula
    def binomial( k,n,p ):
        return ( factorial(n)/(factorial(k)*factorial(n-k)) ) * p**k * (1-p)**(n-k)
    
    if not comp:
        n = currency.investigatorSkill( getattr( context.briefs.defaults.row( inv ), skill), getattr( context.briefs.transforms.row( inv ), skill ) )[1] 
    else:
        n = currency.investigatorComplementSkill( getattr( context.briefs.defaults.row( inv ), skill), getattr( context.briefs.transforms.row( inv ), skill ) ) 

    p = 2 + bound( currency.investigatorConditions( context.briefs.defaults.row( inv ).conditions, context.briefs.transforms.row( inv ).conditions ).blessed_cursed )

    if sum( [ binomial( k, n + modifier, p/6 ) for k in range( difficulty, n + modifier + 1 ) ] ) < uniform( 0,1 ) :
        return False
    return True

def addBuffs( context: Context, inv: str, check: str ) -> int:
    """ Combs through inv's passive buffs and returns any modifiers """

    bonus = 0

    for passive_buff in currency.investigatorPossessions( context.briefs.defaults.row( inv ).possessions, context.briefs.transforms.row( inv ).possessions )['passive_buffs']:
        # look which check the passive buff is good for
        if context.passiveBuffs.constants.row( passive_buff ).check == check:
            bonus += currency.item_stats( context.passiveBuffs.defaults.row( passive_buff ).stats, context.passiveBuffs.transforms.row( passive_buff ).stats ).bonus
            ic( passive_buff, bonus )

    return bonus


def speedCheck( context: Context, inv: str, modifier: int, difficulty: int=1, success_msg: str=None, failure_msg: str=None ) -> SkillRollMsg:

    bonus = addBuffs( context, inv, 'speed' )

    if skillCheck(context, inv, modifier + bonus, difficulty, 'speed' ):
        return SkillRollMsg( result=True, msg=success_msg )
    return SkillRollMsg( result=False, msg=failure_msg )

def sneak_check( context: Context, inv: str, modifier: int, difficulty: int=1, success_msg: str=None, failure_msg: str=None ) -> SkillRollMsg:

    bonus = addBuffs( context, inv, 'sneak' )

    if skillCheck(context, inv, modifier + bonus, difficulty, 'speed', comp=True ):
        return SkillRollMsg( result=True, msg=success_msg )
    return SkillRollMsg( result=False, msg=failure_msg )

def fight_check( context: Context, inv: str, modifier: int, difficulty: int=1, success_msg: str=None, failure_msg: str=None ) -> SkillRollMsg:

    bonus = addBuffs( context, inv, 'fight' )

    if skillCheck(context, inv, modifier + bonus, difficulty, 'fight' ):
        return SkillRollMsg( result=True, msg=success_msg )
    return SkillRollMsg( result=False, msg=failure_msg )

def will_check( context: Context, inv: str, modifier: int, difficulty: int=1, success_msg: str=None, failure_msg: str=None ) -> SkillRollMsg:
    
    bonus = addBuffs( context, inv, 'will' )

    if skillCheck(context, inv, modifier + bonus, difficulty, 'fight', comp=True ):
        return SkillRollMsg( result=True, msg=success_msg )
    return SkillRollMsg( result=False, msg=failure_msg )

def lore_check( context: Context, inv: str, modifier: int, difficulty: int=1, success_msg: str=None, failure_msg: str=None ) -> SkillRollMsg:

    bonus = addBuffs( context, inv, 'lore' )

    if skillCheck(context, inv, modifier + bonus, difficulty, 'lore' ):
        return SkillRollMsg( result=True, msg=success_msg )
    return SkillRollMsg( result=False, msg=failure_msg )

def luckCheck( context: Context, inv: str, modifier: int, difficulty: int=1, success_msg: str=None, failure_msg: str=None ) -> SkillRollMsg:

    bonus = addBuffs( context, inv, 'luck' )

    if skillCheck(context, inv, modifier + bonus, difficulty, 'lore', comp=True ):
        return SkillRollMsg( result=True, msg=success_msg )
    return SkillRollMsg( result=False, msg=failure_msg )


def arrest_investigator( context: Context, inv_defaults: Table.Row, inv_transforms: Table.Row ) -> None:
    """ Puts investigator in jail and removes half their money rounded down. Assumes they are in Arkham """
    # relocate investigator
    inv_transforms.location += [ ( transformers.change_location, 9 ) ]
    context.locations.transforms[ currency.investigatorLocation( inv_defaults.location, inv_transforms.location ).current_location ].investigators += [ (transformers.removeInvestigator, inv_defaults.name) ]
    context.locations.transforms[ 9 ].investigators += [ ( transformers.addOccupant, inv_defaults.name ) ]
    print( f'{inv_defaults.name} is now in jail at the POLICE STATION' )
    # remove half their money
    loss = math.floor( currency.investigatorPossessions( inv_defaults.possessions, inv_transforms.possessions )['money'] / 2 )
    if loss > 0:
        print( f'They will have to post bail! Happens to be ${loss}...' )
        for dollar in range( loss ):
            inv_transforms.possessions += [ transformers.decMoney ]
