import investigator, ancient_ones, random
from icecream import ic

def choose_random_investigator(  ):
    """Randomy chooses an investigator for the player"""
    player_character = random.randrange( len(investigator.investigator_constants[1:]) )
    print( f'You are playing as {investigator.investigator_constants[player_character][0]} {investigator.investigator_constants[player_character][2]}')
    return 

def choose_non_random_investigator(  ):
    """Prints out a list of investigators and gets player selection"""
    print( '\nYou may select from these Investigators... \n')
    option = 1
    for row in investigator.investigator_constants[1:]:
        print( f'({option}) {row[0]}, {row[2]}' )
        option +=1
    while True:
        player_character = int( input( f'Enter your preferred Investigator (1-{option-1}) >>> ' ) )
        if 1 > player_character > option - 1:
            print( 'Try again...')
        else:
            break
    print( f'You are playing as {investigator.investigator_constants[player_character][0]} {investigator.investigator_constants[player_character][2]}')
    return 
        
def choose_random_ancient_one(  ):
    """Randomly chooses an ancient one for the player"""
    ancient_one = random.randrange( len(ancient_ones.ancient_one_constants[1:])) + 1
    print( f'Evil awaits you. You will be facing {ancient_ones.ancient_one_constants[ancient_one][0]}, {ancient_ones.ancient_one_constants[ancient_one][1]}')
    return 
    
def choose_non_random_ancient_one(  ):
    """Prints out a list of Ancient Ones and gets player selection"""
    print( '\nYou may select from these Ancient Ones... \n' )
    option = 1
    for row in ancient_ones.ancient_one_constants[1:]:
        print( f'({option}) {row[0]}, {row[1]}' )
        option += 1
    while True:
        ancient_one = int( input( f'\nEnter your preferred Ancient One (1-{option-1}) >>> ' ) )
        if 1 > ancient_one > option - 1:
            print( 'Hmm... Something isn\'t right. Try again')
            continue
        else:
            break
    print( f'Evil awaits you. You will be facing {ancient_ones.ancient_one_constants[ancient_one][0]}, {ancient_ones.ancient_one_constants[ancient_one][1]}')
    return 


            
    




# select investigator

def select_investigator(  ):
    print( "Would you like to (1) play as a random Investigator or (2) choose your Investigator?" )
    while True:
        random_investigator = int( input('Please enter 1 or 2 >>> ') )
        if random_investigator == 1:
            choose_random_investigator(  )
            break
        elif random_investigator == 2:
            choose_non_random_investigator(  )
            break
        print( 'Hmm... not sure that\'s correct. Try again.')
        continue
    return 

# select ancient one
def select_ancient_one(  ):
    print( "Would you like to (1) let fate decide your doom, or (2) choose your Ancient foe?")
    while True:
        random_ancient_one = int( input('Please enter 1 or 2 >>> ' ) )
        if random_ancient_one == 1:
            choose_random_ancient_one()
            break
        elif random_ancient_one == 2:
            choose_non_random_ancient_one()
            break
        print( 'Hmm... not sure that\'s correct. Try again.')
        continue
     

class Procedure:
    def __init__( self, name, *steps ):
        self.__name__ = name
        self._steps = list(steps)
        self._current_step = 0
    
    def __name__( self ):
        return self.__name__

    def __len__( self ):
        return len( self._steps )
    
    def __iter__( self ):
        while self._current_step < len( self ):
            yield self._steps[ self._current_step ]
            self._current_step += 1
        self._current_step = 0

    def insert_step( self, step, index ):
        self._steps.insert( index, step )
    
    def execute( self, start=0 ):
        self._current_step = start
        for step in self:
            try:
                if type( step ) == Procedure:
                    step.execute()
                else:
                    step()
            except: 
                raise TypeError( 'Wrong type of step supplied for Procedure. Only Procedures and functions accepted.' )

    def reset( self, start=0 ):
        self._current_step = start - 1
    
    
# begin setup 
def begin_setup():
    print( "\n"*2, " "*16, "Welcome to Arkham" ),
    print( '~'*(16+17+16), "\n"*2 )

def confirm_setup():
    while True:
        confirm = input( 'Confirm selection? y/n >>> ' ).upper()
        if confirm == 'Y':
            print( 'Away we go!', '\n', 'Beginning game...')
            return 
        elif confirm == 'N':
            print( 'We\'ll try it from the top.' )
            setup.reset()
            break
        else:
            print( 'Hmm... unclear. Try again.' )
    

def monster_surge():
    print( 'Monster surge' )

def spawn_gate():
    # test for valid transform
    if True:
        mythos.insert_step( monster_surge, 1 )
    print( 'Spawn gate' )

def spawn_clue():
    print( 'Spawn clue' )

def move_monsters():
    print( 'Move monsters' )

def mythos_effect():
    print( 'Mythos effect' )

def upkeep_things():
    print( 'doing upkeep now')

upkeep = Procedure(
    'upkeep',
    upkeep_things
)

mythos = Procedure(
    'mythos',
    spawn_gate,
    spawn_clue,
    move_monsters,
    mythos_effect
)

setup = Procedure(
    'setup',
    begin_setup,
    select_investigator,
    select_ancient_one,
    confirm_setup
)



while True:
    # move setup to outside of game loop since it should only happen once
    setup.execute()
    mythos.execute()
    upkeep.execute()


    

    
