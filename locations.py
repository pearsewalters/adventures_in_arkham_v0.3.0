
import csv

def adjacencies_of_arkham( map_data_csv ):
    neighbors = [  ]

    with open( map_data_csv ) as file:
        table = csv.reader( file, delimiter="," )
        headers = next( table )
        for row in table:
            neighbors.append( [ row[0], row[3], row[4], row[5] ] )

    # add other worlds
    other_worlds = [ 'R\'LYEH','PLATEAU OF LENG','THE DREAMLANDS','GREAT HALL OF CELEANO','YUGGOTH','CITY OF THE GREAT RACE','ABYSS','ANOTHER DIMENSION']
    for world in other_worlds:
        neighbors.append( [ world, 'null', 'null', 'null' ] )

    # initialize matrices
    all_neighbors, left_neighbors, right_neighbors = [ [ None ] ], [ [ None ] ], [ [ None ] ]

    def create_matrix( blank, reference ):
        """Creates a labeled 0-matrix from a blank"""
        num_locations = len( reference )

        for location in reference:
            # add column headers 
            blank[0].append( location[0] )
            # add rows with row headers
            blank.append( [ location[0] ] + [ 0 for n in range( num_locations ) ] )

        return blank

    def assign_neighbors( matrix, reference, direction ):
        """Fills out matrix using reference data"""
        for a,b in zip( matrix[1:], reference ):
            ref = [ w.strip() for w in b[ direction ].split(',') ]
            for index, val in enumerate( matrix[0][1:] ):
                if val in ref:
                    a[index+1] = 1
        return matrix

    all_neighbors = assign_neighbors( create_matrix( all_neighbors, neighbors ), neighbors, 1 )
    left_neighbors = assign_neighbors( create_matrix( left_neighbors, neighbors ), neighbors, 2 )
    right_neighbors = assign_neighbors( create_matrix( right_neighbors, neighbors ), neighbors, 3 )

    return all_neighbors, left_neighbors, right_neighbors
    
    

# locations data

all_neighbors, left_neighbors, right_neighbors = adjacencies_of_arkham( 'locations.csv' )

location_constants = [
    ['name',                          'neighborhood',           'variety',     'special', 'guaranteed',     'possible',                  'instability', 'mystery' ],
    ['CURIOSTIE SHOPPE',              'NORTHSIDE',              'LOCATION',    True,      'unique items',   'common items',              0 ,            0         ],          
    ['NEWSPAPER',                     'NORTHSIDE',              'LOCATION',    False,     None,             'money,clues',               0 ,            0         ],
    ['TRAIN STATION',                 'NORTHSIDE',              'LOCATION',    False,     None,             'common items,unique items', 0 ,            0         ],
    ['ARKHAM ASYLUM',                 'DOWNTOWN',               'LOCATION',    True,      'sanity',         'common items',              0 ,            0         ],
    ['BANK OF ARKHAM',                'DOWNTOWN',               'LOCATION',    True,      'money',          'blessing',                  0 ,            0         ],
    ['INDEPENDENCE SQUARE',           'DOWNTOWN',               'LOCATION',    False,     None,             'common items,unique items', 10,            4         ],
    ['HIBB\'S ROADHOUSE',             'EASTTOWN',               'LOCATION',    False,     None,             'money,common items',        2 ,            5         ],
    ['POLICE STATION',                'EASTTOWN',               'LOCATION',    True,      None,             'common items,clues',        0 ,            0         ],
    ['JAIL CELL',                     'EASTTOWN',               'LOCATION',    False,     None,             None,                        0 ,            0         ],
    ['VELMA\'S DINER',                'EASTTOWN',               'LOCATION',    False,     None,             'money,stamina',             0 ,            0         ],
    ['RIVER DOCKS',                   'MERCHANT DISTRICT',      'LOCATION',    True,      'money',          'common items',              0 ,            0         ],
    ['THE UNNAMABLE',                 'MERCHANT DISTRICT',      'LOCATION',    False,     None,             'unique items,clues',        6 ,            9         ],
    ['UNVISITED ISLE',                'MERCHANT DISTRICT',      'LOCATION',    False,     None,             'clues,spells',              10,            5         ],
    ['BLACK CAVE',                    'RIVERTOWN',              'LOCATION',    False,     None,             'common items,spells',       6 ,            10        ],
    ['GENERAL STORE',                 'RIVERTOWN',              'LOCATION',    True,      'common items',   'money',                     0 ,            0         ],
    ['GRAVEYARD',                     'RIVERTOWN',              'LOCATION',    True,      None,             'clues,unique items',        6 ,            2         ],
    ['ADMINISTRATION',                'MISKATONIC UNIVERSITY',  'LOCATION',    True,      'skills',         'money',                     0 ,            0         ],
    ['SCIENCE BUILDING',              'MISKATONIC UNIVERSITY',  'LOCATION',    True,      'clues',          'unique items',              2 ,            8         ],
    ['LIBRARY',                       'MISKATONIC UNIVERSITY',  'LOCATION',    False,     None,             'unique items,clues',        0 ,            0         ],
    ['THE WITCH HOUSE',               'FRENCH HILL',            'LOCATION',    False,     None,             'clues,spells',              10,            1         ], 
    ['THE SILVER TWILIGHT LODGE',     'FRENCH HILL',            'LOCATION',    True,      None,             'unique items,clues',        2 ,            2         ],
    ['THE INNER SANCTUM',             'FRENCH HILL',            'LOCATION',    False,     None,             None,                        0 ,            0         ], # Inner Sanctum won't ever have a gate on it, since it's only adjacent to the Lodge
    ['ST. MARY\'S HOSPITAL',          'UPTOWN',                 'LOCATION',    True,      'stamina',        'clues',                     0 ,            0         ],
    ['WOODS',                         'UPTOWN',                 'LOCATION',    False,     None,             'money,common items',        10,            6         ],
    ['YE OLDE MAGICK SHOPPE',         'UPTOWN',                 'LOCATION',    True,     'spells',          'unique items',              0 ,            0         ],
    ['MA\'S BOARDING HOUSE',          'SOUTHSIDE',              'LOCATION',    True,     'allies',          'stamina',                   0 ,            0         ],
    ['HISTORICAL SOCIETY',            'SOUTHSIDE',              'LOCATION',    False,    None,              'skills,spells',             2 ,            8         ],
    ['SOUTH CHURCH',                  'SOUTHSIDE',              'LOCATION',    True,     'blessing',        'sanity',                    0 ,            0         ],
    ['NORTHSIDE STREETS',             'NORTHSIDE',              'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['DOWNTOWN STREETS',              'DOWNTOWN',               'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['EASTTOWN STREETS',              'EASTTOWN',               'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['MERCHANT DISTRICT STREETS',     'MERCHANT DISTRICT',      'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['RIVERTOWN STREETS',             'RIVERTOWN',              'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['MISKATONIC UNIVERSITY STREETS', 'MISKATONIC UNIVERSTITY', 'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['FRENCH HILL STREETS',           'FRENCH HILL',            'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['UPTOWN STREETS',                'UPTOWN',                 'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['SOUTHSIDE STREETS',             'SOUTHSIDE',              'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['OUTSKIRTS',                     'OUTSKIRTS',              'SPECIAL',     False,    None,              None,                        0 ,            0         ],
    ['R\'LYEH',                       'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['PLATEAU OF LENG',               'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE DREAMLANDS',                'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['GREAT HALL OF CELEANO',         'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['YUGGOTH',                       'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['CITY OF THE GREAT RACE',        'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['ABYSS',                         'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['ANOTHER DIMENSION',             'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ]
]

location_defaults = [
    ['name',                            'occupants',    'status' ],
    ['CURIOSTIE SHOPPE',                [],             [0,0,0,0,0,0]],
    ['NEWSPAPER' ,                      [],             [0,0,0,0,0,0]],
    ['TRAIN STATION',                   [],             [0,0,0,0,0,0]],
    ['ARKHAM ASYLUM',                   [],             [0,0,0,0,0,0]],
    ['BANK OF ARKHAM',                  [],             [0,0,0,0,0,0]],
    ['INDEPENDENCE SQUARE',             [],             [1,1,0,0,0,0]],
    ['HIBB\'S ROADHOUSE',               [],             [1,1,0,0,0,0]],
    ['POLICE STATION',                  [],             [0,0,0,0,0,0]],
    ['JAIL CELL',                       [],             [0,0,0,0,0,0]],
    ['VELMA\'S DINER',                  [],             [0,0,0,0,0,0]],
    ['RIVER DOCKS',                     [],             [0,0,0,0,0,0]],
    ['THE UNNAMABLE',                   [],             [1,1,0,0,0,0]],
    ['UNVISITED ISLE',                  [],             [1,1,0,0,0,0]],
    ['BLACK CAVE',                      [],             [1,1,0,0,0,0]],
    ['GENERAL STORE',                   [],             [0,0,0,0,0,0]],
    ['GRAVEYARD',                       [],             [1,1,0,0,0,0]],
    ['ADMINISTRATION',                  [],             [0,0,0,0,0,0]],
    ['SCIENCE BUILDING',                [],             [1,1,0,0,0,0]],
    ['LIBRARY',                         [],             [1,1,0,0,0,0]],
    ['THE WITCH HOUSE',                 [],             [1,1,0,0,0,0]],
    ['THE SILVER TWILIGHT LODGE',       [],             [1,1,0,0,0,0]],
    ['THE INNER SANCTUM',               [],             [0,0,0,0,0,0]],
    ['ST. MARY\'S HOSPITAL',            [],             [0,0,0,0,0,0]],
    ['WOODS',                           [],             [1,1,0,0,0,0]],
    ['YE OLDE MAGICK SHOPPE',           [],             [0,0,0,0,0,0]],
    ['MA\'S BOARDING HOUSE',            [],             [0,0,0,0,0,0]],
    ['HISTORICAL SOCIETY',              [],             [1,1,0,0,0,0]],
    ['SOUTH CHURCH',                    [],             [0,0,0,0,0,0]],
    ['NORTHSIDE STREETS',               [],             [0,0,0,0,0,0]],
    ['DOWNTOWN STREETS',                [],             [0,0,0,0,0,0]],
    ['EASTTOWN STREETS',                [],             [0,0,0,0,0,0]],
    ['MERCHANT DISTRICT STREETS',       [],             [0,0,0,0,0,0]],
    ['RIVERTOWN STREETS',               [],             [0,0,0,0,0,0]],
    ['MISKATONIC UNIVERSITY STREETS',   [],             [0,0,0,0,0,0]],
    ['FRENCH HILL STREETS',             [],             [0,0,0,0,0,0]],
    ['UPTOWN STREETS',                  [],             [0,0,0,0,0,0]],
    ['SOUTHSIDE STREETS',               [],             [0,0,0,0,0,0]],
    ['OUTSKIRTS',                       [],             [0,0,0,0,0,0]],
    ['R\'LYEH',                         [],             [0,0,0,0,0,0]],
    ['PLATEAU OF LENG',                 [],             [0,0,0,0,0,0]],
    ['THE DREAMLANDS',                  [],             [0,0,0,0,0,0]],
    ['GREAT HALL OF CELEANO',           [],             [0,0,0,0,0,0]],
    ['YUGGOTH',                         [],             [0,0,0,0,0,0]],
    ['CITY OF THE GREAT RACE',          [],             [0,0,0,0,0,0]],
    ['ABYSS',                           [],             [0,0,0,0,0,0]],
    ['ANOTHER DIMENSION',               [],             [0,0,0,0,0,0]]
]

location_transforms = [
    [ 'name', 'occupants', 'status' ],
    [ 'CURIOSTIE SHOPPE', [], []],
    [ 'NEWSPAPER' , [], []],
    ['TRAIN STATION', [], []],
    ['ARKHAM ASYLUM', [], []],
    ['BANK OF ARKHAM', [], []],
    ['INDEPENDENCE SQUARE', [], []],
    ['HIBB\'S ROADHOUSE', [], []],
    ['POLICE STATION', [], []],
    ['JAIL CELL', [], []],
    ['VELMA\'S DINER', [], []],
    ['RIVER DOCKS', [], []],
    ['THE UNNAMABLE', [], []],
    ['UNVISITED ISLE', [], []],
    ['BLACK CAVE', [], []],
    ['GENERAL STORE', [], []],
    ['GRAVEYARD', [], []],
    ['ADMINISTRATION', [], []],
    ['SCIENCE BUILDING', [], []],
    ['LIBRARY', [], []],
    ['THE WITCH HOUSE', [], []],
    ['THE SILVER TWILIGHT LODGE', [], []],
    ['THE INNER SANCTUM', [], []],
    ['ST. MARY\'S HOSPITAL', [], []],
    ['WOODS', [], []],
    ['YE OLDE MAGICK SHOPPE', [], []],
    ['MA\'S BOARDING HOUSE', [], []],
    ['HISTORICAL SOCIETY', [], []],
    ['SOUTH CHURCH', [], []],
    ['NORTHSIDE STREETS', [], []],
    ['DOWNTOWN STREETS', [], []],
    ['EASTTOWN STREETS', [], []],
    ['MERCHANT DISTRICT STREETS', [], []],
    ['RIVERTOWN STREETS', [], []],
    ['MISKATONIC UNIVERSITY STREETS', [], []],
    ['FRENCH HILL STREETS', [], []],
    ['UPTOWN STREETS', [], []],
    ['SOUTHSIDE STREETS', [], []],
    ['OUTSKIRTS', [], []],
    ['R\'LYEH', [], []],
    ['PLATEAU OF LENG', [], []],
    ['THE DREAMLANDS', [], []],
    ['GREAT HALL OF CELEANO', [], []],
    ['YUGGOTH', [], []],
    ['CITY OF THE GREAT RACE', [], []],
    ['ABYSS', [], []],
    ['ANOTHER DIMENSION', [], []]
]

def add_occupant( vector, occupant ):
    return vector + [ occupant ]

def remove_occupant( vector, occupant ):
    return vector[:vector.index(occupant)] + vector[vector.index(occupant)+1:]

def inc_clue( vector ):
    return [ v + 1 if n == 0 else v for n,v in enumerate(vector) ]

def dec_clue( vector ):
    return [ v - 1 if n == 0 else v for n,v in enumerate(vector) ]

def inc_historical_clues( vector ):
    return [ v + 1 if n == 1 else v for n,v in enumerate(vector) ]

def add_seal( vector ):
    return [ v + 1 if n == 2 else v for n,v in enumerate(vector) ]

def remove_seal( vector ):
    return [ v - 1 if n == 2 else v for n,v in enumerate(vector) ]

def add_gate( vector ):
    return [ v + 1 if n == 3 else v for n,v in enumerate(vector) ]

def remove_gate( vector ):
    return [ v - 1 if n == 3 else v for n,v in enumerate(vector) ]

def mark_explored( vector ):
    return [ v + 1 if n == 4 else v for n,v in enumerate(vector) ]

def mark_unexplored( vector ):
    return [ v - 1 if n == 4 else v for n,v in enumerate(vector) ]

def mark_closed( vector ):
    return [ v + 1 if n == 5 else v for n,v in enumerate(vector) ]

def mark_open( vector ):
    return [ v + 1 if n == 5 else v for n,v in enumerate(vector) ]

def current_location_occupants( vector, transformations):
    location = vector
    for transformation, occupant in transformations:
        location = transformation( location, occupant )
    return location

def current_location_status( vector, transformations ):
    location = vector
    for transformation in transformations:
        location = transformation( location )
    return location


# validators

def location_clues_constraint( matrix, next_transform, prev_transforms ):
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
    transformed_matrix = next_transform( current_location_status( matrix, prev_transforms) )
    # can't be less than 0 or on a location with a gate or a seal
    if transformed_matrix[0] >= 0 and transformed_matrix[2] != 1 and transformed_matrix[3] != 1:
        return 1
    elif transformed_matrix[1] == 1:
        return -1
    elif transformed_matrix[2] == 1:
        return -2
    else:
        return 0
    
def location_seal_constraint( matrix, next_transform, prev_transforms ):
    """
        SEALS ON LOCATIONS
        A gate cannot open on a sealed location. Sealed locations may become unsealed by 
            way of various game effects.
        This stat exists in {0,1} where 0 is unsealed and 1 is sealed.
    """
    transformed_matrix = next_transform( current_location_status( matrix, prev_transforms) )
    # has to be 0 or 1
    if 0 <= transformed_matrix[2] <= 1:
        return True
    else:
        return False
    
def location_gate_constraint( matrix, next_transform, prev_transforms ):
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
    transformed_matrix = next_transform( current_location_status( matrix, prev_transforms) )
    if transformed_matrix[3] < 0:
        return 0
    elif 0 <= transformed_matrix[3] <= 1:
        return 1
    elif 1 < transformed_matrix[3]:
        return 2

def location_explored_constraint( matrix, next_transform, prev_transforms ):
    """
        EXPLORED GATE AT LOCATION
        If a location is marked as having been explored, any investigator who is at that location
            may attempt to close or seal the gate that is at the location. Once an investigator 
            leaves that location, it is no longer considered 'explored.' 
        A location is said to have been explored if an Investigator arrives there from an Other 
            World. 
        This stat exists in {0,1} where 0 is not explored, and 1 is explored.
    """
    transformed_matrix = next_transform( current_location_status( matrix, prev_transforms) )
    # has to be 0 or 1
    if 0 <= transformed_matrix[4] <= 1:
        return True
    else:
        return False
    
def location_closed_constraint( matrix, next_transform, prev_transforms ):
    """
        CLOSED LOCATIONS
        Locations can close for a number of reasons, but commonly because of Terror Track effects.
            If an Investigator travels to a location that is closed, their encounter there will 
            be a Sneak[-1] check. With 1 success they will gain one of the two resources that 
            location has to offer. With 2 successes they will gain both resources the location offers.
            With 0 successes, a Luck[-1] check will occur; on a failure, the Investigator is ARRESTED.
        This stat exists in {0,1} with 0 being open for business, and 1 being closed.
    """
    transformed_matrix = next_transform( current_location_status( matrix, prev_transforms) )
    # has to be 0 or 1
    if 0 <= transformed_matrix[5] <= 1:
        return True
    else:
        return False
    