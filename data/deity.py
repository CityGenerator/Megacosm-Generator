#

self.redis.lpush('deity_favored_stat', 'age')
self.redis.lpush('deity_favored_stat', 'attractiveness')
self.redis.lpush('deity_favored_stat', 'intelligence')
self.redis.lpush('deity_favored_stat', 'charisma')
self.redis.lpush('deity_favored_stat', 'wisdom')
self.redis.lpush('deity_favored_stat', 'endurance')
self.redis.lpush('deity_favored_stat', 'agility')
self.redis.lpush('deity_favored_stat', 'strength')
self.redis.lpush('deity_favored_stat', 'experience')
self.redis.lpush('deity_favored_stat', 'skill')
self.redis.lpush('deity_favored_stat', 'bravery')
self.redis.lpush('deity_favored_stat', 'honor')
self.redis.lpush('deity_favored_stat', 'piety')

# Members of the church are ____________ in their beliefs._
self.redis.zadd('deity_unity', '{"name":"splintered",  "score":10  }', '10')
self.redis.zadd('deity_unity', '{"name":"fractured",   "score":20  }', '20')
self.redis.zadd('deity_unity', '{"name":"divided",     "score":30  }', '30')
self.redis.zadd('deity_unity', '{"name":"fragmented",  "score":70  }', '70')
self.redis.zadd('deity_unity', '{"name":"diverse",     "score":80  }', '80')
self.redis.zadd('deity_unity', '{"name":"faceted",     "score":90  }', '90')
self.redis.zadd('deity_unity', '{"name":"unified",     "score":100 }', '100')

# Followers of Gobesh are ________ organized
self.redis.zadd('deity_organized', '{"name":"formlessly",      "score":10  }', '10')
self.redis.zadd('deity_organized', '{"name":"loosely",         "score":20  }', '10')
self.redis.zadd('deity_organized', '{"name":"lightly",         "score":30  }', '20')
self.redis.zadd('deity_organized', '{"name":"flexibly",        "score":40  }', '20')
self.redis.zadd('deity_organized', '{"name":"generally",       "score":50  }', '30')
self.redis.zadd('deity_organized', '{"name":"stiffly",         "score":60  }', '60')
self.redis.zadd('deity_organized', '{"name":"firmly",          "score":70  }', '70')
self.redis.zadd('deity_organized', '{"name":"tightly",         "score":80  }', '80')
self.redis.zadd('deity_organized', '{"name":"strictly",        "score":90  }', '90')
self.redis.zadd('deity_organized', '{"name":"rigidly",         "score":100 }', '100')

# Gobesh is _____________ in today\'s world
self.redis.zadd('deity_health', '{"name":"nearly forgotten",           "score":10  }', '10')
self.redis.zadd('deity_health', '{"name":"mostly unknown",             "score":20  }', '20')
self.redis.zadd('deity_health', '{"name":"dying out",                  "score":30  }', '30')
self.redis.zadd('deity_health', '{"name":"fading",                     "score":40  }', '40')
self.redis.zadd('deity_health', '{"name":"well known",                 "score":50  }', '50')
self.redis.zadd('deity_health', '{"name":"on the rise",                "score":60  }', '60')
self.redis.zadd('deity_health', '{"name":"maintaining popularity",     "score":70  }', '70')
self.redis.zadd('deity_health', '{"name":"gaining followers",          "score":80  }', '80')
self.redis.zadd('deity_health', '{"name":"gaining in popularity",      "score":90  }', '90')
self.redis.zadd('deity_health', '{"name":"more popular than ever",     "score":100 }', '100')

self.redis.zadd('deity_importance', '{"name":"quasi-deity",         "score":10, "points":1 }', '10')
self.redis.zadd('deity_importance', '{"name":"demi-deity",          "score":20, "points":2 }', '20')
self.redis.zadd('deity_importance', '{"name":"minor deity",         "score":30, "points":3 }', '30')
self.redis.zadd('deity_importance', '{"name":"lesser deity",        "score":50, "points":7 }', '50')
self.redis.zadd('deity_importance', '{"name":"intermediate deity",  "score":80, "points":11 }', '80')
self.redis.zadd('deity_importance', '{"name":"greater deity",       "score":99, "points":13 }', '99')
self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100,"points":21 }', '100')


self.redis.zadd('deity_jealousy', '{"name":"trusting",  "score":10   }', '10')
self.redis.zadd('deity_jealousy', '{"name":"unresentful",  "score":20   }', '20')
self.redis.zadd('deity_jealousy', '{"name":"unquestioning",  "score":30   }', '30')
self.redis.zadd('deity_jealousy', '{"name":"unsuspecting",  "score":40   }', '40')
self.redis.zadd('deity_jealousy', '{"name":"content",  "score":50   }', '50')
self.redis.zadd('deity_jealousy', '{"name":"covetous",  "score":60   }', '60')
self.redis.zadd('deity_jealousy', '{"name":"demanding",  "score":70   }', '70')
self.redis.zadd('deity_jealousy', '{"name":"suspicious",  "score":80   }', '80')
self.redis.zadd('deity_jealousy', '{"name":"selfish",  "score":90   }', '90')
self.redis.zadd('deity_jealousy', '{"name":"jealous",  "score":100   }', '100')

#        <age> <!-- bob is a _____ god-->
self.redis.zadd('deity_age', '{"name":"new",  "score":5   }', '5')
self.redis.zadd('deity_age', '{"name":"young",  "score":10   }', '10')
self.redis.zadd('deity_age', '{"name":"recent",  "score":15   }', '15')
self.redis.zadd('deity_age', '{"name":"latter",  "score":20   }', '20')
self.redis.zadd('deity_age', '{"name":"modern",  "score":25   }', '25')
self.redis.zadd('deity_age', '{"name":"contemporary",  "score":30   }', '30')
self.redis.zadd('deity_age', '{"name":"fledgling",  "score":35   }', '35')
self.redis.zadd('deity_age', '{"name":"primitive",  "score":40   }', '40')
self.redis.zadd('deity_age', '{"name":"old",  "score":45   }', '45')
self.redis.zadd('deity_age', '{"name":"antiquated",  "score":55   }', '55')
self.redis.zadd('deity_age', '{"name":"aboriginal",  "score":60   }', '60')
self.redis.zadd('deity_age', '{"name":"primeval",  "score":65   }', '65')
self.redis.zadd('deity_age', '{"name":"primal",  "score":70   }', '70')
self.redis.zadd('deity_age', '{"name":"primordial",  "score":75   }', '75')
self.redis.zadd('deity_age', '{"name":"archaic",  "score":80   }', '80')
self.redis.zadd('deity_age', '{"name":"eternal",  "score":85   }', '85')
self.redis.zadd('deity_age', '{"name":"ancient",  "score":99   }', '99')
self.redis.zadd('deity_age', '{"name":"original",  "score":100   }', '100')

#        <followerzeal> <!--Bobs followers are -->
self.redis.zadd('deity_followerzeal', '{"name":"noncommittal", "score":5   }', '5')
self.redis.zadd('deity_followerzeal', '{"name":"dispassionate","score":10   }', '10')
self.redis.zadd('deity_followerzeal', '{"name":"insincere",    "score":20   }', '20')
self.redis.zadd('deity_followerzeal', '{"name":"inattentive",  "score":30   }', '30')
self.redis.zadd('deity_followerzeal', '{"name":"dutiful",      "score":40   }', '40')
self.redis.zadd('deity_followerzeal', '{"name":"pious",        "score":50   }', '50')
self.redis.zadd('deity_followerzeal', '{"name":"devoted",      "score":60   }', '60')
self.redis.zadd('deity_followerzeal', '{"name":"reverent",     "score":70   }', '70')
self.redis.zadd('deity_followerzeal', '{"name":"devout",       "score":80   }', '80')
self.redis.zadd('deity_followerzeal', '{"name":"passionate",   "score":90   }', '90')
self.redis.zadd('deity_followerzeal', '{"name":"overzealous",  "score":100   }', '100')

#TODO ZADD popularity growing/dying out

#        <devotion {"name":"<!-- Bob is thought to have _______ current followers in the world-->
self.redis.zadd('deity_followercount', '{"name":"no",  "score":5   }', '5')
self.redis.zadd('deity_followercount', '{"name":"only a few",  "score":10   }', '10')
self.redis.zadd('deity_followercount', '{"name":"several",  "score":15   }', '15')
self.redis.zadd('deity_followercount', '{"name":"a dozen",  "score":20   }', '20')
self.redis.zadd('deity_followercount', '{"name":"several dozen",  "score":25   }', '25')
self.redis.zadd('deity_followercount', '{"name":"over a hundred",  "score":30   }', '30')
self.redis.zadd('deity_followercount', '{"name":"an unknown number of",  "score":60   }', '60')
self.redis.zadd('deity_followercount', '{"name":"hundreds of",  "score":65   }', '65')
self.redis.zadd('deity_followercount', '{"name":"near a thousand",  "score":70   }', '70')
self.redis.zadd('deity_followercount', '{"name":"several thousand",  "score":75   }', '75')
self.redis.zadd('deity_followercount', '{"name":"tens of thousands of",  "score":80   }', '80')
self.redis.zadd('deity_followercount', '{"name":"hundreds of thousands of",  "score":85   }', '85')
self.redis.zadd('deity_followercount', '{"name":"countless",  "score":100   }', '100')

# and are often {{deity.secrecy[\'name\']}} about their affiliation.
self.redis.zadd('deity_secrecy', '{"name":"secretive",     "score":5   }', '5')
self.redis.zadd('deity_secrecy', '{"name":"silent",        "score":10   }', '10')
self.redis.zadd('deity_secrecy', '{"name":"tight lipped",  "score":20   }', '20')
self.redis.zadd('deity_secrecy', '{"name":"cryptic",       "score":30   }', '30')
self.redis.zadd('deity_secrecy', '{"name":"hidden",        "score":40   }', '40')
self.redis.zadd('deity_secrecy', '{"name":"careful",       "score":45   }', '45')
self.redis.zadd('deity_secrecy', '{"name":"reserved",      "score":50   }', '50')
self.redis.zadd('deity_secrecy', '{"name":"honest",        "score":55   }', '55')
self.redis.zadd('deity_secrecy', '{"name":"open",          "score":60   }', '60')
self.redis.zadd('deity_secrecy', '{"name":"indiscreet",    "score":70   }', '70')
self.redis.zadd('deity_secrecy', '{"name":"proud",         "score":80   }', '80')
self.redis.zadd('deity_secrecy', '{"name":"pretentious",   "score":90   }', '90')
self.redis.zadd('deity_secrecy', '{"name":"pompous",       "score":100   }', '100')
#TODO secrecy should include loud and proud

#
self.redis.lpush('deity_clergytype', 'priests')
self.redis.lpush('deity_clergytype', 'clergy')
self.redis.lpush('deity_clergytype', 'clerics')
self.redis.lpush('deity_clergytype', 'friars')
self.redis.lpush('deity_clergytype', 'preachers')
self.redis.lpush('deity_clergytype', 'rectors')
self.redis.lpush('deity_clergytype', 'ministers')
self.redis.lpush('deity_clergytype', 'monks')
self.redis.lpush('deity_clergytype', 'chaplains')
self.redis.lpush('deity_clergytype', 'pastors')
self.redis.lpush('deity_clergytype', 'rabbis')
self.redis.lpush('deity_clergytype', 'abbots')
self.redis.lpush('deity_clergytype', 'evangelists')
self.redis.lpush('deity_clergytype', 'shepherds')

self.redis.lpush('deity_clergytype', 'zealots')
self.redis.lpush('deity_clergytype', 'gurus')
self.redis.lpush('deity_clergytype', 'shamans')
self.redis.lpush('deity_clergytype', 'disciples')
self.redis.lpush('deity_clergytype', 'enlightened ones')
self.redis.lpush('deity_clergytype', 'vicars')
self.redis.lpush('deity_clergytype', 'priests')
self.redis.lpush('deity_clergytype', 'imams')

#   ___________ are the preferred form of worship.
self.redis.lpush('deity_worship', 'sacrifices')
self.redis.lpush('deity_worship', 'offerings')
self.redis.lpush('deity_worship', 'tithings')
self.redis.lpush('deity_worship', 'prayers')
self.redis.lpush('deity_worship', 'supplication')
self.redis.lpush('deity_worship', 'dances')


self.redis.lpush('deity_primarycolor', 'aquamarine')
self.redis.hset('deity_primarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
self.redis.lpush('deity_primarycolor', 'azure')
self.redis.hset('deity_primarycolor_description', 'azure', '{"name":"azure", "hex":"F0FFFF" }')
self.redis.lpush('deity_primarycolor', 'banana')
self.redis.hset('deity_primarycolor_description', 'banana', '{"name":"banana", "hex":"E3CF57" }')
self.redis.lpush('deity_primarycolor', 'beige')
self.redis.hset('deity_primarycolor_description', 'beige', '{"name":"beige", "hex":"F5F5DC" }')
self.redis.lpush('deity_primarycolor', 'bisque')
self.redis.hset('deity_primarycolor_description', 'bisque', '{"name":"bisque", "hex":"FFE4C4" }')
self.redis.lpush('deity_primarycolor', 'black')
self.redis.hset('deity_primarycolor_description', 'black', '{"name":"black", "hex":"000000" }')
self.redis.lpush('deity_primarycolor', 'blanchedalmond')
self.redis.hset('deity_primarycolor_description', 'blanchedalmond', '{"name":"blanched almond", "hex":"FFEBCD" }')
self.redis.lpush('deity_primarycolor', 'blue')
self.redis.hset('deity_primarycolor_description', 'blue', '{"name":"blue", "hex":"0000FF" }')
self.redis.lpush('deity_primarycolor', 'blueviolet')
self.redis.hset('deity_primarycolor_description', 'blueviolet', '{"name":"blue-violet", "hex":"8A2BE2" }')
self.redis.lpush('deity_primarycolor', 'brick')
self.redis.hset('deity_primarycolor_description', 'brick', '{"name":"brick", "hex":"9C661F" }')
self.redis.lpush('deity_primarycolor', 'brown')
self.redis.hset('deity_primarycolor_description', 'brown', '{"name":"brown", "hex":"A52A2A" }')
self.redis.lpush('deity_primarycolor', 'burlywood')
self.redis.hset('deity_primarycolor_description', 'burlywood', '{"name":"burly wood", "hex":"DEB887" }')
self.redis.lpush('deity_primarycolor', 'burntsienna')
self.redis.hset('deity_primarycolor_description', 'burntsienna', '{"name":"burnt sienna", "hex":"8A360F" }')
self.redis.lpush('deity_primarycolor', 'burntumber')
self.redis.hset('deity_primarycolor_description', 'burntumber', '{"name":"burnt umber", "hex":"8A3324" }')
self.redis.lpush('deity_primarycolor', 'cadetblue')
self.redis.hset('deity_primarycolor_description', 'cadetblue', '{"name":"cadet blue", "hex":"5F9EA0" }')
self.redis.lpush('deity_primarycolor', 'cadmiumorange')
self.redis.hset('deity_primarycolor_description', 'cadmiumorange', '{"name":"cadmium orange", "hex":"FF6103" }')
self.redis.lpush('deity_primarycolor', 'cadmiumyellow')
self.redis.hset('deity_primarycolor_description', 'cadmiumyellow', '{"name":"cadmium yellow", "hex":"FF9912" }')
self.redis.lpush('deity_primarycolor', 'carrot')
self.redis.hset('deity_primarycolor_description', 'carrot', '{"name":"carrot", "hex":"ED9121" }')
self.redis.lpush('deity_primarycolor', 'chartreuse')
self.redis.hset('deity_primarycolor_description', 'chartreuse', '{"name":"chartreuse", "hex":"7FFF00" }')
self.redis.lpush('deity_primarycolor', 'chocolate')
self.redis.hset('deity_primarycolor_description', 'chocolate', '{"name":"chocolate-colored", "hex":"D2691E" }')
self.redis.lpush('deity_primarycolor', 'cobalt')
self.redis.hset('deity_primarycolor_description', 'cobalt', '{"name":"cobalt", "hex":"3D59AB" }')
self.redis.lpush('deity_primarycolor', 'cobaltgreen')
self.redis.hset('deity_primarycolor_description', 'cobaltgreen', '{"name":"cobalt green", "hex":"3D9140" }')
self.redis.lpush('deity_primarycolor', 'coldgrey')
self.redis.hset('deity_primarycolor_description', 'coldgrey', '{"name":"cold grey", "hex":"808A87" }')
self.redis.lpush('deity_primarycolor', 'coral')
self.redis.hset('deity_primarycolor_description', 'coral', '{"name":"coral", "hex":"FF7F50" }')
self.redis.lpush('deity_primarycolor', 'cornflowerblue')
self.redis.hset('deity_primarycolor_description', 'cornflowerblue', '{"name":"cornflower blue", "hex":"6495ED" }')



self.redis.lpush('deity_secondarycolor', 'aquamarine')
self.redis.hset('deity_secondarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
self.redis.lpush('deity_secondarycolor', 'azure')
self.redis.hset('deity_secondarycolor_description', 'azure', '{"name":"azure", "hex":"F0FFFF" }')
self.redis.lpush('deity_secondarycolor', 'banana')
self.redis.hset('deity_secondarycolor_description', 'banana', '{"name":"banana", "hex":"E3CF57" }')
self.redis.lpush('deity_secondarycolor', 'beige')
self.redis.hset('deity_secondarycolor_description', 'beige', '{"name":"beige", "hex":"F5F5DC" }')
self.redis.lpush('deity_secondarycolor', 'bisque')
self.redis.hset('deity_secondarycolor_description', 'bisque', '{"name":"bisque", "hex":"FFE4C4" }')
self.redis.lpush('deity_secondarycolor', 'black')
self.redis.hset('deity_secondarycolor_description', 'black', '{"name":"black", "hex":"000000" }')
self.redis.lpush('deity_secondarycolor', 'blanchedalmond')
self.redis.hset('deity_secondarycolor_description', 'blanchedalmond', '{"name":"blanched almond", "hex":"FFEBCD" }')
self.redis.lpush('deity_secondarycolor', 'blue')
self.redis.hset('deity_secondarycolor_description', 'blue', '{"name":"blue", "hex":"0000FF" }')
self.redis.lpush('deity_secondarycolor', 'blueviolet')
self.redis.hset('deity_secondarycolor_description', 'blueviolet', '{"name":"blue-violet", "hex":"8A2BE2" }')
self.redis.lpush('deity_secondarycolor', 'brick')
self.redis.hset('deity_secondarycolor_description', 'brick', '{"name":"brick", "hex":"9C661F" }')
self.redis.lpush('deity_secondarycolor', 'brown')
self.redis.hset('deity_secondarycolor_description', 'brown', '{"name":"brown", "hex":"A52A2A" }')
self.redis.lpush('deity_secondarycolor', 'burlywood')
self.redis.hset('deity_secondarycolor_description', 'burlywood', '{"name":"burly wood", "hex":"DEB887" }')
self.redis.lpush('deity_secondarycolor', 'burntsienna')
self.redis.hset('deity_secondarycolor_description', 'burntsienna', '{"name":"burnt sienna", "hex":"8A360F" }')
self.redis.lpush('deity_secondarycolor', 'burntumber')
self.redis.hset('deity_secondarycolor_description', 'burntumber', '{"name":"burnt umber", "hex":"8A3324" }')
self.redis.lpush('deity_secondarycolor', 'cadetblue')
self.redis.hset('deity_secondarycolor_description', 'cadetblue', '{"name":"cadet blue", "hex":"5F9EA0" }')
self.redis.lpush('deity_secondarycolor', 'cadmiumorange')
self.redis.hset('deity_secondarycolor_description', 'cadmiumorange', '{"name":"cadmium orange", "hex":"FF6103" }')
self.redis.lpush('deity_secondarycolor', 'cadmiumyellow')
self.redis.hset('deity_secondarycolor_description', 'cadmiumyellow', '{"name":"cadmium yellow", "hex":"FF9912" }')
self.redis.lpush('deity_secondarycolor', 'carrot')
self.redis.hset('deity_secondarycolor_description', 'carrot', '{"name":"carrot", "hex":"ED9121" }')
self.redis.lpush('deity_secondarycolor', 'chartreuse')
self.redis.hset('deity_secondarycolor_description', 'chartreuse', '{"name":"chartreuse", "hex":"7FFF00" }')
self.redis.lpush('deity_secondarycolor', 'chocolate')
self.redis.hset('deity_secondarycolor_description', 'chocolate', '{"name":"chocolate-colored", "hex":"D2691E" }')
self.redis.lpush('deity_secondarycolor', 'cobalt')
self.redis.hset('deity_secondarycolor_description', 'cobalt', '{"name":"cobalt", "hex":"3D59AB" }')
self.redis.lpush('deity_secondarycolor', 'cobaltgreen')
self.redis.hset('deity_secondarycolor_description', 'cobaltgreen', '{"name":"cobalt green", "hex":"3D9140" }')
self.redis.lpush('deity_secondarycolor', 'coldgrey')
self.redis.hset('deity_secondarycolor_description', 'coldgrey', '{"name":"cold grey", "hex":"808A87" }')
self.redis.lpush('deity_secondarycolor', 'coral')
self.redis.hset('deity_secondarycolor_description', 'coral', '{"name":"coral", "hex":"FF7F50" }')
self.redis.lpush('deity_secondarycolor', 'cornflowerblue')
self.redis.hset('deity_secondarycolor_description', 'cornflowerblue', '{"name":"cornflower blue", "hex":"6495ED" }')

# in battle, Gokl prefers
self.redis.lpush('deity_favored_weapon', 'axes')
self.redis.lpush('deity_favored_weapon', 'bastard swords')
self.redis.lpush('deity_favored_weapon', 'battle axes')
self.redis.lpush('deity_favored_weapon', 'picks')
self.redis.lpush('deity_favored_weapon', 'bladed gauntlets')
self.redis.lpush('deity_favored_weapon', 'bows')
self.redis.lpush('deity_favored_weapon', 'butterfly swords')
self.redis.lpush('deity_favored_weapon', 'claw bracers')
self.redis.lpush('deity_favored_weapon', 'composite bows')
self.redis.lpush('deity_favored_weapon', 'crossbows')
self.redis.lpush('deity_favored_weapon', 'curved swords')
self.redis.lpush('deity_favored_weapon', 'daggers')
self.redis.lpush('deity_favored_weapon', 'falchion')
self.redis.lpush('deity_favored_weapon', 'flails, maces and clubs')
self.redis.lpush('deity_favored_weapon', 'glaives')
self.redis.lpush('deity_favored_weapon', 'greataxes')
self.redis.lpush('deity_favored_weapon', 'great clubs')
self.redis.lpush('deity_favored_weapon', 'great crossbows')
self.redis.lpush('deity_favored_weapon', 'greatswords')
self.redis.lpush('deity_favored_weapon', 'guisarmes')
self.redis.lpush('deity_favored_weapon', 'halberds')
self.redis.lpush('deity_favored_weapon', 'hand axes')
self.redis.lpush('deity_favored_weapon', 'hand crossbows')
self.redis.lpush('deity_favored_weapon', 'harpoons')
self.redis.lpush('deity_favored_weapon', 'heavy crossbows')
self.redis.lpush('deity_favored_weapon', 'heavy flail')
self.redis.lpush('deity_favored_weapon', 'heavy mace')
self.redis.lpush('deity_favored_weapon', 'javelins')
self.redis.lpush('deity_favored_weapon', 'light crossbows')
self.redis.lpush('deity_favored_weapon', 'light flail')
self.redis.lpush('deity_favored_weapon', 'light mace')
self.redis.lpush('deity_favored_weapon', 'longbows')
self.redis.lpush('deity_favored_weapon', 'long spears')
self.redis.lpush('deity_favored_weapon', 'longswords')
self.redis.lpush('deity_favored_weapon', 'martial arts')
self.redis.lpush('deity_favored_weapon', 'morningstars')
self.redis.lpush('deity_favored_weapon', 'polearms')
self.redis.lpush('deity_favored_weapon', 'ranseurs')
self.redis.lpush('deity_favored_weapon', 'rapiers')
self.redis.lpush('deity_favored_weapon', 'repeating crossbows')
self.redis.lpush('deity_favored_weapon', 'scimitars')
self.redis.lpush('deity_favored_weapon', 'shortbows')
self.redis.lpush('deity_favored_weapon', 'short spears')
self.redis.lpush('deity_favored_weapon', 'shortswords')
self.redis.lpush('deity_favored_weapon', 'simple clubs')
self.redis.lpush('deity_favored_weapon', 'slings')
self.redis.lpush('deity_favored_weapon', 'spears')
self.redis.lpush('deity_favored_weapon', 'spiked clubs')
self.redis.lpush('deity_favored_weapon', 'stump knives')
self.redis.lpush('deity_favored_weapon', 'swords')
self.redis.lpush('deity_favored_weapon', 'throwing axes')
self.redis.lpush('deity_favored_weapon', 'throwing daggers')
self.redis.lpush('deity_favored_weapon', 'throwing hammers')
self.redis.lpush('deity_favored_weapon', 'thrown weapons')
self.redis.lpush('deity_favored_weapon', 'tonfas')
self.redis.lpush('deity_favored_weapon', 'tridents')
self.redis.lpush('deity_favored_weapon', 'unarmed combat')
self.redis.lpush('deity_favored_weapon', 'unique axes')

SET   deity_holysymbol_type_chance 50
self.redis.lpush('deity_holysymbol_type', 'broken')
self.redis.lpush('deity_holysymbol_type', 'double')
self.redis.lpush('deity_holysymbol_type', 'upside-down')
self.redis.lpush('deity_holysymbol_type', 'sideways')
self.redis.lpush('deity_holysymbol_type', 'triple')
self.redis.lpush('deity_holysymbol_type', 'divided')
self.redis.lpush('deity_holysymbol_type', 'tilted')
self.redis.lpush('deity_holysymbol_type', 'burning')
self.redis.lpush('deity_holysymbol_type', 'fragmented')
self.redis.lpush('deity_holysymbol_type', 'circled')
self.redis.lpush('deity_holysymbol_type', 'rocking')
self.redis.lpush('deity_holysymbol_type', 'swinging')

#LPUSH deity_holysymbol_type melting
#LPUSH deity_holysymbol_type cartoonish
#LPUSH deity_holysymbol_type angular
#LPUSH deity_holysymbol_type jagged
#LPUSH deity_holysymbol_type winged
#LPUSH deity_holysymbol_type dragged?
#LPUSH deity_holysymbol_type walking



#LPUSH deity_holysymbol_type running
#LPUSH deity_holysymbol_type decaying
#LPUSH deity_holysymbol_type flaming
#LPUSH deity_holysymbol_type shining
#LPUSH deity_holysymbol_type stylized
#LPUSH deity_holysymbol_type bloody


self.redis.lpush('deity_holysymbol', 'anchor')
self.redis.lpush('deity_holysymbol', 'ankh')
self.redis.lpush('deity_holysymbol', 'anvil')
self.redis.lpush('deity_holysymbol', 'apple')
self.redis.lpush('deity_holysymbol', 'axe')
self.redis.lpush('deity_holysymbol', 'bell')
#LPUSH deity_holysymbol bird
#LPUSH deity_holysymbol bone
#LPUSH deity_holysymbol book
#LPUSH deity_holysymbol bottle
#LPUSH deity_holysymbol brain
#LPUSH deity_holysymbol brush
#LPUSH deity_holysymbol bull
#LPUSH deity_holysymbol butterfly
#LPUSH deity_holysymbol campfire
#LPUSH deity_holysymbol candle
#LPUSH deity_holysymbol chalice
#LPUSH deity_holysymbol circle
#LPUSH deity_holysymbol cloud
#LPUSH deity_holysymbol cog
#LPUSH deity_holysymbol coin
#LPUSH deity_holysymbol crescent
#LPUSH deity_holysymbol cross
#LPUSH deity_holysymbol diamond
#LPUSH deity_holysymbol drop
#LPUSH deity_holysymbol ear
#LPUSH deity_holysymbol egg

#LPUSH deity_holysymbol eye
#LPUSH deity_holysymbol feather
#LPUSH deity_holysymbol fire
#LPUSH deity_holysymbol fish
#LPUSH deity_holysymbol fist
#LPUSH deity_holysymbol flask
#LPUSH deity_holysymbol flower
#LPUSH deity_holysymbol foot
#LPUSH deity_holysymbol footprint

#LPUSH deity_holysymbol gauntlet
#LPUSH deity_holysymbol goat
#LPUSH deity_holysymbol hand
#LPUSH deity_holysymbol harp
#LPUSH deity_holysymbol heart
#LPUSH deity_holysymbol helmet
#LPUSH deity_holysymbol heptagram
#LPUSH deity_holysymbol hexagon
#LPUSH deity_holysymbol hexagram
#LPUSH deity_holysymbol horn
#LPUSH deity_holysymbol horse
#LPUSH deity_holysymbol horseshoe
#LPUSH deity_holysymbol insect
#LPUSH deity_holysymbol key
#LPUSH deity_holysymbol knot
#LPUSH deity_holysymbol ladder
#LPUSH deity_holysymbol lamb
#LPUSH deity_holysymbol lock
#LPUSH deity_holysymbol man
#LPUSH deity_holysymbol mask
#LPUSH deity_holysymbol mobeus
#LPUSH deity_holysymbol moon
#LPUSH deity_holysymbol mouth
#LPUSH deity_holysymbol note
#LPUSH deity_holysymbol octogram
#LPUSH deity_holysymbol palm
#LPUSH deity_holysymbol pearl
#LPUSH deity_holysymbol pendulum
#LPUSH deity_holysymbol pentagon
#LPUSH deity_holysymbol pentagram
#LPUSH deity_holysymbol poison
#LPUSH deity_holysymbol potato
#LPUSH deity_holysymbol pyramid
#LPUSH deity_holysymbol rabbit
#LPUSH deity_holysymbol ram
#LPUSH deity_holysymbol ribbon
#LPUSH deity_holysymbol scale
#LPUSH deity_holysymbol scroll
#LPUSH deity_holysymbol scythe
#LPUSH deity_holysymbol seahorse
#LPUSH deity_holysymbol shield
#LPUSH deity_holysymbol skull
#LPUSH deity_holysymbol snowflake
#LPUSH deity_holysymbol spider
#LPUSH deity_holysymbol spiral
#LPUSH deity_holysymbol square
#LPUSH deity_holysymbol staff
#LPUSH deity_holysymbol stag
#LPUSH deity_holysymbol star
#LPUSH deity_holysymbol statue
#LPUSH deity_holysymbol sun
#LPUSH deity_holysymbol sword
#LPUSH deity_holysymbol tent
#LPUSH deity_holysymbol tornado
#LPUSH deity_holysymbol tree
#LPUSH deity_holysymbol triangle
#LPUSH deity_holysymbol trident
#LPUSH deity_holysymbol trumpet
#LPUSH deity_holysymbol uroborus
#LPUSH deity_holysymbol wheel
#LPUSH deity_holysymbol wolf
#LPUSH deity_holysymbol woman


# Ones I don\'t wanna draw right now.
#LPUSH deity_holysymbol cat
#LPUSH deity_holysymbol door
#LPUSH deity_holysymbol dragon
#LPUSH deity_holysymbol duck
#LPUSH deity_holysymbol eagle
#LPUSH deity_holysymbol earth
#LPUSH deity_holysymbol gate


#Ganthidon sometimes chooses to appear as a _________ before his followers.
self.redis.lpush('deity_form', 'talking jackal')
self.redis.lpush('deity_form', 'burning bush')
self.redis.lpush('deity_form', 'nightmarish vision')
self.redis.lpush('deity_form', 'colorful mist')
self.redis.lpush('deity_form', 'pillar of flame')
self.redis.lpush('deity_form', 'small child')
self.redis.lpush('deity_form', 'elderly man')
self.redis.lpush('deity_form', 'elderly woman')
self.redis.lpush('deity_form', 'hooded figure')
self.redis.lpush('deity_form', 'whisper')
self.redis.lpush('deity_form', 'flash of light from the skies')
self.redis.lpush('deity_form', 'thundering voice')
self.redis.lpush('deity_form', 'heavily armored soldier')
self.redis.lpush('deity_form', 'beautiful maiden')
self.redis.lpush('deity_form', 'beggar')
self.redis.lpush('deity_form', 'small bird')
self.redis.lpush('deity_form', 'insect')
self.redis.lpush('deity_form', 'telepathic plant')
self.redis.lpush('deity_form', 'beautiful vision')
self.redis.lpush('deity_form', 'horrible vision')
self.redis.lpush('deity_form', 'glittering reflection')
self.redis.lpush('deity_form', 'ghostly visage')

self.redis.lpush('deity_form', 'ball of light')
self.redis.lpush('deity_form', 'fool')
self.redis.lpush('deity_form', 'merry dwarf')
self.redis.lpush('deity_form', 'bald elf')
self.redis.lpush('deity_form', 'blindfolded man')
self.redis.lpush('deity_form', 'blindfolded woman')
self.redis.lpush('deity_form', 'eldritch abomination')
self.redis.lpush('deity_form', 'man with white hair and pitch black eyes')
self.redis.lpush('deity_form', 'woman with white hair and pitch black eyes')
self.redis.lpush('deity_form', 'enormous animal')
self.redis.lpush('deity_form', 'mirror image')
self.redis.lpush('deity_form', 'beloved and trusted person')
self.redis.lpush('deity_form', 'the observer\'s greatest fear')
self.redis.lpush('deity_form', 'many-colored dragon')
self.redis.lpush('deity_form', 'grey-skinned dwarf')
self.redis.lpush('deity_form', 'king from days of old')
self.redis.lpush('deity_form', 'queen from days of old')
self.redis.lpush('deity_form', 'wraith')
self.redis.lpush('deity_form', 'walking corpse')




#While in public, clergy of bhaal wear
self.redis.lpush('deity_clergy_dress', 'colored robes')
self.redis.lpush('deity_clergy_dress', 'nondescript robes')
self.redis.lpush('deity_clergy_dress', 'their holy symbol around their neck')
self.redis.lpush('deity_clergy_dress', 'their holy symbol emblazoned on their clothing')
self.redis.lpush('deity_clergy_dress', 'formal dress')
self.redis.lpush('deity_clergy_dress', 'vestments of their faith')
self.redis.lpush('deity_clergy_dress', 'nondescript clothing')
self.redis.lpush('deity_clergy_dress', 'colorful saris')
self.redis.lpush('deity_clergy_dress', 'decorated mantles')
self.redis.lpush('deity_clergy_dress', 'headdresses unique to their faith')
self.redis.lpush('deity_clergy_dress', 'formal uniforms')
self.redis.lpush('deity_clergy_dress', 'trophies from fallen foes')
self.redis.lpush('deity_clergy_dress', 'informal attire')
self.redis.lpush('deity_clergy_dress', 'formal attire')
self.redis.lpush('deity_clergy_dress', 'decorative attire')
self.redis.lpush('deity_clergy_dress', 'single fabrics')
self.redis.lpush('deity_clergy_dress', 'common garb')
self.redis.lpush('deity_clergy_dress', 'decorative frocks')
self.redis.lpush('deity_clergy_dress', 'decorative cassocks')
self.redis.lpush('deity_clergy_dress', 'decorative stoles')
self.redis.lpush('deity_clergy_dress', 'colorful gowns')
self.redis.lpush('deity_clergy_dress', 'decorative copes')
self.redis.lpush('deity_clergy_dress', 'ritual makeup')

#        <vow><!-- clerics of bob often follow a Vow of _______ (a vow to  ____) -->
self.redis.lpush('deity_vow', 'abstinence')
self.redis.lpush('deity_vow', 'celibacy')
self.redis.lpush('deity_vow', 'charity')
self.redis.lpush('deity_vow', 'chastity')
self.redis.lpush('deity_vow', 'humility')
self.redis.lpush('deity_vow', 'independence')
self.redis.lpush('deity_vow', 'itinerancy')
self.redis.lpush('deity_vow', 'nonviolence')
self.redis.lpush('deity_vow', 'obedience')
self.redis.lpush('deity_vow', 'peace')
self.redis.lpush('deity_vow', 'poverty')
self.redis.lpush('deity_vow', 'propriety')
self.redis.lpush('deity_vow', 'purity')
self.redis.lpush('deity_vow', 'reconstruction')
self.redis.lpush('deity_vow', 'silence')
self.redis.lpush('deity_vow', 'stoicism')
self.redis.lpush('deity_vow', 'submission')
self.redis.lpush('deity_vow', 'surety')

self.redis.hset('deity_vow_description', 'abstinence', '{"name":"Abstinence",       "description":"abstain from alcoholic beverages, drugs, and intoxication"                                   }')
self.redis.hset('deity_vow_description', 'celibacy', '{"name":"Celibacy",         "description":"refrain from marriage and sex"                                                               }')
self.redis.hset('deity_vow_description', 'charity', '{"name":"Charity",          "description":"refrain from accepting compensation for any services rendered"                               }')
self.redis.hset('deity_vow_description', 'chastity', '{"name":"Chastity",         "description":"refrain from marriage and sex"                                                               }')
self.redis.hset('deity_vow_description', 'humility', '{"name":"Humility",         "description":"abstain from extolling your own virtues"                                                     }')
self.redis.hset('deity_vow_description', 'independence', '{"name":"Independence",     "description":"never affiliate with or take orders from any organization, including the church"             }')
self.redis.hset('deity_vow_description', 'itinerancy', '{"name":"Itinerancy",       "description":"constantly move from place to place, never settling"                                         }')
self.redis.hset('deity_vow_description', 'nonviolence', '{"name":"Nonviolence",      "description":"avoid violence against other sentient creatures"                                             }')
self.redis.hset('deity_vow_description', 'obedience', '{"name":"Obedience",        "description":"live according to the dictates of a superior in the religious order or similar organization" }')
self.redis.hset('deity_vow_description', 'peace', '{"name":"Peace",            "description":"abstain from harming any living creature"                                                    }')
self.redis.hset('deity_vow_description', 'poverty', '{"name":"Poverty",          "description":"forswear material possessions"                                                               }')
self.redis.hset('deity_vow_description', 'propriety', '{"name":"Propriety",        "description":" seek glory, honor, and victory in tribute"                                                  }')
self.redis.hset('deity_vow_description', 'purity', '{"name":"Purity",           "description":"avoid contact with dead flesh"                                                               }')
self.redis.hset('deity_vow_description', 'reconstruction', '{"name":"Reconstruction",   "description":"reunite factions after a long and bitter feud"                                               }')
self.redis.hset('deity_vow_description', 'silence', '{"name":"Silence",          "description":"not speak under any circumstances"                                                           }')
self.redis.hset('deity_vow_description', 'stoicism', '{"name":"Stoicism",         "description":"speak as few words as possible, often a given word to represent their faith"                 }')
self.redis.hset('deity_vow_description', 'submission', '{"name":"Submission",       "description":"submit to those who ask of it"                                                               }')
self.redis.hset('deity_vow_description', 'surety', '{"name":"Surety",           "description":"defend a group or groups with your very life"                                                }')
