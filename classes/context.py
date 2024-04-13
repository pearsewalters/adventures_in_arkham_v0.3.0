from classes.table import Table
import currency

class Context:
    class Board:
        def __init__( self, phase, bookkeeping, win, gatesOpen, defs, trans ):
            self.phase = phase
            self.bookkeeping = bookkeeping
            self.win = win
            self.gatesOpen = gatesOpen
            self.defaults = defs
            self.transforms = trans

    class Mythos:
        def __init__( self, headline, mystic, urban, weather, mvmtPoints, speed, sneak, fight, will, lore, luck, resolution, cons, defs, trans, deckDefaults, deckTransforms ):
            self.headline = headline
            self.mystic = mystic
            self.urban = urban
            self.weather = weather
            self.mvmtPoint = mvmtPoints
            self.speed = speed
            self.sneak = sneak
            self.fight = fight
            self.will = will
            self.lore = lore
            self.luck = luck
            self.resolution = resolution
            self.constants = cons
            self.defaults = defs
            self.transforms = trans
            self.deckDefaults = deckDefaults
            self.deckTransforms = deckTransforms

    class InvestigatorBriefs:
        def __init__( self, names, cons, defs, trans, locs ):
            self.names = names
            self.current_locations = locs
            self.constants = cons
            self.defaults = defs
            self.transforms = trans

    class Locations:
        def __init__( self, cons, defs, trans, currents, graph, leftGraph, rightGraph ):
            self.constants = cons
            self.defaults = defs
            self.transforms = trans
            self.currents = currents
            self.graph = graph
            self.leftGraph = leftGraph
            self.rightGraph = rightGraph

    class Graph:
        def __init__( self, graphDefaults, leftGraphDefaults, rightGraphDefaults, graphTransforms, leftGraphTransforms, rightGraphTransforms ):
            self.graphDefaults = graphDefaults
            self.leftGraphDefaults = leftGraphDefaults
            self.rightGraphDefaults = rightGraphDefaults
            self.graphTransforms = graphTransforms
            self.leftGraphTransforms = leftGraphTransforms
            self.rightGraphTransforms = rightGraphTransforms

    class Deck:
        def __init__( self, cons: Table, defs: Table, trans: Table, deckDefaults: dict, deckTransforms: list ):
            self.constants = cons
            self.defaults = defs
            self.transforms = trans
            self.deckDefaults = deckDefaults
            self.deckTransforms = deckTransforms

    class Investigator:
        def __init__( self, name: str, cons: Table.Row, defs: Table.row, trans: Table.row ):
            self.name = name
            self.constants = cons
            self.defaults = defs
            self.transforms = trans

            self.nickname = self.constants.nickname
            self.occupation = self.constants.occupation
            self.home = self.constants.home
            self.story = self.constants.story

            self.damage = currency.investigatorDamage( self.defaults.damage, self.transforms.damage )
            self.horror = currency.investigatorHorror( self.defaults.horror, self.transforms.horror )

            self.conditions = currency.investigatorConditions( self.defaults.conditions, self.transforms.conditions )

            self.focus = currency.investigatorFocus( self.defaults.focus, self.transforms.focus )
            self.speed = currency.investigatorSkill( self.defaults.speed, self.transforms.speed )
            self.sneak = currency.investigatorComplementSkill( self.defaults.speed, self.transforms.speed )
            self.fight = currency.investigatorSkill( self.defaults.fight, self.transforms.fight )
            self.will = currency.investigatorComplementSkill( self.defaults.fight, self.transforms.fight )
            self.lore = currency.investigatorSkill( self.defaults.lore, self.transforms.lore )
            self.luck = currency.investigatorComplementSkill( self.defaults.lore, self.transforms.lore )

            self.location = currency.investigatorLocation( self.defaults.location, self.transforms.location )

            self.hands = currency.investigatorEquippedItems( self.defaults.equippedItems, self.transforms.equippedItems ).hands
            self.equipment = currency.investigatorEquippedItems( self.defaults.equippedItems, self.transforms.equippedItems ).equipment
            self.exhaustedItems = currency.investigatorExhaustedItems( self.defaults.exhaustedItems, self.transforms.exhaustedItems )
            self.possessions = currency.investigatorPossessions( self.defaults.possessions, self.transforms.possessions )

    def __init__( self, **kwargs):
        self.board = self.Board( **kwargs['board'] )
        self.mythos = self.Mythos( **kwargs['mythos'] )
        self.briefs = self.InvestigatorBriefs( **kwargs['briefs'] )
        self.locations = self.Locations( **kwargs['locations'] )
        self.graph = self.Graph( **kwargs['graph'] )
        self.monsters = self.Deck( **kwargs['monsters'] )
        self.weapons = self.Deck( **kwargs['weapons'] )
        self.consumables = self.Deck( **kwargs['consumables'] )
        self.tomes = self.Deck( **kwargs['tomes'] )
        self.passiveBuffs = self.Deck( **kwargs['passiveBuffs'] )
        self.activeBuffs = self.Deck( **kwargs['activeBuffs'] )
        self.oddities = self.Deck( **kwargs['oddities'] )
        self.spells = self.Deck( **kwargs['spells'] )
        self.allies = self.Deck( **kwargs['allies'] )
        self.gates = self.Deck( **kwargs['gates'] )
        self.investigator = self.Investigator( **kwargs['investigator'] )