DEBUG_LVL = -1


GATE_LIMIT = '8 - math.floor( (x-1)/2 )'
MONSTER_LIMIT = '3 + x'
OUTSKIRTS_LIMIT = '8 - x'

GATE_SPAWN = 'constants.instability * ( math.log2( 1 + context.locations.currents.row( constants.name ).status.historicalClues) / math.log( 2 + context.locations.currents.row( constants.name ).status.clues, 3 ) )'
CLUE_SPAWN = 'constants.mystery * ( math.log2( 2 + context.locations.currents.row( constants.name ).status.historicalGates ) / math.log( 2 + context.locations.currents.row( constants.name ).status.clues, 3 ) )'

MVMT_GROUPS = [ (0,), (4,), (5,), (8,), (2,3), (1,6,7) ]
NORMAL_MOVE_MSGS = [
    "f'There are reports of odd things going bump in the night near {adj_location.name}'",
    "f'Something loathsome was seen lurking near {adj_location.name}!'",
    "f'People are avoiding {adj_location.name}; perhaps there\\'s something going on there'",
    "f'\"Be carful if you\\'re heading through {adj_location.name},\" says a frightened passerby. \"Most horrible thing I\\'ll ever see.\"'",
]
STATIONARY_MSGS = [
    "f'Something ugly is standing it\\'s ground at {location.name}. It wants to fight!'",
    "f'There are whispers about some odious thing that won\\'t leave {location.name}'",
    "f'\"I don\\'t know what it is, but it\\'s scaring the hell outta me! I just came from {location.name}, but it didn\\'t follow me...'"
]
FLYING_MOVE_MSGS = [
    "f'A hideous shape darts across the sky and you barely catch a glimpse...what was that?'",
]

BLESS_CURSE_DIE = 1/6
RETAINER_DIE = 1/6
BANK_LOAN_DIE = 1/2

RETAINER_PAYOUT = 2

BLESSING_MONSTER_COST = 5
BLESSING_GATE_COST = 1
SKILLS_DOLLAR_COST = 8