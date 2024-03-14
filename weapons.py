# constants


'''
constants...
    Rarity: common
            unique
    Modalilty: physical
               magical
    Uses: integer
    Hands: integer
defaults...
    Bonus: integer
    SanCost: integer
    Exhaustable: 0 = False
                 1 = True
    Losable: 0 = False
             1 = True
    Price: integer
'''

constants = [
    ['name',                'rarity',       'uses',         'hands',    'description'                                               ],
    ['.22 DERRINGER',       'common',       float('inf'),   1,          'A classic, slow-firing weapon, this pistol packs a punch'  ],
    ['.38 REVOLVER',        'common',       float('inf'),   1,          'A standard issue police officer\'s sidearm'                ],
    ['.45 AUTOMATIC',       'common',       float('inf'),   1,          'A standard issue Army sidearm'                             ],
    ['AXE',                 'common',       float('inf'),   1,          'Used for felling, not splitting'                           ],
    ['BULLWHIP',            'common',       float('inf'),   1,          'Indy? Is that you?'                                        ],
    ['CAVALRY SABRE',       'common',       float('inf'),   1,          'A trusty sword, but no trusty steed?'                      ],
    ['DYNAMITE',            'common',       1,              2,          'TNT stands for "blow them all to hell"'                    ],
    ['KNIFE',               'common',       float('inf'),   1,          'A simple hunting knife'                                    ],
    ['RIFLE',               'common',       float('inf'),   2,          'A simply hunting rifle'                                    ],
    ['SHOTGUN',             'common',       float('inf'),   2,          'A "duster," like what they used in bank robberies'         ],
    ['TOMMY GUN',           'common',       float('inf'),   2,          'Excellent for suppressive fire'                            ],
    ['CROSS',               'common',       float('inf'),   1,          'Abominations loathe faith and religion (+3 vs. UNDEAD)'                    ],
    ['ENCHANTED BLADE',     'unique',       float('inf'),   1,          'A truly unique piece of craftsmanship'                     ],
    ['ENCHANTED KNIFE',     'unique',       float('inf'),   1,          'It glints even when there is no light'                     ],
    ['HOLY WATER',          'unique',       1,              2,          'Blessed by the St. Ignatius, patron of knowledge '         ],
    ['POWDER OF IBN-GHAZI', 'unique',       1,              2,          'An alchemist\'s invention; powerful stuff'                 ],
    ['SWORD OF GLORY',      'unique',       float('inf'),   2,          'Ancient, yet somehow still sharp'                          ],
    ['LAMP OF ALHAZRED',    'unique',       float('inf'),   2,          'You rub, yet no genie. What gives?'                        ]
]

# defaults

defaults = [
    ['name',                'stats'                 ],
    ['.22 DERRINGER',       [ 0, 2, 0, 0, 0, 3 ] ],
    ['.38 REVOLVER',        [ 0, 3, 0, 0, 1, 4 ] ],
    ['.45 AUTOMATIC',       [ 0, 4, 0, 0, 1, 5 ] ],
    ['AXE',                 [ 0, 2, 0, 0, 1, 3 ] ],
    ['BULLWHIP',            [ 0, 1, 0, 1, 1, 2 ] ],
    ['CAVALRY SABRE',       [ 0, 2, 0, 0, 1, 3 ] ],
    ['DYNAMITE',            [ 0, 8, 0, 0, 1, 4 ] ],
    ['KNIFE',               [ 0, 1, 0, 0, 1, 2 ] ],
    ['RIFLE',               [ 0, 5, 0, 0, 1, 6 ] ],
    ['SHOTGUN',             [ 0, 4, 0, 0, 1, 6 ] ],
    ['TOMMY GUN',           [ 0, 6, 0, 0, 1, 7 ] ],
    ['CROSS',               [ 1, 0, 0, 0, 1, 3 ] ],
    ['ENCHANTED BLADE',     [ 1, 4, 0, 0, 1, 6 ] ],
    ['ENCHANTED KNIFE',     [ 1, 3, 0, 0, 1, 5 ] ],
    ['HOLY WATER',          [ 1, 6, 0, 0, 1, 4 ] ],
    ['POWDER OF IBN-GHAZI', [ 1, 9, 1, 0, 1, 6 ] ],
    ['SWORD OF GLORY',      [ 1, 6, 0, 0, 1, 8 ] ],
    ['LAMP OF ALHAZRED',    [ 1, 5, 0, 0, 1, 7 ] ]
]

deck_defaults = {
    '.22 DERRINGER' : 2,
    '.38 REVOLVER' : 2,
    '.45 AUTOMATIC' : 2,
    'AXE' : 2,
    'BULLWHIP' : 2,
    'CAVALRY SABRE' : 2,
    'DYNAMITE' : 2,
    'KNIFE' : 2,
    'RIFLE' : 2,
    'SHOTGUN' : 2,
    'TOMMY GUN' : 2,
    'CROSS' : 2,
    'ENCHANTED BLADE' : 2,
    'ENCHANTED KNIFE' : 2,
    'HOLY WATER' : 4,
    'POWDER OF IBN-GHAZI' : 1,
    'SWORD OF GLORY' : 1,
    'LAMP OF ALHAZRED' : 1
}

# transforms

transforms = [
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

deck_transforms = [ ]

# transformers

def increase( vector, dimension ):
    """ Increases a dimension in a vector by 1 """
    return [ v+1 if i == dimension else v for i,v in enumerate(vector) ]

def decrease( vector, dimension ):
    """ Decreases a dimension in a vector by 1 """
    return [ v-1 if i == dimension else v for i,v in enumerate(vector) ]

def cycle( vector, dimension ):
    """ Switches a dimension in a vector back and forth between 0 and 1 """
    return [ (v+1)%2 if i == dimension else v for i,v in enumerate(vector) ]

def change_modality( vector ):
    """ Changes a physical weapon in a magical one, a magical into physical """
    return cycle( vector, 0 )

def inc_bonus( vector ):
    """ Increases weapon bonus """
    return increase( vector, 1 )

def dec_bonus( vector ):
    """ Decreases weapon bonus """
    return decrease( vector, 1 )

def inc_san_cost( vector ):
    """ Increases weapon sanity cost """
    return increase( vector, 2 )

def dec_san_cost( vector ):
    """ Decrease weapon sanity cost """
    return decrease( vector, 2 )

def change_exhaust( vector ):
    """ Makes a non-exhaustible weapon exhaustible, exhaustible to non """
    return cycle( vector, 3 )

def change_losable( vector ):
    """ Makes a non-losable weapon losable, losable to non """
    return cycle( vector, 4 )

def inc_price( vector ):
    """ Increases the weapon price """
    return increase( vector, 5 )

def dec_price( vector ):
    return decrease( vector, 5 )


# validators