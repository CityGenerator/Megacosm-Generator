#

self.redis.lpush('gem_template', 'You find {{params.amount[\'name\']}} {{params.quality[\'name\']}} {{params.cut}} {{params.kind_description[\'name\']|pluralize(params.count)}}. The color is {{params.saturation[\'name\']}} {{params.color}}. {{"This"| plural_adj(params.count)}} {{"gem"| pluralize(params.count)}} {{"is"| plural_verb(params.count)}} {{params.value[\'name\']}}.')

ZADD gem_amount  10 { "name":"a single",           "min":1,    "max":1,    "score":10  }
ZADD gem_amount  20 { "name":"a pair of",          "min":2,    "max":2,    "score":20  }
ZADD gem_amount  30 { "name":"a few",              "min":3,    "max":4,    "score":30  }
ZADD gem_amount  40 { "name":"several",            "min":3,    "max":8,    "score":40  }
ZADD gem_amount  60 { "name":"a handful",          "min":4,    "max":10,   "score":60  }
ZADD gem_amount  80 { "name":"about a dozen",      "min":8,    "max":15,   "score":80  }
ZADD gem_amount  90 { "name":"about two dozen",    "min":20,   "max":30,   "score":90  }
ZADD gem_amount  95 { "name":"a few dozen",        "min":30,   "max":60,   "score":95  }
ZADD gem_amount 100 { "name":"a large pile of",    "min":30,   "max":120,  "score":100 }

ZADD gem_value  10 { "name":"near worthless",           "score":10  }
ZADD gem_value  20 { "name":"of little value",          "score":20  }
ZADD gem_value  30 { "name":"worth a few coins",        "score":30  }
ZADD gem_value  40 { "name":"cheap",                    "score":40  }
ZADD gem_value  50 { "name":"of moderate value",        "score":50  }
ZADD gem_value  60 { "name":"costly",                   "score":60  }
ZADD gem_value  70 { "name":"very valuable",            "score":70  }
ZADD gem_value  80 { "name":"worth a small fortune",    "score":80  }
ZADD gem_value  90 { "name":"of inestimable value",     "score":90  }
ZADD gem_value 100 { "name":"worth a king\'s ransom",    "score":100  }

ZADD gem_saturation  10 { "name":"blanched",    "score":10  }
ZADD gem_saturation  20 { "name":"dull",        "score":20  }
ZADD gem_saturation  30 { "name":"washed out",  "score":30  }
ZADD gem_saturation  40 { "name":"pale",        "score":40  }
ZADD gem_saturation  50 { "name":"strong",      "score":50  }
ZADD gem_saturation  60 { "name":"intense",     "score":60  }
ZADD gem_saturation  70 { "name":"rich",        "score":70  }
ZADD gem_saturation  80 { "name":"vivid",       "score":80  }
ZADD gem_saturation  90 { "name":"brilliant",   "score":90  }
ZADD gem_saturation 100 { "name":"vibrant",     "score":100 }

ZADD gem_quality  20 { "name":"chipped"     , "score":20   }
ZADD gem_quality  40 { "name":"flawed"      , "score":40   }
ZADD gem_quality  60 { "name":"flawless"    , "score":60   }
ZADD gem_quality  80 { "name":"radiant"     , "score":80   }
ZADD gem_quality 100 { "name":"perfect"     , "score":100  }


SET   gem_cut_chance 50
self.redis.lpush('gem_cut', 'baguette')
self.redis.lpush('gem_cut', 'briolette')
self.redis.lpush('gem_cut', 'cushion')
self.redis.lpush('gem_cut', 'fancy')
self.redis.lpush('gem_cut', 'flower')
self.redis.lpush('gem_cut', 'heart')
self.redis.lpush('gem_cut', 'marquise')
self.redis.lpush('gem_cut', 'octagon')
self.redis.lpush('gem_cut', 'oval')
self.redis.lpush('gem_cut', 'pear')
self.redis.lpush('gem_cut', 'round')
self.redis.lpush('gem_cut', 'slice')
self.redis.lpush('gem_cut', 'sphere')
self.redis.lpush('gem_cut', 'square')
self.redis.lpush('gem_cut', 'trillion')


self.redis.hset('gem_kind_description', 'agate', '{ "name":"agate", "color":["black","blue","brown","green","white","yellow"]   }')
self.redis.hset('gem_kind_description', 'amethyst', '{ "name":"amethyst", "color":["violet"]   }')
self.redis.hset('gem_kind_description', 'ametrine', '{ "name":"ametrine", "color":["multicolor"]   }')
self.redis.hset('gem_kind_description', 'andalusite', '{ "name":"andalusite", "color":["multicolor"]   }')
self.redis.hset('gem_kind_description', 'andesine', '{ "name":"andesine", "color":["orange","red"]   }')
self.redis.hset('gem_kind_description', 'apatite', '{ "name":"apatite", "color":["blue","green"]   }')
self.redis.hset('gem_kind_description', 'aquamarine', '{ "name":"aquamarine", "color":["blue"]   }')
self.redis.hset('gem_kind_description', 'aventurine', '{ "name":"aventurine", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'beryl', '{ "name":"beryl", "color":["yellow"]   }')
self.redis.hset('gem_kind_description', 'chalcedony', '{ "name":"chalcedony", "color":["violet"]   }')
self.redis.hset('gem_kind_description', 'chromediopside', '{ "name":"chrome diopside", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'chrometourmaline', '{ "name":"chrome tourmaline", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'chrysoberyl', '{ "name":"chrysoberyl", "color":["yellow"]   }')
self.redis.hset('gem_kind_description', 'citrine', '{ "name":"citrine", "color":["orange","yellow"]   }')
self.redis.hset('gem_kind_description', 'demantoidgarnet', '{ "name":"demantoid garnet", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'diamond', '{ "name":"diamond", "color":["black","white","yellow"]   }')
self.redis.hset('gem_kind_description', 'emerald', '{ "name":"emerald", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'fireopal', '{ "name":"fire opal", "color":["orange","white","yellow"]   }')
self.redis.hset('gem_kind_description', 'fluorite', '{ "name":"fluorite", "color":["blue","multicolor","silver","violet"]   }')
self.redis.hset('gem_kind_description', 'garnet', '{ "name":"garnet", "color":["red"]   }')
self.redis.hset('gem_kind_description', 'imperialtopaz', '{ "name":"imperial topaz", "color":["brown","orange"]   }')
self.redis.hset('gem_kind_description', 'iolite', '{ "name":"iolite", "color":["blue"]   }')
self.redis.hset('gem_kind_description', 'jade', '{ "name":"jade", "color":["green","white"]   }')
self.redis.hset('gem_kind_description', 'kunzite', '{ "name":"kunzite", "color":["pink"]   }')
self.redis.hset('gem_kind_description', 'kyanite', '{ "name":"kyanite", "color":["blue"]   }')
self.redis.hset('gem_kind_description', 'lapislazuli', '{ "name":"lapis lazuli", "color":["blue"]   }')
self.redis.hset('gem_kind_description', 'moonstone', '{ "name":"moonstone", "color":["orange","white"]   }')
self.redis.hset('gem_kind_description', 'morganite', '{ "name":"morganite", "color":["pink"]   }')
self.redis.hset('gem_kind_description', 'mysticquartz', '{ "name":"mystic quartz", "color":["multicolor"]   }')
self.redis.hset('gem_kind_description', 'mystictopaz', '{ "name":"mystic topaz", "color":["multicolor"]   }')
self.redis.hset('gem_kind_description', 'onyx', '{ "name":"onyx", "color":["black"]   }')
self.redis.hset('gem_kind_description', 'opal', '{ "name":"opal", "color":["multicolor"]   }')
self.redis.hset('gem_kind_description', 'orthoclase', '{ "name":"orthoclase", "color":["yellow"]   }')
self.redis.hset('gem_kind_description', 'paraibatourmaline', '{ "name":"paraiba tourmaline", "color":["blue","green"]   }')
self.redis.hset('gem_kind_description', 'peridot', '{ "name":"peridot", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'prehnite', '{ "name":"prehnite", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'quartz', '{ "name":"quartz", "color":["white","yellow"]   }')
self.redis.hset('gem_kind_description', 'rainbowmoonstone', '{ "name":"rainbow moonstone", "color":["blue"]   }')
self.redis.hset('gem_kind_description', 'rhodolitegarnet', '{ "name":"rhodolite garnet", "color":["pink"]   }')
self.redis.hset('gem_kind_description', 'rosequartz', '{ "name":"rose quartz", "color":["pink"]   }')
self.redis.hset('gem_kind_description', 'ruby', '{ "name":"ruby", "color":["red"]   }')
self.redis.hset('gem_kind_description', 'rubyzoisite', '{ "name":"ruby-zoisite", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'sapphire', '{ "name":"sapphire", "color":["black","blue","green","multicolor","orange","pink","violet","white","yellow"]   }')
self.redis.hset('gem_kind_description', 'smokyquartz', '{ "name":"smoky quartz", "color":["brown"]   }')
self.redis.hset('gem_kind_description', 'spessartitegarnet', '{ "name":"spessartite garnet", "color":["orange"]   }')
self.redis.hset('gem_kind_description', 'sphene', '{ "name":"sphene", "color":["multicolor","yellow"]   }')
self.redis.hset('gem_kind_description', 'spinel', '{ "name":"spinel", "color":["blue","pink","red","silver", "violet"]   }')
self.redis.hset('gem_kind_description', 'spodumene', '{ "name":"spodumene", "color":["yellow"]   }')
self.redis.hset('gem_kind_description', 'starmoonstone', '{ "name":"star moonstone", "color":["orange"]   }')
self.redis.hset('gem_kind_description', 'starsapphire', '{ "name":"star sapphire", "color":["black"]   }')
self.redis.hset('gem_kind_description', 'tanzanite', '{ "name":"tanzanite", "color":["blue"]   }')
self.redis.hset('gem_kind_description', 'tigerseye', '{ "name":"tiger\'s eye", "color":["brown"]   }')
self.redis.hset('gem_kind_description', 'topaz', '{ "name":"topaz", "color":["blue","white"]   }')
self.redis.hset('gem_kind_description', 'tourmaline', '{ "name":"tourmaline", "color":["black","blue","brown","green","multicolor","orange","pink","red","silver","violet","yellow"]   }')
self.redis.hset('gem_kind_description', 'tsavoritegarnet', '{ "name":"tsavorite garnet", "color":["green"]   }')
self.redis.hset('gem_kind_description', 'zircon', '{ "name":"zircon", "color":["blue","orange","red","white","yellow"]   }')

self.redis.lpush('gem_kind', 'agate')
self.redis.lpush('gem_kind', 'amethyst')
self.redis.lpush('gem_kind', 'ametrine')
self.redis.lpush('gem_kind', 'andalusite')
self.redis.lpush('gem_kind', 'andesine')
self.redis.lpush('gem_kind', 'apatite')
self.redis.lpush('gem_kind', 'aquamarine')
self.redis.lpush('gem_kind', 'aventurine')
self.redis.lpush('gem_kind', 'beryl')
self.redis.lpush('gem_kind', 'chalcedony')
self.redis.lpush('gem_kind', 'chromediopside')
self.redis.lpush('gem_kind', 'chrometourmaline')
self.redis.lpush('gem_kind', 'chrysoberyl')
self.redis.lpush('gem_kind', 'citrine')
self.redis.lpush('gem_kind', 'demantoidgarnet')
self.redis.lpush('gem_kind', 'diamond')
self.redis.lpush('gem_kind', 'emerald')
self.redis.lpush('gem_kind', 'fireopal')
self.redis.lpush('gem_kind', 'fluorite')
self.redis.lpush('gem_kind', 'garnet')
self.redis.lpush('gem_kind', 'imperialtopaz')
self.redis.lpush('gem_kind', 'iolite')
self.redis.lpush('gem_kind', 'jade')
self.redis.lpush('gem_kind', 'kunzite')
self.redis.lpush('gem_kind', 'kyanite')
self.redis.lpush('gem_kind', 'lapislazuli')
self.redis.lpush('gem_kind', 'moonstone')
self.redis.lpush('gem_kind', 'morganite')
self.redis.lpush('gem_kind', 'mysticquartz')
self.redis.lpush('gem_kind', 'mystictopaz')
self.redis.lpush('gem_kind', 'onyx')
self.redis.lpush('gem_kind', 'opal')
self.redis.lpush('gem_kind', 'orthoclase')
self.redis.lpush('gem_kind', 'paraibatourmaline')
self.redis.lpush('gem_kind', 'peridot')
self.redis.lpush('gem_kind', 'prehnite')
self.redis.lpush('gem_kind', 'quartz')
self.redis.lpush('gem_kind', 'rainbowmoonstone')
self.redis.lpush('gem_kind', 'rhodolitegarnet')
self.redis.lpush('gem_kind', 'rosequartz')
self.redis.lpush('gem_kind', 'ruby')
self.redis.lpush('gem_kind', 'rubyzoisite')
self.redis.lpush('gem_kind', 'sapphire')
self.redis.lpush('gem_kind', 'smokyquartz')
self.redis.lpush('gem_kind', 'spessartitegarnet')
self.redis.lpush('gem_kind', 'sphene')
self.redis.lpush('gem_kind', 'spinel')
self.redis.lpush('gem_kind', 'spodumene')
self.redis.lpush('gem_kind', 'starmoonstone')
self.redis.lpush('gem_kind', 'starsapphire')
self.redis.lpush('gem_kind', 'tanzanite')
self.redis.lpush('gem_kind', 'tigerseye')
self.redis.lpush('gem_kind', 'topaz')
self.redis.lpush('gem_kind', 'tourmaline')
self.redis.lpush('gem_kind', 'tsavoritegarnet')
self.redis.lpush('gem_kind', 'zircon')
