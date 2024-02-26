# MONSTER DATA

- Movement *scalar* { 0,...5 }
    - Normal *{ 0 }*
    - Fast *{ 1 }*
    - Stationary *{ 2 }*
    - Flying *{ 3 }*
    - Chthonian *{ 4 }*
    - Hound of Tindalos *{ 5 }*
- Dimension *scalar* { 0, ...8 } 
    - Circle *{ 0 }*
    - Triangle *{ 1 }*
    - Square *{ 2 }*
    - Diamond *{ 3 }*
    - Hexagon *{ 4 }*
    - Crescent *{ 5 }*
    - Star *{ 6 }*
    - Slash *{ 7 }*
    - Plus *{ 8 }*
- Abilities *vector* [ { 0, 1 }, { 0, 1 }, { 0, 1 }, { 0, 0.5, 1 }, { 0, 0.5, 1 }, { 0, 1, 2... }, { 0, 1, 2... } ]
    - Ambush *{ 0, 1 }*
    - Endless *{ 0, 1 }*
    - Undead *{ 0, 1 }*
    - Physical Resistance/Immunity *{ 0, 0.5, 1 }*
    - Magical Resistance/Immunity *{ 0, 0.5, 1 }*
    - Nightmarish *{ 0, 1, 2... }*
    - Overwhelming *{ 0, 1, 2... }*
- Evasion *scalar* { 0, 1 } 
    - Normal *{ 0 }* 
    - Elder Thing *{ 1 }*
- Combat *scalar* { 0, ...10 }
    - Normal *{ 0 }*
    - Dimensional Shambler *{ 1 }*
    - Elder Thing *{ 2 }*
    - Mi-Go *{ 5 }*
    - Nightgaunt *{ 6 }*
    - The Black Man *{ 7 }*
    - The Bloated Man *{ 8 }*
    - The Dark Pharaoh *{ 9 }*
    - Warlock *{ 10 }*
- Stats *vector* [ a, t, h<sub>1</sub>, h<sub>2</sub>, c<sub>1</sub>, c<sub>2</sub> ] | {a,t,h<sub>1</sub>, h<sub>2</sub>, c<sub>1</sub>, c<sub>2</sub>} ∈ ℤ
    - Awareness *{ ...-1, 0, 1, ... }*
    - Toughness *{ ...-1, 0, 1, ... }*
    - Horror Rating *{ ...-1, 0, 1, ... }*
    - Horror Damage *{ ...-1, 0, 1, ... }*
    - Combat Rating *{ ...-1, 0, 1, ... }*
    - Combat Damage *{ ...-1, 0, 1, ... }*
- Frequency *scalar*


## Movement

This is an integer greater than or equal to 0 that represents the movement rules that a monster follows. 

    0 := Normal
    1 := Fast
    2 := Stationary
    3 := Flying
    4 := Chthonian
    5 := Hound of Tindalos

Doing it this way means that if more monsters are added and if they have unique movement rules (like the Chthonian and the Hound of Tindalos), I can add their rule in as a function later and reference that rule with a number. 

Currently, as I write this, my idea for how monster movement ought to work is this:

    1. As monsters are added to Arkham, register them in a "Monsters in Arkham" registry, indexed by Dimension.
    2. When monsters of a certain dimension are required to move, a lookup in the registry returns which locations have those monsters if any, and which movement rule those monsters abide by.
    3. For monsters that have non-unique movement types, a procedure runs which removes them from their current location and adds them to their new location as per their movement type.
    4. For monsters that have a unique movement type, a procedure runs which executes their movement rule. For instance, the Chthonian procedure randomly selects from a range(2); on a 1, all the Investigators in Arkham gain 1 damage. Further, the Hound of Tindalos procedure will find the Investigator nearest its location, and then perform the necessary transforms to move the Hound to that location.

## Dimension

This is an integer greater than or equal to 0. The analog game uses shapes to convey this information, but that isn't necessary for this version. There are two reasons monsters have an associated dimension:

1. It is how monsters are referenced for moving instructions. During a Mythos phase, the procedure will randomly select from a "deck" which dimesnions move left and which move right on the board.
2. It is a monster's "home." When a gate is removed from the board (closed or sealed), all monsters whose dimension matches that of the gate are removed from the board. 

## Abilities

This is a vector like this: `[0,0,1,1,0,0]`. This example vector represents a monster with no special abilities. In order they are:

- Ambush
    - { 0, 1 } where 0 represents does not have this ability, and 1 represents does have this ability. If a monster has the Ambush abililty, an Investigator will always fail their Evade check against it.
- Endless
    - { 0, 1 } where 0 represents does not have this ability, and 1 represents does have this ability. If a monster has the Endless ability, they are worth 0 toughness points in Monster Trophies and defeating it will trigger the monster "deck" to increase its frequency by 1.
- Undead
    - { 0, 1 } where 0 represents does not have this ability, and 1 represents does have this ability. If a monster has the Undead ability, they are weak against certain items or spells. 
- Physical Resistance/Immunity
    - { 0, 0.5, 1 } where 0 represents has physical immunity, 0.5 represents has physical resistance, and 1 represents has neither of these abilities. This is so because if an Investigator is using a physical weapon, this modifier is applied to the weapon's bonus by multiplication. A monster with physical immunity reduces the bonus to zero ( `ceil(bonus * 0)` ), a monster with physical resistance reduces the bonus to half rounded up ( `ceil(bonus * 0.5)` ), and a monster with neither does not reduce the bonus at all ( `ceil(bonus * 1)` ). 
- Magical Resistance/Immunity
    - { 0, 0.5, 1 } where 0 represents has magical immunity, 0.5 represents has magical resistance, and 1 represents has neither of these abilities. This is so because if an Investigator is using a magical weapon, this modifier is applied to the weapon's bonus by multiplication. A monster with magical immunity reduces the bonus to zero ( `ceil(bonus * 0)` ), a monster with magical resistance reduces the bonus to half rounded up ( `ceil(bonus * 0.5)` ), and a monster with neither does not reduce the bonus at all ( `ceil(bonus * 1)` ). 
- Nightmarish 
    - [ 0, inf ) where the number represents the horror an Investigator receives immediately after a Horror check. A 0 represents a monster that is not nightmarish, while any number greater than 0 represents a monster that is nightmarish. This is so because this value is applied regardless of whether or not the Investigator passes the check, as in the horror an Investigator receives is always `nightmarish_value + (horror_damage if horror_check_failed else 0)`.
- Overwhelming 
    - [ 0, inf ) where the number represents the damage an Investigator receives immediately after a Combat check. A 0 represents a monster that is not overwhelming, while any number greater than 0 represents a monster that is overwhelming. This is so because this value is applied regardless of whether or not the Investigator passes the check, as in the combat an Investigator receives is always `overwhelming_value + (combat_damage if combat_check_failed else 0)`. 

## Evasion & Combat

Similarly to movement, certain monsters have specific rules that apply during certain contexts. For Evasion and Combat, if an Investigator fails an Evade or Combat check against a monster, the rules that apply to that monster should be followed. In the case of most monsters, these will be the normal rules, but some monsters have unique rules. 

These will each be an integer greater than or equal to 0, where the number represents the ruleset that needs to be followed after the appropriate skill check.

## Stats

This is a vector representing each of the numerical stats a monster has. A vector looks like this: `[-2,1,-1,1,0,2]`, where, in order they are:

- Awareness
- Toughness
- Horror Rating
- Horror Damage
- Combat Rating
- Combat Damage

These are modifiers, with the exception of Horror Damage and Combat Damage, to be added to the appropriate skil check. In the case of awareness, the skill check is Evade; horror rating, Horror check; and combat rating, Combat check. Horror damage and Combat damage are applied to the Investigators health stats if the respective check is failed. 

## Frequency

Frequency is the number of tokens the analog game contains for a given monster. These data will be kept separately from the rest in a dict, like so:

```
{
    'Byakhee' : 3,
    'Chthonian' : 2,
    'Cultist' : 6,
    'Dark Young' : 3
    ...
}
```

The purpose for this is that because monsters generally show up all the time and are randomly selected to do so, a frequency table represents the distribution of monsters to be selected. As monsters are removed from the cup and are added to the board, the transformations on this dict will represent those changes. This allows for 

1. a better representation of a "monster cup" or "monster bag." Instead of using a list and randomizing it to use as a stack, or even an ordered list and randomly choosing an element, I only have to represent each monster once with its initial frequency. The total number of monsters is built in, and the proportion is simply the value divided by that sum.
2. different distributions for different scenarios or Ancient Ones. If Shub-Niggurath is in play, shouldn't there be more Dark Young? If Cthulhu is awakening, shouldn't there be more Star Spawn? I can load in custom parameters much more easily with a simple dict swap. 

