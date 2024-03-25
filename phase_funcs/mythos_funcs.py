from context import Context
import math, random
import tools, currency, constraints, params, transformers
from tools import debugger as db, Table, current_locations_desc

from icecream import ic

def choose_random_location( context: Context, weight_formula: str, exclusion=None ):
    """ Returns a random location based on the weight formula provided, excluding any listed locations """

    return tools.rand_from_distro( { constants.name:eval( weight_formula ) for constants in context.locations.constants if constants.name != exclusion } )

def choose_gate_location( context: Context ):
    """ Randomly selects a location for a gate based on instability, current clues, and historical clues """

    return choose_random_location( context, params.GATE_SPAWN )

def choose_gate_to( context: Context ):
    return tools.rand_from_distro( currency.gate_freqs( context.gates.deck_defaults, context.gates.deck_transforms) )

def choose_clue_location( context: Context, exclusion: str ):
    """ Randomly selects a location for a clue based on instability, current clues, and historical clues """

    return choose_random_location( context, params.CLUE_SPAWN, exclusion )

def spawn_gate( gate_limit: int ):

    def spawn_gate_protocol( context: Context, location, gate ):
        db( 2 )
        # inc gates in arkham
        context.board.transforms['gates_in_arkham'] += [ transformers.inc_gates_in_arkham ]
        # add gate to location and inc historical gate count
        context.locations.transforms.row( location ).status += [ transformers.add_gate, transformers.inc_historical_gates ]
        context.locations.transforms.row( location ).gate_to += [ (transformers.add_gate_to, gate) ]
        
        print( f'Something strange suddenly appeared at {location}! Better get there quickly! \n' )

        return True
    
    if gate_limit == 1:
        return spawn_gate_protocol
    
    return None

def spawn_clue( clue_limit ):
    
    def spawn_clue_protocol( context: Context, location ):
        db( 2 )
        # add clue to location and inc historical clue count
        context.locations.transforms.row( location ).status += [ transformers.inc_loc_clues, transformers.inc_historical_clues ]
        
        msgs = [
            f'A stranger mentions there might be something of interest to you at {location} \n',
            f'You\'ve been given a lead! Head to {location}, and perhaps there will be something interesting... \n',
            f'Rumors circulate. You might want to check out {location} for a CLUE... \n'
        ]

        print( random.choice( msgs ) )

    if not clue_limit:
        return spawn_clue_protocol
    return None

def spawn_doom( doom_limit ):
    
    def spawn_doom_protocol( context: Context ):
        db( 2 )
        context.board.transforms['doom_track'] += [ transformers.inc_doom_track ]

        print( f'...a sense of doom grows ever more in the town of Arkham... \n' )

    if not doom_limit: 
        return spawn_doom_protocol
    
    return None

def spawn_terror( terror_limit ):

    def spawn_terror_protocol( context: Context ):
        db( 2 )
        # randomly select ally
        ally = tools.rand_from_distro( 
            currency.deck_frequency(
                context.allies.deck_defaults,
                context.allies.deck_transforms
            )
        )
        # remove that ally from the deck
        if ally:
            context.allies.deck_transforms += [ (transformers.dec_freq, ally) ]
        # increase doom track
        context.board.transforms['terror_track'] += [ transformers.inc_terror_track ]
        # close businesses
        def close_business( business ):
            if constraints( context.locations.defaults.row( business ).status, transformers.add_closed, context.locations.transforms.row( business ).status ):
                context.locations.transforms.row( business ).status += [ transformers.add_closed ]
                print( f'{business} has closed up shop! The terror in Arkham is too much for some \n' )

        if terror_limit == 4:
            # close magick shoppe
            close_business( 'YE OLDE MAGICK SHOPPE' )
        if terror_limit == 3:
            # close curio
            close_business( 'CURIOSITIE SHOPPE' )
        if terror_limit == 2:
            # close general store
            close_business( 'GENERAL STORE' )

    if not terror_limit:
        return spawn_terror_protocol
    
    return 

def spawn_monster_in_arkham( monster_limit: int ):

    def spawn_monster_in_arkham_protocol( context: Context, location ):
        db( 2 )
        # randomly select monster
        monster = tools.rand_from_distro( 
            currency.deck_frequency( 
                context.monsters.deck_defaults,
                context.monsters.deck_transforms
            )
        ) 
        db( 2, monster )
        # place monster in location
        context.locations.transforms.row( location ).occupants += [ (transformers.add_occupant, monster) ]
        # reduce freq of monster
        context.monsters.deck_transforms += [ ( transformers.dec_freq, monster ) ]
        # increase monsters in arkham count
        context.board.transforms['monsters_in_arkham'] += [ transformers.inc_monster_count ]
        # update current frame context 
        context.locations.currents = current_locations_desc( context.locations.defaults, context.locations.transforms )
        return None
    
    if monster_limit == 1:
        return spawn_monster_in_arkham_protocol
    
    return None

def spawn_monster_in_outskirts( outskirts_limit: int ):

    def spawn_monster_in_outskirts_protocol( context: Context ):
        db( 2 )
        # increase monsters in outskirts count
        context.board.transforms['monsters_in_outskirts'] += [ transformers.inc_monster_count ]
        return None
    
    if outskirts_limit == 1:
        return spawn_monster_in_outskirts_protocol
    
    return None

def clue_factory( context: Context, new_clue ):
    # check clue constrains
    clue = spawn_clue(
        context.locations.currents.row( new_clue ).status.gate
    )
    if clue:
        # add clue to that location
        clue( context, new_clue )
    else:
        # there is a gate there, increase historical clues
        context.locations.transforms.row( new_clue ).status += [ transformers.inc_historical_clues ] 

def doom_factory( context: Context, callback=None, *args ):
    # check for doom constraints
    doom = spawn_doom(
        constraints.doom_track_constraint(
            context.board.defaults['doom_track'],
            transformers.inc_doom_track,
            context.board.transforms['doom_track']
        )
    )
    if doom:
        # doom limit not reached
        doom( context )
        # do spawn monster things
        if callback:
            callback( context, *args )
    else:
        # doom limit reached
        awaken_the_ancient_one( context )

def monster_factory( context: Context, num_monsters, locations ):
        """ Spawns monsters and calls for checks along the way """
        db( 2 )
        if num_monsters:
            # check monsters in arkham contraints
            spawn_in_arkham = spawn_monster_in_arkham(
                constraints.too_many_monsters_constraint( 
                    context.board.defaults['monsters_in_arkham'], 
                    transformers.inc_monster_count, 
                    context.board.transforms['monsters_in_arkham']
                )
            )
            if spawn_in_arkham:
                # monster limit not reached
                spawn_in_arkham( context, locations[-num_monsters] )
            else:
                # monster limit reached
                # check outskirts contraints
                spawn_in_outskirts = spawn_monster_in_outskirts(
                    constraints.outskirts_full_constraint( 
                        context.board.defaults['monsters_in_outskirts'], 
                        transformers.inc_outskirts_count, 
                        context.board.transforms['monsters_in_outskirts']
                    )
                )
                if spawn_in_outskirts:
                    # outskirts limit not reached
                    spawn_in_outskirts( context )
                else:
                    # outskirts limit reached
                    outskirts_full( context )
                    
            return monster_factory( context, num_monsters - 1, locations )

def terror_factory( context: Context ):
    db( 2 )
    terror_in_arkham = spawn_terror(
        constraints.terror_track_constraint(
            context.board.defaults['terror_track'],
            transformers.inc_terror_track,
            context.board.transforms['terror_track']
        )
    )

    if terror_in_arkham:
        # terror limit not reached
        terror_in_arkham( context )
    else:
        # terror track is full, spawn doom
        doom_factory( context )


    return None

def outskirts_full( context: Context ):
    db( 2 )
    # empty the outskirts
    tools.set_limit( 
        context.board.transforms['monsters_in_outskirts'], 
        transformers.dec_monster_count, 
        params.OUTSKIRTS_LIMIT, 
        x=len( currency.board_investigators( 
            context.board.defaults['investigators'], 
            context.board.transforms['investigators'] 
        ) )
    )
    # do terror track things
    terror_factory( context )

    return None

def monster_surge( context: Context, factory ):

    # get list of all the gate locations in arkham
    gates = []
    for location in context.locations.currents:
        if location.status.gate:
            gates += [location.name]
    # send those to the monster factory
    
    factory( context, len(gates), gates )

    return None
   
class MovementRules:

    def normal( context: Context, monster: str, location: Table.Row, adjacencies: Table, msg=True ):
        """ Normal monsters move once along their path """
        # find the adjacent location
        ## left_ and right_graphs are directed, so all locations only have 1 adjacency 
        adj_location = adjacencies[ adjacencies.row( location.name ).index( 1 ) ]
        # remove monster from starting location
        context.locations.transforms.row( location.name ).occupants += [ ( transformers.remove_occupant, monster ) ]
        # add monster to adjacent location
        context.locations.transforms.row( adj_location.name ).occupants += [ ( transformers.add_occupant, monster ) ]

        if msg:
            print( eval( random.choice( params.NORMAL_MOVE_MSGS ) ) )

        return adj_location
        
    def fast( context: Context, monster: str, location: Table.Row, adjacencies: Table):
        """ Fast monster immediately to two spots ahead, skipping the location in between """
        # square the adj table
        square = tools.matrix_square( adjacencies.headless )
        # put the head back on
        for row, loc in zip( square, adjacencies ):
            row.insert( 0, loc.name )
        square.insert( 0, adjacencies.table[0] )

        # normal moves but with squared matrix
        MovementRules.normal( context, monster, location, Table( square ) )

    def stationary( context: Context, monster: str, location: Table.Row, adjacencies: Table):
        """ Stationary monsters don't move, but will still cause a message to print """

        print( eval( random.choice( params.STATIONARY_MSGS ) ) )


    def flying( context: Context, monster: str, location: Table.Row, adjacencies: Table ):
        """ Flying monsters move into any adjacent street area only if there is an investigator there; otherwise they go to or stay in the sky"""

        adj_locations_indeces = [ i for i,v in enumerate( context.locations.graph.row( location.name ) ) if v == 1 ]

        for index in adj_locations_indeces:
            # no matter what, the monster is leaving its original location
            context.locations.transforms.row( location.name ).occupants += [ (transformers.remove_occupant, monster) ]
            # find investigators in these locations
            if len( context.locations.currents[index].investigators ):
                # move monster
                context.locations.transforms[index].occupants += [ (transformers.add_occupant, monster) ]
                print( 'A terrible monster is circling the skies over your head! Perhaps you should COMBAT it or even try to EVADE it?' )
                break
            else:
                # it flies into the sky
                context.locations.transforms.row( 'THE SKY' ).occupants += [ (transformers.add_occupant, monster) ]
                print( eval( random.choice( params.FLYING_MOVE_MSGS ) ) )
                break


    def chthonian( context: Context, monster: str, location: Table.Row, adjacencies: Table):
        """ The Chthonian rolls a die, and on a 1-3 increases damage to Investigators in Arkham """

        def investigators_in_arkham( names, locations ):
            for inv, loc in zip( names, locations ):
                if loc.in_arkham:
                    yield inv

        if tools.roll_die( 2 ):
            for inv in investigators_in_arkham( context.briefs.names, context.briefs.current_locations ):
                # inc_damage on inv
                context.briefs.transforms.row( inv ).damage += [ transformers.inc_current_damage ]
            

        print( 'An immense howling pierces through your very core!' )


    def hound( context: Context, monster: str, location: Table.Row, adjacencies: Table):
        """ 
            The Hound of Tindalos makes their way to the nearest investigator location. 
            The way I will accomplish this ( for now ) is by moving the monster "normally" 
            until it reaches a street location with an adjacent investigator. If there are  
            at least two Investigators adjacent to the Hound, the investigator with the 
            lowest sneak will be targeted. If there is a tie, the location is chosen randomly. 
            This will only occur when there are investigators in Arkham.
        """

        def move_hound( hound_location ):

            # first check to see if there are investigators in adjacent locations
            adj_locations_indeces = [ i for i,v in enumerate( context.locations.graph.row( hound_location.name ) ) if v == 1 ]        
            potential_targets = [ ]
    
            for index in adj_locations_indeces:
                if len( context.locations.currents[index].investigators ):
                    potential_targets += context.locations.currents[index].investigators

            if not len( potential_targets ):
                # nobody nearby, move along
                next_location = MovementRules.normal( context, monster, hound_location, adjacencies, msg=False )
                # try again
                return move_hound( next_location )
            
            # otherwise, 
            lowest_sneak = min( [ currency.investigator_complement_skill( context.briefs.defaults.row( inv ).speed, context.briefs.transforms.row( inv ).speed ) for inv in potential_targets ] )
            targets = [ inv for inv in potential_targets if currency.investigator_complement_skill( context.briefs.defaults.row( inv ).speed, context.briefs.transforms.row( inv ).speed ) <= lowest_sneak ]
            # randomly select from amongst the targets
            target = random.choice( targets ) 
            target_location = currency.investigator_location( context.briefs.defaults.row( target ).location, context.briefs.transforms.row( target ).location ).current_location 
            
            # relocate monster
            context.locations.transforms.row( hound_location.name ).occupants += [ (transformers.remove_occupant, monster ) ]
            context.locations.transforms[ target_location ].occupants += [ (transformers.add_occupant, monster) ]

            print( f'What is that coming out of the corner?? {target} has been stalked and there is now a horrible monster in their location!' )

        # check to see if there are any investigators in arkham right now
        if sum( [ loc.in_arkham for loc in context.briefs.current_locations ] ):
            move_hound( location )
            
           
    
    funcs = [
        normal,
        fast,
        stationary,
        flying,
        chthonian,
        hound
    ]

    def __iter__( self ):
        yield from self.funcs

    def __getitem__( self, index ):
        return self.funcs[ index ]


def move_monsters( context: Context ):
    db( 2 )
    # monsters move in groups
    left_group = tools.rand_from_distro( { group:1 for group in params.MVMT_GROUPS } )
    right_group = tools.rand_from_distro( { group:1 for group in params.MVMT_GROUPS if group != left_group } )

    ic( left_group, right_group )

    def find_monsters( group ):
        db( 2 )
        # filter for occupied locations
        for location in context.locations.currents.filter( 'occupants', [], "!="):
            for monster in location.occupants:
                if context.monsters.constants.row( monster ).dimension in group:
                    yield monster, location

    def move_protocols( group ):
        db( 2 )
        for monster, location in find_monsters( group ):
            # find movement ruleset
            yield monster, location, MovementRules()[ currency.monster_rulesets( 
                context.monsters.defaults.row( monster ).rulesets,
                context.monsters.transforms.row( monster ).rulesets,
            ).movement ]

    left_moves = [ ruleset for ruleset in move_protocols( left_group ) ]
    right_moves = [ ruleset for ruleset in move_protocols( right_group ) ]        

    ic( left_moves, right_moves )

    # move left monsters left
    for monster, location, ruleset in left_moves:
        ruleset( context, monster, location, context.locations.left_graph )
    # move right monsters right
    for monster, location, ruleset in right_moves:
        ruleset( context, monster, location, context.locations.right_graph )


def awaken_the_ancient_one( context: Context ):
    db( 2 )
    context.board.transforms['awakened'] += [ transformers.set_awakened ]

    
