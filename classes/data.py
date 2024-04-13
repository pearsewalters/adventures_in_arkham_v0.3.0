from collections import namedtuple

class Ability:

    abilityDetails = namedtuple( "abilityDetails", ["variety", "func", "phase", "resource", "deck", "amt"] )

class Location:
    # default value 1 for "passable" 
    status = namedtuple( "locationStatus", ["clues", "historicalClues", "sealed", "gate", "historicalGates", "explored", "closed", "passable"], defaults=[1] )

class Monster:

    rulesets = namedtuple( "rulesets", ["movement", "combat", "evade"] )
    abilities = namedtuple( "abilities", ["ambush","endless","undead","physical","magical","nightmarish","overwhelming"] )
    stats = namedtuple( "stats", ["awareness","toughness","horrorMod","horror","combatMod","damage"] )


class Investigator:

    damage = namedtuple( "damageStats", ["maxDamage", "currentDamage", "unconscious" ] )
    horror = namedtuple( "horrorStats", ["maxHorror", "currentHorror", "insane" ] )
    conditions = namedtuple( "conditions", [
        "lostInTimeAndSpace",
        "delayed",
        "arrested",
        "retainer",
        "bankLoan",
        "stlMembership",
        "deputized",
        "blessedCursed"
    ])
    focus = namedtuple( "focusStats", ["maxFocus", "currentFocus" ] )
    speed = namedtuple( "speedStats", ["maxSpeed", "currentSpeed", "speedSneakSum" ] )
    fight = namedtuple( "fightStats", ["maxFight", "currentFight", "fightWillSum" ] )
    lore = namedtuple( "loreStats", ["maxLore", "currentLore", "loreLuckSum" ] )
    location = namedtuple( "locationStats", ["currentLocation", "mvmtPoints", "inArkham"] )
    randomPossessions = namedtuple( "randomPossessions", ["commonItems", "uniqueItems", "spells", "skills"] )
    equippedItems = namedtuple( "equippedItems", [ "hands", "equipment"] )


class Items:
    weapon = namedtuple( "weaponStats", ["modality", "bonus", "sanityCost", "exhaustable", "losable", "price"] )
    consumable = namedtuple( "consumableStats", ["bonus", "price"] )
    tome = namedtuple( "tomeStats", ["mvmtCost", "sanityCost", "modifier", "price"] )
    passiveBuff = namedtuple( "passiveBuffStats", ["bonus", "price"] )
    activeBuff = namedtuple( "activeBuffStats", ["bonus","price"] )
    oddity = namedtuple( "oddityStats", "price" )

class Mythos:
    banner = namedtuple( "mythosBanner", [ "title", "description" ] )
    modifiers = namedtuple( "mythosModifier", [ "mvmtPoints", "speed", "sneak", "fight", "will", "lore", "luck" ] )