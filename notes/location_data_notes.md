# LOCATION DATA

- Graph:  *labeled adjacency matrix*
    - Neighbors
    - Left
    - Right
- Neighborhoood: *str*
- Variety ( Location, Street Area, Other World, etc. ): *str*
- Special Encounter: *callable* 
- Guaranteed Resources: *str*
- Possible Resources: *str*
- Stabililty: *{False, True}*
- Occupants: *list[str]*
- Status
    - Clues: *int*
    - Sealed: *{0,1}*
    - Gate: *{0,1}*
    - Explored: *{0,1}*
    - Closed (for business): *{0,1}*

Of these the things that can transform are the graphs, occupants, and status.

## GRAPH

This is a labeled adjacency matrix. The first row and column are the name of the location represented 
    by that row or column. The default adjacencies are in {0,1}. This matrix includes Other Worlds.

The Neighbors graph is an undirected graph resolving regular adjacencies for Investigator movement. 
    The Left and Right graphs are directed graphs. These will resolve monster movement.

Adding an adjacency (like when a gate appears) or removing an adjacency (like when a business closes)
    is a matter of adding or subtracting 1 from the correct elements in the matrix. 

```
# closing the General Store means it is no longer adjacent to anything
...
for row in graph[1:]:
    # transform the row
    if row[0] == 'GENERAL STORE':
        return [ row[0] ] + [ 0 for n in row[1:] ]
# similar function for tranforming the column
```

## Neighborhood & Variety

These are strings required for reference. Sometimes occupancy will change based on neighborhood.
    For instance, a Mythos effect like "all monsters in the Downtown Streets and Locations are 
    returned to the Monster Cup" will need to find all Downtown neighborhood locations.

## Special Encounters

These are optional procedures that become available when an Investigator lands on that space.

## Guaranteed and Possible Resources

When inspecting the board, a player should be able to ask which resources are available from 
    which locations. Guaranteed resources (if not `None`) also indicates a special encounter.

## Stability

Locations that are 'unstable' are locations that could produce a Clue and where a gate could 
    open up. This is here for reference.

## Occupants

This is the list of monsters that are currently at the location. Adding a monster looks like 
    returning a list concatenation.

```
occupants = []
def add_occupant( matrix, occupant ):
    return matrix + [ occupant ]
```

## Status

This will be a list that gets passed into a transformer. It looks like `[ 0, 0, 0, 0, 0, 0 ]`

In order, the elements are:
- number of clues at that location
- number of clues that have ever been at the location
- whether or not the location is sealed (gates cannot appear on sealed locations)
- whether or not there is a gate on the location
- whether or not a gate has been explored
- whether or not the location is closed for business

### Clues

An integer representing the number of Clues at a location. 

Locations with higher clue counts are locations more likely to spawn a gate. 

### Sealed

This is in {0,1}. Sealed locations cannot spawn a gate. If the gate spawn procedure selects a 
    sealed location, nothing will change.

### Gate

This is in {0,1}. 0 indicates no gate, 1 indicates gate. The gate itself is listed in Occupants.

### Explored

This is in {0,1}. Gates that are explored (1) can be closed or sealed. If an Investigator moves 
    away from a location that is explored, it will become unexplored. An unexplored location 
    with a gate has to become explored again (by visiting the Other World!) in order to close or 
    seal the gate.

Additionally, an Investigator who is at an explored location won't be relocated to the Other World 
    at the top of the Encounters phase. An Investigator who is at an unexplored location will be 
    relocated to the Other World at the top of the Encounters phase. 

### Closed

This is in {0,1}. If a location is closed, an Investigator visiting that location is "breaking in."
    The outcome during the Encounters phase will be either nothing, a resource is found, or the 
    Investigator is arrested.
