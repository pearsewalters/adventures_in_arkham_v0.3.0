import currency

def cluesAtLocation( matrix, next_transform, prev_transforms ):
    """
        CLUES AT LOCATIONS
        There is no upper limit to the number of clues at a location, but it should 
            never be less than 0. That is unless, of course, some future release has 
            a feature wherein a location could make an Investigator forget what they've
            discovered...
        Additionally, clues cannot appear on locations that have a gate already or have
            already been sealed
        This stat exists in [0, inf), at least for now...
        This validator returns -2 if there is a gate on the location,
                               -1 if there is a seal on the location,
                               0 if passed a bad transform,
                               1 if passed a good transform.
    """
    transformed_matrix = next_transform( currency.locationStatus( matrix, prev_transforms) )
    # can't be less than 0 or on a location with a gate or a seal
    if transformed_matrix[0] >= 0 and transformed_matrix[2] != 1 and transformed_matrix[3] != 1:
        return 1
    elif transformed_matrix[1] == 1:
        return -1
    elif transformed_matrix[2] == 1:
        return -2
    else:
        return 0
    
def sealAtLocation( matrix, next_transform, prev_transforms ):
    """
        SEALS ON LOCATIONS
        A gate cannot open on a sealed location. Sealed locations may become unsealed by 
            way of various game effects.
        This stat exists in {0,1} where 0 is unsealed and 1 is sealed.
    """
    transformed_matrix = next_transform( currency.locationStatus( matrix, prev_transforms) )
    # has to be 0 or 1
    if 0 <= transformed_matrix[2] <= 1:
        return True
    else:
        return False
    
def gateAtLocation( matrix, next_transform, prev_transforms ):
    """
        GATES ON LOCATIONS
        A gate on a location is a portal to one of the Other Worlds. A location cannot have 
            more than 1 gate on it. If a gate attempts to open on a location with a gate 
            already, a monster surge ensues, wherein every a monster spills out of every open
            gate in Arkham.
        This stat exists in {0,1} where 0 is 'has no gate' and 1 is 'has gate.'
        This function returns from {0,1,2} where 0 is a bad transform,
                                                 1 is a good transform but no monster surge, and
                                                 2 is a good transform with a monster surge.
    """
    transformed_matrix = next_transform( currency.locationStatus( matrix, prev_transforms) )
    if transformed_matrix[3] < 0:
        return 0
    elif 0 <= transformed_matrix[3] <= 1:
        return 1
    elif 1 < transformed_matrix[3]:
        return 2

def exploredLocation( matrix, next_transform, prev_transforms ):
    """
        EXPLORED GATE AT LOCATION
        If a location is marked as having been explored, any investigator who is at that location
            may attempt to close or seal the gate that is at the location. Once an investigator 
            leaves that location, it is no longer considered 'explored.' 
        A location is said to have been explored if an Investigator arrives there from an Other 
            World. 
        This stat exists in {0,1} where 0 is not explored, and 1 is explored.
    """
    transformed_matrix = next_transform( currency.locationStatus( matrix, prev_transforms) )
    # has to be 0 or 1
    if 0 <= transformed_matrix[4] <= 1:
        return True
    else:
        return False
    
def openCloseLocation( matrix, next_transform, prev_transforms ):
    """
        CLOSED LOCATIONS
        Locations can close for a number of reasons, but commonly because of Terror Track effects.
            If an Investigator travels to a location that is closed, their encounter there will 
            be a Sneak[-1] check. With 1 success they will gain one of the two resources that 
            location has to offer. With 2 successes they will gain both resources the location offers.
            With 0 successes, a Luck[-1] check will occur; on a failure, the Investigator is ARRESTED.
        This stat exists in {0,1,∞} with 0 being open for business, 1 being closed, and ∞ being permanently
        closed.
    """
    condition = next_transform( currency.locationStatus( matrix, prev_transforms) ).closed
    # has to be 0 or 1
    if condition in { 0, 1, float('inf') }:
        return True
    else:
        return False
    
def investigatorDamage( matrix, next_transform, prev_transforms ):
    """
        DAMAGE:
        A Character who receives greater than or equal to their max_damage becomes unconscious. 
        A Character cannot remove damage to less than 0. 

        This validator returns 0 if the Character's damage is on the interval (-inf, 0)
                               1 if the Character's damage is on the interval [0, max), or
                               2 if the Character's damage is on the interval [max, inf) 
    """
    transformed_matrix = next_transform( currency.investigatorDamage( matrix, prev_transforms ) )
    # damage can't less than 0 or greater than max
    if 0 <= transformed_matrix[1] <= transformed_matrix[0]:
        return 1
    # character is unconscious if max damage is reached
    elif transformed_matrix[1] > transformed_matrix[0]:
        return 2
    # otherwise, invalid transform
    else:
        return 0
    
def investigatorHorror( matrix, next_transform, prev_transforms ):
    """
        HORROR:
        A Character who receives greater than or equal to their max_horror becomes insane. 
        A Character cannot remove horror to less than 0. 

        This validator returns 0 if the Character's horror is on the interval (-inf, 0)
                               1 if the Character's horror is on the interval [0, max), or
                               2 if the Character's horror is on the interval [max, inf) 
    """
    return investigatorDamage( matrix, next_transform, prev_transforms )

def investigatorUnconscious( matrix, next_transform, prev_transforms ):
    """
        UNCONCIOUS:
        A Character becomes unconscious if they receive total damage of at least their max damage.
        This stat exists in {0,1}, where 0 is conscious and 1 is unconscious.
    """
    transformed_matrix = next_transform( currency.investigatorDamage( matrix, prev_transforms ) )
    # unconscious can only be 0 or 1 
    if 0 <= transformed_matrix[1] <= 1:
        return True
    else:
        return False
    
def investigatorInsane( matrix, next_transform, prev_transforms ):
    """
        INSANE:
        A Character becomes insane if they receive total horror of at least their max horror.
        This stat exists in {0,1}, where 0 is sane and 1 is insane.
    """
    return investigatorUnconscious( matrix, next_transform, prev_transforms )

def investigatorDelay( matrix, next_transform, prev_transforms ):
    """
        DELAYED
        A Character becomes delayed for a number of reasons. If delayed, a Character cannot take their turn until they 
            become undelayed during the following Upkeep phase.
        This stat exists in {0,1} where 0 is undelayed, and 1 is delayed.
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[0] <= 1:
        return True
    else:
        return False
    
def investigatorArrested( matrix, next_transform, prev_transforms ):
    """
        ARRESTED
        A Character can be arrested because of certain in-game events. If arrested, a Character becomes DELAYED.
        This stat exists in {0,1,∞} where 0 is un-arrested, and 1 is arrested. Additionally, there are game effects
        that will make a character "unarrestable." In this case, the stat is set to infinity, (which causes any 
        attempt to arrest the investigator to fail) 
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[1] <= 1:
        return True
    else:
        return False
    
def investigatorLostInTimeAndSpace( matrix, next_transform, prev_transforms ):
    """
        LOST IN TIME & SPACE
        A Character becomes lost in time & space for a number of reasons. If lost in time & space, a Character becomes DELAYED.
        A Character remains lost in time & space after becoming undelayed until the following Upkeep phase.
        This stat exists in {0,1} where 0 is not lost in time & space, and 1 is lost in time & space.
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[2] <= 1:
        return True
    else:
        return False
    
def investigatorRetainer( matrix, next_transform, prev_transforms ):
    """
        RETAINER
        A Character gains a retainer likely from the Newspaper. If a Character has a retainer, they gain $1 every Upkeep.
        After gaining their dollar, there is a chance the Character loses their retainer.
        This stat exists in {0,1} where 0 is 'has no retainer', and 1 is 'has retainer'.
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[3] <= 1:
        return True
    else:
        return False
    
def investigatorBankLoan( matrix, next_transform, prev_transforms ):
    """
        BANK LOAN
        A Character gains a loan from the Bank of Arkham. When a Character gets the loan, 
        they immediately gain $10. If a Character has a loan, there is a chance they must pay 
        $1 or, if unable, lose all of their items. If this occurs, the Character may not take
        out another loan.\n
        This stat exists in {0,1,inf} where 0 is 'has no bank loan', 1 is 'has bank loan', 
        and inf is 'may not receive a bank loan.
        This constraint check returns 0 if passed a bad transform, 1 if a good transform, and
        2 if a transform on a loan that can't be given.
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0, 1, or inf
    if 0 <= transformed_matrix[4] <= 1:
        return 1
    elif transformed_matrix[4] == float('inf'):
        return 2
    else:
        return 0
    
def investigatorSTLMembership( matrix, next_transform, prev_transforms ):
    """
        SILVER TWILIGHT LODGE MEMBERSHIP
        A Character gains a lodge membership from the Silver Twilight Lodge. If a Character has 
        a lodge membership, they can optionally have an encounter in the Inner Sanctum.
        This stat exists in {0,1} where 0 is 'has no lodge membership', and 1 is 'has lodge membership'.
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[5] <= 1:
        return True
    else:
        return False

def investigatorDeputy( matrix, next_transform, prev_transforms ):
    """
        DEPUTY OF ARKHAM
        A Character is deputized for certain heroic acts. If a Character is a deputy, they 
        immediately gain a Patrol Wagon and a Deputy's Revolver, and they gain $1 every Upkeep.
        This stat exists in {0,1} where 0 is 'not deputized', and 1 is 'deputized'.
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )
    # this value has to be 0 or 1
    if 0 <= transformed_matrix[6] <= 1:
        return True
    else:
        return False
    
def investigatorBlessedCursed( matrix, next_transform, prev_transforms ):
    """
        BLESSED & CURSED
        A Character can receive a blessing or a curse for a number of reasons. This status affects the outcome of skill checks.
        If a Character is cursed and becomes blessed, their condition is now normal (the effects cancel). Similarly, if a Character
            is blessed and becomes cursed, their condition is normal.
        This stat exists in {-2,-1,0,1,2} where -2 is cursed (first turn) -1 is cursed, 0 is normal, 1 is blessed, and 2 is blessed (first turn).
    """
    transformed_matrix = next_transform( currency.investigatorConditions( matrix, prev_transforms) )

    if transformed_matrix.blessedCursed in { -1, 0, 1 }:
        return 1
    if transformed_matrix.blessedCursed in { -2, 2 }:
        return 2
    return 0
    
def investigatorSkills( matrix, next_transform, prev_transforms ):
    """
        SKILLS
        Skills adjustments are bound by the maximum of that skill. The minimum is
        always 3 less than the max, hence the boundary.
        Use this to constrain the complement skill, as well.
    """
    transformed_matrix = next_transform( currency.investigatorSkill( matrix, prev_transforms) )
    # skill must be inside the range defined on the investigator sheets
    if transformed_matrix[0] - 3 <= transformed_matrix[1] <= transformed_matrix[0]:
        return True
    else:
        return False


def investigatorFocus( matrix, next_transform, prev_transforms ):
    """
        FOCUS
        Focus is adjusted along with skills. Focus can't be less than 0 or more than 
            the maximum for that player.
    """
    transformed_matrix = next_transform( currency.investigatorFocus( matrix, prev_transforms) )
    # focus can't be less than 0 or greater than the max
    if 0 <= transformed_matrix[1] <= transformed_matrix[0]:
        return True
    else:
        return False

def investigatorChangeLoc( matrix, next_transform, prev_transforms, adjacency_matrix ):
    """
        CHANGING LOCATION
        Movement is a matter of substituting the current location for a desired location.
        This validator requires an adjacency matrix in order to behave normally.
        It will return true if the locations are adjacent, false if not.
    """
    most_recent_location = currency.investigatorLocation( matrix, prev_transforms )[0]
    transformed_location = next_transform( currency.investigatorLocation( matrix, prev_transforms ) )[0]
    # look at the adjaceny matrix to see if the moves are adjacent
    return bool( adjacency_matrix[most_recent_location][transformed_location] )

def investigatorMvmtPoints( matrix, next_transform, prev_transforms ):
    """
        MOVEMENT POINTS
        Movement points are spent moving around the map of Arkham (not the Other Worlds).
        They are also spent on certain items, like Tomes, for a chance to gain clues, spells, or items.
        Movement points are assigned every Movement phase, and are based on current Speed, including 
            buffs and allies.
        Movement points cannot be adjusted below 0.
    """
    transformed_matrix = next_transform( currency.investigatorLocation( matrix, prev_transforms ) )
    # can't be less than zero
    if transformed_matrix[1] < 0:
        return False
    else:
        return True

def investigatorInArkham( matrix, next_transform, prev_transforms ):
    """
        IN ARKHAM
        Certain game effects will only apply to Characters in Arkham (not in Other Worlds).
        This stat exists in {0,1}, where 0 is 'in Other Worlds,' and 1 is 'in Arkham.'
    """
    transformed_matrix = next_transform( currency.investigatorLocation( matrix, prev_transforms ) )
    # can't be less than zero
    if 0 <= transformed_matrix[1] <= 1:
        return True
    else:
        return False
    
def investigatorHands( matrix, next_transform, prev_transforms ):
    """
        HANDS
        Investigators have a standard 2 hands available. Reducing this to less than 0 is illegal.
        Some items or spells may increase the number of hands, but this constraint gives no upper limit.

        Returns True if the proposed transform is 0 <= hands, else returns False
    """
    transformed_matrix = next_transform( currency.investigatorEquippedItems( matrix, prev_transforms ) )
    # can't be less than 0
    if 0 <= transformed_matrix[0]:
        return True
    else:
        return False
    
def investigatorMoney( dictionary, next_transform, prev_transforms ):
    """
        MONEY
        Money exists in [0,inf). While the analog game has a finite amount of money tokens, 
            right now there is no rule regarding what happens when that pool of tokens runs out.
            Since this is the case, I am assuming there's no reason to believe the money should 
            run out for any reason.
    """
    transformed_dictionary = next_transform( currency.investigatorPossessions( dictionary, prev_transforms ) )
    # can't be less than 0
    if 0 <= transformed_dictionary['money']:
        return True
    else:
        return False

def investigatorClues( dictionary, next_transform, prev_transforms ):
    """
        CLUES
        Clues exists in [0,inf), and so 'negative clues' is illegal. The analog game may have something to 
            say about running out of clue tokens, but I'm choosing to treat clue tokens as an infinite resource.
    """
    transformed_dictionary = next_transform( currency.investigatorPossessions( dictionary, prev_transforms ) )
    # can't be less than 0
    if 0 <= transformed_dictionary['clues']:
        return True
    else:
        return False
    
def investigatorGateTrophies( dictionary, next_transform, prev_transforms ):
    """
        GATE TROPHIES
        Gate trophies exist in [0,num_gates] where num_gates is the number of gate tokens in the game.
        Base game includes 16 gate tokens. Rewrite this constraint when including expansions.
    """
    transformed_dictionary = next_transform( currency.investigatorPossessions( dictionary, prev_transforms ) )
    if 0 <= transformed_dictionary['gate_trophies'] <= 16:
        return True
    else:
        return False
    
def investigatorMonsterTrophies( dictionary, next_transform, prev_transforms ):
    """
        MONSTER TROPHIES
        Monster trophies exist in [0,num_monsters] where num_monsters is the number of monster tokens in the game.
        Base game includes 55 regular monsters. 
        Rewrite this constraint whenever additional monsters are added, such as Nyarlathotep's masks or including 
            expansions.
    """
    transformed_dictionary = next_transform( currency.investigatorPossessions( dictionary, prev_transforms ) )
    if 0 <= transformed_dictionary['monster_trophies'] <= 55:
        return True
    else:
        return False
    
def boardGateLimit( integer, next_transform, prev_transforms ):
    """
        TOO MANY GATES
        There is a limit to the number of gates that can be open at once.
        The way the gate limit is handled is incrementing up from the negative of the
        gate limit. If the gate count ever reaches 0, the gate limit is reached.
        This function returns -1 if passed a bad transform, 0 if passed a good transform,
        or 1 if passed a transform that surpasses the gate limit.
    """
    transformed_integer = next_transform( currency.boardGatesInArkham( integer, prev_transforms ) )
    if transformed_integer <= 0:
        return 0
    elif 0 < transformed_integer:
        return 1
    return -1

def boardMonstersInArkhamLimit( integer, next_transform, prev_transforms ):
    """
        TOO MANY MONSTERS
        The monster limit is set at the beginning of the game at according to how
        many investigators there are. The monster limit is the number of Investigators
        plus 3. 
        The way the monster limit is handled is incrementing up from the negative of the
        monster limit. If the monster count ever reaches 0, the monster limit is reached.
        This function returns 0 if passed a bad transform, 1 if passed a good
        transform, and 2 if the monster limit has been reached.
    """
    transformed_integer = next_transform( currency.board_monsters_in_arkham( integer, prev_transforms ) )
    if transformed_integer <= 0:
        return 1
    elif 0 < transformed_integer:
        return 2
    return 0
    
def boardMonstersInOutskirtsLimit( integer, next_transform, prev_transforms ):
    """
        OUTSKIRTS ARE FULL
        When there are too many monsters in the outskirts, the terror level increases. 
        The way the outskirts limit is handled is incrementing up from the negative of the
        outskirts limit. If the outskirts count ever reaches 0, the outskirts limit is reached.
        This function returns 0 when passed a bad transform, 1 when passed a good 
            transform, and 2 if the outskirts are full.
    """
    transformed_integer = next_transform( currency.board_monsters_in_outskirts( integer, prev_transforms ) )
    if transformed_integer <= 0:
        return 1
    elif 0 < transformed_integer:
        return 2
    return 0
    
def boardTerrorTrack( integer, next_transfrom, prev_transforms ):
    """
        TERROR TRACK
        As the terror track increases, various business close down and allies leave town.
        If the terror track ever reaches 10, doom is added to the doom track instead.
        The way the terror limit is handled is to increment up from the negative of the 
        terror limit. If the terror limit ever reaches 0, the terror limit is reached.
        This function returns 0 when passed a bad transform, 1 if no businesses should 
        close, 2 when the first business should close, 3 when the second business should 
        close, 4 when the third business should close, 5 if the terror track is full
    """
    transformed_integer = next_transfrom( currency.board_terror_track( integer, prev_transforms ) )
    if 0 <= transformed_integer:
        return 5
    elif -1 <= transformed_integer < 0:
        return 4
    elif -4 <= transformed_integer < 1:
        return 3
    elif -7 <= transformed_integer < -4:
        return 2
    elif -10 <= transformed_integer < -7:
        return 1
    return 0

def boardDoomTrack( integer, next_transform, prev_transforms ):
    """
        DOOM TRACK
        Every time a gate appears, the Doom Track increases by one. Additionally,
        if the Terror Track is ever full but needs to be increased, the Doom
        Track will increase instead. There are other, rarer game events that could
        increase the Doom Track.
        If the Doom Track ever reachs 0, the Ancient One wakes up. Technically, there
        is no lower bound for doom, but there are virtually zero ways to decrease it beyond
        the Ancient One's threshold. 
        This function returns 0 if the Doom Track is not full, and 1 if it is.
    """
    transformed_integer = next_transform( currency.board_doom_track( integer, prev_transforms ) )

    if transformed_integer < 0:
        return 0
    elif 0 <= transformed_integer:
        return 1
    
def monsterMvmtRules( vector, next_transform, prev_transforms ):
    """
        MONSTER MOVEMENT RULESETS
        Monsters will move when the Mythos procedure calls for it. "Movement" looks different
            for different monsters.
        0. Normal Movement
            This monster will move 1 adjacent space in the direction supplied by the Mythos.
        1. Fast Movement
            This monster will move 2 adjacent spaces in the direction supplied by the Mythos.
        2. Stationary
            This monster will not be moved, even if called for by the Mythos.
        3. Flying
            This monsters will move to
                - from a location/street area to an adjacent street area if an Investigator is present
                - from a location/street area to the sky if an Investigator is not present
                - from the sky to a street area if an Investigator is present 
            This monster will not move if no Investigator is in any street area.
        4. Chthonian
            This monster will not change location. Instead it will 'roll a 2-sided die', and add 1 damage 
            to every investigator in Arkham on a 1 and nothing on a 2.
        5. Hound of Tindalos
            This monster will move to the Investigator in the nearest location to it, barring the Hospital
            and Asylum.

        This validator returns True if the proposed ruleset is one of these. Otherwise, False. 
    """
    transformed_vector = next_transform( currency.monster_rulesets( vector, prev_transforms ) )
    if transformed_vector[0] not in { 0, 1, 2, 3, 4, 5 }:
        return False
    else:
        return True
    
def monsterEvadeRules( vector, next_transform, prev_transforms ):
    """
        MONSTER EVASION RULESETS
        When an Investigator performs an Evade check against monster, the monster's evade ruleset
            is invoked.
        0. Standard Evade 
            On a failure, the Investigator immediately receives the appropriate Horror and combat
            begins. 
            On a success, the Investigator returns to moving as they were.
        1. Elder Thing 
            On a failure, in addition to immediately receiving Horror and beginning combat, the 
                Investigator must also discard a Weapon or Spell.
            On a success, the Investigator returns to moving as they were.
        2. Nightgaunt
            On a failure, the Investigator is moved to the nearest gate if in Arkham, or to the corresponding
                gate in Arkham if in an Other World.
            On a success, the Investigator returns to moving as they were.

        This validator returns True if the proposed ruleset is one of these. Otherwise, False.
    """
    transformed_vector = next_transform( currency.monster_rulesets( vector, prev_transforms ) )
    if transformed_vector[0] not in { 0, 1 }:
        return False
    else:
        return True

def monsterCombatRules( vector, next_transform, prev_transforms ):
    """
        MONSTER COMBAT RULESETS
        When an Investigator performs a Combat check against a monster, the monster's combat
            ruleset is invoked.
        0. Standard Combat
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, the Investigator receives the appropriate amount of Damage, and, if conscious,
                must begin the combat cycle again. 
        1. Dimensional Shambler
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, the Investigator is now lost in time & space.
        2. Elder Thing
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, in addition to receiving the appropriate amount of Damage, and, if conscious,
                beginning the combat cycle again, the Investigator must discard a Weapon or Spell.
        3. Mi-Go
            On a success, the Investigator earns a random Unique Item, but does not get to collect any
                monster trophies. In addition, the Mi-Go is not returned to the Monster Cup, but is 
                removed from Arkham.
            On a failure, the Investigator receives the appropriate amount of Damage, and, if conscious,
                must begin the combat cycle again.
        4. Nightgaunt
            On a success, the Investigator removes the monster from Arkham and receives the monster's
                toughness in monster trophies.
            On a failure, the Investigator is moved to the nearest gate if in Arkham, or to the corresponding
                gate in Arkham if in an Other World.
        5. The Black Man
            Instead of performing a Combat check, the Investigator must pass a Luck(-1) check or be devoured. If
                passed, the Investigator earns 2 clues. In either case, the Black Man is removed from Arkham.
        6. The Bloated Woman
            Before the Horror check during Combat, the Investigator must pass a Will(-2) check or immediately fail 
                both the Horror and Combat checks.
        7. The Dark Pharaoh
            Lore is used in Combat instead of Fight
        8. Warlock
            On a success, the Investigator earns 2 clues tokens, but does not collect any monster trophies. In 
                addition, this monster is not returned to the Monster Cup, but is removed from Arkham.
            On a failure, the Investigator receives the appropriate amount of Damage, and, if conscious,
                must begin the combat cycle again.

        This validator returns True if the proposed rulelset is one of these. Otherwise, False.
    """
    transformed_vector = next_transform( currency.monster_rulesets( vector, prev_transforms ) )
    if transformed_vector[0] not in { 0, 1, 2, 3, 4, 5, 6, 7, 8 }:
        return False
    else:
        return True
    
def monsterAmbush( vector, next_transform, prev_transforms ):
    """
        AMBUSH

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[0] <= 1:
        return True
    else:
        return False
    
def monsterEndless( vector, next_transform, prev_transforms ):
    """
        ENDLESS

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[1] <= 1:
        return True
    else:
        return False
    
def monsterUndead( vector, next_transform, prev_transforms ):
    """
        UNDEAD

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[2] <= 1:
        return True
    else:
        return False
    
def monsterPhysical( vector, next_transform, prev_transforms ):
    """
        PHYSICAL RESISTANCE AND IMMUNITY

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[3] <= 1:
        return True
    else:
        return False
    
def monsterMagical( vector, next_transform, prev_transforms ):
    """
        MAGICAL RESISTANCE AND IMMUNITY

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[4] <= 1:
        return True
    else:
        return False
    
def monsterNightmarish( vector, next_transform, prev_transforms ):
    """
        NIGHTMARISH

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[5] <= 1:
        return True
    else:
        return False
    
def monsterOverwhelming( vector, next_transform, prev_transforms ):
    """
        OVERWHELMING

    """
    transformed_vector = next_transform( currency.monster_abilities( vector, prev_transforms ) )
    if 0 <= transformed_vector[6] <= 1:
        return True
    else:
        return False

def monsterToughness( vector, next_transform, prev_transforms ):
    """
        TOUGHNESS

    """
    transformed_vector = next_transform( currency.monster_stats( vector, prev_transforms ) )
    if transformed_vector[1] > 0:
        return True
    else:
        return False
    