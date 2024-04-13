from classes.data import Investigator
from classes.context import Context
from typing import Callable
from phaseFuncs import movementFuncs
from tools import debugger as db

def onGate( location: Investigator.location ) -> Callable | None:

    def onGateProtocol( context: Context ) -> None:
        db( 2 )
        # this is actually the same procedure as movementFuncs.inOtherWorld
        movementFuncs.inOtherWorld( context )

    if location.inArkham:
        return onGateProtocol
    return None