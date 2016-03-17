# You find ____________ coins[s].

self.redis.zadd('currency_amount', '{ "name":"a single",           "min":1,    "max":1,    "score":5   }', '5')
self.redis.zadd('currency_amount', '{ "name":"a pair of",          "min":2,    "max":2,    "score":10  }', '10')
self.redis.zadd('currency_amount', '{ "name":"a few",              "min":3,    "max":4,    "score":20  }', '20')
self.redis.zadd('currency_amount', '{ "name":"several",            "min":3,    "max":8,    "score":20  }', '20')
self.redis.zadd('currency_amount', '{ "name":"a handful",          "min":4,    "max":10,   "score":30  }', '30')
self.redis.zadd('currency_amount', '{ "name":"about a dozen",      "min":8,    "max":15,   "score":40  }', '40')
self.redis.zadd('currency_amount', '{ "name":"about two dozen",    "min":20,   "max":30,   "score":60  }', '60')
self.redis.zadd('currency_amount', '{ "name":"a few dozen",        "min":30,   "max":60,   "score":70  }', '70')
self.redis.zadd('currency_amount', '{ "name":"several dozen",      "min":50,   "max":100,  "score":80  }', '80')
self.redis.zadd('currency_amount', '{ "name":"around a hundred",   "min":90,   "max":130,  "score":90  }', '90')
self.redis.zadd('currency_amount', '{ "name":"a couple hundred",   "min":190,  "max":250,  "score":95  }', '95')
self.redis.zadd('currency_amount', '{ "name":"a large pile of",    "min":100,  "max":3000, "score":100 }', '100')

self.redis.zadd('currency_size', '{ "name":"tiny ( 18mm )"    , "score":10  }', '10')
self.redis.zadd('currency_size', '{ "name":"small ( 20mm )"   , "score":30  }', '30')
self.redis.zadd('currency_size', '{ "name":"medium ( 24mm )"  , "score":70  }', '70')
self.redis.zadd('currency_size', '{ "name":"large ( 30mm )"   , "score":90  }', '90')
self.redis.zadd('currency_size', '{ "name":"giant (40mm )"    , "score":100 }', '100')

# the Bon is a worthless ingot
self.redis.zadd('currency_value', '{ "name":"worthless",         "score":10  }', '10')
self.redis.zadd('currency_value', '{ "name":"low-value",         "score":30  }', '30')
self.redis.zadd('currency_value', '{ "name":"moderate-value",    "score":70  }', '70')
self.redis.zadd('currency_value', '{ "name":"high-value",        "score":98  }', '98')
self.redis.zadd('currency_value', '{ "name":"priceless",         "score":100  }', '100')

self.redis.zadd('currency_scope', '{ "name":"city",        "score":15  }', '15')
self.redis.zadd('currency_scope', '{ "name":"region",      "score":95  }', '95')
self.redis.zadd('currency_scope', '{ "name":"continent",   "score":100  }', '100')

# The level of detail on the Dorsh is ________
self.redis.zadd('currency_detail', '{     "name":"crude" , "score":5  }', '5')
self.redis.zadd('currency_detail', '{     "name":"rough" , "score":10  }', '10')
self.redis.zadd('currency_detail', '{     "name":"careless" , "score":15  }', '15')
self.redis.zadd('currency_detail', '{     "name":"lax" , "score":20  }', '20')
self.redis.zadd('currency_detail', '{     "name":"uncomplicated" , "score":25  }', '25')
self.redis.zadd('currency_detail', '{     "name":"precise" , "score":30  }', '30')
self.redis.zadd('currency_detail', '{     "name":"refined" , "score":40  }', '40')
self.redis.zadd('currency_detail', '{     "name":"exact" , "score":50  }', '50')
self.redis.zadd('currency_detail', '{     "name":"sophisticated" , "score":60  }', '60')
self.redis.zadd('currency_detail', '{     "name":"intricate" , "score":70  }', '70')
self.redis.zadd('currency_detail', '{     "name":"elaborate" , "score":80  }', '80')
self.redis.zadd('currency_detail', '{     "name":"meticulous" , "score":90  }', '90')
self.redis.zadd('currency_detail', '{     "name":"unmistakable" , "score":100  }', '100')

# the kole is _____ for its size.-->
self.redis.zadd('currency_weight', '{      "name":"lightweight" , "score":20  }', '20')
self.redis.zadd('currency_weight', '{      "name":"ideally weighted" , "score":80  }', '80')
self.redis.zadd('currency_weight', '{      "name":"hefty" , "score":100  }', '100')

# and is made out of
self.redis.lpush('currency_material', 'wood')
self.redis.lpush('currency_material', 'shell')
self.redis.lpush('currency_material', 'copper')
self.redis.lpush('currency_material', 'silver')
self.redis.lpush('currency_material', 'electrum')
self.redis.lpush('currency_material', 'gold')
self.redis.lpush('currency_material', 'platinum')
self.redis.lpush('currency_material', 'steel')

# the Drachma is a[n] _______ ingot minted by the regional authority
self.redis.lpush('currency_shape', 'triangular')
self.redis.lpush('currency_shape', 'square')
self.redis.lpush('currency_shape', 'rectangular')
self.redis.lpush('currency_shape', 'pentagonal')
self.redis.lpush('currency_shape', 'hexagonal')
self.redis.lpush('currency_shape', 'circular')

# with _____ edges
SET   currency_edges_chance 10
self.redis.lpush('currency_edges', 'ridged')
self.redis.lpush('currency_edges', 'wavy')
self.redis.lpush('currency_edges', 'smooth')
self.redis.lpush('currency_edges', 'cornered')
self.redis.lpush('currency_edges', 'ringed')

# On the front side of the coin is a[n] ________, while the reverse side has a[n] _________.
self.redis.lpush('currency_front', 'man\'s face')
self.redis.lpush('currency_front', 'king\'s face')
self.redis.lpush('currency_front', 'queen\'s face')

self.redis.lpush('currency_back', 'dragon')
self.redis.lpush('currency_back', 'building')
self.redis.lpush('currency_back', 'crest')
self.redis.lpush('currency_back', 'religious symbol')

self.redis.lpush('currency_template', '{{params.name.fullname|article|title}} is {{params.weight[\'name\'] | article}}, {{params.value[\'name\']}} coin that is common in the {{params.scope[\'name\']}}. It is {{params.size[\'name\']}}, {{params.shape}}, and made of {{params.material}}. The coins are covered with {{params.detail[\'name\']}} designs.')
self.redis.lpush('currency_template', '{{params.name.fullname|article|title}} is {{params.value[\'name\'] | article}}, {{params.weight[\'name\']}} coin that is minted in the {{params.scope[\'name\']}}. It is {{params.shape}}, {{params.size[\'name\']}}, and made of {{params.material}}. The designs on the coin are {{params.detail[\'name\']}}.  On the front side of the coin is {{params.front |article}}, while the reverse side has {{params.back |article}}.')


