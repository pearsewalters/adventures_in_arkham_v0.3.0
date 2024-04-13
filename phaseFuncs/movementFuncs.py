from classes.context import Context
from classes.data import Investigator
import currency, investigatorFuncs, transformers
from typing import Callable
from tools import debugger as db


def delayed( conditions: Investigator.conditions  ) -> Callable | None:

    def delayedProtocol( context: Context ) -> None:
        db( 2 )
        # remove delay from investigator
        context.investigator.transforms.conditions += [ transformers.removeDelayed ]

        print( f"{ context.investigator.nickname} is no longer DELAYED. However, they are still recuperating and cannot move this turn." )


    if conditions.delayed:
        return delayedProtocol
    return None

def inArkham( location: Investigator.location ) -> Callable | None:

    def inArkhamProtocol( context: Context ) -> None:
        db( 2 )
        # assign mvmt points to investigator
        context.investigator.transforms.location += [ transformers.incMvmtPoints ] * currency.investigatorSkill( context.investigator.defaults.speed, context.investigator.transforms.speed ).currentSpeed
        # search through investigator items for mvmt point buffs
        for passiveBuff in context.investigator.possessions['passiveBuffs']:
            if context.passiveBuffs.constants.row( passiveBuff ).check == 'mvmt':
                 context.investigator.transforms.location += [ transformers.incMvmtPoints ] * currency.item_stats( context.passiveBuffs.defaults.row( passiveBuff ).stats, context.passiveBuffs.transforms.row( passiveBuff ).stats ).bonus

    if location.inArkham:
        return inArkhamProtocol
    return None

def inOtherWorld( context: Context ) -> None:
    """ 
        Moves investigator along to next location; doesn't work with multiple adjacencies and 
        is only appropriate for moving investigator through an other world and back to arkham 
    """    
    db( 2 )
    # move investigator to next location
    locConst = investigatorFuncs.relocateInvestigator(
        context,
        context.investigator.defaults,
        context.investigator.transforms,
        currency.graph( 
            context.graph.graphDefaults, 
            context.graph.graphTransforms 
        ).table[
            currency.investigatorLocation( 
                context.investigator.defaults.location, 
                context.investigator.transforms.location 
            ).currentLocation
        ].index( 1 )
    )

    if locConst.variety == "LOCATION":
        # they are safely back from the other world, mark location as explored, investigator in arkham, 
        #   and reinstate the edge between location & street
        context.locations.transforms.row( locConst.name ).status += [ transformers.addExplored ]
        context.investigator.transforms.conditions += [ transformers.addInArkham ]
        for row in currency.graph( context.graph.graphDefaults, context.graph.graphTransforms ).table:
            # if there is an incoming adjacency to the location, make sure there is now an outgoing adjacency as well 
            if row[ context.graph.graphDefaults.index( locConst.name ) ] == 1:
                context.graph.graphTransforms += [( 
                    transformers.addAdjacency,
                    context.graph.graphDefaults.index( row[0] ),
                    context.graph.graphDefaults.index( locConst.name )
                )]
    
    
    