
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