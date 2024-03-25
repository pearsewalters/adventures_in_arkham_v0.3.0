from context import Context
import tools, transformers

def azathoth_rules( context: Context ):
    """Apply ancient one rules for Azathoth"""
   
    # maniacs have their toughness increased by 1
    context.monsters.transforms.row('MANIAC').stats += [ transformers.inc_toughness]
    
    # doom track is set to 14
    tools.set_limit( context.board.transforms['doom_track'], transformers.dec_doom_track, 14 )
    
RULES = {
    'AZATHOTH' : azathoth_rules
}
