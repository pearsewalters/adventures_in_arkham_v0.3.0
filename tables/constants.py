from classes.table import Table
from classes.data import Ability, Mythos
from classes.mythosEffects import Effects, Resolutions
from classes.encountersEffects import specialEffects
from classes import abilities

ancientOnes = Table([
    ['name',        'title',                'combatMod',   'defenses',                                                             'worshippers',                                                                                                                                                                  'power',                                                                                                                            'startOfBattle',                                                                      'attack',                                                                                                                                           'doomTrack'],
    ['AZATHOTH',    'the Daemon Sultan',    float('-inf'),  'There is nothing to defend; AZATHOTH\'s omnipotence is everlasting.',  'Since Azathoth promises nothing except destruction, only the insane worship him. However, their fanaticism gives them strength. MANIACS have their TOUGHNESS increased by 1.', 'ABSOLUTE DESTRUCTION - If Azathoth awakens, the game is over and the investigators lose.',                                         'The world ends, as it never began. Your existence is over, as you never came to be.',  'The end is here! Azathoth destroys the world.',                                                                                                    14          ],
    ['CTHULHU',     'the Dreamer',          -6,             'CTHULHU will spread more doom with every attack.',                     'Cthulhu\'s worshippers often have the Innsmouth Look, a sign of monstrous ancestors. CULTISTS have a HORROR RATING of -2, traumatizing their beholder with 2 HORROR.',         'DREAMS OF MADNESS - While Cthulhu stirs in his slumber, INVESTIGATORS have their maximum HORROR and maximum DAMAGE reduced by 1.', 'Pray that you may last long enough to witness the glory of Dreamer CTHULTHU.',         'Each INVESTIGATOR\'s maximum HORROR or maximum DAMAGE will reduce by 1 until they are devoured. After CTHULHU attacks, he will spread more doom.', 13          ],
])

locations = Table([
    ['name',                                            'neighborhood',           'variety',     'special', 'guaranteed',     'possible',                  'instability', 'mystery' ],
    ['CURIOSITIE SHOPPE',                               'NORTHSIDE',              'LOCATION',    True,      'unique items',   'common items',              0 ,            0         ],          
    ['NEWSPAPER',                                       'NORTHSIDE',              'LOCATION',    False,     None,             'money,clues',               0 ,            0         ],
    ['TRAIN STATION',                                   'NORTHSIDE',              'LOCATION',    False,     None,             'common items,unique items', 0 ,            0         ],
    ['ARKHAM ASYLUM',                                   'DOWNTOWN',               'LOCATION',    True,      'sanity',         'common items',              0 ,            0         ],
    ['BANK OF ARKHAM',                                  'DOWNTOWN',               'LOCATION',    True,      'money',          'blessing',                  0 ,            0         ],
    ['INDEPENDENCE SQUARE',                             'DOWNTOWN',               'LOCATION',    False,     None,             'common items,unique items', 10,            4         ],
    ['HIBB\'S ROADHOUSE',                               'EASTTOWN',               'LOCATION',    False,     None,             'money,common items',        2 ,            5         ],
    ['POLICE STATION',                                  'EASTTOWN',               'LOCATION',    True,      None,             'common items,clues',        0 ,            0         ],
    ['JAIL CELL',                                       'EASTTOWN',               'LOCATION',    False,     None,             None,                        0 ,            0         ],
    ['VELMA\'S DINER',                                  'EASTTOWN',               'LOCATION',    False,     None,             'money,stamina',             0 ,            0         ],
    ['RIVER DOCKS',                                     'MERCHANT DISTRICT',      'LOCATION',    True,      'money',          'common items',              0 ,            0         ],
    ['THE UNNAMABLE',                                   'MERCHANT DISTRICT',      'LOCATION',    False,     None,             'unique items,clues',        6 ,            9         ],
    ['UNVISITED ISLE',                                  'MERCHANT DISTRICT',      'LOCATION',    False,     None,             'clues,spells',              10,            5         ],
    ['BLACK CAVE',                                      'RIVERTOWN',              'LOCATION',    False,     None,             'common items,spells',       6 ,            10        ],
    ['GENERAL STORE',                                   'RIVERTOWN',              'LOCATION',    True,      'common items',   'money',                     0 ,            0         ],
    ['GRAVEYARD',                                       'RIVERTOWN',              'LOCATION',    True,      None,             'clues,unique items',        6 ,            2         ],
    ['ADMINISTRATION',                                  'MISKATONIC UNIVERSITY',  'LOCATION',    True,      'skills',         'money',                     0 ,            0         ],
    ['SCIENCE BUILDING',                                'MISKATONIC UNIVERSITY',  'LOCATION',    True,      'clues',          'unique items',              2 ,            8         ],
    ['LIBRARY',                                         'MISKATONIC UNIVERSITY',  'LOCATION',    False,     None,             'unique items,clues',        0 ,            0         ],
    ['THE WITCH HOUSE',                                 'FRENCH HILL',            'LOCATION',    False,     None,             'clues,spells',              10,            1         ], 
    ['THE SILVER TWILIGHT LODGE',                       'FRENCH HILL',            'LOCATION',    True,      None,             'unique items,clues',        2 ,            2         ],
    ['THE INNER SANCTUM',                               'FRENCH HILL',            'LOCATION',    False,     None,             None,                        0 ,            0         ], # Inner Sanctum won't ever have a gate on it, since it's only adjacent to the Lodge
    ["ST. MARY'S HOSPITAL",                             'UPTOWN',                 'LOCATION',    True,      'stamina',        'clues',                     0 ,            0         ],
    ['WOODS',                                           'UPTOWN',                 'LOCATION',    False,     None,             'money,common items',        10,            6         ],
    ['YE OLDE MAGICK SHOPPE',                           'UPTOWN',                 'LOCATION',    True,     'spells',          'unique items',              0 ,            0         ],
    ['MA\'S BOARDING HOUSE',                            'SOUTHSIDE',              'LOCATION',    True,     'allies',          'stamina',                   0 ,            0         ],
    ['HISTORICAL SOCIETY',                              'SOUTHSIDE',              'LOCATION',    False,    None,              'skills,spells',             2 ,            8         ],
    ['SOUTH CHURCH',                                    'SOUTHSIDE',              'LOCATION',    specialEffects.southChurch,     'blessing',        'sanity',                    0 ,            0         ],
    ['NORTHSIDE STREETS',                               'NORTHSIDE',              'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['DOWNTOWN STREETS',                                'DOWNTOWN',               'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['EASTTOWN STREETS',                                'EASTTOWN',               'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['MERCHANT DISTRICT STREETS',                       'MERCHANT DISTRICT',      'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['RIVERTOWN STREETS',                               'RIVERTOWN',              'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['MISKATONIC UNIVERSITY STREETS',                   'MISKATONIC UNIVERSTITY', 'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['FRENCH HILL STREETS',                             'FRENCH HILL',            'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['UPTOWN STREETS',                                  'UPTOWN',                 'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['SOUTHSIDE STREETS',                               'SOUTHSIDE',              'STREETS',     False,    None,              None,                        0 ,            0         ],
    ['OUTSKIRTS',                                       'OUTSKIRTS',              'SPECIAL',     False,    None,              None,                        0 ,            0         ],
    ['THE SKY',                                         'THE SKY',                'SPECIAL',     False,    None,              None,                        0,             0,        ],
    ["R'LYEH",                                          'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ["NIGHTMARE CORPSE-CITY",                   'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE PLATEAU OF LENG',                                 'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['HIDEOUS TABLELANDS',             'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ["THE DREAMLANDS",                                  'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ["CARTER'S QUEST",                  'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE GREAT HALL OF CELEANO',                       'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE STOLEN LIBRARY',   'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['YUGGOTH',                                         'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['FUNGOID PLANET',                         'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE CITY OF THE GREAT RACE',                      'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['PNAKOTUS',            'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE ABYSS',                                       'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['HOME OF LIVING SHADOW',                'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['ANOTHER DIMENSION',                               'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ],
    ['THE ALTERNATIVE WORLD',        'OTHER WORLD',            'OTHER WORLD', False,    None,              None,                        0 ,            0         ]
])

monsters = Table([
    ['name',                    'dimension', 'variety' ],
    ['BYAKHEE',                  0,          'standard'],
    ['CHTHONIAN',                1,          'standard'],
    ['CULTIST',                  5,          'standard'],
    ['DARK YOUNG',               4,          'standard'],
    ['DHOLE',                    0,          'standard'],
    ['DIMENSIONAL SHAMBLER',     2,          'standard'],
    ['ELDER THING',              3,          'standard'],
    ['FIRE VAMPIRE',             6,          'standard'],
    ['FLYING POLYP',             4,          'standard'],
    ['FORMLESS SPAWN',           4,          'standard'],
    ['GHOST',                    5,          'standard'],
    ['GHOUL',                    4,          'standard'],
    ['GUG',                      7,          'standard'],
    ['HIGH PRIEST',              8,          'standard'],
    ['HOUND OF TINDALOS',        2,          'standard'],
    ['MANIAC',                   5,          'standard'],
    ['MI-GO',                    0,          'standard'],
    ['NIGHTGAUNT',               7,          'standard'],
    ['SHOGGOTH',                 3,          'standard'],
    ['STAR SPAWN',               8,          'standard'],
    ['VAMPIRE',                  5,          'standard'],
    ['WARLOCK',                  0,          'standard'],
    ['WITCH',                    0,          'standard'],
    ['ZOMBIE',                   5,          'standard'],
    ['GOD OF THE BLOODY TONGUE', 1,          'mask'    ],
    ['HAUNTER OF THE DARK',      2,          'mask'    ],
    ['THE BLACK MAN',            5,          'mask'    ],
    ['THE BLOATED WOMAN',        4,          'mask'    ],
    ['THE DARK PHARAOH',         7,          'mask'    ]
])

investigators = Table([
    ['name',	        'nickname',	            'occupation',	    'home',	                    'story',    'expansion' ],
    ['Harvey Walters',  'Professor Walters',    'the Professor',    'ADMINISTRATION',           "Harvey is a visiting Professor at Miskatonic University. With Doctorates in History and Archaeology, he has uncovered several interesting artifacts over the years and learned a little of the arcane arts. Recently, by carefully studying the papers and talking to people in the streets, he has begun to detect a disturbance in the city-- something that could potentially herald the arrival of something unthinkable from beyond time and space.\n\nChecking his notes, Professor Walters prepares himself for one last trip into the streets of Arkham to confirm his theory. If he's right, it could spell the end of everything.",                                                                                                                                                                                                                                                                                                                                                   'base'      ],
    ['Amanda Sharpe',   'Amanda',               'the Student',      'BANK OF ARKHAM',           "Amanda has been a student at Miskatonic University for 2 years now. On her way to talk to one of her professors last month, she saw a painting in the hallway that captured her attention with its hazy depiction of some horrible creature rising up out of the ocean. Ever since, Amanda has heard strange whispers in a foreign language whenever her attention drifts. More disturbingly, she has begun to dream of the vast green depths of the ocean and terrible alien cities that lie in its darkest crevasses.\n\nThis evening, as she finishes her shift as a bank teller at the First Bank of Arkham, something out of the night calls to her-- something dark and sinister that leaves the feel of sea foam in her mind and makes her gasp with the effort of resisting it. Leaning against the brick wall of the bank, Amanda realizes that she has to find out what's happening to her or she's going to fall prey to whatever alien presence is invading her mind.",             'base'      ],
    ['Carolyn Fern',    'Dr. Fern',             'the Psychologist', 'ARKHAM ASYLUM',            'Carolyn is a first year resident at a sanitarium in Providence. Over the past six months, she has been studying the dreams of her patients using hypnosis. One patient in particular gave her vivid and disturbing descriptions of his dreams, right up until he was murdered with a strange knife that closely resembled something from one of his nightmares.\n\nDisturbed and frightened by his murder, Carolyn dug back through her notes, poring over them late into the night. Finally, she found some subtle clues that led her here, to Arkham, where he was previously an inmate in Arkham Asylum. Someone here has to know why a harmless man was murdered for talking about his dreams to his psychologist.',                                                                                                                                                                                                                                                                        'base'      ],
    ['Jenny Barnes',    'Ms. Barnes',           'the Dilettante',   'TRAIN STATION',            "The job sounded simple enough-- pick up a statue at the Providence Museum and deliver it to a guy at the Silver Twilight Lodge. The money was good, and the dame who gave him the job seemed sincere.\n\nSadly, things never seem to work out that easily for Joe. Now the statue is missing, two people are dead, strange cultists are on his tail, and all clues lead to Arkham. Lady Luck can be funny that way.\n\nHe's already tried talking to the Sheriff, but that flatfoot proved to be worse than useless. Looks like it's once again going to be up to Joe Diamond to solve the case.",                                                                                                                                                                                                                                                                                                                                                                                              'base'      ],
    ['"Ashcan" Pete',   'Pete',                 'the Drifter',      'RIVER DOCKS',              "When you've lived on the streets as long as Pete has, you see things. Things that would drive braver men screaming into the night. But you also learn to be quiet, to stay hidden, and to play stupid if all else fails. It also helps to have a good dog, like Duke, to scare away the meaner elements of the street.\n\nUnfortunately, this time, Pete can't hide, and there's nothing Duke can do to protect him. His nightmares have been growing steadily worse over the last month, driving him all the way here... to Arkham. Even the whiskey isn't helping much anymore. Soon, he won't be able to sleep at all. Still, there are always opportunities for a man who knows how to stay quiet... as long as he isn't too picky.",                                                                                                                                                                                                                                                       'base'      ],
    ['Bob Jenkins',     'Bob',                  'the Salesman',     'GENERAL STORE',            'As a traveling salesman, Bob is always on the go. But yesterday, he saw something that made him decide to stay in Arkham and miss his train. While he was in the General Store selling his wares, a robed man came in and bought several items, paying with old gold coins. Astounded, Bob turned to the shopkeeper for an explanation, but the man just ignored his questions, simply saying, "That happens, sometimes."\n\nNow, Bob isn\'t leaving until he figues out where those gold coins came from. If he plays his cards right, maybe this will be the big score. Maybe he\'ll finally be able to retire and buy that boat he\'s had his eye on and spend the rest of his days fishing in a tropical paradise. Then again, moybe Bob will finally come to see that all that glitters is not gold.',                                                                                                                                                                                     'base'      ],
    ['Darrell Simmons', 'Darrell',              'the Photographer', 'NEWSPAPER',                "Even while growing up in Arkham, Darrell always knew that there was something not quite right about the strange little town. After graduating from high school, he went to work for the Arkham Advertiser as a photographer, and in the years since, he's crawled over every square inch of the city.\n\nLast night, however, Darrell saw something horrible-- something that has shaken his world to its core and torn away the safe illusions we all foster to protect our minds and our souls. His editor says he was just seeing things, but as he leaves the newspaper building, he knows just what he saw and he intends to show the world! This time he'll be more careful. This time he'll take pictures and prove that things are not normal in Arkham.",                                                                                                                                                                                                                              'base'      ],
    ['Dexter Drake',    'Dexter',               'the Magician',     'YE OLDE MAGICK SHOPPE',    'After returning from his stint in the army during WWI, Dexter became a stage magician, and proved to be very successful at his trade, but he always longed to find real magic. As they say, be careful what you wish for. Years later, in a rundown store, Dexter came across a burnt and torn fragment of the Necronomicon itself. Intrigued by this ancient piece of occult knowledge, Dexter began to use his wealth in search of the truth about the ancient lore, and what he found horrified him.\n\nNow, the more he learns, the less he wants to know, but his studies have led him to believe that a great evil will soon arise in Arkham. He knows that he may well be the only person with the ability to stop this evil from swallowing the world, so he has come to that sleepy town to speak with the proprietor of Ye Olde Magick Shoppe, one of the few magic shops that contain true lore, and not merely the stage tricks he once studied.',                                  'base'      ],
    ['Gloria Goldberg', 'Gloria',               'the Author',       "VELMA'S DINER",            "As a young girl, Gloria was haunted by terrible visions. After years of visiting doctors and some therapy, she learned to control her visions somewhat by writing stories. Her weird and disturbing fiction somehow spoke to the public in these troubled times, and has made her a bestselling writer.\n\nThis evening, while leaving a book signing she's attending in Arkham, she was knocked to the ground by the most powerful vision she's ever experienced. Gloria saw the sky tear open, and a huge and montrous form pour out of the very air itself, wreaking untold havoc and killing thousands. As she sat on the ground with her arms wrapped around herself, Gloria knew, somehow, that this vision was real, and that it would come to pass unless she did something about it.\n\nNow, she finds herself in a run-down diner, sipping coffee and trying to decide what to do.",                                                                                                  'base'      ],
    ['Joe Diamond',     'Joe',                  'the Private Eye',  'POLICE STATION',           "A brilliant researcher, but a shy, lonely person, Kate Winthrop has been working at the Miskatonic Science Labs for 4 years now and her supervisor still doesn't know her name. That doesn't matter to her though, as she has been working to complete a private quest for most of that time. Almost 3 years ago, she watched as a device malfunctioned, and Professor Young, her long-time mentor and friend, was torn apart by an indistinct creature that shrieked and gibbered before vanishing into the night. Since then, she has delved into darker scientific studies, always hoping to find something that would allow her to find and defeat that creature along with others of its kind.\n\nTonight, her research has finally paid off, allowing her to create a device that can defeat the alien beings she has detected in Arkham!",                                                                                                                                               'base'      ],
    ['Kate Winthrop',   'Dr. Winthrop',         'the Scientist',    'SCIENCE BUILDING',         "A brilliant researcher, but a shy, lonely person, Kate Winthrop has been working at the Miskatonic Science Labs for 4 years now and her supervisor still doesn't know her name. That doesn't matter to her though, as she has been working to complete a private quest for most of that time. Almost 3 years ago, she watched as a device malfunctioned, and Professor Young, her long-time mentor and friend, was torn apart by an indistinct creature that shrieked and gibbered before vanishing into the night. Since then, she has delved into darker scientific studies, always hoping to find something that would allow her to find and defeat that creature along with others of its kind.\n\nTonight, her research has finally paid off, allowing her to create a device that can defeat the alien beings she has detected in Arkham!",                                                                                                                                               'base'      ],
    ['Mandy Thompson',  'Mandy',                'the Researcher',   'LIBRARY',                  'Mandy came to Arkham several years ago looking for work as a researcher for Miskatonic University. Since then, she has worked with many of the University professors, delving into esoteric tomes filled with scientific information, historical reports, and sometimes even occult ramblings.\n\nIt was while reading an old book of prophecies last week that she first felt that she had stumbled onto something big. Mandy came to believe that certain signs and portents described in the book were taking place in Arkham right now-- omens that indicated the return of a terrible being reffered to as an Ancient One, which would grind the cities of Man beneath its loathsome tread.\n\nTonight, the full moon has turned blood red, which is the final omen of the return of the Ancient One. Slipping into the night, and armed with her knowledge of the prophecy, Mandy has decided to see if she can defy fate and stop these events from taking place.',                      'base'      ],
    ['Michael McGlen',  'Michael',              'the Gangster',     "MA'S BOARDING HOUSE",      "As a soldier in the O'Bannion gang, Michael didn't really believe in all this voodoo mumbo jumbo around town. Or at least, he didn't until the night of the Foreman job, when he saw Fast Louie Farrell pulled screaming into the river by a scaly green creature. As they say, seeing is believing and Michael is starting to believe.\n\n\nNow, he has gathered his belongings together in the room that he rents at Ma's Boarding House. Louie was a friend of his, and he won't rest until he finds out what's happening in this town and avenges his buddy ...",                                                                                                                                                                                                                                                                                                                                                                                                                           'base'      ],
    ['Monterey Jack',   'Monterey',             'the Archeologist', 'CURIOSITIE SHOPPE',        "Monterey has been a globe-trotting treasure hunter and adventurer for many years. Following in his father's footsteps, he's always tried to ensure that the specific value of his finds is preserved. Recently, he followed a lead on an odd prehistoric statue to Arkham. However, when he arrived, the man he came to buy the statue from was locked up in the asylum. Monterey was just about to give up and go home in disgust when a robed figure pushed past him.\n\n\nFor just an instant, there was a flash of a silver pendant with a symbol on it Monterey would never forget. That symbol had been carved into his murdered father's forehead, and had haunted his dreams for years.\n\nChasing after the mysterious figure, he turned a corner only to discover that he had lost his quarry.\n\nHowever, Monterey knows that somewhere in Arkham may lie the answer to the mystery of his father's murder, and he's not leaving until he finds it.",                                'base'      ],
    ['Sister Mary',     'Mary',                 'the Nun',          'SOUTH CHURCH',             "Sister Mary has served the Church faithfully for many years, so when she was sent to Arkham to work with Father Michael, a man whose writings she had admired for many years, she felt that she was truly blessed. Now, after witnessing Father Michael's strange mood swings and seeing some of the bizarre practices that go on in this town, she's beginning to feel that she may have been a bit too hasty ...\n\nFor instance, last night, there was a knock on the door of the church, and when she answered it, there was nothing but a handwritten journal laying on the steps outside. Reading it, she learned of strange cults and terrible creatures that lurk in the darkness. Worse, when she laughingly showed it to Father Michael, he turned pale and threw it into the fire, yelling at her to forget what she'd seen.\n\nNow, gathering her things and quietly leaving South Church, Sister Mary has decided to investigate this town, and in so doing, reaffirm her faith.", 'base'      ],
    ['Vincent Lee',     'Dr. Lee',              'the Doctor',       "ST. MARY'S HOSPITAL",      "A Yale graduate of Medicine, Vincent has recently moved to Arkham from Boston to practice at St. Mary's Hospital. Since his coming to Arkham, he has seen far too many horrible and unexplained deaths - an elderly victim torn apart by unknown wild animals, a healthy young man whose heart exploded, and so many others. Their faces haunt his dreams, especially the young man's terrified expression. After all this, small wonder that Vincent has begun to wonder if there's something sinister going on in this quiet Massachusetts town.\n\nTonight Dr. Lee made the decision to investigate the mysteries of Arkham and stop the strange deaths. He is determined to see this through, even if in so doing he becomes another puzzle for the next doctor who comes to Arkham.",                                                                                                                                                                                                      'base'      ],
])

invAbilities = Table([
    ['name',                'investigator',     'abilityDetails',                                                                                                                                            'abilityDescription'                                                                                                                                                           ],
    ['STRONG MIND',          'Harvey Walters',   Ability.abilityDetails( variety="lossReducer",          func=None,             phase={1,2,3},  resource="sanity",  deck=None,                          amt=1   ),  'Any Phase: Harvey reduces all Sanity losses he suffers by 1, to a minumum of 0.',                                                                                             ],
    ['STUDIOUS',             'Amanda Sharpe',    Ability.abilityDetails( variety="deckDiver",            func=None,             phase={1,2,3},  resource=None,      deck="learned",                     amt=1   ),  'Whenever Amanda draws one or more cards from the Skill deck, she draws one extra card and then discards one of the cards.',                                                   ],
    ['PSYCHOLOGY',           'Carolyn Fern',     Ability.abilityDetails( variety="healer",               func=None,             phase={1,2,3},  resource="sanity",  deck=None,                          amt=1   ),  "Upkeep: Dr. Fern may restore 1 Sanity to herself or another character in her location. She cannot raise a character's Sanity higher than that character's maximum Sanity.",   ],
    ['TRUST FUND',           'Jenny Barnes',     Ability.abilityDetails( variety="resourceGenerator",    func=None,             phase={1},      resource="money",   deck=None,                          amt=1   ),  'Upkeep: Jenny gains $1',                                                                                                                                                      ],
    ['SCROUNGE',             '"Ashcan" Pete',    Ability.abilityDetails( variety="scrounger",            func=None,             phase={1,2,3},  resource=None,      deck={"common","unique","spell"},   amt=1   ),  '...'                                                                                                                                                                          ],
    ['SNOOP',                '"Ashcan" Pete',    Ability.abilityDetails( variety="snooper",              func=abilities.snoop,  phase={1,2,3},  resource=None,      deck={"commonTrash","uniqueTrash","spellTrash"},   amt=1   ),  '...'                                                                                                                                                                          ],
    ['SHREWD DEALER',        'Bob Jenkins',      Ability.abilityDetails( variety="deckDiver",            func=None,             phase={1,2,3},  resource=None,      deck="learned",                     amt=1   ),  '...'                                                                                                                                                                          ],
    ['HOMETOWN ADVANTAGE',   'Darrell Simmons',  Ability.abilityDetails( variety="deckDiver",            func=None,             phase={3},      resource=None,      deck="arkham",                      amt=1   ),  '...'                                                                                                                                                                          ],
    ['MAGICAL GIFT',         'Dexter Drake',     Ability.abilityDetails( variety="deckDiver",            func=None,             phase={1,2,3},  resource=None,      deck="spell",                       amt=1   ),  '...'                                                                                                                                                                          ],
    ['PSYCHIC SENSITIVITY',  'Gloria Goldberg',  Ability.abilityDetails( variety="deckDiver",            func=None,             phase={3},      resource=None,      deck="otherWorlds",                 amt=1   ),  '...'                                                                                                                                                                          ],
    ['HUNCHES',              'Joe Diamond',      Ability.abilityDetails( variety="checkModder",          func=None,             phase={1,2,3},  resource="clues",   deck=None,                          amt=1   ),  '...'                                                                                                                                                                          ],
    ['SCIENCE!',             'Kate Winthrop',    Ability.abilityDetails( variety="gateModder",           func=None,             phase={0},      resource=None,      deck=None,                          amt=0   ),  '...'                                                                                                                                                                          ],
])

weapons = Table([
    ['name',                'rarity',       'uses',         'hands',    'description'                                               ],
    ['.22 DERRINGER',       'common',       float('inf'),   1,          'A classic, slow-firing weapon, this pistol packs a punch'  ],
    ['.38 REVOLVER',        'common',       float('inf'),   1,          'A standard issue police officer\'s sidearm'                ],
    ['.45 AUTOMATIC',       'common',       float('inf'),   1,          'A standard issue Army sidearm'                             ],
    ['AXE',                 'common',       float('inf'),   1,          'Used for felling, not splitting'                           ],
    ['BULLWHIP',            'common',       float('inf'),   1,          'Indy? Is that you?'                                        ],
    ['CAVALRY SABRE',       'common',       float('inf'),   1,          'A trusty sword, but no trusty steed?'                      ],
    ['DYNAMITE',            'common',       1,              2,          'TNT stands for "blow them all to hell"'                    ],
    ['KNIFE',               'common',       float('inf'),   1,          'A simple hunting knife'                                    ],
    ['RIFLE',               'common',       float('inf'),   2,          'A simple hunting rifle'                                    ],
    ['SHOTGUN',             'common',       float('inf'),   2,          'A "duster," like what they used in bank robberies'         ],
    ['TOMMY GUN',           'common',       float('inf'),   2,          'Excellent for suppressive fire'                            ],
    ['CROSS',               'common',       float('inf'),   1,          'Abominations loathe faith and religion (+3 vs. UNDEAD)'    ],
    ['ENCHANTED BLADE',     'unique',       float('inf'),   1,          'A truly unique piece of craftsmanship'                     ],
    ['ENCHANTED KNIFE',     'unique',       float('inf'),   1,          'It glints even when there is no light'                     ],
    ['HOLY WATER',          'unique',       1,              2,          'Blessed by the St. Ignatius, patron of knowledge '         ],
    ['POWDER OF IBN-GHAZI', 'unique',       1,              2,          'An alchemist\'s invention; powerful stuff'                 ],
    ['SWORD OF GLORY',      'unique',       float('inf'),   2,          'Ancient, yet somehow still sharp'                          ],
    ['LAMP OF ALHAZRED',    'unique',       float('inf'),   2,          'You rub, yet no genie. What gives?'                        ]
])

consumables = Table([
    ['name',                    'rarity', 'stat',     'check',   'description'                                                                                       ],
    ['FOOD',                    'common', 'damage',   None,       'Sustenance will cure you of your physical ails. Use this to reduce your DAMAGE'                    ],
    ['WHISKEY',                 'common', 'horror',   None,       'Fortifies the mind, fortifies the spirit. Use this to reduce your HORROR'                          ],
    ['LUCKY CIGARETTE CASE',    'common', None,       'any',      'Did that just happen? Or was it your imagination? Use this to try again at a failed skill check'   ],
    ['RESEARCH MATERIALS',      'common', 'clues',    None,       'Aha! Just as you thought. Use this to gain a CLUE'                                                 ]
])

tomes = Table([
    ['name',                'rarity',   'uses',         'description'   ],
    ['ANCIENT TOME',        'common',   1,              'An old, ratty book'            ],
    ['OLD JOURNAL',         'common',   1,              'Scrawling notes of a mad person'            ],
    ['BOOK OF DZYAN',       'common',   2,              'A secret Tibetan work, written in Senzar script'            ],
    ['CABALA OF SABOTH',    'unique',   1,              'An esoteric treatise, translated by Bloch'            ],
    ['CULTES DES GOULES',   'unique',   1,              'On black magic, by the Comte d\'Erlette'            ],
    ['NAMELESS CULTS',      'unique',   1,              'A translation of von Juntz\'s Unaussprechlichen Kulten'            ],
    ['NECRONOMICON',        'unique',   float('inf'),   'Authored by Abdul Alhazred; a book of evil repute'            ],
    ['THE KING IN YELLOW',  'unique',   1,              'A strange and unsettling play, by no known author'            ]
])

passiveBuffs = Table([
    ['name',            'rarity',   'stat', 'check',    'description'   ],
    ['DARK CLOAK',      'common',   None,   'evade',    'Useful for avoiding being seen by the unseen'            ],
    ['LANTERN',         'common',   None,   'luck',     'Lucky to have a spot of light, now, don\'t you think?'            ],
    ['PALLID MASK',     'unique',   None,   'evade',    'The mask of a stranger who wears no mask'            ],
    ["RUBY OF R'LYEH",  'unique',  'mvmt',  None,       'Glinting in the light, in it you see awful, terrifying shapes'            ],
    ['SPEED',           'learned',  None,   'speed',    'You have learned to be faster on your feet (Offers a +1 bonus when using CLUES to augment SPEED checks)'            ],
    ['SNEAK',           'learned',  None,   'sneak',    'You have learned to be lighter on your feet (Offers a +1 bonus when using CLUES to augment SNEAK checks)'            ],
    ['FIGHT',           'learned',  None,   'fight',    'You have become brawnier and bolder (Offers a +1 bonus when using CLUES to augment FIGHT checks)'            ],
    ['WILL',            'learned',  None,   'will',     'Your intestinal fortitude is mightier (Offers a +1 bonus when using CLUES to augment WILL checks)'            ],
    ['LORE',            'learned',  None,   'lore',     'You learn quickly the secrets of the mythos (Offers a +1 bonus when using CLUES to augment LORE checks)'            ],
    ['LUCK',            'learned',  None,   'luck',     'Your optimism shines through (Offers a +1 bonus when using CLUES to augment LUCK checks)'            ],
])

activeBuffs = Table([
    ['name',                'rarity',   'phase',    'check',    'stat', 'description'   ],
    ['MAP OF ARKHAM',       'common',   2,          None,       'mvmt', 'Well, this is handy (try typing "map"...)'            ],
    ['MOTORCYCLE',          'common',   2,          None,       'mvmt', 'It\'s not a horse, but it will do'            ],
    ['BRAVERY',             'learned',  123,        'horror',   None,   'None are as courageous as those who learned their bravery'            ],
    ['STEALTH',             'learned',  123,        'evade',    None,   'You are an adroit rascal, a deft creep'            ],
    ['EXPERT OCCULTIST',    'learned',  123,        'spell',    None,   'You have studied the esoteric texts time and again'            ],
    ['MARKSMAN',            'learned',  123,        'combat',   None,   'Prize fighter? I barely know \'er!'            ]
])

oddities = Table([
    ['name',                        'rarity',   'description'                                                                           ],
    ['ALIEN STATUE',                'unique',   'Of unknown origin, of unknown power'                                                   ],
    ['BLUE WATCHER OF THE PYRAMID', 'unique',   'It seems to glow wildly when you hold it in your hands'                                ],
    ["DRAGON'S EYE",                'unique',   'Would you not peer into the future if given the chance?'                               ],
    ['ELDER SIGN',                  'unique',   'Could it be? The sigil of lore? A ward against these arcane portals?'                  ],
    ['ENCHANTED JEWELRY',           'unique',   'It begs to be worn like armor'                                                         ],
    ['FLUTE OF THE OUTER GODS',     'unique',   'Made of a wood you\'ve never felt, tuned in a key you\'ve never heard'                 ],
    ['GATE BOX',                    'unique',   'It seems...bigger on the inside than on the outside, somehow'                          ],
    ['HEALING STONE',               'unique',   'It gives you a regenerative sensation just to hold it'                                 ],
    ['OBSIDIAN STATUE',             'unique',   'It feels magnetic, but not toward iron...'                                             ],
    ['SILVER KEY',                  'unique',   'This would open a door, if keyholes were shaped like that'                             ],
    ['WARDING STATUE',              'unique',   'It seems to absorb your touch, as if the impact of your fingers were nothing to it'    ],
])

spells = Table([
    ['name',                        'modifier', 'sanityCost',  'phase', 'hands',   'description' ],
    ['BIND MONSTER',                +4,         2,              123,    2,         'Cast to immediately dispatch a MONSTER. This spell is powerful and is immediately forgotten after successful casting.'                                                                     ],
    ['DREAD CURSE OF AZATHOTH',     -2,         2,              123,    2,         'Cast to gain +9 to all COMBAT CHECKS until the end of COMBAT. This spell is EXHAUSTED after successful casting.'                                                                           ],
    ['ENCHANT WEAPON',              +0,         1,              123,    0,         'Cast to make one PHYSICAL WEAPON a MAGICAL WEAPON until the end of this combat.This spell is EXHAUSTED after successful casting.'                                                          ],
    ['FIND GATE',                   -1,         1,              2,       0,         'Cast to immediately return to Arkham from an OTHER WORLD. This spell will not work if you are in Arkham, and is EXHAUSTED after successful casting.'                                       ],
    ['FLESH WARD',                  -2,         1,              123,    0,         'Cast to ignore DAMAGE received from a single source. This spell is EXHAUSTED after successful casting.'                                                                                    ],
    ['HEAL',                        +1,         1,              1,       0,         'Cast to remove DAMAGE from yourself or another investigator in your AREA. This spell is EXHAUSTED after successful casting.'                                                               ],
    ['MISTS OF RELEH',              +0,         0,              123,    0,         'Cast to immediately EVADE a MONSTER. This spell is EXHAUSTED after successful casting.'                                                                                                    ],
    ["RED SIGN OF SHUDDE M'ELL",    -1,         1,              123,    1,         'Cast to decrease the TOUGHNESS of a MONSTER by 1 (to a minimum of 1), and ignore 1 ABILITY of that MONSTER, until the end of COMBAT. This spell is EXHAUSTED after successful casting.'    ],
    ['SHRIVELLING',                 -1,         1,              123,    1,         'Cast to gain +6 to all COMBAT CHECKS until the end of COMBAT. This spell is EXHAUSTED after successful casting.'                                                                           ],
    ['VOICE OF RA',                 -1,         1,              1,       0,         'Cast to gain +1 to all SKILL CHECKS for the rest of this turn. This spell is EXHAUSTED after successful casting.'                                                                          ],
    ['WITHER',                      +0,         0,              123,    1,         'Cast to gain +3 to all COMBAT CHECKS until the end of COMBAT. This spell is EXHAUSTED after successful casting.'                                                                           ]
])

allies = Table([
    ['name',                    'description',                                                                                                                                    'description'   ],
    ['ANNA KASLOW'              '+2 LUCK. Gain 2 CLUES when ANNA KASLOW joins you',                                                                                         None            ],
    ['DUKE'                     '+1 max HORROR. Let DUKE run away (type "run away DUKE") to restore your sanity, reducing your HORROR to 0',                                None            ],
    ['ERIC COLT'                '+2 SPEED. With ERIC COLT by your side, you receive no extra HORROR when combatting NIGHTMARISH MONSTERS',                                  None            ],
    ['JOHN LEGRASSE'            '+2 WILL. With JOHN LEGRASSE by your side, you can claim MONSTER TROPHIES for ENDLESS MONSTERS',                                            None            ],
    ['PROFESSOR ARMITAGE'       '+2 LORE. With PROF. ARMITAGE by your side, your attacks are unaffected by MAGICAL RESISTANCE',                                             None            ],
    ['RICHARD UPTON PICKMAN'    '+1 SPEED, +1 LUCK. With RICHARD UPTON PICKMAN by your side, your attacks are unaffected by PHYSICAL RESISTANCE',                           None            ],
    ['RUBY STANDISH'            '+2 SNEAK. Gain 1 UNIQUE ITEM when RUBY STANDISH joins you',                                                                                None            ],
    ['SIR WILLIAM BRINTON'      '+1 max DAMAGE. SIR WILLIAM will drain his life force (type "sacrifice SIR WILLIAM") to restore your stamina, reducing your DAMAGE to 0',   None            ],
    ['THOMAS F. MALONE'         '+1 FIGHT, +1 LORE. Gain 1 SPELL when THOMAS F. MALONE joins you',                                                                          None            ],
    ['TOM "MOUNTAIN" MURPHY'    '+2 FIGHT. With TOM "MOUNTAIN" MURPHY by your sie, you receive no extra DAMAGE when combatting OVERWHELMING MONSTERS',                      None            ] 
])

gates = Table([
    ['name',                        'dimension' ],
    ['YUGGOTH',                     0           ],
    ['THE CITY OF THE GREAT RACE',  1           ],
    ['THE PLATEAU OF LENG',         3           ],
    ['THE ABYSS',                   4           ],
    ['ANOTHER DIMENSION',           5           ],
    ['THE GREAT HALL OF CELEANO',   6           ],
    ['THE DREAMLANDS',              7           ],
    ["R'LYEH",                      8           ],
])

mythosEffects = Table([
    [   'banner',
        'variety', 'activity', 
        'modifiers',
        'monsterSpawnCount', 'monsterSpawnLocation', 'monsterDespawnLocation', 'bannedMonsters',
        'effect', 'resolution' 
    ],

    # effect_001
    [    Mythos.banner( 
            title='LODGE MEMBER HELD FOR QUESTIONING', 
            description='Esoteric solstice ritual at the Silver Twilight Lodge lets something loose into the FRENCH HILL STREETS' ), 
        'headline', None,       
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        2, 'FRENCH HILL STREETS', None, None,
        None, None 
    ],

    # effect_002
    [   Mythos.banner(
            title="HORROR AT GROUNDBREAKING",
            description="New construction at MISKATONIC U. became delayed when an odd petroglyph was uncovered. Authorities remain silent as to what happened to the crew." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'MISKATONIC UNIVERSITY STREETS', None, None,
        None, None 
    ],

    # effect_003
    [   Mythos.banner(
            title="PICNICKERS PANIC",
            description="Families flee DOWNTOWN after seeing two loathsome figures lurking near the park." ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, "DOWNTOWN STREETS", None, None,
        None, None 
    ],

    # effect_004
    [   Mythos.banner( 
            title='WITCH BURNING ANNIVERSARY', 
            description="Scientists will not explain how the soil has suddenly become ash at the site of Arkham's historic witch trials."),  
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'RIVERTOWN STREETS', None, None,
        None, None  
    ], 

    # effect_005
    [   Mythos.banner( 
            title='SLUM MURDERS CONTINUE',  
            description='Brutal, mysterious deaths worry the residents of EASTTOWN STREETS. "Stay out of your basement!" says one witness.'), 
        'headline', 
        None,    
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'EASTTOWN STREETS', None, None,
        None, None  
    ],

    # effect_006
    [   Mythos.banner( 
            title='SHELDON GANG TURNS TO POLICE FOR AID',  
            description='The suspected criminal organization, notorious for alleged bootlegging and tax evasion, claims to have run-ins with horrible creatures around UPTOWN neighborhood.'), 
        'headline', 
        None,    
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'UPTOWN STREETS', None, None,
        None, None  
    ],

    # effect_007
    [   Mythos.banner( 
            title='"GHOST SHIP" DOCKS BY ITSELF',  
            description='The Dockmaster alleges a "mighty shadow" moved into the RIVER DOCKS and released its evil into the MERCHANT DISTRIC.'), 
        'headline', 
        None,    
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'MERCHANT DISTRIC STREETS', None, None,
        None, None  
    ],

    # effect_008
    [   Mythos.banner( 
            title='TERROR AT THE TRAIN STATION',  
            description='Passengers worried for their safety when they spotted "creatures" roaming about the station.'), 
        'headline', 
        None,    
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'NORTHSIDE STREETS', None, None,
        None, None  
    ],

    # effect_009
    [   Mythos.banner( 
            title='SOUTHSIDE STRANGLER SUSPECTED',  
            description='Murders in SOUTHSIDE continue; the Arkham Advertiser urges police to go after the Strangler; residents claim a different culprit is responsible.'), 
        'headline', None,    
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        2, 'SOUTHSIDE STREETS', None, None,
        None, None  
    ],

    # effect_010
    [   Mythos.banner( 
            title='LODGE MEMBERS WATCH THE NIGHT', 
            description="The FRENCH HILL neighborhood has been cleaned up by members of the SILVER TWILIGHT LODGE. Word is kept secret on what was stalking the area."), 
        'headline', None, 
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),     
        0, None, "FRENCH HILL", None,
        None, None  
    ],

    # effect_011
    [   Mythos.banner( 
          title="RIVERTOWN RESIDENTS TAKE BACK THE STREETS",
          description="Neighbors crowd around the body of what they call an 'inhuman monster from the stars.'" ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, "RIVERTOWN", None,
        None, None  
    ],

    # effect_012
    [   Mythos.banner( 
            title="VIGILANTE GUARDS THE NIGHT",
            description="A mysterious hero has been taking care of DOWNTOWN; there have been reports of 'creeps' in the area." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, "DOWNTOWN", None,
        None, None  
    ],

    # effect_013
    [    Mythos.banner(
            title="MERCHANTS MARCH ON CRIME",
            description="Witnesses to strange goings-on claim that the criminals may be supernatural in origin. This reporter has her doubts." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "MERCHANT DISTRICT", None,
        None, None  
    ],

    # effect_014
    [    Mythos.banner(
            title="CHURCH GROUP RECLAIMS SOUTHSIDE",
            description='The SOUTHSIDE neighborhood is bouncing back after parishioners band together against "devilspawn from Hell."' ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "SOUTHSIDE", None,
        None, None  
    ],

    # effect_015
    [    Mythos.banner(
            title="CAMPUS SECURITY INCREASED",
            description="Worrying for their students' safety considering reports of strange creatures in Arkham, MISKATONIC UNIVERSITY administration has upped the precautions around the neighborhood." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "MISKATONIC UNIVERSITY", None,
        None, None  
    ],

    # effect_016
    [    Mythos.banner(
            title="POLICE STEP UP PATROLS IN NORTHSIDE",
            description="Arkham PD, responding to complaints of unidentified animals causing harm to residents, have cleared the area of danger, says deputy." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "NORTHSIDE", None,
        None, None  
    ],

    # effect_017
    [    Mythos.banner(
            title="GANG CLEANS UP EASTTOWN",
            description='The Sheldon Gang, usually in this newspaper for more nefarious reasons, have eased neighborhood tensions by ridding it of what residents have called "monsters."' ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "EASTTOWN", None,
        None, None  
    ],

    # effect_018
    [    Mythos.banner(
            title="PRIVATE SECURITY HIRED IN UPTOWN",
            description='The more affluent neighborhood has taken measures to guard against what locals are calling a "supernatural infestation."' ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "UPTOWN", None,
        None, None  
    ],

    # effect_019
    [    Mythos.banner(
            title="BIG STORM SWEEPS ARKHAM",
            description="Rare summer nor'easter has cleared THE SKY and quieted the OUTSKIRTS around town." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "SPECIAL", None,
        None, None  
    ],

    # effect_020
    [    Mythos.banner(
            title="FEDS RAID ARKHAM",
            description='The Federal Bureau of Investigation appeared in Arkham yesterday, claiming interest in "street safety" said a spokesperson.' ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "STREETS", None,
        None, None  
    ],

    # effect_021
    [    Mythos.banner(
            title="MANHUNT IN ARKHAM",
            description='Police claim they are after the Southside Strangler, witnesses cannot explain what was piled up in the back of the Patrol Wagon.' ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, "LOCATIONS", None,
        None, None  
    ],

    # effect_022
    [   Mythos.banner(
            title="FAMILY FOUND BUTCHERED",
            description="Witnesses claim a troop of robed figures stole into the house the night of the murder." ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None,  None,
        Effects.effect_022, None 
    ],

    # effect_023
    [   Mythos.banner(
          title="BIZARRE DREAMS PLAGUE CITIZENS",
          description="Many Arkhamites, this reporter included, are experiencing corrupting nightmares of various themes. What can explain this mass hysteria?" ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),    
        0, None, None, None,
        Effects.effect_023, None  
    ],

    # effect_024
    [   Mythos.banner(
          title="GOAT-LIKE CREATURE SPOTTED IN THE WOODS",
          description='"Large, hideous beast" seen skulking through the forests, according to most recent blotter.' ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),    
        0, None, None, None,
        Effects.effect_024, None  
    ],

    # effect_025
    [   Mythos.banner(
          title="STRANGE TREMORS CEASE",
          description='Residents are relieved to rid of the shaking, but fear for the stability of their homes.' ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),    
        0, None, None, None,
        Effects.effect_025, None  
    ],

    # effect_026
    [   Mythos.banner(
          title="SCIENTIST WARNS OF DIMENSIONAL RIFT",
          description='At a symposium at MISKATONIC UNIVERSITY, Professor Harriet Dough attempts explanation of odd "space-time fissures."' ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),    
        0, None, None, None,
        Effects.effect_026, None  
    ],

    # effect_027
    [   Mythos.banner(
            title="STRANGE POWER FLUX PLAGUES CITY",
            description="Power company is uncertain what has been causing the flux; will not comment on sudden appearances of people near outages." ),
        'headline', None,  
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, None, None,
        Effects.effect_027, None  
    ],

    # effect_028
    [   Mythos.banner(
            title="BLUE FLU",
            description="Police across the Northeast are calling sick to strike for better wages. But who will arrest the criminals?" ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_028, Resolutions.resolution_028
    ],

    # effect_029
    [   Mythos.banner(
            title="MISSING PEOPLE RETURN",
            description="Strange appearances of people once thought to be missing are a relief, if not a puzzle, to Arkham citizens." ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_029, None 
    ],

    # effect_030
    [   Mythos.banner(
            title="ILL WIND GRIPS ARKHAM",
            description="Ripping gale silences typically vibrant community. People report feelings of emptiness in the quietude."),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),                         
        0, None, None, None,
        Effects.effect_030, None  
    ],

    # effect_031
    [   Mythos.banner( 
            title='TEMPERENCE FEVER SWEEPS CITY', 
            description='Anyone caught with alcohol (such as WHISKEY) will immediately be arrested, say Arkham PD'),  
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_031, Resolutions.resolution_031
    ],

    # effect_032
    [
        Mythos.banner( 
            title='ALL QUIET IN ARKHAM',
            description='Despite recent events, Arkhamites feel the blessing of some peace and quiet.'),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_032, None 
    ],

     # effect_033
    [
        Mythos.banner( 
            title='CITY GRIPPED BY BLACKOUTS',
            description='Arkham Water & Power gave no comment when asked about the reliability of the grid.' ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_033, Resolutions.resolution_033
    ],

    # effect_034
    [
        Mythos.banner( 
            title='STRANGE LIGHTS ON CAMPUS',
            description='Dean Bartles has assured the phenomenon is under control; yet, the campus is closed until further notice. What could be going on?' ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_034, Resolutions.resolution_034
    ],

    # effect_035
    [
        Mythos.banner(
            title="FOURTH OF JULY PARADE",
            description="The MERCHANT DISTRICT STREETS are packed today with crowds observing our nation's 150th, making the area impassable." ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_035, Resolutions.resolution_035
    ],

    # effect_036
    [
        Mythos.banner(
            title="MISKATONIC ARCTIC EXPEDITION RETURNS",
            description="Sources indicate that the expedition brought something back that was supposed to be studied, but instead has escaped." ),
        'headline', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, None,
        Effects.effect_036, None 
    ],

    # effect_037
    [
        Mythos.banner(
            title="UNSEASONABLE FOG SETTLES OVER ARKHAM",
            description="The thick mist itself has an oppressive odor; meteorologists uncertain on when this will lift." ),
        'weather', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=1, fight=0, will=-1, lore=0, luck=0 ),
        0, None, None, None,
        None, None 
    ],

    # effect_038
    [
        Mythos.banner(
            title="HEAT WAVE BLASTS NORTHEAST",
            description="" ),
        'weather', None,
        Mythos.modifiers( mvmtPoints=0, speed=0, sneak=0, fight=-1, will=0, lore=1, luck=0 ),
        0, None, None, None,
        None, None 
    ],

    # effect_039
    [
        Mythos.banner(
            title="RAINING CATS AND DOGS",
            description="" ),
        'weather', None,
        Mythos.modifiers( mvmtPoints=-1, speed=-1, sneak=+1, fight=0, will=0, lore=0, luck=0 ),
        0, None, None, 'FIRE VAMPIRES',
        None, None 

    ],

])   
