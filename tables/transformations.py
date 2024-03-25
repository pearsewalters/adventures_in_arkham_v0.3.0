from tools import Table

board = {
    'investigators'         :   [ ],
    'current_player'        :   [ ],
    'current_phase'         :   [ ],
    'bookkeeping'           :   [ ],
    'ancient_one'           :   [ ],
    'awakened'              :   [ ],
    'doom_track'            :   [ ],
    'terror_track'          :   [ ],
    'gates_in_arkham'       :   [ ],
    'gates_sealed'          :   [ ],
    'clues_to_seal'         :   [ ],
    'win_cond'              :   [ ],
    'gate_limit'            :   [ ],
    'monsters_in_arkham'    :   [ ],
    'monsters_in_outskirts' :   [ ],
    'monster_locations'     :   [ ]
}

locations = Table([
    ['name',                            'investigators',    'occupants',    'gate_to',  'status'    ],
    ['CURIOSITIE SHOPPE',               [],                 [],             [],         []          ],
    [ 'NEWSPAPER' ,                     [],                 [],             [],         []          ],
    ['TRAIN STATION',                   [],                 [],             [],         []          ],
    ['ARKHAM ASYLUM',                   [],                 [],             [],         []          ],
    ['BANK OF ARKHAM',                  [],                 [],             [],         []          ],
    ['INDEPENDENCE SQUARE',             [],                 [],             [],         []          ],
    ['HIBB\'S ROADHOUSE',               [],                 [],             [],         []          ],
    ['POLICE STATION',                  [],                 [],             [],         []          ],
    ['JAIL CELL',                       [],                 [],             [],         []          ],
    ['VELMA\'S DINER',                  [],                 [],             [],         []          ],
    ['RIVER DOCKS',                     [],                 [],             [],         []          ],
    ['THE UNNAMABLE',                   [],                 [],             [],         []          ],
    ['UNVISITED ISLE',                  [],                 [],             [],         []          ],
    ['BLACK CAVE',                      [],                 [],             [],         []          ],
    ['GENERAL STORE',                   [],                 [],             [],         []          ],
    ['GRAVEYARD',                       [],                 [],             [],         []          ],
    ['ADMINISTRATION',                  [],                 [],             [],         []          ],
    ['SCIENCE BUILDING',                [],                 [],             [],         []          ],
    ['LIBRARY',                         [],                 [],             [],         []          ],
    ['THE WITCH HOUSE',                 [],                 [],             [],         []          ],
    ['THE SILVER TWILIGHT LODGE',       [],                 [],             [],         []          ],
    ['THE INNER SANCTUM',               [],                 [],             [],         []          ],
    ['ST. MARY\'S HOSPITAL',            [],                 [],             [],         []          ],
    ['WOODS',                           [],                 [],             [],         []          ],
    ['YE OLDE MAGICK SHOPPE',           [],                 [],             [],         []          ],
    ['MA\'S BOARDING HOUSE',            [],                 [],             [],         []          ],
    ['HISTORICAL SOCIETY',              [],                 [],             [],         []          ],
    ['SOUTH CHURCH',                    [],                 [],             [],         []          ],
    ['NORTHSIDE STREETS',               [],                 [],             [],         []          ],
    ['DOWNTOWN STREETS',                [],                 [],             [],         []          ],
    ['EASTTOWN STREETS',                [],                 [],             [],         []          ],
    ['MERCHANT DISTRICT STREETS',       [],                 [],             [],         []          ],
    ['RIVERTOWN STREETS',               [],                 [],             [],         []          ],
    ['MISKATONIC UNIVERSITY STREETS',   [],                 [],             [],         []          ],
    ['FRENCH HILL STREETS',             [],                 [],             [],         []          ],
    ['UPTOWN STREETS',                  [],                 [],             [],         []          ],
    ['SOUTHSIDE STREETS',               [],                 [],             [],         []          ],
    ['OUTSKIRTS',                       [],                 [],             [],         []          ],
    ['THE SKY',                          [],                 [],             [],         []          ],
    ['R\'LYEH',                         [],                 [],             [],         []          ],
    ['PLATEAU OF LENG',                 [],                 [],             [],         []          ],
    ['THE DREAMLANDS',                  [],                 [],             [],         []          ],
    ['GREAT HALL OF CELEANO',           [],                 [],             [],         []          ],
    ['YUGGOTH',                         [],                 [],             [],         []          ],
    ['CITY OF THE GREAT RACE',          [],                 [],             [],         []          ],
    ['ABYSS',                           [],                 [],             [],         []          ],
    ['ANOTHER DIMENSION',               [],                 [],             [],         []          ]
])

monsters = Table([
    ['name',                     'rulesets',    'abilities',  'stats'  ],
    ['BYAKHEE',                  [  ],          [  ],         [  ]     ],
    ['CULTIST',                  [  ],          [  ],         [  ]     ],
    ['DARK YOUNG',               [  ],          [  ],         [  ]     ],
    ['CHTHONIAN',                [  ],          [  ],         [  ]     ],
    ['DHOLE',                    [  ],          [  ],         [  ]     ],
    ['DIMENSIONAL SHAMBLER',     [  ],          [  ],         [  ]     ],
    ['ELDER THING',              [  ],          [  ],         [  ]     ],
    ['FIRE VAMPIRE',             [  ],          [  ],         [  ]     ],
    ['FLYING POLYP',             [  ],          [  ],         [  ]     ],
    ['FORMLESS SPAWN',           [  ],          [  ],         [  ]     ],
    ['GHOST',                    [  ],          [  ],         [  ]     ],
    ['GHOUL',                    [  ],          [  ],         [  ]     ],
    ['GOD OF THE BLOODY TONGUE', [  ],          [  ],         [  ]     ],
    ['GUG',                      [  ],          [  ],         [  ]     ],
    ['HAUNTER OF THE DARK',      [  ],          [  ],         [  ]     ],
    ['HIGH PRIEST',              [  ],          [  ],         [  ]     ],
    ['HOUND OF TINDALOS',        [  ],          [  ],         [  ]     ],
    ['MANIAC',                   [  ],          [  ],         [  ]     ],
    ['MI-GO',                    [  ],          [  ],         [  ]     ],
    ['NIGHTGAUNT',               [  ],          [  ],         [  ]     ],
    ['SHOGGOTH',                 [  ],          [  ],         [  ]     ],
    ['STAR SPAWN',               [  ],          [  ],         [  ]     ],
    ['THE BLACK MAN',            [  ],          [  ],         [  ]     ],
    ['THE BLOATED WOMAN',        [  ],          [  ],         [  ]     ],
    ['THE DARK PHARAOH',         [  ],          [  ],         [  ]     ],
    ['VAMPIRE',                  [  ],          [  ],         [  ]     ],
    ['WARLOCK',                  [  ],          [  ],         [  ]     ],
    ['WITCH',                    [  ],          [  ],         [  ]     ],
    ['ZOMBIE',                   [  ],          [  ],         [  ]     ],
])

monster_cup = [ ]

investigators = Table([
    ['name',            'damage',   'horror',   'conditions',   'focus',   'speed',   'fight',   'lore',    'location', 'random_possessions',    'equipped_items',   'exhausted_items', 'possessions'   ],
    ['Amanda Sharpe',   [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['"Ashcan" Pete',   [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Bob Jenkins',     [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Carolyn Fern',    [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Darrell Simmons', [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Dexter Drake',    [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Gloria Goldberg', [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Harvey Walters',  [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Jenny Barnes',    [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Joe Diamond',     [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Kate Winthrop',   [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Mandy Thompson',  [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Michael McGlen',  [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Monterey Jack',   [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Sister Mary',     [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ],
    ['Vincent Lee',     [],         [],         [],             [],        [],       [],         [],        [],         [],                      [],                 [],                []              ]
])

weapons = [
    ['name',                'stats'                                 ],
    ['.22 DERRINGER',       [  ]                                    ],
    ['.38 REVOLVER',        [  ]                                    ],
    ['.45 AUTOMATIC',       [  ]                                    ],
    ['AXE',                 [  ]                                    ],
    ['BULLWHIP',            [  ]                                    ],
    ['CAVALRY SABRE',       [  ]                                    ],
    ['DYNAMITE',            [  ]                                    ],
    ['KNIFE',               [  ]                                    ],
    ['RIFLE',               [  ]                                    ],
    ['SHOTGUN',             [  ]                                    ],
    ['TOMMY GUN',           [  ]                                    ],
    ['CROSS',               [  ]                                    ],
    ['ENCHANTED BLADE',     [  ]                                    ],
    ['ENCHANTED KNIFE',     [  ]                                    ],
    ['HOLY WATER',          [  ]                                    ],
    ['POWDER OF IBN-GHAZI', [  ]                                    ],
    ['SWORD OF GLORY',      [  ]                                    ],
    ['LAMP OF ALHAZRED',    [  ]                                    ]
]

weapons_deck = [ ]

consumables = [
    ['name',                    'bonus',    'price' ],
    ['FOOD',                    -1,         1       ],
    ['WHISKEY',                 -1,         1       ],
    ['LUCKY CIGARETTE CASE',    0,          1       ],
    ['RESEARCH MATERIALS',      1,          1       ]
]

consumables_deck = {
    'FOOD'                  : 2,
    'WHISKEY'               : 2,
    'LUCKY CIGARETTE CASE'  : 2,
    'RESEARCH MATERIALS'    : 2
}

tomes = [
    ['name',                'mvmt_cost',     'sanity_cost',    'modifier', 'price' ],
    ['OLD JOURNAL',         [],              [],              [],         []       ],
    ['ANCIENT TOME',        [],              [],              [],         []       ],
    ['BOOK OF DZYAN',       [],              [],              [],         []       ],
    ['CABALA OF SABOTH',    [],              [],              [],         []       ],
    ['CULTES DES GOULES',   [],              [],              [],         []       ],
    ['NAMELESS CULTES',     [],              [],              [],         []       ],
    ['NECRONOMICON',        [],              [],              [],         []       ],
    ['THE KING IN YELLOW',  [],              [],              [],         []       ]
]

tomes_deck = [ ]

passive_buffs = [
    ['name',            'bonus',    'price'  ],
    ['DARK CLOAK',      [],         []       ],
    ['LANTERN',         [],         []       ],
    ['PALLID MASK',     [],         []       ],
    ["RUBY OF R'LYEH",  [],         []       ],
    ['SPEED',           [],         []       ],
    ['SNEAK',           [],         []       ],
    ['FIGHT',           [],         []       ],
    ['WILL',            [],         []       ],
    ['LORE',            [],         []       ],
    ['LUCK',            [],         []       ],
]

passive_buffs_deck = [ ]

active_buffs = [
    ['name',                'bonus',    'price' ],
    ['MAP OF ARKHAM',       [ ],          [ ]       ],
    ['MOTORCYCLE',          [ ],          [ ]       ],
    ['BRAVERY',             [ ],          [ ]       ],
    ['STEALTH',             [ ],          [ ]       ],
    ['EXPERT OCCULTIST',    [ ],          [ ]       ],
    ['MARKSMAN',            [ ],          [ ]       ]
]

active_buffs_deck = [ ]

oddities = [
    ['name',                        'price'           ],
    ['ALIEN STATUE',                [ ]               ],
    ['BLUE WATCHER OF THE PYRAMID', [ ]               ],
    ["DRAGON'S EYE",                [ ]               ],
    ['FLUTE OF THE OUTER GODS',     [ ]               ],
    ['GATE BOX',                    [ ]               ],
    ['HEALING STONE',               [ ]               ],
    ['OBSIDIAN STATUE',             [ ]               ],
    ['SILVER KEY',                  [ ]               ],
    ['WARDING STATUE',              [ ]               ],
    ['ELDER SIGN',                  [ ]               ],
    ['ENCHANTED JEWELRY',           [ ]               ]
]

oddities_deck = [ ]

spells_deck = [ ]

allies_deck = [ ]

gates = Table([
    ['name',                        'modifier'  ],
    ['YUGGOTH',                     []          ],
    ['THE CITY OF THE GREAT RACE',  []          ],
    ['THE PLATEAU OF LENG',         []          ],
    ['THE ABYSS',                   []          ],
    ['ANOTHER DIMENSION',           []          ],
    ['THE GREAT HALL OF CELEANO',   []          ],
    ['THE DREAMLANDS',              []          ],
    ["R'LYEH",                      []          ],
])

gates_deck = [ ]