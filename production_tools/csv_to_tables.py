import csv

# this will be the initial investigator data table
investigator_defaults = [ [ 'name','damage','horror','conditions','focus','speed','fight','lore','location','random_possessions','equipped_items','exhausted_items','possessions'] ]

# open the csv file
file = open( 'investigator_defaults.csv' )
# convert the csv to a 2d array
t = csv.reader( file )
table = [ row for row in t ]
# close the csv file
file.close()

# add rows to default
for row in table[1:]:
    investigator_defaults.append( [ row[0] ] )

# add columns to defaults
for i in range( len( table[1:] ) ) :
    # damage
    investigator_defaults[i+1].append( [ table[i+1][1], 0, 0 ] )
    # horror
    investigator_defaults[i+1].append( [ table[i+1][2], 0, 0 ] )
    # condtions
    investigator_defaults[i+1].append( [ table[i+1][3], table[i+1][4], table[i+1][5], table[i+1][6], table[i+1][7], table[i+1][8], table[i+1][9], table[i+1][10] ] )
    # focus
    investigator_defaults[i+1].append( [ table[i+1][11] , table[i+1][11] , 0 ] )
    # speed/sneak
    investigator_defaults[i+1].append( [ table[i+1][12], table[i+1][12], table[i+1][13] ] )
    # fight/lore
    investigator_defaults[i+1].append( [ table[i+1][14], table[i+1][14], table[i+1][15] ] )
    # lore/luck
    investigator_defaults[i+1].append( [ table[i+1][16], table[i+1][16], table[i+1][17] ] )
    # locational
    investigator_defaults[i+1].append( [ table[i+1][18], 0, table[i+1][19] ] )
    # random possessions
    investigator_defaults[i+1].append( [ table[i+1][20], table[i+1][21], table[i+1][22], table[i+1][23] ] )
    # equipment
    investigator_defaults[i+1].append( [ table[i+1][24], [] ] )
    # fixed possessions
    investigator_defaults[i+1].append( 
        { 
            'money' : int( table[i+1][25] ), 
            'clues' : int( table[i+1][26] ), 
            'gate_trophies' : 0, 
            'monster_trophies' : 0, 
            'common' : [ w.strip() for w in table[i+1][27].split(',') ], 
            'unique' : [ w.strip() for w in table[i+1][28].split(',') ], 
            'spells' : [ w.strip() for w in  table[i+1][29].split(',') ], 
            'buffs' : [ w.strip() for w in  table[i+1][30].split(',') ], 
            'allies' : [ w.strip() for w in  table[i+1][31].split(',') ]  
        })

 # convert 'int' to int
for row in investigator_defaults[1:]:
    for i in range(1,10):
        row[i] = [ int(num) for num in row[i] ]
    # equipment
    row[10] = [ int(num) if type(num) == str else num for num in row[10] ]
    # convert 'int' to in in the possessions dict
    for key in row[11]:
        if type( row[11][key] ) == str:
            row[11][key] = int( row[11][key] )  
        elif type( row[11][key] ) == list and row[11][key][0] == '':
            row[11][key] = []
        


