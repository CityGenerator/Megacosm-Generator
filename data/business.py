
# TODO we need entries for how business is going, current troubles, etc.
# bob\'s hut has recently had  _____________
set business_trouble_chance 20
self.redis.lpush('business_trouble', 'concerns over a recent rash of break-ins in the neighborhood')
self.redis.lpush('business_trouble', 'problems with local law enforcement')
self.redis.lpush('business_trouble', 'problems with petty theft')
self.redis.lpush('business_trouble', 'supply caravans never show up')
self.redis.lpush('business_trouble', 'problems with pests')
self.redis.lpush('business_trouble', 'issues with thieves')
self.redis.lpush('business_trouble', 'a fire')
self.redis.lpush('business_trouble', 'slumping sales')

# Business is  _____________.
ZADD business_status  10 {  "name":"horrible",           "score":10  }
ZADD business_status  20 {  "name":"bad",                "score":20  }
ZADD business_status  30 {  "name":"not good",           "score":30  }
ZADD business_status  40 {  "name":"stagnant",           "score":40  }
ZADD business_status  50 {  "name":"middling",           "score":50  }
ZADD business_status  60 {  "name":"ok",                 "score":60  }
ZADD business_status  70 {  "name":"not bad",            "score":70  }
ZADD business_status  80 {  "name":"doing great",        "score":80  }
ZADD business_status  90 {  "name":"going excellent",    "score":90  }
ZADD business_status 100 {  "name":"booming",            "score":100 }


#        The Perfumed Twins Vintners is a[n] _______, disgusting-looking vineyard.
ZADD business_size 5   {  "name":"tiny"           , "score":5   }
ZADD business_size 10  {  "name":"insignificant"  , "score":10  }
ZADD business_size 15  {  "name":"squat"          , "score":15  }
ZADD business_size 20  {  "name":"small"          , "score":20  }
ZADD business_size 25  {  "name":"minor"          , "score":25  }
ZADD business_size 30  {  "name":"insubstantial"  , "score":30  }
ZADD business_size 35  {  "name":"paltry"         , "score":35  }
ZADD business_size 40  {  "name":"normal"         , "score":40  }
ZADD business_size 45  {  "name":"typical"        , "score":45  }
ZADD business_size 50  {  "name":"humdrum"        , "score":50  }
ZADD business_size 55  {  "name":"ordinary"       , "score":55  }
ZADD business_size 60  {  "name":"average"        , "score":60  }
ZADD business_size 65  {  "name":"familiar"       , "score":65  }
ZADD business_size 70  {  "name":"large"          , "score":70  }
ZADD business_size 75  {  "name":"sizable"        , "score":75  }
ZADD business_size 80  {  "name":"epic"           , "score":80  }
ZADD business_size 85  {  "name":"monumental"     , "score":85  }
ZADD business_size 90  {  "name":"massive"        , "score":90  }
ZADD business_size 95  {  "name":"enormous"       , "score":95  }
ZADD business_size 100 {  "name":"vast"           , "score":100 }

#   The Wet Frog is a garden-variety tavern that  ____________.
ZADD business_popularity 5   {  "name":"is avoided by the locals for reasons unknown"       , "score":5   }
ZADD business_popularity 10  {  "name":"is unappreciated by the locals"                     , "score":10  }
ZADD business_popularity 15  {  "name":"is usually empty"                                   , "score":15  }
ZADD business_popularity 20  {  "name":"is usually busy but is strangely quiet as of late"  , "score":20  }
ZADD business_popularity 25  {  "name":"holds the record for worst service in the region"   , "score":25  }
ZADD business_popularity 30  {  "name":"has strange opening hours"                          , "score":30  }
ZADD business_popularity 35  {  "name":"only attracts people from out of town"              , "score":35  }
ZADD business_popularity 40  {  "name":"is popular on market days"                          , "score":40  }
ZADD business_popularity 45  {  "name":"is eerily empty"                                    , "score":45  }
ZADD business_popularity 50  {  "name":"is completely abandoned, and often forgotten"       , "score":50  }
ZADD business_popularity 55  {  "name":"usually has few visitors"                           , "score":55  }
ZADD business_popularity 60  {  "name":"is empty during the day but busy in the evening"    , "score":60  }
ZADD business_popularity 65  {  "name":"is on the verge of closing"                         , "score":65  }
ZADD business_popularity 70  {  "name":"is busy most days"                                  , "score":70  }
ZADD business_popularity 75  {  "name":"is crowded every night"                             , "score":75  }
ZADD business_popularity 80  {  "name":"rarely has room for new business"                   , "score":80  }
ZADD business_popularity 85  {  "name":"has people queuing out in the street"               , "score":85  }
ZADD business_popularity 90  {  "name":"is one of the busiest places in town"               , "score":90  }
ZADD business_popularity 95  {  "name":"is always busy, regardless of the time"             , "score":95  }
ZADD business_popularity 100 {  "name":"is constantly crowded"                              , "score":100 }


# The tavern has a reputation for _____________.
ZADD business_reputation 10 {  "name":"deplorable clientele"                     , "score":10  }
ZADD business_reputation 20 {  "name":"being a hive of scum and villainy"        , "score":20  }
ZADD business_reputation 30 {  "name":"unpaid bills being bad for your health"   , "score":30  }
ZADD business_reputation 40 {  "name":"poor sanitation"                          , "score":40  }
ZADD business_reputation 50 {  "name":"unfortunate accidents"                    , "score":50  }
ZADD business_reputation 60 {  "name":"being dull"                               , "score":60  }
ZADD business_reputation 70 {  "name":"being open all hours"                     , "score":70  }
ZADD business_reputation 80 {  "name":"having good services"                     , "score":80  }
ZADD business_reputation 90 {  "name":"being a good place to find rumors"        , "score":90  }
ZADD business_reputation 100 {  "name":"being a pillar of the community"          , "score":100  }


# ... is known for ______________ prices for...
ZADD business_price 6 {  "name":"suspiciously low"   , "score":6  }
ZADD business_price 12 {  "name":"next to nothing"    , "score":12  }
ZADD business_price 18 {  "name":"dirt cheap"         , "score":18  }
ZADD business_price 24 {  "name":"inexpensive"        , "score":24  }
ZADD business_price 30 {  "name":"fair"               , "score":30  }
ZADD business_price 36 {  "name":"slightly high"      , "score":36  }
ZADD business_price 42 {  "name":"minimal"            , "score":42  }
ZADD business_price 48 {  "name":"varying"            , "score":48  }
ZADD business_price 54 {  "name":"reasonable"         , "score":54  }
ZADD business_price 60 {  "name":"moderate"           , "score":60  }
ZADD business_price 66 {  "name":"steep"              , "score":66  }
ZADD business_price 72 {  "name":"unreasonable"       , "score":72  }
ZADD business_price 78 {  "name":"extravagant"        , "score":78  }
ZADD business_price 94 {  "name":"high"               , "score":94  }
ZADD business_price 100 {  "name":"very high"          , "score":100  }


#TODO chance this to a stat
ZADD business_age  50 {  "name":"new"          , "score":50  }
ZADD business_age 100 {  "name":"old"          , "score":100  }

#TODO turn this into a stat
ZADD business_neighborhood  10 { "name":"seedy",        "score":10  }
ZADD business_neighborhood  20 { "name":"trashy",       "score":20  }
ZADD business_neighborhood  30 { "name":"empty",        "score":30  }
ZADD business_neighborhood  40 { "name":"rundown",      "score":40  }
ZADD business_neighborhood  70 { "name":"new",          "score":70  }
ZADD business_neighborhood  80 { "name":"old",          "score":80  }
ZADD business_neighborhood  90 { "name":"nice",         "score":90  }
ZADD business_neighborhood 100 { "name":"expensive",    "score":100 }

self.redis.lpush('business_condition', 'neat')
self.redis.lpush('business_condition', 'tidy')
self.redis.lpush('business_condition', 'messy')
self.redis.lpush('business_condition', 'crowded')
self.redis.lpush('business_condition', 'dirty')
self.redis.lpush('business_condition', 'clean')
self.redis.lpush('business_condition', 'packed')
self.redis.lpush('business_condition', 'orderly')
self.redis.lpush('business_condition', 'dusty')
self.redis.lpush('business_condition', 'cluttered')
self.redis.lpush('business_condition', 'damp')
self.redis.lpush('business_condition', 'smelly')
self.redis.lpush('business_condition', 'disgusting')
self.redis.lpush('business_condition', 'filthy')

self.redis.lpush('business_rooftype', 'tile')
self.redis.lpush('business_rooftype', 'slate')
self.redis.lpush('business_rooftype', 'thatch')
self.redis.lpush('business_rooftype', 'turf')

self.redis.lpush('business_storefront', 'lap board')
self.redis.lpush('business_storefront', 'stone')
self.redis.lpush('business_storefront', 'brick')
self.redis.lpush('business_storefront', 'wood')
self.redis.lpush('business_storefront', 'bamboo')
self.redis.lpush('business_storefront', 'mud')
self.redis.lpush('business_storefront', 'masonry')
self.redis.lpush('business_storefront', 'split wood')

# The building has _______ windows.
self.redis.lpush('business_windows', 'no')
self.redis.lpush('business_windows', 'round')
self.redis.lpush('business_windows', 'barred')
self.redis.lpush('business_windows', 'tiny')
self.redis.lpush('business_windows', 'dirty')
self.redis.lpush('business_windows', 'stained')
self.redis.lpush('business_windows', 'broken')
self.redis.lpush('business_windows', 'large')
self.redis.lpush('business_windows', 'a few')
self.redis.lpush('business_windows', 'clean')
self.redis.lpush('business_windows', 'many')
self.redis.lpush('business_windows', 'small')
self.redis.lpush('business_windows', 'two')
self.redis.lpush('business_windows', 'three')

self.redis.lpush('business_shade', 'bright')
self.redis.lpush('business_shade', 'dark')

self.redis.lpush('business_direction', 'west')
self.redis.lpush('business_direction', 'northwest')
self.redis.lpush('business_direction', 'north')
self.redis.lpush('business_direction', 'northeast')
self.redis.lpush('business_direction', 'east')
self.redis.lpush('business_direction', 'southeast')
self.redis.lpush('business_direction', 'south')
self.redis.lpush('business_direction', 'southwest')

