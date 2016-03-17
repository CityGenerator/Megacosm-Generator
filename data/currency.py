# You find ____________ coins[s].

ZADD currency_amount   5 { "name":"a single",           "min":1,    "max":1,    "score":5   }
ZADD currency_amount  10 { "name":"a pair of",          "min":2,    "max":2,    "score":10  }
ZADD currency_amount  20 { "name":"a few",              "min":3,    "max":4,    "score":20  }
ZADD currency_amount  20 { "name":"several",            "min":3,    "max":8,    "score":20  }
ZADD currency_amount  30 { "name":"a handful",          "min":4,    "max":10,   "score":30  }
ZADD currency_amount  40 { "name":"about a dozen",      "min":8,    "max":15,   "score":40  }
ZADD currency_amount  60 { "name":"about two dozen",    "min":20,   "max":30,   "score":60  }
ZADD currency_amount  70 { "name":"a few dozen",        "min":30,   "max":60,   "score":70  }
ZADD currency_amount  80 { "name":"several dozen",      "min":50,   "max":100,  "score":80  }
ZADD currency_amount  90 { "name":"around a hundred",   "min":90,   "max":130,  "score":90  }
ZADD currency_amount  95 { "name":"a couple hundred",   "min":190,  "max":250,  "score":95  }
ZADD currency_amount 100 { "name":"a large pile of",    "min":100,  "max":3000, "score":100 }

ZADD currency_size  10 { "name":"tiny ( 18mm )"    , "score":10  }
ZADD currency_size  30 { "name":"small ( 20mm )"   , "score":30  }
ZADD currency_size  70 { "name":"medium ( 24mm )"  , "score":70  }
ZADD currency_size  90 { "name":"large ( 30mm )"   , "score":90  }
ZADD currency_size 100 { "name":"giant (40mm )"    , "score":100 }

# the Bon is a worthless ingot
ZADD currency_value  10 { "name":"worthless",         "score":10  }
ZADD currency_value  30 { "name":"low-value",         "score":30  }
ZADD currency_value  70 { "name":"moderate-value",    "score":70  }
ZADD currency_value  98 { "name":"high-value",        "score":98  }
ZADD currency_value 100 { "name":"priceless",         "score":100  }

ZADD currency_scope  15 { "name":"city",        "score":15  }
ZADD currency_scope  95 { "name":"region",      "score":95  }
ZADD currency_scope 100 { "name":"continent",   "score":100  }

# The level of detail on the Dorsh is ________
ZADD currency_detail   5 {     "name":"crude" , "score":5  }
ZADD currency_detail  10 {     "name":"rough" , "score":10  }
ZADD currency_detail  15 {     "name":"careless" , "score":15  }
ZADD currency_detail  20 {     "name":"lax" , "score":20  }
ZADD currency_detail  25 {     "name":"uncomplicated" , "score":25  }
ZADD currency_detail  30 {     "name":"precise" , "score":30  }
ZADD currency_detail  40 {     "name":"refined" , "score":40  }
ZADD currency_detail  50 {     "name":"exact" , "score":50  }
ZADD currency_detail  60 {     "name":"sophisticated" , "score":60  }
ZADD currency_detail  70 {     "name":"intricate" , "score":70  }
ZADD currency_detail  80 {     "name":"elaborate" , "score":80  }
ZADD currency_detail  90 {     "name":"meticulous" , "score":90  }
ZADD currency_detail 100 {     "name":"unmistakable" , "score":100  }

# the kole is _____ for its size.-->
ZADD currency_weight  20 {      "name":"lightweight" , "score":20  }
ZADD currency_weight  80 {      "name":"ideally weighted" , "score":80  }
ZADD currency_weight 100 {      "name":"hefty" , "score":100  }

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


