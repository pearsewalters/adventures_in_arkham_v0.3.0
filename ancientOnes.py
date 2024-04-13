import tools, transformers

def azathothRules( context ):
    """Apply ancient one rules for Azathoth"""
   
    # maniacs have their toughness increased by 1
    context.monsters.transforms.row('MANIAC').stats += [ transformers.incToughness ]
    
    # doom track is set to 14
    tools.setLimit( context.board.transforms['doomTrack'], transformers.decDoomTrack, 14 )
    
RULES = {
    'AZATHOTH' : azathothRules
}
