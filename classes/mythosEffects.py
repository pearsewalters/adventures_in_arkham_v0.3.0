from icecream import ic
import constraints, transformers
import investigatorFuncs
from classes.context import Context, currency
from typing import Generator, Callable
from classes.table import Table
from phaseFuncs.mythosFuncs import removeMonster, terrorFactory, monsterFactory

# useful funcs...
def monstersOfTypeLocation( context: Context, monster: str=None, dimension: int=None ) -> Generator:
    """ Yields location defaults and transforms for each monster of the provided kind"""
    for location in context.locations.currents:
        for occupant in location.occupants:
            if occupant == monster or context.monsters.constants.row( monster ).dimension == dimension:
                yield occupant, context.locations.defaults.row( location.name ), context.locations.transforms.row( location.name )

def clearMonstersOfType( context: Context, monster: str=None, dimension: int=None ) -> int:
    """ Removes monsters of provided kind from anywhere in Arkham """
    monsters_cleared = 0
    for monster, loc_defaults, loc_transforms in monstersOfTypeLocation( context, monster, dimension ):
        removeMonster( context, monster, loc_defaults.name )
        monsters_cleared += 1

    return monsters_cleared

def investigatorsInOtherWorlds( context: Context ) -> Generator:
    """ Yields investigators who are not in Arkham """
    for inv_defaults, inv_transforms in zip( context.briefs.defaults, context.briefs.transforms ):
        if not currency.investigatorLocation( inv_defaults.location, inv_transforms.location ).inArkham:
            yield currency.investigatorLocation( inv_defaults.location, inv_transforms.location ).currentLocation, inv_defaults, inv_transforms

def allGatesInArkham( context: Context ) -> Generator:
    """ Yields gate, defaults, and transforms for locations that have any gate on them """
    for location in context.locations.currents:
        if location.status.gate:
            yield location.gate_to, context.locations.defaults.row( location.name ), context.locations.transforms.row( location.name )

def gatesTo( context: Context, other_world: str ) -> Generator:
    """ Yields defaults and transforms that have a gate to other_world on them """
    for location in context.locations.currents:
        if other_world in location.gate_to:
            yield context.locations.defaults.row( location.name ), context.locations.transforms.row( location.name )


class Effects:

    def effect_022( context: Context ) -> None:
        """ Family Found Butchered! """

        # increase the terror track
        terrorFactory( context )

    def effect_023( context: Context ) -> None:
        """ Bizarre Dreams Plague Citizens! """

        # remove all gugs and nightgaunts
        for monster in { "GUG", "NIGHTGAUNT" }:
            monsters_cleared = clearMonstersOfType( context, monster=monster )
        
        for monster in range( monsters_cleared ):
            terrorFactory( context )

    def effect_024( context: Context ) -> None:
        """ Goat-like Creature Spotted in the Woods! """

        # remove all gugs and nightgaunts
        for monster in { "DARK YOUNG" }:
            monsters_cleared = clearMonstersOfType( context, monster=monster )
        
        for monster in range( monsters_cleared ):
            terrorFactory( context )

    def effect_025( context: Context ) -> None:
        """ Strange Tremors Cease! """

        # remove all gugs and nightgaunts
        for monster in { "CHTHONIAN", "DHOLE" }:
            monsters_cleared = clearMonstersOfType( context, monster=monster )
        
        for monster in range( monsters_cleared ):
            terrorFactory( context )

    def effect_026( context: Context ) -> None:
        """ Scientist Warns of Dimensional Rift! """

        # remove all gugs and nightgaunts
        for monster in { "DIMENSIONAL SHAMBLER", "HOUND OF TINDALOS" }:
            monstersCleared = clearMonstersOfType( context, monster=monster )
        
        for monster in range( monstersCleared ):
            terrorFactory( context )

    def effect_027( context: Context ) -> None:
        """ Strange Power Flux Plagues City! """
        
        for otherWorldID, invDefaults, invTransforms in investigatorsInOtherWorlds( context ):
            # get the first location that has a gate to that world on it
            try:
                locDefaults, locTransforms = next( gatesTo( context, context.locations.constants[ otherWorldID ].name ) )
                investigatorFuncs.relocateInvestigator( context, invDefaults, invTransforms, context.locations.constants.index( locDefaults.name ) )
                invTransforms.location += [ transformers.addInArkham ]
                print( f'{invDefaults.name} has suddenly reappeared at {locDefaults.name}! Perhaps now they can try to close the GATE TO {context.locations.constants[ otherWorldID ].name}')
            except StopIteration:
                # if there is no gate open, they return home instead...
                investigatorFuncs.relocateInvestigator( context, invDefaults, invTransforms, context.locations.constants.index( context.briefs.constants.row( invDefaults.name ).home ) )
                invTransforms.location += [ transformers.addInArkham ]
                print( f'{invDefaults.name} is amazingly back in Arkham at {context.briefs.constants.row( invDefaults.name ).home}!' )

    def effect_028( context: Context ) -> Callable:
        """ Blue Flu! """

        # rescue the investigators from jail
        for inv in context.locations.currents[ 9 ].investigators:
            investigatorFuncs.relocateInvestigator( context, context.briefs.defaults.row( inv ), context.briefs.transforms.row( inv ), 8 )
            print( f"{inv} has been let go from their jail cell! They are now left alone in the POLICE STATION" )

        # make everyone unnarrestable 
        for inv in context.briefs.transforms:
            inv.conditions += [ transformers.setUnarrestable ]

        return Resolutions.resolution_028 
    
    def effect_029( context: Context ) -> None:
        """ Missing People Return! """

        for inv_defaults, inv_transforms in zip( context.briefs.defaults, context.briefs.transforms ):
            investigatorFuncs.relocateInvestigator( context, inv_defaults, inv_transforms, context.locations.constants.index( context.briefs.constants.row( inv_defaults.name ).home ) )
            # the investigator might have been delayed...
            if constraints.investigatorDelay( inv_defaults.conditions, transformers.removeDelayed, inv_transforms.conditions ):
                inv_transforms.conditions += [ transformers.removeDelayed ]
            inv_transforms.conditions += [ transformers.removeLostInTimeAndSpace ]
            print( f'{inv_defaults.name} is amazingly back in Arkham at {context.briefs.constants.row( inv_defaults.name ).home}!' )
    
    def effect_030( context: Context ) -> None:
        """ Ill Wind Grips Arkham! """

        # get first player by name
        inv = currency.boardInvestigators( 
            context.board.defaults['investigators'], 
            context.board.transforms['investigators'] 
        )[ currency.boardCurrentPlayer( context.board.defaults['current_player'], context.board.transforms['current_player'] ) ]

        success, msg = investigatorFuncs.luckCheck( context, inv, -1, success_msg=f"{inv} feels a harsh breeze on their neck; they turn up their collar", failure_msg=f"{inv} feels the cold deep in their bones. If they were blessed, they are no longer. Otherwise they are cursed." )

        if not success:
            # add curse to investigator
            if constraints.investigatorBlessedCursed( context.briefs.defaults.row( inv ).conditions, transformers.add_curse, context.briefs.transforms.row( inv ).conditions ): 
                context.briefs.transforms.row( inv ).conditions += [ transformers.add_curse ]

        print( msg )

    def effect_031( context: Context ) -> Callable:
        """ Temperance Fever Sweeps City! """
        
        def has_whiskey( inv_defaults: Table.Row, inv_transforms: Table.Row ):
            # current possessions
            if "WHISKEY" in currency.investigatorPossessions( inv_defaults.possessions, inv_transforms.possessions )['consumables']:
                return True
            return False
    
        # check everyone in arkham for whiskey and chuck them in jail if they fail a sneak check

        for inv_default, inv_transform in zip( context.briefs.defaults, context.briefs.transforms ):
            if currency.investigatorLocation( inv_default.location, inv_transform.location ).in_arkham and has_whiskey( inv_default, inv_transform ):
                success, msg = investigatorFuncs.sneak_check( context, inv_default.name, -1, success_msg=f"{inv_default.name} got away this time! That was a close one", failure_msg=f"{inv_default.name} was caught! Their boozing has landed them in the slammer for the night" )
                print( msg )
                if not success:
                    investigatorFuncs.arrest_investigator( context, inv_default, inv_transform )

        # close down hibb's for the turn
                    
        if constraints.openCloseLocation( context.locations.defaults.row( "HIBB'S ROADHOUSE" ).status, transformers.addClosed, context.locations.transforms.row( "HIBB'S ROADHOUSE" ).status ):
            context.locations.transforms.row( "HIBB'S ROADHOUSE" ).status += [ transformers.addClosed ]

            print( "HIBB'S ROADHOUSE has been shut down by the cops. Who knows when it will open up again?\n")

        return Resolutions.resolution_031
    
    def effect_032( context: Context ) -> None:
        """ All Quiet in Arkham! """

        for invDefault, invTransforms in zip( context.briefs.defaults, context.briefs.transforms ):
            # only luck check if the investigator isn't already blessed
            if currency.investigatorConditions( invDefault.conditions, invTransforms.conditions ).blessed_cursed <= 0:
                success, msg = investigatorFuncs.luckCheck( 
                    context, 
                    invDefault.name, 
                    -1,
                    success_msg=f"{invDefault.name} has become blessed!",
                    failure_msg=None )
                
                if success:
                    invTransforms.conditions += [ transformers.addBlessing ]
                    print( msg )
                    
    def effect_033( context: Context ) -> Callable:
        """ City Gripped by Blackouts! """

        for location in context.locations.currents.filter( "name", { "YE OLDE MAGICK SHOPPE", "CURIOSITIE SHOPPE", "GENERAL SHOPPE" }, cond="in" ):
            if constraints.openCloseLocation( context.locations.defaults.row( location.name ).status, transformers.addClosed, context.locations.transforms.row( location.name ).status ):
                context.locations.transforms.row( location.name ).status += [ transformers.addClosed ]
                print( f"{location.name} is closed for business due to the blackouts" )

        return Resolutions.resolution_033
    
    def effect_034( context: Context ) -> Callable:
        """ Strange Lights on Campus! """

        for location in context.locations.currents.filter( "name", { "LIBRARY", "ADMINISTRATION", "SCIENCE BUILDING" }, "in" ):
            if constraints.openCloseLocation( context.locations.defaults.row( location.name ).status, transformers.addClosed, context.locations.transforms.row( location.name ).status ):
                context.locations.transforms.row( location.name ).status += [ transformers.addClosed ]
                print( f"{location.name} is shut down because of the lights" )

        return Resolutions.resolution_033
    
    def effect_035( context: Context ) -> Callable:
        """ Fourth of July Parade! """

        context.locations.transforms.row( "MERCHANT DISTRICT STREETS" ).status += [ transformers.removePassable ]

        return Resolutions.resolution_035
            
    def effect_036( context: Context ) -> None:
        """ Miskatonic Arctic Expedition Returns! """

        for inv_defaults, inv_transforms in zip( context.briefs.defaults, context.briefs.transforms ):
            # if investigator has 2 monster trophy points to spare, deduct them and try spawning an elder thing
            if constraints.investigatorMonsterTrophies( inv_defaults.possessions, transformers.decMonsterTrophies, inv_transforms.possessions + [ transformers.decMonsterTrophies ]):
                inv_transforms.possessions += [ transformers.decMonsterTrophies ] * 2
                monsterFactory( context, 1, ["RIVER DOCKS"], monster_type="ELDER THING" )

class Resolutions:

    def resolution_028( context: Context ) -> None:
        """ Blue Flu! """

         # make everyone arrestable 
        for inv in context.briefs.transforms:
            inv.conditions += [ transformers.setArrestable ]

    def resolution_031( context: Context ) -> None:
        """ Temperance Fever Sweeps City! """

        # open up hibb's roadhouse 

        if constraints.openCloseLocation( context.locations.defaults.row( "HIBB'S ROADHOUSE" ).status, transformers.removeClosed, context.locations.transforms.row( "HIBB'S ROADHOUSE" ).status ):
            context.locations.transforms.row( "HIBB'S ROADHOUSE" ).status += [ transformers.removeClosed ]

            print( "HIBB'S ROADHOUSE is back open for business! Tell them Joe sent ya\n")
        
    def resolution_033( context: Context ) -> None:

        for location in context.locations.currents.filter( "name", { "YE OLDE MAGICK SHOPPE", "CURIOSITIE SHOPPE", "GENERAL SHOPPE" }, "in" ):
            if constraints.openCloseLocation( context.locations.defaults.row( location.name ).status, transformers.removeClosed, context.locations.transforms.row( location.name ).status ):
                context.locations.transforms.row( location.name ).status += [ transformers.removeClosed ]

        print( "Businesses affected by the recent blackouts are opening back up.")

    def resolution_034( context: Context ) -> None:

        for location in context.locations.currents.filter( "name", { "LIBRARY", "ADMINISTRATION", "SCIENCE BUILDING" }, "in" ):
            if constraints.openCloseLocation( context.locations.defaults.row( location.name ).status, transformers.removeClosed, context.locations.transforms.row( location.name ).status ):
                context.locations.transforms.row( location.name ).status += [ transformers.removeClosed ]

        print( 'MISKATONIC UNIVERSITY claimes to have fixed the "strange light phenomenon" on campus. The buildings are once again open to the public.' )

    def resolution_035( context: Context ) -> None:

        context.locations.transforms.row( "MERCHANT DISTRICT STREETS" ).status += [ transformers.addPassable ]

                