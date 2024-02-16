
import csv

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
    other_worlds = [ 'R\'LYEH','PLATEAU OF LENG','THE DREAMLANDS','GREAT HALL OF CELEANO','YUGGOTH','CITY OF THE GREAT RACE','ABYSS','ANOTHER DIMENSION']
    # add labels the first row
    arkham[0] += other_worlds 
    no_adjacencies = [ 0 for _ in arkham[0][1:]]
    # add new rows with labels in the first column
    for w in other_worlds:
        arkham.append( [w] + no_adjacencies )

    return arkham


# locations data

location_constants = [
    [ 'name', 'neighborhood', 'variety','special','guaranteed','possible','stability']
    [ 'CURIOSTIE SHOPPE', 'NORTHSIDE', 'LOCATION', True, 'unique items','common items',True],          
    [ 'NEWSPAPER', 'NORTHSIDE', 'LOCATION', False, None, 'money,clues', True],
    ['TRAIN STATION', 'NORTHSIDE', 'LOCATION', False, None, 'common items,unique items', True],
    ['ARKHAM ASYLUM', 'DOWNTOWN', 'LOCATION', True, 'sanity', 'common items', True],
    ['BANK OF ARKHAM', 'DOWNTOWN', 'LOCATION', True, 'money', 'blessing', True ],
    ['INDEPENDENCE SQUARE', 'DOWNTOWN', 'LOCATION', False, None, 'common items,unique items', False ],
    ['HIBB\'S ROADHOUSE','EASTTOWN', 'LOCATION', False, None, 'money,common items', False ],
    ['POLICE STATION', 'EASTTOWN', 'LOCATION', True, None, 'common items,clues', True],
    ['JAIL CELL', 'EASTTOWN', 'LOCATION', False, None, None, True],
    ['VELMA\'S DINER', 'EASTTOWN', 'LOCATION', False, None, 'money,stamina', True],
    ['RIVER DOCKS','MERCHANT DISTRICT', 'LOCATION', True, 'money','common items',True ],
    ['THE UNNAMABLE', 'MERCHANT DISTRICT', 'LOCATION', False, None, 'unique items,clues', False],
    ['UNVISITED ISLE', 'MERCHANT DISTRICT', 'LOCATION', False, None, 'clues,spells',False],
    ['BLACK CAVE', 'RIVERTOWN', 'LOCATION', False,None,'common items,spells',False],
    ['GENERAL STORE', 'RIVERTOWN', 'LOCATION', True,'common items','money',True],
    ['GRAVEYARD', 'RIVERTOWN', 'LOCATION', True, None,'clues,unique items',False],
    ['ADMINISTRATION', 'MISKATONIC UNIVERSITY', 'LOCATION', True, 'skills','money', True],
    ['SCIENCE BUILDING', 'MISKATONIC UNIVERSITY', 'LOCATION', True, 'clues','unique items',False],
    ['LIBRARY', 'MISKATONIC UNIVERSITY', 'LOCATION', False, None,'unique items,clues', False],
    ['THE WITCH HOUSE', 'FRENCH HILL', 'LOCATION', False, None, 'clues,spells', False], 
    ['THE SILVER TWILIGHT LODGE', 'FRENCH HILL', 'LOCATION', True, None, 'unique items,clues',False],
    ['THE INNER SANCTUM', 'FRENCH HILL', 'LOCATION', False, None, None, True], # Inner Sanctum won't ever have a gate on it, since it's only adjacent to the Lodge
    ['ST. MARY\'S HOSPITAL', 'UPTOWN', 'LOCATION', True, 'stamina','clues',True],
    ['WOODS', 'UPTOWN', 'LOCATION', False, None,'money,common items',False],
    ['YE OLDE MAGICK SHOPPE', 'UPTOWN', 'LOCATION', True, 'spells','unique items',True],
    ['MA\'S BOARDING HOUSE', 'SOUTHSIDE', 'LOCATION', True, 'allies','stamina',True],
    ['HISTORICAL SOCIETY', 'SOUTHSIDE', 'LOCATION', False, None,'skills,spells',False],
    ['SOUTH CHURCH', 'SOUTHSIDE', 'LOCATION', True, 'blessing','sanity',True],
    ['NORTHSIDE STREETS', 'NORTHSIDE', 'STREETS', False, None, None, None],
    ['DOWNTOWN STREETS', 'DOWNTOWN', 'STREETS', False, None, None, None],
    ['EASTTOWN STREETS', 'EASTTOWN', 'STREETS', False, None, None, None],
    ['MERCHANT DISTRICT STREETS', 'MERCHANT DISTRICT', 'STREETS', False, None, None, None],
    ['RIVERTOWN STREETS', 'RIVERTOWN', 'STREETS', False, None, None, None],
    ['MISKATONIC UNIVERSITY STREETS', 'MISKATONIC UNIVERSTITY', 'STREETS', False, None, None, None],
    ['FRENCH HILL STREETS', 'FRENCH HILL', 'STREETS', False, None, None, None],
    ['UPTOWN STREETS', 'UPTOWN', 'STREETS', False, None, None, None],
    ['SOUTHSIDE STREETS', 'SOUTHSIDE', 'STREETS', False, None, None, None],
    ['OUTSKIRTS', 'OUTSKIRTS', 'SPECIAL', False, None, None, None],
    ['R\'LYEH', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['PLATEAU OF LENG', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['THE DREAMLANDS', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['GREAT HALL OF CELEANO', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['YUGGOTH', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['CITY OF THE GREAT RACE', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['ABYSS', 'OTHER WORLD', 'OTHER WORLD', False, None, None, None],
    ['ANOTHER DIMENSION', 'OTHER WORLD', 'OTHER WORLD, False, None, None, None']
]

location_defaults = [
    [ 'name', 'occupants', 'status' ],
    [ 'CURIOSTIE SHOPPE', [], [0,0,0,0,0]],
    [ 'NEWSPAPER' , [], [0,0,0,0,0]],
    ['TRAIN STATION ', [], [0,0,0,0,0]],
    ['ARKHAM ASYLUM ', [], [0,0,0,0,0]],
    ['BANK OF ARKHAM ', [], [0,0,0,0,0]],
    ['INDEPENDENCE SQUARE ', [], [0,0,0,0,0]],
    ['HIBB\'S ROADHOUSE ', [], [0,0,0,0,0]],
    ['POLICE STATION ', [], [0,0,0,0,0]],
    ['JAIL CELL', [], [0,0,0,0,0]],
    ['VELMA\'S DINER', [], [0,0,0,0,0]],
    ['RIVER DOCKS', [], [0,0,0,0,0]],
    ['THE UNNAMABLE', [], [0,0,0,0,0]],
    ['UNVISITED ISLE', [], [0,0,0,0,0]],
    ['BLACK CAVE', [], [0,0,0,0,0]],
    ['GENERAL STORE', [], [0,0,0,0,0]],
    ['GRAVEYARD', [], [0,0,0,0,0]],
    ['ADMINISTRATION', [], [0,0,0,0,0]],
    ['SCIENCE BUILDING', [], [0,0,0,0,0]],
    ['LIBRARY', [], [0,0,0,0,0]],
    ['THE WITCH HOUSE', [], [0,0,0,0,0]],
    ['THE SILVER TWILIGHT LODGE', [], [0,0,0,0,0]],
    ['THE INNER SANCTUM', [], [0,0,0,0,0]],
    ['ST. MARY\'S HOSPITAL', [], [0,0,0,0,0]],
    ['WOODS', [], [0,0,0,0,0]],
    ['YE OLDE MAGICK SHOPPE', [], [0,0,0,0,0]],
    ['MA\'S BOARDING HOUSE', [], [0,0,0,0,0]],
    ['HISTORICAL SOCIETY', [], [0,0,0,0,0]],
    ['SOUTH CHURCH', [], [0,0,0,0,0]],
    ['NORTHSIDE STREETS', [], [0,0,0,0,0]],
    ['DOWNTOWN STREETS', [], [0,0,0,0,0]],
    ['EASTTOWN STREETS', [], [0,0,0,0,0]],
    ['MERCHANT DISTRICT STREETS', [], [0,0,0,0,0]],
    ['RIVERTOWN STREETS', [], [0,0,0,0,0]],
    ['MISKATONIC UNIVERSITY STREETS', [], [0,0,0,0,0]],
    ['FRENCH HILL STREETS', [], [0,0,0,0,0]],
    ['UPTOWN STREETS', [], [0,0,0,0,0]],
    ['SOUTHSIDE STREETS', [], [0,0,0,0,0]],
    ['OUTSKIRTS', [], [0,0,0,0,0]],
    ['R\'LYEH', [], [0,0,0,0,0]],
    ['PLATEAU OF LENG', [], [0,0,0,0,0]],
    ['THE DREAMLANDS', [], [0,0,0,0,0]],
    ['GREAT HALL OF CELEANO', [], [0,0,0,0,0]],
    ['YUGGOTH', [], [0,0,0,0,0]],
    ['CITY OF THE GREAT RACE', [], [0,0,0,0,0]],
    ['ABYSS', [], [0,0,0,0,0]],
    ['ANOTHER DIMENSION', [], [0,0,0,0,0]]
]

def add_occupant( matrix, occupant ):
    return matrix + [ occupant ]

def remove_occupant( matrix, occupant ):
    return matrix[:matrix.index(occupant)] + matrix[matrix.index(occupant)+1:]

def inc_clue( matrix ):
    return [ matrix[0]+1, matrix[1], matrix[2], matrix[3], matrix[4] ]

def dec_clue( matrix ):
    return [ matrix[0]-1, matrix[1], matrix[2], matrix[3], matrix[4] ]

def add_seal( matrix ):
    return [ matrix[0], matrix[1]+1, matrix[2], matrix[3], matrix[4] ]

def remove_seal( matrix ):
    return [ matrix[0], matrix[1]-1, matrix[2], matrix[3], matrix[4] ]

def add_gate( matrix ):
    return [ matrix[0], matrix[1], matrix[2]+1, matrix[3], matrix[4] ]

def remove_gate( matrix ):
    return [ matrix[0], matrix[1], matrix[2]-1, matrix[3], matrix[4] ]

def mark_explored( matrix ):
    return [ matrix[0], matrix[1], matrix[2], matrix[3]+1, matrix[4] ]

def mark_unexplored( matrix ):
    return [ matrix[0], matrix[1], matrix[2], matrix[3]-1, matrix[4] ]

def mark_closed( matrix ):
    return [ matrix[0], matrix[1], matrix[2], matrix[3], matrix[4]+1 ]

def mark_open( matrix ):
    return [ matrix[0], matrix[1], matrix[2], matrix[3], matrix[4]-1 ]
