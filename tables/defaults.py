from tools import Table, Location, Monster, Investigator, Items

board = {
    'investigators'         :   [  ],
    'current_player'        :   0,
    'current_phase'         :   1,
    'bookkeeping'           :   1,
    'ancient_one'           :   [ ],
    'awakened'              :   0,
    'doom_track'            :   0,
    'terror_track'          :   -10,
    'gates_in_arkham'       :   0,
    'gates_sealed'          :   0,
    'clues_to_seal'         :   5,
    'win_cond'              :   [ 0, 6 ], 
    'monsters_in_arkham'    :   0,
    'monsters_in_outskirts' :   0,
    'monster_locations'     :   [ [],[],[],[],[],[],[],[],[] ]
}

locations = Table([
    ['name',                            'investigators',    'occupants', 'gate_to',    'status'     ],
    ['CURIOSITIE SHOPPE',               [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['NEWSPAPER' ,                      [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['TRAIN STATION',                   [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['ARKHAM ASYLUM',                   [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['BANK OF ARKHAM',                  [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['INDEPENDENCE SQUARE',             [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['HIBB\'S ROADHOUSE',               [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['POLICE STATION',                  [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['JAIL CELL',                       [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['VELMA\'S DINER',                  [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['RIVER DOCKS',                     [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['THE UNNAMABLE',                   [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['UNVISITED ISLE',                  [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['BLACK CAVE',                      [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['GENERAL STORE',                   [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['GRAVEYARD',                       [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['ADMINISTRATION',                  [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['SCIENCE BUILDING',                [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['LIBRARY',                         [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['THE WITCH HOUSE',                 [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['THE SILVER TWILIGHT LODGE',       [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['THE INNER SANCTUM',               [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['ST. MARY\'S HOSPITAL',            [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['WOODS',                           [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['YE OLDE MAGICK SHOPPE',           [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['MA\'S BOARDING HOUSE',            [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['HISTORICAL SOCIETY',              [],                 [],          [],           Location.status( clues=1, historical_clues=1, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['SOUTH CHURCH',                    [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['NORTHSIDE STREETS',               [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['DOWNTOWN STREETS',                [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['EASTTOWN STREETS',                [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['MERCHANT DISTRICT STREETS',       [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['RIVERTOWN STREETS',               [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['MISKATONIC UNIVERSITY STREETS',   [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['FRENCH HILL STREETS',             [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['UPTOWN STREETS',                  [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['SOUTHSIDE STREETS',               [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['OUTSKIRTS',                       [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['THE SKY',                         [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['R\'LYEH',                         [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['PLATEAU OF LENG',                 [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['THE DREAMLANDS',                  [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['GREAT HALL OF CELEANO',           [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['YUGGOTH',                         [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['CITY OF THE GREAT RACE',          [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['ABYSS',                           [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ],
    ['ANOTHER DIMENSION',               [],                 [],          [],           Location.status( clues=0, historical_clues=0, sealed=0, gate=0, historical_gates=0, explored=0, closed=0 ) ]
])

monsters = Table([
    ['name',                     'rulesets',    'abilities',                'stats'                  ],
    ['CHTHONIAN',                Monster.rulesets( movement=4, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=+1, toughness=+3, horror_mod=-2, horror=+2, combat_mod=-3, damage=+3 )  ],
    ['CULTIST',                  Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+1, horror_mod=+0, horror=+0, combat_mod=+1, damage=+1 )  ],
    ['BYAKHEE',                  Monster.rulesets( movement=3, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-2, toughness=+1, horror_mod=-1, horror=+1, combat_mod=+0, damage=+1 )  ],
    ['DARK YOUNG',               Monster.rulesets( movement=2, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=0.5, magical=1, nightmarish=1, overwhelming=0 ),   Monster.stats( awareness=-2, toughness=+3, horror_mod=+0, horror=+3, combat_mod=-1, damage=+3 )  ],
    ['DHOLE',                    Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=0.5, magical=0.5, nightmarish=1, overwhelming=1 ), Monster.stats( awareness=-1, toughness=+3, horror_mod=-1, horror=+4, combat_mod=-3, damage=+4 )  ],
    ['DIMENSIONAL SHAMBLER',     Monster.rulesets( movement=1, combat=0, evade=1 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+1, horror_mod=-2, horror=+1, combat_mod=-2, damage=+0 )  ],
    ['ELDER THING',              Monster.rulesets( movement=0, combat=1, evade=2 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-2, toughness=+2, horror_mod=-3, horror=+2, combat_mod=+0, damage=+1 )  ],
    ['FIRE VAMPIRE',             Monster.rulesets( movement=3, combat=0, evade=0 ),   Monster.abilities(ambush=1, endless=0, undead=0, physical=0, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=+0, toughness=+1, horror_mod=+0, horror=+0, combat_mod=-2, damage=+2 )  ],
    ['FLYING POLYP',             Monster.rulesets( movement=3, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=0.5, magical=1, nightmarish=1, overwhelming=1 ),   Monster.stats( awareness=+0, toughness=+3, horror_mod=-2, horror=+4, combat_mod=-3, damage=+3 )  ],
    ['FORMLESS SPAWN',           Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=0, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=+0, toughness=+2, horror_mod=-1, horror=+2, combat_mod=-2, damage=+2 )  ],
    ['GHOST',                    Monster.rulesets( movement=2, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=1, physical=0, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+1, horror_mod=-2, horror=+2, combat_mod=-2, damage=+2 )  ],
    ['GHOUL',                    Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=1, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+1, horror_mod=+0, horror=+1, combat_mod=-1, damage=+1 )  ],
    ['GOD OF THE BLOODY TONGUE', Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=1, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=1 ),     Monster.stats( awareness=+1, toughness=+4, horror_mod=-3, horror=+3, combat_mod=-4, damage=+4 )  ],
    ['GUG',                      Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=1 ),     Monster.stats( awareness=-2, toughness=+3, horror_mod=-1, horror=+2, combat_mod=-2, damage=+4 )  ],
    ['HAUNTER OF THE DARK',      Monster.rulesets( movement=3, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=1, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+2, horror_mod=-2, horror=+2, combat_mod=-2, damage=+2 )  ],
    ['HIGH PRIEST',              Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=0, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-2, toughness=+2, horror_mod=+1, horror=+1, combat_mod=-1, damage=+2 )  ],
    ['HOUND OF TINDALOS',        Monster.rulesets( movement=5, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=0, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-1, toughness=+2, horror_mod=-2, horror=+4, combat_mod=-1, damage=+3 )  ],
    ['MANIAC',                   Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-1, toughness=+1, horror_mod=+0, horror=+0, combat_mod=+1, damage=+1 )  ],
    ['MI-GO',                    Monster.rulesets( movement=3, combat=0, evade=3 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-2, toughness=+1, horror_mod=-1, horror=+2, combat_mod=+0, damage=+1 )  ],
    ['NIGHTGAUNT',               Monster.rulesets( movement=3, combat=2, evade=4 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-2, toughness=+2, horror_mod=-1, horror=+1, combat_mod=-2, damage=+0 )  ],
    ['SHOGGOTH',                 Monster.rulesets( movement=1, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=0.5, magical=1, nightmarish=1, overwhelming=0 ),   Monster.stats( awareness=-1, toughness=+3, horror_mod=-1, horror=+3, combat_mod=-1, damage=+3 )  ],
    ['STAR SPAWN',               Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-1, toughness=+3, horror_mod=-3, horror=+2, combat_mod=-3, damage=+3 )  ],
    ['THE BLACK MAN',            Monster.rulesets( movement=0, combat=0, evade=5 ),   Monster.abilities(ambush=0, endless=1, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+1, horror_mod=+0, horror=+0, combat_mod=+0, damage=+0 )  ],
    ['THE BLOATED WOMAN',        Monster.rulesets( movement=0, combat=0, evade=6 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-1, toughness=+2, horror_mod=-1, horror=+2, combat_mod=-2, damage=+2 )  ],
    ['THE DARK PHARAOH',         Monster.rulesets( movement=0, combat=0, evade=7 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-1, toughness=+2, horror_mod=-1, horror=+1, combat_mod=-3, damage=+3 )  ],
    ['VAMPIRE',                  Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=1, physical=0.5, magical=1, nightmarish=0, overwhelming=0 ),   Monster.stats( awareness=-3, toughness=+1, horror_mod=+0, horror=+2, combat_mod=-3, damage=+3 )  ],
    ['WARLOCK',                  Monster.rulesets( movement=2, combat=0, evade=8 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=0, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=-3, toughness=+2, horror_mod=-1, horror=+1, combat_mod=-3, damage=+1 )  ],
    ['WITCH',                    Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=0, physical=1, magical=0.5, nightmarish=0, overwhelming=0 ),   Monster.stats( awareness=-1, toughness=+1, horror_mod=+0, horror=+0, combat_mod=-3, damage=+2 )  ],
    ['ZOMBIE',                   Monster.rulesets( movement=0, combat=0, evade=0 ),   Monster.abilities(ambush=0, endless=0, undead=1, physical=1, magical=1, nightmarish=0, overwhelming=0 ),     Monster.stats( awareness=+1, toughness=+1, horror_mod=-1, horror=+1, combat_mod=-1, damage=+2 )  ],
])
 
monster_cup = {
    'BYAKHEE'                   : 3,
    'CHTHONIAN'                 : 2,
    'CULTIST'                   : 6,
    'DARK YOUNG'                : 3,
    'DHOLE'                     : 1,
    'DIMENSIONAL SHAMBLER'      : 2,
    'ELDER THING'               : 2,
    'FIRE VAMPIRE'              : 2,
    'FLYING POLYP'              : 1, 
    'FORMLESS SPAWN'            : 2, 
    'GHOST'                     : 3,
    'GHOUL'                     : 3,
    'GOD OF THE BLOODY TONGUE'  : 0,
    'GUG'                       : 2,
    'HAUNTER OF THE DARK'       : 0,
    'HIGH PRIEST'               : 1,
    'HOUND OF TINDALOS'         : 2,
    'MANIAC'                    : 3,
    'MI-GO'                     : 3,
    'NIGHTGAUNT'                : 2,
    'SHOGGOTH'                  : 2,
    'STAR SPAWN'                : 2,
    'THE BLACK MAN'             : 0,
    'THE BLOATED WOMAN'         : 0,
    'THE DARK PHARAOH'          : 0,
    'VAMPIRE'                   : 1, 
    'WARLOCK'                   : 2,
    'WITCH'                     : 2,
    'ZOMBIE'                    : 3
}

investigators = Table([
    ['name',            'damage',  'horror',  'conditions',             'focus',   'speed',   'fight',   'lore',    'location', 'random_possessions', 'equipped_items', 'exhausted_items', 'possessions'],
    ['Amanda Sharpe',   Investigator.damage(max_damage=5, current_damage=0, unconscious=0), Investigator.horror(max_horror=5, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=4, current_speed=4, speed_sneak_sum=5), Investigator.fight(max_fight=4, current_fight=4, fight_will_sum=5), Investigator.lore(max_lore=4, current_lore=4, lore_luck_sum=5), Investigator.location(current_location=19, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=1, unique_items=1, spells=1, skills=2), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 1, 'clues': 1, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['"Ashcan" Pete',   Investigator.damage(max_damage=5, current_damage=0, unconscious=0), Investigator.horror(max_horror=5, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=1, current_focus=1), Investigator.speed(max_speed=3, current_speed=3, speed_sneak_sum=6), Investigator.fight(max_fight=5, current_fight=5, fight_will_sum=7), Investigator.lore(max_lore=3, current_lore=3, lore_luck_sum=3), Investigator.location(current_location=11, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=1, unique_items=1, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 1, 'clues': 3, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': ['DUKE']}],
    ['Bob Jenkins',     Investigator.damage(max_damage=6, current_damage=0, unconscious=0), Investigator.horror(max_horror=4, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=1, current_focus=1), Investigator.speed(max_speed=5, current_speed=5, speed_sneak_sum=5), Investigator.fight(max_fight=4, current_fight=4, fight_will_sum=7), Investigator.lore(max_lore=3, current_lore=3, lore_luck_sum=4), Investigator.location(current_location=15, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=2, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 9, 'clues': 0, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Carolyn Fern',    Investigator.damage(max_damage=4, current_damage=0, unconscious=0), Investigator.horror(max_horror=6, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=3, current_speed=3, speed_sneak_sum=3), Investigator.fight(max_fight=4, current_fight=4, fight_will_sum=5), Investigator.lore(max_lore=5, current_lore=5, lore_luck_sum=7), Investigator.location(current_location=4,  mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=2, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 7, 'clues': 1, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Darrell Simmons', Investigator.damage(max_damage=6, current_damage=0, unconscious=0), Investigator.horror(max_horror=4, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=2, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=5, current_speed=5, speed_sneak_sum=5), Investigator.fight(max_fight=5, current_fight=5, fight_will_sum=6), Investigator.lore(max_lore=3, current_lore=3, lore_luck_sum=4), Investigator.location(current_location=2,  mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=1, unique_items=2, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 4, 'clues': 1, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Dexter Drake',    Investigator.damage(max_damage=5, current_damage=0, unconscious=0), Investigator.horror(max_horror=5, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=5, current_speed=5, speed_sneak_sum=6), Investigator.fight(max_fight=4, current_fight=4, fight_will_sum=4), Investigator.lore(max_lore=5, current_lore=5, lore_luck_sum=5), Investigator.location(current_location=25, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=1, unique_items=1, spells=2, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 5, 'clues': 0, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': ['SHRIVELLING'], 'allies': []}],
    ['Gloria Goldberg', Investigator.damage(max_damage=4, current_damage=0, unconscious=0), Investigator.horror(max_horror=6, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=4, current_speed=4, speed_sneak_sum=4), Investigator.fight(max_fight=3, current_fight=3, fight_will_sum=5), Investigator.lore(max_lore=4, current_lore=4, lore_luck_sum=6), Investigator.location(current_location=10, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=0, spells=2, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 7, 'clues': 2, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Harvey Walters',  Investigator.damage(max_damage=3, current_damage=0, unconscious=0), Investigator.horror(max_horror=7, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=3, current_speed=3, speed_sneak_sum=5), Investigator.fight(max_fight=3, current_fight=3, fight_will_sum=3), Investigator.lore(max_lore=6, current_lore=6, lore_luck_sum=7), Investigator.location(current_location=17, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=0, unique_items=2, spells=2, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 5, 'clues': 1, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Jenny Barnes',    Investigator.damage(max_damage=4, current_damage=0, unconscious=0), Investigator.horror(max_horror=6, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=1, current_focus=1), Investigator.speed(max_speed=3, current_speed=3, speed_sneak_sum=4), Investigator.fight(max_fight=4, current_fight=4, fight_will_sum=6), Investigator.lore(max_lore=4, current_lore=4, lore_luck_sum=6), Investigator.location(current_location=3,  mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=1, spells=1, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 10, 'clues': 0, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Joe Diamond',     Investigator.damage(max_damage=6, current_damage=0, unconscious=0), Investigator.horror(max_horror=4, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=3, current_focus=3), Investigator.speed(max_speed=6, current_speed=6, speed_sneak_sum=7), Investigator.fight(max_fight=5, current_fight=5, fight_will_sum=5), Investigator.lore(max_lore=3, current_lore=3, lore_luck_sum=0), Investigator.location(current_location=8,  mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=0, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 8, 'clues': 3, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': ['.45 AUTOMATIC'], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Kate Winthrop',   Investigator.damage(max_damage=4, current_damage=0, unconscious=0), Investigator.horror(max_horror=6, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=1, current_focus=1), Investigator.speed(max_speed=4, current_speed=4, speed_sneak_sum=6), Investigator.fight(max_fight=4, current_fight=4, fight_will_sum=4), Investigator.lore(max_lore=5, current_lore=5, lore_luck_sum=6), Investigator.location(current_location=18, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=1, unique_items=1, spells=2, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 7, 'clues': 2, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Mandy Thompson',  Investigator.damage(max_damage=5, current_damage=0, unconscious=0), Investigator.horror(max_horror=5, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=4, current_speed=4, speed_sneak_sum=6), Investigator.fight(max_fight=3, current_fight=3, fight_will_sum=5), Investigator.lore(max_lore=4, current_lore=4, lore_luck_sum=4), Investigator.location(current_location=19, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=1, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 6, 'clues': 4, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Michael McGlen',  Investigator.damage(max_damage=7, current_damage=0, unconscious=0), Investigator.horror(max_horror=3, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=1, current_focus=1), Investigator.speed(max_speed=5, current_speed=5, speed_sneak_sum=6), Investigator.fight(max_fight=6, current_fight=6, fight_will_sum=7), Investigator.lore(max_lore=3, current_lore=3, lore_luck_sum=3), Investigator.location(current_location=26, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=0, unique_items=1, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 8, 'clues': 0, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': ['DYNAMITE', 'TOMMY GUN'], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Monterey Jack',   Investigator.damage(max_damage=7, current_damage=0, unconscious=0), Investigator.horror(max_horror=3, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=4, current_speed=4, speed_sneak_sum=4), Investigator.fight(max_fight=5, current_fight=5, fight_will_sum=5), Investigator.lore(max_lore=4, current_lore=4, lore_luck_sum=6), Investigator.location(current_location=1,  mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=0, unique_items=2, spells=0, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 7, 'clues': 1, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': ['BULLWHIP', '.38 REVOLVER'], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Sister Mary',     Investigator.damage(max_damage=3, current_damage=0, unconscious=0), Investigator.horror(max_horror=7, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=2, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=2), Investigator.focus(max_focus=1, current_focus=1), Investigator.speed(max_speed=4, current_speed=4, speed_sneak_sum=5), Investigator.fight(max_fight=3, current_fight=3, fight_will_sum=4), Investigator.lore(max_lore=4, current_lore=4, lore_luck_sum=7), Investigator.location(current_location=28, mvmt_points=9, in_arkham=1), Investigator.random_possessions(common_items=0, unique_items=0, spells=2, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 0, 'clues': 0, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': ['CROSS', 'HOLY WATER'], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}],
    ['Vincent Lee',     Investigator.damage(max_damage=5, current_damage=0, unconscious=0), Investigator.horror(max_horror=5, current_horror=0, insane=0), Investigator.conditions(lost_in_time_and_space=0, delayed=0, arrested=0, retainer=0, bank_loan=0, stl_membership=0, deputized=0, blessed_cursed=0), Investigator.focus(max_focus=2, current_focus=2), Investigator.speed(max_speed=3, current_speed=3, speed_sneak_sum=5), Investigator.fight(max_fight=3, current_fight=3, fight_will_sum=4), Investigator.lore(max_lore=5, current_lore=5, lore_luck_sum=6), Investigator.location(current_location=23, mvmt_points=0, in_arkham=1), Investigator.random_possessions(common_items=2, unique_items=0, spells=2, skills=1), Investigator.equipped_items(hands=2, equipment=[]), [], {'money': 9, 'clues': 1, 'gate_trophies': 0, 'monster_trophies': 0, 'weapons': [], 'consumables' : [], 'tomes': [], 'passive_buffs': [], 'active_buffs' : [], 'oddities': [], 'spells': [], 'allies': []}]
])

weapons = Table([
    ['name',                'stats'                 ],
    ['.22 DERRINGER',       Items.weapon( modality=0,bonus=2,sanity_cost=0,exhaustable=0,losable=0,price=3 )    ],
    ['.38 REVOLVER',        Items.weapon( modality=0,bonus=3,sanity_cost=0,exhaustable=0,losable=1,price=4 )    ],
    ['.45 AUTOMATIC',       Items.weapon( modality=0,bonus=4,sanity_cost=0,exhaustable=0,losable=1,price=5 )    ],
    ['AXE',                 Items.weapon( modality=0,bonus=2,sanity_cost=0,exhaustable=0,losable=1,price=3 )    ],
    ['BULLWHIP',            Items.weapon( modality=0,bonus=1,sanity_cost=0,exhaustable=1,losable=1,price=1 )    ],
    ['CAVALRY SABRE',       Items.weapon( modality=0,bonus=2,sanity_cost=0,exhaustable=0,losable=1,price=3 )    ],
    ['DYNAMITE',            Items.weapon( modality=0,bonus=8,sanity_cost=0,exhaustable=0,losable=1,price=4 )    ],
    ['KNIFE',               Items.weapon( modality=0,bonus=1,sanity_cost=0,exhaustable=0,losable=1,price=2 )    ],
    ['RIFLE',               Items.weapon( modality=0,bonus=5,sanity_cost=0,exhaustable=0,losable=1,price=6 )    ],
    ['SHOTGUN',             Items.weapon( modality=0,bonus=4,sanity_cost=0,exhaustable=0,losable=1,price=6 )    ],
    ['TOMMY GUN',           Items.weapon( modality=0,bonus=6,sanity_cost=0,exhaustable=0,losable=1,price=7 )    ],
    ['CROSS',               Items.weapon( modality=1,bonus=0,sanity_cost=0,exhaustable=0,losable=1,price=3 )    ],
    ['ENCHANTED KNIFE',     Items.weapon( modality=1,bonus=3,sanity_cost=0,exhaustable=0,losable=1,price=5 )    ],
    ['ENCHANTED BLADE',     Items.weapon( modality=1,bonus=4,sanity_cost=0,exhaustable=0,losable=1,price=6 )    ],
    ['POWDER OF IBN-GHAZI', Items.weapon( modality=1,bonus=9,sanity_cost=1,exhaustable=0,losable=1,price=6 )    ],
    ['HOLY WATER',          Items.weapon( modality=1,bonus=6,sanity_cost=0,exhaustable=0,losable=1,price=4 )    ],
    ['LAMP OF ALHAZRED',    Items.weapon( modality=1,bonus=5,sanity_cost=0,exhaustable=0,losable=1,price=7 )    ],
    ['SWORD OF GLORY',      Items.weapon( modality=1,bonus=6,sanity_cost=0,exhaustable=0,losable=1,price=8 )    ],
])

weapons_deck = {
    '.22 DERRINGER'         : 2,
    '.38 REVOLVER'          : 2,
    '.45 AUTOMATIC'         : 2,
    'AXE'                   : 2,
    'BULLWHIP'              : 2,
    'CAVALRY SABRE'         : 2,
    'DYNAMITE'              : 2,
    'KNIFE'                 : 2,
    'RIFLE'                 : 2,
    'SHOTGUN'               : 2,
    'TOMMY GUN'             : 2,
    'CROSS'                 : 2,
    'ENCHANTED BLADE'       : 2,
    'ENCHANTED KNIFE'       : 2,
    'HOLY WATER'            : 4,
    'POWDER OF IBN-GHAZI'   : 1,
    'SWORD OF GLORY'        : 1,
    'LAMP OF ALHAZRED'      : 1
}

consumables = Table([
    ['name',                    'stats'                                          ],
    ['FOOD',                    Items.consumable( bonus=-1,price=1 )       ],
    ['WHISKEY',                 Items.consumable( bonus=-1,price=1 )       ],
    ['LUCKY CIGARETTE CASE',    Items.consumable( bonus=0, price=1 )       ],
    ['RESEARCH MATERIALS',      Items.consumable( bonus=1, price=1 )       ]
])

consumables_deck = {
    'FOOD'                  : 2,
    'WHISKEY'               : 2,
    'LUCKY CIGARETTE CASE'  : 2,
    'RESEARCH MATERIALS'    : 2
}

tomes = Table([
    ['name',                'stats',                                                        ],
    ['OLD JOURNAL',         Items.tome( mvmt_cost=1,sanity_cost=0,modifier=-1,price=1 ) ],
    ['ANCIENT TOME',        Items.tome( mvmt_cost=2,sanity_cost=0,modifier=-1,price=4 ) ],
    ['BOOK OF DZYAN',       Items.tome( mvmt_cost=2,sanity_cost=0,modifier=-1,price=3 ) ],
    ['CABALA OF SABOTH',    Items.tome( mvmt_cost=2,sanity_cost=0,modifier=-2,price=5 ) ],
    ['CULTES DES GOULES',   Items.tome( mvmt_cost=2,sanity_cost=2,modifier=-2,price=3 ) ],
    ['NAMELESS CULTES',     Items.tome( mvmt_cost=1,sanity_cost=1,modifier=-1,price=3 ) ],
    ['NECRONOMICON',        Items.tome( mvmt_cost=2,sanity_cost=2,modifier=-2,price=6 ) ],
    ['THE KING IN YELLOW',  Items.tome( mvmt_cost=2,sanity_cost=1,modifier=-2,price=2 ) ]
])

tomes_deck = {
    'ANCIENT TOME'          : 2,
    'OLD JOURNAL'           : 2,
    'BOOK OF DZYAN'         : 1,
    'CABALA OF SABOTH'      : 2,
    'CULTES DES GOULES'     : 2,
    'NAMELESS CULTS'        : 2,
    'NECROMICON'            : 1,
    'THE KING IN YELLOW'    : 2
}

passive_buffs = Table([
    ['name',            'stats'                                   ],
    ['DARK CLOAK',      Items.passive_buff( bonus=1,price=2 ) ],
    ['LANTERN',         Items.passive_buff( bonus=1,price=3 ) ],
    ['PALLID MASK',     Items.passive_buff( bonus=2,price=4 ) ],
    ["RUBY OF R'LYEH",  Items.passive_buff( bonus=3,price=4 ) ],
    ['SPEED',           Items.passive_buff( bonus=1,price=0 ) ],
    ['SNEAK',           Items.passive_buff( bonus=1,price=0 ) ],
    ['FIGHT',           Items.passive_buff( bonus=1,price=0 ) ],
    ['WILL',            Items.passive_buff( bonus=1,price=0 ) ],
    ['LORE',            Items.passive_buff( bonus=1,price=0 ) ],
    ['LUCK',            Items.passive_buff( bonus=1,price=0 ) ],
])

passive_buffs_deck = {
    'DARK CLOAK'        : 2,  
    'LANTERN'           : 2,
    'PALLID MASK'       : 1,
    "RUBY OF R'LYEH"    : 1,
    'SPEED'             : 2,
    'SNEAK'             : 2,
    'FIGHT'             : 2,
    'WILL'              : 2,
    'LORE'              : 2,
    'LUCK'              : 2
}

active_buffs = Table([
    ['name',                'stats'                                  ],
    ['MAP OF ARKHAM',       Items.active_buff( bonus=1,price=2 )],
    ['MOTORCYCLE',          Items.active_buff( bonus=2,price=4 )],
    ['BRAVERY',             Items.active_buff( bonus=0,price=0 )],
    ['STEALTH',             Items.active_buff( bonus=0,price=0 )],
    ['EXPERT OCCULTIST',    Items.active_buff( bonus=0,price=0 )],
    ['MARKSMAN',            Items.active_buff( bonus=0,price=0 )]
])

active_buffs_deck = {
    'MAP OF ARKHAM'         : 2,
    'BRAVERY'               : 2,
    'MOTORCYCLE'            : 2,
    'STEALTH'               : 2,
    'EXPERT OCCULTIST'      : 2,
    'MARKSMAN'              : 2
}

oddities = Table([
    ['name',                        'stats'                          ],
    ['ALIEN STATUE',                Items.oddity( price=5 )    ],
    ['BLUE WATCHER OF THE PYRAMID', Items.oddity( price=8 )    ],
    ["DRAGON'S EYE",                Items.oddity( price=4 )    ],
    ['ELDER SIGN',                  Items.oddity( price=5 )    ],
    ['ENCHANTED JEWELRY',           Items.oddity( price=3 )    ],
    ['FLUTE OF THE OUTER GODS',     Items.oddity( price=6 )    ],
    ['GATE BOX',                    Items.oddity( price=4 )    ],
    ['HEALING STONE',               Items.oddity( price=8 )    ],
    ['OBSIDIAN STATUE',             Items.oddity( price=4 )    ],
    ['SILVER KEY',                  Items.oddity( price=4 )    ],
    ['WARDING STATUE',              Items.oddity( price=6 )    ],
])

oddities_deck = {
    'ALIEN STATUE'                  : 1,
    'BLUE WATCHER OF THE PYRAMID'   : 1,
    "DRAGON'S EYE"                  : 1,
    'ELDER SIGN'                    : 4,
    'ENCHANTED JEWELRY'             : 1,
    'FLUTE OF THE OUTER GODS'       : 1,
    'GATE BOX'                      : 1,
    'HEALING STONE'                 : 1,
    'OBSIDIAN STATUE'               : 1,
    'SILVER KEY'                    : 1,
    'WARDING STATUE'                : 1,
}

spells_deck = {
    'BIND MONSTER'              : 2,
    'DREAD CURSE OF AZATHOTH'   : 4,
    'ENCHANT WEAPON'            : 3,
    'FIND GATE'                 : 4,
    'FLESH WARD'                : 4,
    'HEAL'                      : 3,
    'MISTS OF RELEH'            : 4,
    "RED SIGN OF SHUDDE M'ELL"  : 2,
    'SHRIVELLING'               : 5,
    'VOICE OF RA'               : 3,
    'WITHER'                    : 6
}

allies_deck = {
    'ANNA KASLOW'           : 1,
    'DUKE'                  : 1,
    'ERIC COLT'             : 1,
    'JOHN LEGRASSE'         : 1,
    'PROFESSOR ARMITAGE'    : 1,
    'RICHARD UPTON PICKMAN' : 1,
    'RUBY STANDISH'         : 1,
    'SIR WILLIAM BRINTON'   : 1,
    'THOMAS F. MALONE'      : 1,
    'TOM "MOUNTAIN" MURPHY' : 1
}

gates = Table([
    ['name',                        'modifier'  ],
    ['YUGGOTH',                     -2          ],
    ['THE CITY OF THE GREAT RACE',  0           ],
    ['THE PLATEAU OF LENG',         -1          ],
    ['THE ABYSS',                   -2          ],
    ['ANOTHER DIMENSION',           0           ],
    ['THE GREAT HALL OF CELEANO',   -1          ],
    ['THE DREAMLANDS',              1           ],
    ["R'LYEH",                      -3          ],
])

gates_deck = {
    'YUGGOTH'                      : 2,
    'THE CITY OF THE GREAT RACE'   : 2,
    'THE PLATEAU OF LENG'          : 2,
    'THE ABYSS'                    : 2,
    'ANOTHER DIMENSION'            : 2,
    'THE GREAT HALL OF CELEANO'    : 2,
    'THE DREAMLANDS'               : 2,
    "R'LYEH"                       : 2
}