
# LOCATION DATA SOURCES

- Graph:  *labeled adjacency matrix*
    - Neighbors
    - Left
    - Right
- Neighborhoood: *str*
- Variety ( Location, Street Area, Other World, etc. ): *str*
- Special Encounter: callable 
- Guaranteed Resources: *str*
- Possible Resources: *str*
- Stabililty: *{0,1}*
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

## Neighborhood
