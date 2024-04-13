from classes.table import Table

board = {
    'investigators'         :   [ ],
    'currentPlayer'        :   [ ],
    'currentPhase'         :   [ ],
    'bookkeeping'           :   [ ],
    'ancientOne'           :   [ ],
    'awakened'              :   [ ],
    'doomTrack'            :   [ ],
    'terrorTrack'          :   [ ],
    'gatesInArkham'       :   [ ],
    'gatesSealed'          :   [ ],
    'cluesToSeal'         :   [ ],
    'winCond'              :   [ ],
    'gateLimit'            :   [ ],
    'monstersInArkham'    :   [ ],
    'monstersInOutskirts' :   [ ],
    'monsterLocations'     :   [ ]
}

locations = Table([
    ['name',                                            'investigators',    'occupants',    'gateTo',  'status'    ],
    ['CURIOSITIE SHOPPE',                               [],                 [],             [],         []          ],
    [ 'NEWSPAPER' ,                                     [],                 [],             [],         []          ],
    ['TRAIN STATION',                                   [],                 [],             [],         []          ],
    ['ARKHAM ASYLUM',                                   [],                 [],             [],         []          ],
    ['BANK OF ARKHAM',                                  [],                 [],             [],         []          ],
    ['INDEPENDENCE SQUARE',                             [],                 [],             [],         []          ],
    ['HIBB\'S ROADHOUSE',                               [],                 [],             [],         []          ],
    ['POLICE STATION',                                  [],                 [],             [],         []          ],
    ['JAIL CELL',                                       [],                 [],             [],         []          ],
    ['VELMA\'S DINER',                                  [],                 [],             [],         []          ],
    ['RIVER DOCKS',                                     [],                 [],             [],         []          ],
    ['THE UNNAMABLE',                                   [],                 [],             [],         []          ],
    ['UNVISITED ISLE',                                  [],                 [],             [],         []          ],
    ['BLACK CAVE',                                      [],                 [],             [],         []          ],
    ['GENERAL STORE',                                   [],                 [],             [],         []          ],
    ['GRAVEYARD',                                       [],                 [],             [],         []          ],
    ['ADMINISTRATION',                                  [],                 [],             [],         []          ],
    ['SCIENCE BUILDING',                                [],                 [],             [],         []          ],
    ['LIBRARY',                                         [],                 [],             [],         []          ],
    ['THE WITCH HOUSE',                                 [],                 [],             [],         []          ],
    ['THE SILVER TWILIGHT LODGE',                       [],                 [],             [],         []          ],
    ['THE INNER SANCTUM',                               [],                 [],             [],         []          ],
    ['ST. MARY\'S HOSPITAL',                            [],                 [],             [],         []          ],
    ['WOODS',                                           [],                 [],             [],         []          ],
    ['YE OLDE MAGICK SHOPPE',                           [],                 [],             [],         []          ],
    ['MA\'S BOARDING HOUSE',                            [],                 [],             [],         []          ],
    ['HISTORICAL SOCIETY',                              [],                 [],             [],         []          ],
    ['SOUTH CHURCH',                                    [],                 [],             [],         []          ],
    ['NORTHSIDE STREETS',                               [],                 [],             [],         []          ],
    ['DOWNTOWN STREETS',                                [],                 [],             [],         []          ],
    ['EASTTOWN STREETS',                                [],                 [],             [],         []          ],
    ['MERCHANT DISTRICT STREETS',                       [],                 [],             [],         []          ],
    ['RIVERTOWN STREETS',                               [],                 [],             [],         []          ],
    ['MISKATONIC UNIVERSITY STREETS',                   [],                 [],             [],         []          ],
    ['FRENCH HILL STREETS',                             [],                 [],             [],         []          ],
    ['UPTOWN STREETS',                                  [],                 [],             [],         []          ],
    ['SOUTHSIDE STREETS',                               [],                 [],             [],         []          ],
    ['OUTSKIRTS',                                       [],                 [],             [],         []          ],
    ['THE SKY',                                         [],                 [],             [],         []          ],
    ["R'LYEH",                                          [],                 [],             [],         []          ],
    ["NIGHTMARE CORPSE-CITY",                           [],                 [],             [],         []          ],
    ['THE PLATEAU OF LENG',                             [],                 [],             [],         []          ],
    ['HIDEOUS TABLELANDS',                              [],                 [],             [],         []          ],
    ["THE DREAMLANDS",                                  [],                 [],             [],         []          ],
    ["CARTER'S QUEST",                                  [],                 [],             [],         []          ],
    ['THE GREAT HALL OF CELEANO',                       [],                 [],             [],         []          ],
    ['THE STOLEN LIBRARY',                              [],                 [],             [],         []          ],
    ['YUGGOTH',                                         [],                 [],             [],         []          ],
    ['FUNGOID PLANET',                                  [],                 [],             [],         []          ],
    ['THE CITY OF THE GREAT RACE',                      [],                 [],             [],         []          ],
    ['PNAKOTUS',                                        [],                 [],             [],         []          ],
    ['THE ABYSS',                                       [],                 [],             [],         []          ],
    ['HOME OF LIVING SHADOW',                           [],                 [],             [],         []          ],
    ['ANOTHER DIMENSION',                               [],                 [],             [],         []          ],
    ['THE ALTERNATIVE WORLD',                           [],                 [],             [],         []          ]
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

monsterCup = [ ]

investigators = Table([
    ['name',            'damage',   'horror',   'conditions',   'focus',   'speed',   'fight',   'lore',    'location', 'randomPossessions',    'equippedItems',   'exhaustedItems', 'possessions'   ],
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

weapons = Table([
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
])

weaponsDeck = [ ]

consumables = Table([
    ['name',                    'stats',  ],
    ['FOOD',                    [ ],      ],
    ['WHISKEY',                 [ ],      ],
    ['LUCKY CIGARETTE CASE',    [ ],      ],
    ['RESEARCH MATERIALS',      [ ],      ]
])

consumablesDeck = [ ]


tomes = Table([
    ['name',                'stats',     ],
    ['OLD JOURNAL',         [],          ],
    ['ANCIENT TOME',        [],          ],
    ['BOOK OF DZYAN',       [],          ],
    ['CABALA OF SABOTH',    [],          ],
    ['CULTES DES GOULES',   [],          ],
    ['NAMELESS CULTES',     [],          ],
    ['NECRONOMICON',        [],          ],
    ['THE KING IN YELLOW',  [],          ]
])

tomesDeck = [ ]

passiveBuffs = Table([
    ['name',            'stats'      ],
    ['DARK CLOAK',      [],          ],
    ['LANTERN',         [],          ],
    ['PALLID MASK',     [],          ],
    ["RUBY OF R'LYEH",  [],          ],
    ['SPEED',           [],          ],
    ['SNEAK',           [],          ],
    ['FIGHT',           [],          ],
    ['WILL',            [],          ],
    ['LORE',            [],          ],
    ['LUCK',            [],          ],
])

passiveBuffsDeck = [ ]

activeBuffs = Table([
    ['name',                'stats',    ],
    ['MAP OF ARKHAM',       [ ],        ],
    ['MOTORCYCLE',          [ ],        ],
    ['BRAVERY',             [ ],        ],
    ['STEALTH',             [ ],        ],
    ['EXPERT OCCULTIST',    [ ],        ],
    ['MARKSMAN',            [ ],        ]
])

activeBuffsDeck = [ ]

oddities = Table([
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
])

odditiesDeck = [ ]

spellsDeck = [ ]

alliesDeck = [ ]

gates = Table([
    ['name',                        'modifier'  ],
    ['ANOTHER DIMENSION',           []          ],
    ['THE ABYSS',                   []          ],
    ['THE CITY OF THE GREAT RACE',  []          ],
    ['THE DREAMLANDS',              []          ],
    ['THE GREAT HALL OF CELEANO',   []          ],
    ['THE PLATEAU OF LENG',         []          ],
    ["R'LYEH",                      []          ],
    ['YUGGOTH',                     []          ],
])

gatesDeck = [ ]

mythosEffects = {
    'headline'      : [],
    'mystic'        : [],
    'urban'         : [],
    'weather'       : [],
    'modifiers'     : [],
    'resolution'    : [],
    'bannedMonster' : []
}

mythosDeck = [ ]

graph = [ ]
leftGraph = [ ]
rightGraph = [ ]