from tables import constants, defaults, transformations
from tools import Table
import currency

class Context:
    class Board:

        def __init__( self, phase, bookkeeping, win, gates_open, defs, trans ):
            self.phase = phase
            self.bookkeeping = bookkeeping
            self.win = win
            self.gates_open = gates_open
            self.defaults = defs
            self.transforms = trans
    
    class InvestigatorBriefs:
        def __init__( self, names, defs, trans ):
            self.names = names
            self.current_locations = [ currency.investigator_location( defs.row( inv ).location, trans.row( inv ).location ) for inv in self.names ]
            self.defaults = Table( [defs.table[0]] + [ defs.row( inv, bundled=False ) for inv in self.names ] )
            self.transforms = Table( [trans.table[0]] + [ trans.row( inv, bundled=False ) for inv in self.names ] )

    class Locations:
        def __init__( self, cons, defs, trans, currents, graph, left_graph, right_graph ):
            self.constants = cons
            self.defaults = defs
            self.transforms = trans
            self.currents = currents
            self.graph = graph
            self.left_graph = left_graph
            self.right_graph = right_graph

    class Deck:
        def __init__( self, cons, defs, trans, deck_defaults, deck_transforms ):
            self.constants = cons
            self.defaults = defs
            self.transforms = trans
            self.deck_defaults = deck_defaults
            self.deck_transforms = deck_transforms

    class Investigator:
        def __init__( self, name ):
            self.name = name
            self.constants = constants.investigators.row( name )
            self.defaults = defaults.investigators.row( name )
            self.transforms = transformations.investigators.row( name )

            self.nickname = self.constants.nickname
            self.occupation = self.constants.occupation
            self.home = self.constants.home
            self.ability_name = self.constants.ability_name
            self.ability_desc = self.constants.ability_description
            self.story = self.constants.story

            self.damage = currency.investigator_damage( self.defaults.damage, self.transforms.damage )
            self.horror = currency.investigator_horror( self.defaults.horror, self.transforms.horror )

            self.conditions = currency.investigator_conditions( self.defaults.conditions, self.transforms.conditions )

            self.focus = currency.investigator_focus( self.defaults.focus, self.transforms.focus )
            self.speed = currency.investigator_skill( self.defaults.speed, self.transforms.speed )
            self.sneak = currency.investigator_complement_skill( self.defaults.speed, self.transforms.speed )
            self.fight = currency.investigator_skill( self.defaults.fight, self.transforms.fight )
            self.will = currency.investigator_complement_skill( self.defaults.fight, self.transforms.fight )
            self.lore = currency.investigator_skill( self.defaults.lore, self.transforms.lore )
            self.luck = currency.investigator_complement_skill( self.defaults.lore, self.transforms.lore )

            self.location = currency.investigator_location( self.defaults.location, self.transforms.location )

            self.hands = currency.investigator_equipped_items( self.defaults.equipped_items, self.transforms.equipped_items ).hands
            self.equipment = currency.investigator_equipped_items( self.defaults.equipped_items, self.transforms.equipped_items ).equipment
            self.exhausted_items = currency.investigator_exhausted_items( self.defaults.exhausted_items, self.transforms.exhausted_items )
            self.possessions = currency.investigator_possessions( self.defaults.possessions, self.transforms.possessions )

    def __init__( self, **kwargs):
        self.board = self.Board( **kwargs['board'] )
        self.briefs = self.InvestigatorBriefs( **kwargs['briefs'] )
        self.locations = self.Locations( **kwargs['locations'] )
        self.monsters = self.Deck( **kwargs['monsters'] )
        self.weapons = self.Deck( **kwargs['weapons'] )
        self.consumables = self.Deck( **kwargs['consumables'] )
        self.tomes = self.Deck( **kwargs['tomes'] )
        self.passive_buffs = self.Deck( **kwargs['passive_buffs'] )
        self.active_buffs = self.Deck( **kwargs['active_buffs'] )
        self.oddities = self.Deck( **kwargs['oddities'] )
        self.spells = self.Deck( **kwargs['spells'] )
        self.allies = self.Deck( **kwargs['allies'] )
        self.gates = self.Deck( **kwargs['gates'] )
        self.investigator = self.Investigator( kwargs['investigator'] )