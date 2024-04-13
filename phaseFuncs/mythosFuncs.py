import math, random
import currency, constraints, params, transformers
from classes.monsterRulesets import MovementRules
from classes.context import Context
from tools import debugger as db, currentLocationsDesc, randFromDistro, setLimit
from typing import Callable

from icecream import ic
# ic.disable()

def chooseRandomLocation( context, weight_formula: str, exclusion=None ):
    """ Returns a random location based on the weight formula provided, excluding any listed locations """

    return randFromDistro( { constants.name:eval( weight_formula ) for constants in context.locations.constants if constants.name != exclusion } )

def chooseGateLocation( context ):
    """ Randomly selects a location for a gate based on instability, current clues, and historical clues """

    return chooseRandomLocation( context, params.GATE_SPAWN )

def chooseGateTo( context: Context ):
    return randFromDistro( currency.gateFreqs( context.gates.deckDefaults, context.gates.deckTransforms) )

def chooseClueLocation( context, exclusion: str ):
    """ Randomly selects a location for a clue based on instability, current clues, and historical clues """

    return chooseRandomLocation( context, params.CLUE_SPAWN, exclusion )

def removeMonster( context: Context, monster: str, location: str ) -> None:
    """ Removes monster from location, puts it back in the cup, and decreases monster count """
    context.locations.transforms.row( location ).occupants += [ (transformers.removeOccupant, monster ) ]
    context.monsters.deckTransforms += [ (transformers.incFreq, monster ) ]
    context.board.transforms['monstersInArkham'] += [ transformers.decMonsterCount ]
    
def clearMonstersFromLoc( context: Context, location: str ) -> None:
    """ Removes monsters from provided location, increases the monster freq in cup, and decreases monster count in Arkham """
    for monster in context.locations.currents.row( location ).occupants:
        removeMonster( context, monster, location )

#################################

def spawnGate( gate_limit: int ):

    def spawnGateProtocol( context: Context, location, gate: str ) -> Callable:
        db( 2 )
        # inc gates in arkham
        context.board.transforms['gatesInArkham'] += [ transformers.incGatesInArkham ]
        # add gate to location and inc historical gate count
        context.locations.transforms.row( location ).status += [ transformers.addGate, transformers.incHistoricalGates ]
        context.locations.transforms.row( location ).gateTo += [ (transformers.addGateTo, gate) ]
        # add new adjacencies and remove old adjacencies
        # OLD e.g. : street <-> location
        # NEW e.g. : street --> location --> other world 1 --> other world 2 --> location
        for index, adj in enumerate( currency.graph( context.graph.graphDefaults, context.graph.graphTransforms).row( location ) ):
            if adj == 1:
                ic( gate, context.locations.constants.index( gate ) )
                context.graph.graphTransforms += [ 
                    # other world 2 --> location
                    (transformers.addAdjacency, context.locations.constants.index( location ), context.locations.constants.index( gate ) + 1 ),
                    # street -X-> location
                    (transformers.removeAdjacency, index, context.locations.constants.index( location ) ) 
                    ]
        context.graph.graphTransforms += [ 
            # location --> other world 1
            (transformers.addAdjacency, context.locations.constants.index( gate ),  context.locations.constants.index( location ) ) ]

        print( f'Something strange suddenly appeared at {location}! Better get there quickly! \n' )

        return True
    
    if gate_limit == 1:
        return spawnGateProtocol
    
    return None

def spawnClue( clue_limit ):
    
    def spawnClueProtocol( context, location ):
        db( 2 )
        # add clue to location and inc historical clue count
        context.locations.transforms.row( location ).status += [ transformers.incLocClues, transformers.incHistoricalClues ]
        
        msgs = [
            f'A stranger mentions there might be something of interest to you at {location} \n',
            f'You\'ve been given a lead! Head to {location}, and perhaps there will be something interesting... \n',
            f'Rumors circulate. You might want to check out {location} for a CLUE... \n'
        ]

        print( random.choice( msgs ) )

    if not clue_limit:
        return spawnClueProtocol
    return None

def spawnDoom( doom_limit ):
    
    def spawnDoomProtocol( context: Context ):
        db( 2 )
        context.board.transforms['doomTrack'] += [ transformers.incDoomTrack ]

        print( f'...a sense of doom grows ever more in the town of Arkham... \n' )

    if not doom_limit: 
        return spawnDoomProtocol
    
    return None

def spawnTerror( terror_limit ):

    def spawnTerrorProtocol( context ):
        db( 2 )
        # randomly select ally
        ally = randFromDistro( 
            currency.deckFrequency(
                context.allies.deckDefaults,
                context.allies.deckTransforms
            )
        )
        # remove that ally from the deck
        if ally:
            context.allies.deckTransforms += [ (transformers.decFreq, ally) ]
        # increase doom track
        context.board.transforms['terror_track'] += [ transformers.incTerrorTrack ]
        # close businesses
        def close_business( business ):
            if constraints.boardTerrorTrack( context.locations.defaults.row( business ).status, transformers.addClosed, context.locations.transforms.row( business ).status ):
                context.locations.transforms.row( business ).status += [ transformers.addClosed ]
                print( f'{business} has closed up shop! The terror in Arkham is too much for some \n' )
        
        if terror_limit == 5:
            # remove monster limit
            context.board.transforms['monstersInArkham'] += [ transformers.removeMonsterLimit ]
        if terror_limit == 4:
            # close magick shoppe
            close_business( 'YE OLDE MAGICK SHOPPE' )
        if terror_limit == 3:
            # close curio
            close_business( 'CURIOSITIE SHOPPE' )
        if terror_limit == 2:
            # close general store
            close_business( 'GENERAL STORE' )

    if terror_limit:
        return spawnTerrorProtocol
    
    return None

def spawnMonsterInArkham( monsterLimit: int ):

    def spawnMonsterInArkhamProtocol( context: Context, location, monsterType=None ):
        db( 2 )
        
        monster = None

        # there might not be monsters of specified type to draw
        if monsterType and currency.deckFrequency( context.monsters.deckDefaults, context.monsters.deckTransforms )[ monsterType ]:
            monster = monsterType
        elif not monsterType:
            # randomly select monster only if monster_type not specified, excluding any banned monster in the process
            monster = randFromDistro( {  mon: 0 if mon == currency.mythosBannedMonster( 
                context.mythos.defaults['bannedMonster'], 
                context.mythos.transforms['bannedMonster'] ) else freq for mon,freq in                                        
                currency.deckFrequency( 
                    context.monsters.deckDefaults,
                    context.monsters.deckTransforms
                ).items() }
            )
        db( 2, monster )
        # only spawn if a monster was selected
        if monster:
            ic( location )
            # place monster in location
            context.locations.transforms.row( location ).occupants += [ (transformers.addOccupant, monster) ]
            # reduce freq of monster
            context.monsters.deckTransforms += [ ( transformers.decFreq, monster ) ]
            # increase monsters in arkham count
            context.board.transforms['monstersInArkham'] += [ transformers.incMonsterCount ]
            # update current frame context 
            context.locations.currents = currentLocationsDesc( context.locations.defaults, context.locations.transforms )
            return None
    
    if monsterLimit == 1:
        return spawnMonsterInArkhamProtocol
    
    return None

def spawnMonsterInOutskirts( outskirts_limit: int ):

    def spawnMonsterInOutskirtsProtocol( context ):
        db( 2 )
        # increase monsters in outskirts count
        context.board.transforms['monsters_in_outskirts'] += [ transformers.incMonsterCount ]
        return None
    
    if outskirts_limit == 1:
        return spawnMonsterInOutskirtsProtocol
    
    return None

def clueFactory( context, new_clue ):
    # check clue constrains
    clue = spawnClue(
        context.locations.currents.row( new_clue ).status.gate
    )
    if clue:
        # add clue to that location
        clue( context, new_clue )
    else:
        # there is a gate there, increase historical clues
        context.locations.transforms.row( new_clue ).status += [ transformers.incHistoricalClues ] 

def doomFactory( context, callback=None, *args ):
    # check for doom constraints
    doom = spawnDoom(
        constraints.boardDoomTrack(
            context.board.defaults['doomTrack'],
            transformers.incDoomTrack,
            context.board.transforms['doomTrack']
        )
    )
    if doom:
        # doom limit not reached
        doom( context )
        # do spawn monster things
        if callback:
            callback( context, *args )
    else:
        # doom limit reached
        awakenTheAncientOne( context )

def monsterFactory( context: Context, num_monsters, locations, monster_type=None ):
        """ Spawns monsters and calls for checks along the way """
        db( 2 )
        if num_monsters:
            # check monsters in arkham contraints
            spawnInArkham = spawnMonsterInArkham(
                constraints.boardMonstersInArkhamLimit( 
                    context.board.defaults['monstersInArkham'], 
                    transformers.incMonsterCount, 
                    context.board.transforms['monstersInArkham']
                )
            )
            if spawnInArkham:
                # monster limit not reached
                spawnInArkham( context, locations[-num_monsters], monster_type )
            else:
                # monster limit reached
                # check outskirts contraints
                spawnInOutskirts = spawnMonsterInOutskirts(
                    constraints.boardMonstersInOutskirtsLimit( 
                        context.board.defaults['monstersInOutskirts'], 
                        transformers.incOutskirtsCount, 
                        context.board.transforms['monstersInOutskirts']
                    )
                )
                if spawnInOutskirts:
                    # outskirts limit not reached
                    spawnInOutskirts( context )
                else:
                    # outskirts limit reached
                    outskirtsFull( context )
                    
            return monsterFactory( context, num_monsters - 1, locations )

def terrorFactory( context ):
    db( 2 )
    terrorInArkham = spawnTerror(
        constraints.boardTerrorTrack(
            context.board.defaults['terrorTrack'],
            transformers.incTerrorTrack,
            context.board.transforms['terrorTrack']
        )
    )

    ic( terrorInArkham )

    if terrorInArkham:
        # terror limit not reached
        terrorInArkham( context )
    else:
        # terror track is full, spawn doom
        doomFactory( context )

    return None

def outskirtsFull( context ):
    db( 2 )
    # empty the outskirts
    setLimit( 
        context.board.transforms['monsters_in_outskirts'], 
        transformers.decMonsterCount, 
        params.OUTSKIRTS_LIMIT, 
        x=len( currency.boardInvestigators( 
            context.board.defaults['investigators'], 
            context.board.transforms['investigators'] 
        ) )
    )
    # do terror track things
    terrorFactory( context )

    return None

def monsterSurge( context, factory ):

    # get list of all the gate locations in arkham
    gates = []
    for location in context.locations.currents:
        if location.status.gate:
            gates += [location.name]
    # send those to the monster factory
    
    factory( context, len(gates), gates )

    return None
   
def moveMonsters( context ):
    db( 2 )
    # monsters move in groups
    leftGroup = randFromDistro( { group:1 for group in params.MVMT_GROUPS } )
    rightGroup = randFromDistro( { group:1 for group in params.MVMT_GROUPS if group != leftGroup } )

    ic( leftGroup, rightGroup )

    def find_monsters( group ):
        db( 2 )
        # filter for occupied locations
        for location in context.locations.currents.filter( 'occupants', [], "!="):
            for monster in location.occupants:
                if context.monsters.constants.row( monster ).dimension in group:
                    yield monster, location

    def move_protocols( group ):
        db( 2 )
        for monster, location in find_monsters( group ):
            # find movement ruleset
            yield monster, location, MovementRules()[ currency.monster_rulesets( 
                context.monsters.defaults.row( monster ).rulesets,
                context.monsters.transforms.row( monster ).rulesets,
            ).movement ]

    leftMoves = [ ruleset for ruleset in move_protocols( leftGroup ) ]
    rightMoves = [ ruleset for ruleset in move_protocols( rightGroup ) ]        

    ic( leftMoves, rightMoves )

    # move left monsters left
    for monster, location, ruleset in leftMoves:
        ruleset( context, monster, location, context.locations.leftGraph )
    # move right monsters right
    for monster, location, ruleset in rightMoves:
        ruleset( context, monster, location, context.locations.rightGraph )

def awakenTheAncientOne( context ):
    db( 2 )
    context.board.transforms['awakened'] += [ transformers.setAwakened ]

def activateEffect( context: Context ):
    
    # randomly select the mythos card
    index = randFromDistro( currency.deckFrequency( context.mythos.deckDefaults, context.mythos.deckTransforms ) ) 
    effect = context.mythos.constants[ index ]
    context.mythos.deckTransforms += [ (transformers.decFreq, index ) ]
    
    # slap in the title
    context.mythos.transforms[ effect.variety ] += [ ( transformers.setTitle, effect.banner.title ) ]
    context.mythos.transforms[ effect.variety ] += [ ( transformers.setDescription, effect.banner.description ) ]

    if effect.variety == 'headline':
        announce = f"{'-'*37}  EXTRA! EXTRA! READ ALL ABOUT IT!  {'-'*37}\n\n"
    elif effect.variety == 'weather':
        announce = f"{'-'*33}  WEATHER REPORT FOR ARKHAM, MASSACHUSETTS  {'-'*33}\n\n"
    elif effect.variety in { 'urban', 'mystic', 'rumor' } :
        announce = ""

    headline = f"{' '*int( (len( announce ) - 6 - len( effect.banner.title )) / 2 )}...\x1b[1;4m" + effect.banner.title + f"\x1b[22;24m...{' '*int( (len( announce ) - 6 - len( effect.banner.title )) / 2 )}\n"
    msg = announce + headline
    msg += f"{' '*int( (len( announce ) - 6 - len( effect.banner.description )) / 2 )}" + effect.banner.description + f"{' '*int( (len( announce ) - 6 - len( effect.banner.description )) / 2 )}\n\n"
        

    print( msg )
            
    # apply mods
    context.mythos.transforms['modifiers'] += [
        ( transformers.setMythosMvmtPoints, effect.modifiers.mvmtPoints ),
        ( transformers.setMythosSpeed,  effect.modifiers.speed ),
        ( transformers.setMythosSneak, effect.modifiers.sneak ),
        ( transformers.setMythosFight, effect.modifiers.fight ),
        ( transformers.setMythosWill, effect.modifiers.will ),
        ( transformers.setMythosLore, effect.modifiers.lore ),
        ( transformers.setMythosLuck, effect.modifiers.luck )
    ]

    # spawn monsters
    if effect.monsterSpawnCount:
        monsterFactory( context, effect.monsterSpawnCount, [ effect.monsterSpawnLocation ] * effect.monsterSpawnCount )

    # despawn monsters
    if effect.monsterDespawnLocation:
        if effect.monsterDespawnLocation in { "LOCATION", "STREETS", "SPECIAL" } :
            for location in context.locations.constants.filter( 'variety', effect.monsterSpawnLocation ):
                clearMonstersFromLoc( context, location )
        else:
            for location in context.locations.constants.filter( 'neighborhood', effect.monsterSpawnLocation ):
                clearMonstersFromLoc( context, location )
    
    
    # any other function
    if effect.effect: 
        # returns a resolution function
        return effect.effect( context )
    
