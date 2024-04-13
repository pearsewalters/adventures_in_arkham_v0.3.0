import random
from tools import Table, roll_die, matrix_square
import currency, params, transformers

class MovementRules:

    def normal( context, monster: str, location: Table.Row, adjacencies: Table, msg=True ):
        """ Normal monsters move once along their path """
        # find the adjacent location
        ## left_ and right_graphs are directed, so all locations only have 1 adjacency 
        adj_location = adjacencies[ adjacencies.row( location.name ).index( 1 ) ]
        # remove monster from starting location
        context.locations.transforms.row( location.name ).occupants += [ ( transformers.removeOccupant, monster ) ]
        # add monster to adjacent location
        context.locations.transforms.row( adj_location.name ).occupants += [ ( transformers.addOccupant, monster ) ]

        if msg:
            print( eval( random.choice( params.NORMAL_MOVE_MSGS ) ) )

        return adj_location
        
    def fast( context, monster: str, location: Table.Row, adjacencies: Table):
        """ Fast monster immediately to two spots ahead, skipping the location in between """
        # square the adj table
        square = matrix_square( adjacencies.headless )
        # put the head back on
        for row, loc in zip( square, adjacencies ):
            row.insert( 0, loc.name )
        square.insert( 0, adjacencies.table[0] )

        # normal moves but with squared matrix
        MovementRules.normal( context, monster, location, Table( square ) )

    def stationary( context, monster: str, location: Table.Row, adjacencies: Table):
        """ Stationary monsters don't move, but will still cause a message to print """

        print( eval( random.choice( params.STATIONARY_MSGS ) ) )


    def flying( context, monster: str, location: Table.Row, adjacencies: Table ):
        """ Flying monsters move into any adjacent street area only if there is an investigator there; otherwise they go to or stay in the sky"""

        adj_locations_indeces = [ i for i,v in enumerate( context.locations.graph.row( location.name ) ) if v == 1 ]

        for index in adj_locations_indeces:
            # no matter what, the monster is leaving its original location
            context.locations.transforms.row( location.name ).occupants += [ (transformers.removeOccupant, monster) ]
            # find investigators in these locations
            if len( context.locations.currents[index].investigators ):
                # move monster
                context.locations.transforms[index].occupants += [ (transformers.addOccupant, monster) ]
                print( 'A terrible monster is circling the skies over your head! Perhaps you should COMBAT it or even try to EVADE it?' )
                break
            else:
                # it flies into the sky
                context.locations.transforms.row( 'THE SKY' ).occupants += [ (transformers.addOccupant, monster) ]
                print( eval( random.choice( params.FLYING_MOVE_MSGS ) ) )
                break


    def chthonian( context, monster: str, location: Table.Row, adjacencies: Table):
        """ The Chthonian rolls a die, and on a 1-3 increases damage to Investigators in Arkham """

        def investigators_in_arkham( names, locations ):
            for inv, loc in zip( names, locations ):
                if loc.in_arkham:
                    yield inv

        if roll_die( 2 ):
            for inv in investigators_in_arkham( context.briefs.names, context.briefs.current_locations ):
                # inc_damage on inv
                context.briefs.transforms.row( inv ).damage += [ transformers.inc_current_damage ]
            

        print( 'An immense howling pierces through your very core!' )


    def hound( context, monster: str, location: Table.Row, adjacencies: Table):
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
            lowest_sneak = min( [ currency.investigatorComplementSkill( context.briefs.defaults.row( inv ).speed, context.briefs.transforms.row( inv ).speed ) for inv in potential_targets ] )
            targets = [ inv for inv in potential_targets if currency.investigatorComplementSkill( context.briefs.defaults.row( inv ).speed, context.briefs.transforms.row( inv ).speed ) <= lowest_sneak ]
            # randomly select from amongst the targets
            target = random.choice( targets ) 
            target_location = currency.investigatorLocation( context.briefs.defaults.row( target ).location, context.briefs.transforms.row( target ).location ).current_location 
            
            if target_location in { 4, 23 }:
                # if that location is the hospital or asylum, move along
                next_location = MovementRules.normal( context, monster, hound_location, adjacencies, msg=False )
                # try again
                return move_hound( next_location )

            # relocate monster
            context.locations.transforms.row( hound_location.name ).occupants += [ (transformers.removeOccupant, monster ) ]
            context.locations.transforms[ target_location ].occupants += [ (transformers.addOccupant, monster) ]

            print( f'What is that coming out of the corner?? {target} has been stalked and there is now a horrible monster in their location!' )

        # check to see if there are any investigators in arkham right now, and if they are only in the hospital or asylum
        stalk = 0
        for loc in context.briefs.current_locations:
            if loc.in_arkham and loc.current_location != 4 and loc.current_location != 23:
                stalk += 1
        
        if stalk: 
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