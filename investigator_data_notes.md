# INVESTIGATOR DATA 


- Health Status ✔︎
    - Damage: *matrix*
        - Maximum Damage: *int*
        - Current Damage: *int*
        - Consciousness: *{ 0,1 }*
    - Horror: *matrix*
        - Maximum Horror: *int*
        - Current Horror: *int*
        - Sanity: *{ 0,1 }*
- Condition ✔︎
    - Arrested: *{ 0,1 }*
    - Delayed: *{ 0,1 }*
    - Lost in Time & Space: *{ 0,1 }*
    - Retainer: *{ 0,1 }*
    - Bank Loan: *{ 0,1 }*
    - Silver Twilight Lodge Membership: *{ 0,1 }*
    - Deputy of Arkham: *{ 0,1 }*
    - Blessed/Cursed: *{ -1,0,1 }*
- Locational ✔︎
    - Current location: *int*
    - In Arkham: *{ 0,1 }*
- Skills ✔︎
    - Focus: *matrix*
        - Maximum Focus: *int*
        - Default Focus: *int*
        - Empty value: *int*
    - Speed/Sneak: *matrix*
        - Maximum Speed: *int*
        - Default Speed: *int*
        - Speed/Sneak Sum: *int*
    - Fight/Will: *matrix*
        - Maximum Fight: *int*
        - Default Fight: *int*
        - Fight/Will Sum: *int*
    - Lore/Luck: *matrix*
        - Maximum Lore: *int*
        - Default Lore: *int*
        - Lore/Luck Sum: *int* 
- Inventory ✔︎
    - Random Possessions: *matrix*
        - Common Items *int*
        - Unique Items *int*
        - Spells *int*
        - Buffs (Skills) *int*
    - Fixed Possessions: *dict*
        - Clues: *int*
        - Money: *int*
        - Gate Trophies: *int*
        - Monster Trophies: *int*
        - Common Items: *list[ str ]*
        - Unique Items: *list[ str ]*
        - Spells: *list[ str ]*
        - Buffs (Skills): *int*
    - Equipment: *matrix*
        - Available Hands: *int*
        - Equipped Items: *list[ str ]*
    - Exhausted Items: *list[ str ]*           

## HEALTH STATUS 

Represented by a matrix. `[0,0,0]` is used for stamina/damage and sanity/horror. The first element is the maximum damage or horror an Investigator can receive; the second is the default (this is likely always be 0); the third is whether or not the Investigator is unconscious or insane. 

Whenever an Investigator recieves damage or horror, the default value is incremented up, and the reverse is true for when an Investigator heals themselves. If an Investigator's current damage or horror is equal to or greater than their maximum value, they become unconcscious or insane, respective of the type of stat.

Default damage and horror cannot fall below 0. 

## CONDITIONS

`[ 0, 0, 0, 0, 0, 0, 0, 0 ]` represents an investigator's current conditions. In order they are:

- whether or not the Investigator is delayed
- whether or not the Investigator is arrested
- whether or not the Investigator is lost in time & space
- whether or not the Investigator has a retainer
- whether or not the Investigator has a bank loan
- whether or not the Investigator has a Silver Twilight Lodge Membership
- whether or not the Investigator has been deputized
- whether or not the Investigator is blessed, cursed, or neither.

All of these excepting blessed/cursed are in { 0,1 }. Blessed/cursed is in { -1,0,1 }, where 1 is blessed, -1 is cursed, and 0 is neither. 

## LOCATIONAL

### Current Location

This is an integer in { 1,...N } where N is the number of locations in the game. Transforming this number just looks like replacing it with a new number, but there is a mathematical basis for the transform:

$a*\frac{b}{a}\longrightarrow\frac{a*b}{a}\longrightarrow\frac{a}{a}*b$ 

Therefore a function of a and b that maps a to b is thus:

$f: a \longrightarrow b $

A bit silly, but I like that there's at least an attempt at rigor here.

### In Arkham

This is in {0,1}. Certain procedures in the game will only affect Investigators who are either in or not in Arkham.

The validator that handles current location transformations has a local copy of the map of Arkham, which is a matrix:

[ 
    [ None, 'A', 'B', 'C', ... ],
    [ 'A',   1,   1,   0,  ... ],
    [ 'B',   1,   1,   1,  ... ],
    [ 'C',   0,   1,   1,  ... ],
    ...
]
Here we have represented at least 3 locations, A, B, and C and their adjacency. On a graph, A shares an edges with B, which 
    shares an edges with C. A and C do not share an edge, and each location is assumed to be self-adjacent:

A -- B -- C

Row 0 is the headers row. Row 1-N are each unique locations, and every column is an adjacency score; 0 := not adjacent, 
    and 1 := adjacent. 
Investigator locational data represents current location as a number that corresponds to a row in the matrix. 
There exists some transformation that takes in a locational data matrix for a given Character, and transforms the current 
    location (the row) into a new one (a column). 
The validator then only needs to ask if the current row has marked the column as a 0 or a 1, and return False or True respectively.
There is a None value at [0][0] to offset the rows and columns appropriately.

This is a redundant representation, since it is symmetric across the diagonal. However, this will actually be convenient because it
    will allow me to skip the step of converting questions into their converse. That is, if A is adjacent to B, then due to the symmetry
    of the matrix, we know that B is adjacent to A. Both is_adjacent(A,B) and is_adjacent(B, A) both return True through the same logic 
    without the added complexity of converting B->A into A->B. The information for both statements is in the matrix. 

Investigator locational data looks like this: [ N, M, A ], where N := current location as a natural number representing a row in the 
    matrix above, M := movement points available to the Investigator, and A := in Arkham, existing in   where 1 is in Arkham, and 0
    is not in Arkham.

## SKILLS

Skills are matrices that describe max, default, and sum. The sum is there to imply the level of a skills complement. For instance, if speed is set to 3, and the sum is 5, `sum - speed == sneak` so sneak is 2. 

A skill minimum is found by `max - 3`. 

When a passive buff is applied, such as a Fight skill, the maximum increases, the default increase, and the sum must also increase. For example, with the buff "Fight + 1" applied to a default `[4,4,5]`, the transformed matrix becomes `[5,5,6]`. This is because with the buff a current fight of 4 (on the analog character sheet) should be read as a 5. Since this will not affect Will (still a 1), the sum must increase. Alternatively, if the buff is for the complementary skill, only the sum needs to increase. From the above example, we get `[4,4,6]`, indicating that current fight is 4 and current will is 2.

### Focus

A matrix: `[a,b,c]`, where `a` is maximum, `b` is the default, and `c` is an empty value. This is so it matches the shape of the other skill matrices.

Focus cannot be less than 0.

### Speed/Sneak

A matrix: `[a,b,c]`, where `a` is maximum speed, `b` is the default speed, and `c` is the sum of the two skills. 

### Fight/Will

A matrix: `[a,b,c]`, where `a` is maximum fight, `b` is the default fight, and `c` is the sum of the two skills. 

### Lore/Luck

A matrix: `[a,b,c]`, where `a` is maximum lore, `b` is the default lore, and `c` is the sum of the two skills. 

## POSSESSIONS

### Random Possessions

Random possessions are represented as a list of numbers, such as `[ 1, 1, 1, 2 ]`. They are, in order:
- common items
- unique items
- spells
- buffs (skills)

This default setup has no transforms.

### Fixed Possessions

This is where starting items can be defined, and is the working inventory for the character. It is a dictionary for ease of reference.

```
fixed_possessions = { 
    'money' : 0,
    'clues' : 0,
    'gate_trophies' : 0,
    'monster_trophies' : 0, 
    'common' : [],
    'unique' : [],
    'spells' : [],
    'buffs' : [] 
}
```

Money, clues, and trophies are all in $[0,\infty)$. Items, spells, and buffs (skills) are lists. 

Storing transforms and getting current possessions will be different than, for example, getting current damage.
Since adding & removing items requires both the dictionary to be transformed and the item to added or removed, the transformation list includes both the transform and any arguments given, packed in a tuple. For instance:

```
transforms = [ 
    (add_common_item, 'knife'), 
    (remove_common_item, 'spoon') 
]
```
The `get_current` function will have all of the necessary components to rebuild the current state of possessions.

### Equipment
Equipped items are represented by a list, such as `[ 2, [] ]`, representing available hands and equipped items, respectively. Hands can't be less than zero, but won't have an upper bound.

This is where the procedure that handles combat will look to get weapon and spell bonuses.







