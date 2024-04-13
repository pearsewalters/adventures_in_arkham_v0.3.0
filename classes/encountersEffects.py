from classes.context import Context
from typing import Callable
import constraints, currency, transformers
import params
from tools import debugger as db, clobber, randFromDistro

def drawCards( deck: dict, numCards=1 ) -> tuple:
    """ Returns a tuple of card of cards from a provided deck """

    def draw( d, n, drawn=None ):
        drawnCards = [ ]
        if numCards - 1:
            drawnCards += draw( d, n - 1, drawn=drawnCards )
        drawnCards += [ randFromDistro( { k:v-1 if k in drawnCards else v for k,v in deck.items() } ) ]
        return drawnCards
    
    return draw( deck, numCards )

    
        
class specialEffects:

    def administration( context: Context ) -> Callable | None:

        def skillsFromAdministration( context: Context ) -> None:
            """ Randomly select 2 skills """

            isDeckDiver = True if context.investigator.ability.variety == "deckDiver" else False
            correctPhase = True if currency.boardCurrentPhase( context.board.defaults['currentPhase'], context.board.transforms['currentPhase'] ) in context.investigator.ability.phase else False
            fromLearnedDeck = True if context.investigator.ability.deck == "learned" else False
            extraDraw = context.investigator.ability.amt 

            # draw skills
            if isDeckDiver and correctPhase and fromLearnedDeck:
                drawCards( clobber( context, "learned" ), 2 + extraDraw )
            else:
                drawCards( clobber( context, "learned" ), 2 )
            
            


            

        if context.investigator.possessions['money'] >= params.SKILLS_DOLLAR_COST:
            return skillsFromAdministration
        
        return None


    def southChurch( context: Context ) -> Callable | None:
        db( 3 )

        def blessingFromSouthChurch( context: Context ) -> None:
            # deduct the cost, prioritizing gates first
            if context.investigator.possessions['gateTrophies'] >= params.BLESSING_GATE_COST:
                context.investigator.transforms.possessions += [ transformers.decGateTrophies ] * params.BLESSING_GATE_COST
            elif context.investigator.possessions['monsterTrophies'] >= params.BLESSING_MONSTER_COST:
                context.investigator.transforms.possessions += [ transformers.decMonsterTrophies ] * params.BLESSING_MONSTER_COST

            # add blessing
            context.investigator.transforms.conditions += [ transformers.addBlessing ]


        # check if investigator has 5 monster trophies or 1 gate trophy and investigator isn't already blessed
        if (context.investigator.possessions['monsterTrophies'] >= params.BLESSING_MONSTER_COST or context.investigator.possessions['gateTrophies'] >= params.BLESSING_GATE_COST ) and context.investigator.conditions.blessedCursed <= 0:
            return blessingFromSouthChurch
        
        return None