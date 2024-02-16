import csv

"""

For future reference, here's the official row number for each location.

1: CURIOSITIE SHOPPE
2: NEWSPAPER
3: TRAIN STATION
4: ARKHAM ASYLUM
5: BANK OF ARKHAM
6: INDEPENDENCE SQUARE
7: HIBB'S ROADHOUSE
8: POLICE STATION
9: JAIL CELL
10: VELMA'S DINER
11: RIVER DOCKS
12: THE UNNAMABLE
13: UNVISITED ISLE
14: BLACK CAVE
15: GENERAL STORE
16: GRAVEYARD
17: ADMINISTRATION
18: SCIENCE BUILDING
19: LIBRARY
20: THE WITCH HOUSE
21: THE SILVER TWILIGHT LODGE
22: THE INNER SANCTUM
23: ST. MARY'S HOSPITAL
24: WOODS
25: YE OLDE MAGICK SHOPPE
26: MA'S BOARDING HOUSE
27: HISTORICAL SOCIETY
28: SOUTH CHURCH
29: NORTHSIDE STREETS
30: DOWNTOWN STREETS
31: EASTTOWN STREETS
32: MERCHANT DISTRICT STREETS
33: RIVERTOWN STREETS
34: MISKATONIC UNIVERSITY STREETS
35: FRENCH HILL STREETS
36: UPTOWN STREETS
37: SOUTHSIDE STREETS
38: OUTSKIRTS
39: R'LYEH
40: PLATEAU OF LENG
41: THE DREAMLANDS
42: GREAT HALL OF CELEANO
43: YUGGOTH
44: CITY OF THE GREAT RACE
45: ABYSS
46: ANOTHER DIMENSION
"""


def adjacencies_of_arkham( map_data_csv ):
    arkham = [ [None] ]
    neighbors = {}  
    with open( map_data_csv ) as file:
        table = csv.reader( file, delimiter="," )
        
        # transpose the first column into a header row
        for row in table:
            if row[0] != 'name':
                # append to header
                arkham[0].append( row[0] )
                # add to neighbors dict
                neighbors[ row[0] ] = [ w.lstrip() for w in row[3].split(',') ]

    # add adjacencies
    for location in neighbors:
        location_row = [ location ]
        for neighbor in arkham[0][1:]:
            if neighbor in neighbors[location]:
                location_row += [1]
            else: 
                location_row += [0]
        arkham.append( location_row )
    
    # add other worlds 
    no_adjacencies = [ 0 for n in arkham[0][1:]]
    other_worlds = [ 'R\'LYEH','PLATEAU OF LENG','THE DREAMLANDS','GREAT HALL OF CELEANO','YUGGOTH','CITY OF THE GREAT RACE','ABYSS','ANOTHER DIMENSION']
    for w in other_worlds:
        arkham.append( [w] + no_adjacencies )

    return arkham

# locational data

locational_defaults = [
    [ 'name',           'location'    ],
    [ 'Amanda Sharpe',  [ 19, 0, 1 ]  ],
    [ 'Harvey Walters', [ 17, 0, 1 ]  ]
]

locational_transforms = [
    [ 'name',           'location_transforms'   ],
    [ 'Amanda Sharpe',  [],                     ],
    [ 'Harvey Walters', [],                     ]
]

# locational transformers

def change_loc( matrix, new_loc ):
    return [ new_loc, matrix[1], matrix[2] ]

# northside neighborhood
def move_to_CURIOSITIE_SHOPPE( matrix ):
    return change_loc( matrix, 1 )
def move_to_NEWSPAPER( matrix ):
    return change_loc( matrix, 2 )
def move_to_TRAIN_STATION( matrix ):
    return change_loc( matrix, 3 )
def move_to_NORTHSIDE_STREETS( matrix ):
    return change_loc( matrix, 29 )
# downtown neighborhood
def move_to_ARKHAM_ASYLUM( matrix ):
    return change_loc( matrix, 4 )
def move_to_BANK_OF_ARKHAM( matrix ):
    return change_loc( matrix, 5 )
def move_to_INDEPENDENCE_SQUARE( matrix ):
    return change_loc( matrix, 6)
def move_to_DOWNTOWN_STREETS( matrix ):
    return change_loc( matrix, 30)
# easttown neighborhood
def move_to_HIBBS_ROADHOUSE( matrix ):
    return change_loc( matrix, 7 )
def move_to_POLICE_STATION( matrix ):
    return change_loc( matrix, 8 )
def move_to_JAIL( matrix ):
    return change_loc( matrix, 9)
def move_to_VELMAS_DINER( matrix ):
    return change_loc( matrix, 10)
def move_to_DOWNTOWN_STREETS( matrix ):
    return change_loc( matrix, 31)
# merchant district neighborhood
def move_to_RIVER_DOCKS( matrix ):
    return change_loc( matrix, 11 )
def move_to_THE_UNNAMEABLE( matrix ):
    return change_loc( matrix, 12 )
def move_to_UNVISITED_ISLE( matrix ):
    return change_loc( matrix, 13)
def move_to_MERCHANT_DISTRICT_STREETS( matrix ):
    return change_loc( matrix, 32)
# rivertown neighborhood
def move_to_BLACK_CAVE( matrix ):
    return change_loc( matrix, 14 )
def move_to_GENERAL_STORE( matrix ):
    return change_loc( matrix, 15 )
def move_to_GRAVEYARD( matrix ):
    return change_loc( matrix, 16)
def move_to_RIVERTOWN_STREETS( matrix ):
    return change_loc( matrix, 33)
# miskatonic university neighborhood
def move_to_ADMINISTRATION( matrix ):
    return change_loc( matrix, 17 )
def move_to_SCIENCE_BUILDING( matrix ):
    return change_loc( matrix, 18 )
def move_to_LIBRARY( matrix ):
    return change_loc( matrix, 19)
def move_to_MISKATONIC_UNIVERSITY_STREETS( matrix ):
    return change_loc( matrix, 34)
# french hill neighborhood
def move_to_THE_WITCH_HOUSE( matrix ):
    return change_loc( matrix, 20 )
def move_to_THE_SILVER_TWILIGHT_LODGE( matrix ):
    return change_loc( matrix, 21 )
def move_to_THE_INNER_SANCTUM( matrix ):
    return change_loc( matrix, 22)
def move_to_FRENCH_HILL_STREETS( matrix ):
    return change_loc( matrix, 35)
# uptown neighborhood
def move_to_ST_MARYS_HOSPITAL( matrix ):
    return change_loc( matrix, 23 )
def move_to_WOODS( matrix ):
    return change_loc( matrix, 24 )
def move_to_YE_OLDE_MAGICK_SHOPPE( matrix ):
    return change_loc( matrix, 25)
def move_to_UPTOWN_STREETS( matrix ):
    return change_loc( matrix, 36)
# southside neighborhood
def move_to_MAS_BOARDING_HOUSE( matrix ):
    return change_loc( matrix, 26 )
def move_to_HISTORICAL_SOCIETY( matrix ):
    return change_loc( matrix, 27 )
def move_to_SOUTH_CHURCH( matrix ):
    return change_loc( matrix, 28)
def move_to_SOUTHSIDE_STREETS( matrix ):
    return change_loc( matrix, 37)

def inc_movement( matrix ):
    return [ matrix[0], matrix[1]+1, matrix[2] ]
def dec_movement( matrix ):
    return [ matrix[0], matrix[1]-1, matrix[2] ]
def set_in_arkham( matrix ):
    return [ matrix[0], matrix[1], matrix[2]+1 ]
def set_in_other_world( matrix ):
    return [ matrix[0], matrix[1], matrix[2]-1 ]

def get_current_loc( matrix, transformations ):
    loc = matrix
    for transformation in transformations:
        loc = transformation( loc )
    return loc

get_current_mvmt_pts = get_current_in_arkham = get_current_loc

# locational validators
# dependency: adjacencies_of_arkham produces the adjacency matrix

adjacency_matrix = adjacencies_of_arkham( 'locations.csv' )

def change_loc_constraint( matrix, next_transform, prev_transforms ):
    """
        CHANGING LOCATION
    """
    most_recent_location = get_current_loc( matrix, prev_transforms )[0]
    transformed_location = next_transform( get_current_loc( matrix, prev_transforms ) )[0]
    # look at the adjaceny matrix to see if the moves are adjacent
    return bool( adjacency_matrix[most_recent_location][transformed_location] )

def movement_pts_constraint( matrix, next_transform, prev_transforms ):
    """
        MOVEMENT POINTS
    """
    transformed_matrix = next_transform( get_current_loc( matrix, prev_transforms ) )
    # can't be less than zero
    if transformed_matrix[1] < 0:
        return False
    else:
        return True

def in_arkham_constraint( matrix, next_transform, prev_transforms ):
    """
        MOVEMENT POINTS
    """
    transformed_matrix = next_transform( get_current_loc( matrix, prev_transforms ) )
    # can't be less than zero
    if 0 <= transformed_matrix[1] <= 1:
        return True
    else:
        return False









