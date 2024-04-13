from icecream import ic
from params import DEBUG_LVL
from tools import debugger as db
from classes.table import Table


# generalizable functions
def increase( vector, dimension ):
    """ Increases a dimension in a vector by 1 """
    return vector._replace(**{ dimension: getattr(vector,dimension) + 1} )

def decrease( vector, dimension ):
    """ Decreases a dimension in a vector by 1 """
    return vector._replace(**{ dimension: getattr(vector,dimension) - 1} )

def cycleInt( integer, mod ):
    """ Cycles an integer up, 0 thru mod-1 """
    return (integer + 1) % mod

def cycle( vector, dimension, mod ):
    """ Cycles a dimension in a vector from 0 through mod-1 """
    return vector._replace( **{ dimension : (getattr( vector, dimension) + 1) % mod } )

def addToList( l, element ):
    return l + [ element ]

def removeFromList( l, element ):
    return l[ :l.index(element) ] + l[ l.index(element)+1: ]

def incFreq( dictionary, key ):
    return { m:f+1 if m == key else f for m,f in dictionary.items() }

def decFreq( dictionary, key ):
    return { m:f-1 if m == key else f for m,f in dictionary.items() }

def incMaxSkill( skill ):
    db( 3 )
    return increase( skill, 'max'+skill.capitalize() )

def decMaxSkill( skill ):
    db( 3 )
    return decrease( skill, 'max'+skill.capitalize() )

def incCurrentSkill( skill ):
    db( 3 )
    return increase( skill, 'current'+skill.capitalize() )

def decCurrentSkill( skill ):
    db( 3 )
    return decrease( skill, 'current'+skill.capitalize() )

# board

def addInvestigator( vector, investigator ):
    return addToList( vector, investigator )

def removeInvestigator( vector, investigator ):
    return removeFromList( vector, investigator )

def advanceCurrentPhase( integer ):
    return cycleInt( integer, 4 )

def toggleBookkeeping( integer ):
    return cycleInt( integer, 2 )

def setAncientOne( vector, ancientOne ):
    return addToList( vector, ancientOne )

def setAwakened( awakened ):
    return awakened + 1

def incDoomTrack( integer ):
    return integer + 1

def decDoomTrack( integer ):
    return integer - 1

def incTerrorTrack( integer ):
    return integer + 1

def decTerrorTrack( integer ):
    return integer - 1

def incGatesInArkham( integer ):
    return integer + 1

def decGatesInArkham( integer ):
    return integer - 1

def incGatesSealed( integer ):
    return integer + 1

def decGatesSealed( integer ):
    return integer - 1

def incCluesToSeal( integer ):
    return integer + 1

def decCluesToSeal( integer ):
    return integer - 1

def incGatesClosedToWin( vector ):
    return [ vector[0] + 1, vector[1] ]

def decGatesClosedToWin( vector ):
    return [ vector[0] - 1, vector[1] ]

def incSealsToWin( vector ):
    return [ vector[0], vector[1] + 1 ]

def decSealsToWin( vector ):
    return [ vector[0], vector[1] -1 ]

def incMonsterCount( integer ):
    return integer + 1

def decMonsterCount( integer ):
    return integer - 1

def removeMonsterLimit( integer ):
    """Intended for removing the monster limit"""
    return float('-inf')

def incOutskirtsCount( integer ):
    return integer + 1

def decOutskirtsCount( integer ):
    return integer - 1

def addMonsterLocation( vector, dimension, location ):
    return [ locs + [location] if dim == dimension else locs for dim, locs in enumerate( vector ) ]

def removeMonsterLocation( vector, dimension, location ):
    return [ locs[:locs.index(location)] + locs[locs.index(location)+1:] if dim == dimension else locs for dim, locs in enumerate( vector ) ] 

# mythos

def setTitle( banner, title ):
    ic( banner, title )
    return banner._replace( title=title )

def setDescription( banner, description ):
    return banner._replace( description=description )

def setMythosMvmtPoints( modifiers, mvmtPoints ):
    return modifiers._replace( mvmtPoints=mvmtPoints )

def setMythosSpeed( modifiers, speed ):
    return modifiers._replace( speed=speed )

def setMythosSneak( modifiers, sneak ):
    return modifiers._replace( sneak=sneak )

def setMythosFight( modifiers, fight ):
    return modifiers._replace( fight=fight )

def setMythosWill( modifiers, will ):
    return modifiers._replace( will=will )

def setMythosLore( modifiers, lore ):
    return modifiers._replace( lore=lore )

def setMythosLuck( modifiers, luck ):
    return modifiers._replace( luck=luck )

def setBannedMonster( mythos, bannedMonster ):
    return bannedMonster

def setResolution( mythos, resolution ):
    return resolution

# locations

def addOccupant( locationOccupants, newOccupant ):
    db( 3 )
    return addToList( locationOccupants, newOccupant )

def removeOccupant( locationOccupants, oldOccupant ):
    db( 3 )
    return removeFromList( locationOccupants, oldOccupant )

def addGateTo( locationGateTo, newGate ):
    db( 3 )
    return addToList( locationGateTo, newGate )

def removeGateTo( locationGateTo, oldGate ):
    db( 3 )
    return removeFromList( locationGateTo, oldGate )
    
def incLocClues( location ):
    db( 3 )
    return increase( location, 'clues' )

def decLocClues( location ):
    db( 3 )
    return decrease( location, 'clues' )

def incHistoricalClues( location ):
    db( 3 )
    return increase( location, 'historicalClues' )

def decHistoricalClues( location ):
    db( 3 )
    return decrease( location, 'historicalClues' )

def addSeal( location ):
    db( 3 )
    return increase( location, 'sealed' )

def removeSeal( location ):
    db( 3 )
    return decrease( location, 'sealed' )

def addGate( location ):
    db( 3 )
    return increase( location, 'gate' )

def removeGate( location ):
    db( 3 )
    return decrease( location, 'gate' )

def incHistoricalGates( location ):
    db( 3 )
    return increase( location, 'historicalGates' )

def decHistoricalGates( location ):
    db( 3 )
    return decrease( location, 'historicalGates' )

def addExplored( location ):
    db( 3 )
    return increase( location, 'explored' )

def removeExplored( location ):
    db( 3 )
    return decrease( location, 'explored' )

def addClosed( location ):
    db( 3 )
    return increase( location, 'closed' ) 

def removeClosed( location ):
    db( 3 )
    return decrease( location, 'closed' )

def permanentlyClose( location ):
    db( 3 )
    return location._replace( closed=float('inf') )

def addPassable( location ):
    db( 3 )
    return increase( location, 'passable' ) 

def removePassable( location ):
    db( 3 )
    return decrease( location, 'passable' )

# graph

def addAdjacency( table: Table, x: int, y: int ):
    """ Add a 1 to an adj table, signifying that y joins x """
    return Table([ [ 1 if m == x and n == y else u for m,u in enumerate( table.table[n] ) ] for n,v in enumerate( table.table ) ])

def removeAdjacency( table: Table, x: int, y: int ):
    """ Add a 0 to an adj table, signifying that y disjoins x """
    return Table([ [ 0 if m == x and n == y else u for m,u in enumerate( table.table[n] ) ] for n,v in enumerate( table.table ) ])

# monsters

def setMovement( rulesets, moveRules ):
    db( 3 )
    return rulesets._replace( movement=moveRules )

def setCombat( rulesets, combatRules ):
    db( 3 )
    return rulesets._replace( combat=combatRules )

def setEvade( rulesets, evadeRules ):
    db( 3 )
    return rulesets._replace( evade=evadeRules )

def addAmbush( abilities ):
    db( 3 )
    return increase( abilities, 'ambush' )

def removeAmbush( abilities ):
    db( 3 )
    return decrease( abilities, 'ambush' )

def addEndless( abilities ):
    db( 3 )
    return increase( abilities, 'endless' )

def removeEndless( abilities ):
    db( 3 )
    return decrease( abilities, 'endless' )

def addUndead( abilities ):
    db( 3 )
    return increase( abilities, 'undead' )

def removeUndead( abilities ):
    db( 3 )
    return decrease( abilities, 'undead' )

def setPhysicalImmunity( abilities ):
    db( 3 )
    return abilities._replace( physical=0 )

def setPhysicalResistance( abilities ):
    db( 3 )
    return abilities._replace( physical=0.5 )

def removePhysical( abilities ):
    db( 3 )
    return abilities._replace( physical=1 )

def setMagicalImmunity( abilities ):
    db( 3 )
    return abilities._replace( magical=0 )

def setMagicalResistance( abilities ):
    db( 3 )
    return abilities._replace( magical=0.5 )

def removeMagical( abilities ):
    db( 3 )
    return abilities._replace( magical=1 )

def incNightmarish( abilities ):
    db( 3 )
    return increase( abilities, 'nightmarish' )

def decNightmarish( abilities ):
    db( 3 )
    return decrease( abilities, 'nightmarish' )

def incOverwhelming( abilities ):
    db( 3 )
    return increase( abilities, 'overwhelming' )

def decOverwhelming( abilities ):
    db( 3 )
    return decrease( abilities, 'overwhelming' )

def incAwareness( stats ):
    db( 3 )
    return increase( stats, 'awareness' )

def decAwareness( stats ):
    db( 3 )
    return decrease( stats, 'awareness' )

def incToughness( stats ):
    db( 3 )
    return increase( stats, 'toughness' )

def decToughness( stats ):
    db( 3 )
    return decrease( stats, 'toughness' )

def incHorrorMod( stats ):
    db( 3 )
    return increase( stats, 'horrorMod' )

def decHorrorMod( stats ):
    db( 3 )
    return decrease( stats, 'horrorMod' )

def incHorrorReceived( stats ):
    db( 3 )
    return increase( stats, 'horror' )

def decHorrorReceived( stats ):
    db( 3 )
    return decrease( stats, 'horror' )

def incCombatMod( stats ):
    db( 3 )
    return increase( stats, 'combatMod' )

def decCombatMod( stats ):
    db( 3 )
    return decrease( stats, 'combatMod' )

def incDamageReceived( stats ):
    db( 3 )
    return increase( stats, 'damage' )

def decDamageReceived( stats ):
    db( 3 )
    return decrease( stats, 'damage' )

# investigators

def incMaxDamage( damage ):
    db( 3 )
    return increase( damage, 'maxDamage' )

def decMaxDamage( damage ):
    db( 3 )
    return decrease( damage, 'maxDamage' )

def incCurrentDamage( damage ):
    db( 3 )
    return increase( damage, 'currentDamage' )

def decCurrentDamage( damage ):
    db( 3 )
    return decrease( damage, 'currentDamage' )

def setUnconscious( damage ):
    db( 3 )
    return increase( damage, 'unconscious' )

def setConscious( damage ):
    db( 3 )
    return decrease( damage, 'unconscious' )

def incMaxHorror( horror ):
    db( 3 )
    return increase( horror, 'maxHorror' )

def decMaxHorror( horror ):
    db( 3 )
    return decrease( horror, 'maxHorror' )

def incCurrentHorror( horror ):
    db( 3 )
    return increase( horror, 'currentHorror' )

def decCurrentHorror( horror ):
    db( 3 )
    return decrease( horror, 'currentHorror' )

def setInsane( horror ):
    db( 3 )
    return increase( horror, 'insane' )

def setSane( horror ):
    db( 3 )
    return decrease( horror, 'insane' )

def addLostInTimeAndSpace( conditions ):
    db( 3 )
    return increase( conditions, 'lostInTimeAndSpace' )

def removeLostInTimeAndSpace( conditions ):
    db( 3 )
    return decrease( conditions, 'lostInTimeAndSpace' )

def addDelayed( conditions ):
    db( 3 )
    return increase( conditions, 'delayed' )

def removeDelayed( conditions ):
    db( 3 )
    return decrease( conditions, 'delayed' )

def addArrested( conditions ):
    db( 3 )
    return increase( conditions, 'arrested' )

def removeArrested( conditions ):
    db( 3 )
    return decrease( conditions, 'arrested' )

def setUnarrestable( conditions ):
    db( 3 )
    return conditions._replace( arrested=float('inf') )

def setArrestable( conditions ):
    db( 3 )
    return conditions._replace( arrested=0 )

def addRetainer( conditions ):
    db( 3 )
    return increase( conditions, 'retainer' )

def removeRetainer( conditions ):
    db( 3 )
    return decrease( conditions, 'retainer' )

def addBankLoan( conditions ):
    db( 3 )
    return increase( conditions, 'bankLoan' )

def removeBankLoan( conditions ):
    db( 3 )
    return decrease( conditions, 'bankLoan' )

def setBankrupt( conditions ):
    db( 3 )
    return conditions._replace( bankLoan=float('inf') )

def addStlMembership( conditions ):
    db( 3 )
    return increase( conditions, 'stlMembership' )

def removeStlMembership( conditions ):
    db( 3 )
    return decrease( conditions, 'stlMembership' )

def addDeputized( conditions ):
    db( 3 )
    return increase( conditions, 'deputized' )

def removeDeputized( conditions ):
    db( 3 )
    return decrease( conditions, 'deputized' )

def addBlessing( conditions ):
    db( 3 )
    return increase( conditions, 'blessedCursed' )

def removeBlessing( conditions ):
    db( 3 )
    return decrease( conditions, 'blessedCursed' )

def addCurse( conditions ):
    db( 3 )
    return addBlessing( conditions )

def removeCurse( conditions ):
    db( 3 )
    return removeBlessing( conditions )

# skills

def incMaxFocus( focus ):
    db( 3 )
    return increase( focus, 'maxFocus' )

def decMaxFocus( focus ):
    db( 3 )
    return decrease( focus, 'maxFocus' )

def incCurrentFocus( focus ):
    db( 3 )
    return increase( focus, 'currentFocus' )

def decCurrentFocus( focus ):
    db( 3 )
    return decrease( focus, 'currentFocus' )

def incMaxSpeed( speed ):
    db( 3 )
    return increase( speed, 'maxSpeed' )

def decMaxSpeed( speed ):
    db( 3 )
    return decrease( speed, 'maxSpeed' )

def incCurrentSpeed( speed ):
    db( 3 )
    return increase( speed, 'currentSpeed' )

def decCurrentSpeed( speed ):
    db( 3 )
    return decrease( speed, 'currentSpeed' )

def incCurrentSneak( speed ):
    db( 3 )
    return decrease( speed, 'currentSpeed' )

def decCurrentSneak( speed ):
    db( 3 )
    return increase( speed, 'currentSpeed' )

def incSumSpeedSneak( speed ):
    db( 3 )
    return increase( speed, 'speedSneakSum' )

def decSumSpeedSneak( speed ):
    db( 3 )
    return decrease( speed, 'speedSneakSum' )

def incMaxFight( fight ):
    db( 3 )
    return increase( fight, 'maxFight' )

def decMaxFight( fight ):
    db( 3 )
    return decrease( fight, 'maxFight' )

def incCurrentFight( fight ):
    db( 3 )
    return increase( fight, 'currentFight' )

def decCurrentFight( fight ):
    db( 3 )
    return decrease( fight, 'currentFight' )

def incCurrentWill( fight ):
    db( 3 )
    return decrease( fight, 'currentFight' )

def decCurrentWill( fight ):
    db( 3 )
    return increase( fight, 'currentFight' )

def incSumFightWill( fight ):
    db( 3 )
    return increase( fight, 'fightWillSum' )

def decSumFightWill( fight ):
    db( 3 )
    return decrease( fight, 'fightWillSum' )

def incMaxLore( lore ):
    db( 3 )
    return increase( lore, 'maxLore' )

def decMaxLore( lore ):
    db( 3 )
    return decrease( lore, 'maxLore' )

def incCurrentLore( lore ):
    db( 3 )
    return increase( lore, 'currentLore' )

def decCurrentLore( lore ):
    db( 3 )
    return decrease( lore, 'currentLore' )

def incCurrentLuck( fight ):
    db( 3 )
    return decrease( fight, 'currentFight' )

def decCurrentLuck( fight ):
    db( 3 )
    return increase( fight, 'currentFight' )

def incSumLoreLuck( lore ):
    db( 3 )
    return increase( lore, 'loreLuckSum' )

def decSumLoreLuck( lore ):
    db( 3 )
    return decrease( lore, 'loreLuckSum' )

def changeLocation( location, newLocId ):
    db( 3 )
    return location._replace( currentLocation=newLocId )

def incMvmtPoints( location ):
    db( 3 )
    return increase( location, 'mvmtPoints' )

def decMvmtPoints( location ):
    db( 3 )
    return decrease( location, 'mvmtPoints' )

def addInArkham( location ):
    db( 3 )
    return increase( location, 'inArkham' )

def removeInArkham( location ):
    db( 3 )
    return decrease( location, 'inArkham' )

def incHands( equippedItems ):
    db( 3 )
    return increase( equippedItems, 'hands' )

def decHands( equippedItems ):
    db( 3 )
    return decrease( equippedItems, 'hands' )

def equipItem( equippedItems, item ):
    db( 3 )
    return equippedItems._replace( equipment = addToList( equippedItems, item ) )

def dequipItem( equippedItems, item ):
    db( 3 )
    return equippedItems._replace( equipment = removeFromList( equippedItems, item ) )

def exhaustItem( exhaustedItems, item ):
    db( 3 )
    return addToList( exhaustedItems, item )

def refreshExhausted( exhaustedItems ):
    db( 3 )
    return exhaustedItems[:0] 

# possessions

def incMoney( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'money' else v) for k,v in possessions.items() }

def decMoney( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'money' else v) for k,v in possessions.items() }

def incInvClues( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'clues' else v) for k,v in possessions.items() }

def decInvClues( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'clues' else v) for k,v in possessions.items() }

def incGateTrophies( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'gateTrophies' else v) for k,v in possessions.items() }

def decGateTrophies( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'gateTrophies' else v) for k,v in possessions.items() }

def incMonsterTrophies( possessions ):
    db( 3 )
    return { k:(v+1 if k == 'monsterTrophies' else v) for k,v in possessions.items() }

def decMonsterTrophies( possessions ):
    db( 3 )
    return { k:(v-1 if k == 'monsterTrophies' else v) for k,v in possessions.items() }

def addItem( possessions, variety, item ):
    db( 3 )
    return { k:(v+[item] if k == variety else v) for k,v in possessions.items() }

def removeItem( possessions, variety, item ):
    db( 3 )
    return { k:( v[:v.index(item)] + v[v.index(item)+1:] if k == variety else v) for k,v in possessions.items() }

def addWeapon( possessions, item ):
    db( 3 )
    return addItem( possessions, 'weapons', item )
    
def removeWeaponItem( possessions, item ):
    db( 3 )
    return removeItem( possessions, 'weapons', item )

def addConsumableItem( possessions, item ):
    db( 3 )
    return addItem( possessions, 'consumables', item )

def removeConsumableItem( possessions, item ):
    db( 3 )
    return removeItem( possessions, 'consumables', item )

def addTomeItem( possessions, item ):
    db( 3 )
    return addItem( possessions, 'tomes', item )

def removeTomeItem( possessions, item ):
    db( 3 )
    return removeItem( possessions, 'tomes', item )

def addPassiveBuff( possessions, item ):
    db( 3 )
    return addItem( possessions, 'passiveBuffs', item )

def removePassiveBuff( possessions, item ):
    db( 3 )
    return removeItem( possessions, 'passiveBuffs', item )

def addActiveBuff( possessions, item ):
    db( 3 )
    return addItem( possessions, 'activeBuffs', item )

def removeActiveBuff( possessions, item ):
    db( 3 )
    return removeItem( possessions, 'activeBuffs', item )

def addOddityItem( possessions, item ):
    db( 3 )
    return addItem( possessions, 'oddities', item )

def removeOddityItem( possessions, item ):
    db( 3 )
    return removeItem( possessions, 'oddities', item )

def addSpell( possessions, spell ):
    db( 3 )
    return addItem( possessions, 'spells', spell )

def removeSpell( possessions, spell ):
    db( 3 )
    return removeItem( possessions, 'spells', spell )

def addAlly( possessions, ally ):
    db( 3 )
    return addItem( possessions, 'allies', ally )

def removeAlly( possessions, ally ):
    db( 3 )
    return removeItem( possessions, 'allies', ally )

# non-specific item transforms

def incPrice( item ):
    """ Increases the item price """
    db( 3 )
    return increase( item, 'price' )

def decPrice( item ):
    """ Decreases the item price """
    db( 3 )
    return decrease( item, 'price' )

def incBonus( item ):
    """ Increases item bonus """
    db( 3 )
    return increase( item, 'bonus' )

def decBonus( item ):
    """ Decreases item bonus """
    db( 3 )
    return decrease( item, 'bonus' )

def incSanityCost( item ):
    """ Increases item sanity cost """
    db( 3 )
    return increase( item, 'sanityCost' )

def decSanityCost( item ):
    """ Decrease item sanity cost """
    db( 3 )
    return decrease( item, 'sanityCost' )

# weapons-specific transforms

def changeModality( weapon ):
    """ Changes a physical weapon in a magical one, a magical into physical """
    db( 3 )
    return cycle( weapon, 'modality', 2 )

def changeExhaustable( weapon ):
    """ Makes a non-exhaustible weapon exhaustable, exhaustible to non """
    db( 3 )
    return cycle( weapon, 'exhaustable', 2 )

def changeLosable( weapon ):
    """ Makes a non-losable weapon losable, losable to non """
    db( 3 )
    return cycle( weapon, 'losable', 2 )

# gates

def incGateModifier( gate ):
    db( 3 )
    return increase( gate, 'modifier' )

def decGateModifier( gate ):
    db( 3 )
    return decrease( gate, 'modifier' )
