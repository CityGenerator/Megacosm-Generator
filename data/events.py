

self.redis.lpush('event_template', '{{params.variety }} {{params.kind}}, which is {{params.magnitude[\'name\']}} to the people in the area.')


#Magnitude - How important is this event?
# The event is _________ to the people in the area.
ZADD event_magnitude   0 {  "name":"negligible",                    "score":0        }
ZADD event_magnitude   5 {  "name":"trivial",                       "score":5        }
ZADD event_magnitude  10 {  "name":"unimportant",                   "score":10       }
ZADD event_magnitude  15 {  "name":"of minor importance",           "score":15       }
ZADD event_magnitude  20 {  "name":"of lesser concern",             "score":20       }
ZADD event_magnitude  25 {  "name":"of casual interest",            "score":25       }
ZADD event_magnitude  40 {  "name":"relevant",                      "score":40       }
ZADD event_magnitude  45 {  "name":"of some importance",            "score":45       }
ZADD event_magnitude  50 {  "name":"of some concern",               "score":50       }
ZADD event_magnitude  55 {  "name":"worthy of consideration",       "score":55       }
ZADD event_magnitude  70 {  "name":"important",                     "score":70       }
ZADD event_magnitude  75 {  "name":"of significant import",         "score":75       }
ZADD event_magnitude  80 {  "name":"of considerable importance",    "score":80       }
ZADD event_magnitude  85 {  "name":"of major concern",              "score":85       }
ZADD event_magnitude  90 {  "name":"of great significance",         "score":90       }
ZADD event_magnitude  95 {  "name":"of critical concern",           "score":95       }
ZADD event_magnitude 100 {  "name":"of dire importance",            "score":100      }


self.redis.lpush('event_kind', 'festival')
self.redis.lpush('eventfestival_variety', 'a religious')
self.redis.lpush('eventfestival_variety', 'a trade')

   
self.redis.lpush('event_kind', 'celebration')
self.redis.lpush('eventcelebration_variety', 'a birthday')
self.redis.lpush('eventcelebration_variety', 'a wedding')
self.redis.lpush('eventcelebration_variety', 'a new year')
self.redis.lpush('eventcelebration_variety', 'a holiday')
self.redis.lpush('eventcelebration_variety', 'a victory')
self.redis.lpush('eventcelebration_variety', 'a spontaneous')
   
self.redis.lpush('event_kind', 'trial')
self.redis.lpush('eventtrial_variety', 'a murder')
self.redis.lpush('eventtrial_variety', 'a witch')
self.redis.lpush('eventtrial_variety', 'a spy')
self.redis.lpush('eventtrial_variety', 'a brigand')
self.redis.lpush('eventtrial_variety', 'a thief')
   
self.redis.lpush('event_kind', 'war')
self.redis.lpush('eventwar_variety', 'preparations for')
self.redis.lpush('eventwar_variety', 'on ongoing')
self.redis.lpush('eventwar_variety', 'the aftermath of a')
   
self.redis.lpush('event_kind', 'raid')
self.redis.lpush('eventraid_variety', 'the midst of a')
self.redis.lpush('eventraid_variety', 'the aftermath of a')
   
self.redis.lpush('event_kind', 'hunt')
self.redis.lpush('eventhunt_variety', 'lost child')
self.redis.lpush('eventhunt_variety', 'wandering monster')
self.redis.lpush('eventhunt_variety', 'escaped prisoner')
self.redis.lpush('eventhunt_variety', 'food')
self.redis.lpush('eventhunt_variety', 'vermin')
self.redis.lpush('eventhunt_variety', 'fox')
self.redis.lpush('eventhunt_variety', 'sport')
   
self.redis.lpush('event_kind', 'disaster')

self.redis.lpush('eventdisaster_variety', 'animal infestation')
self.redis.lpush('eventdisaster_variety', 'avalanche')
self.redis.lpush('eventdisaster_variety', 'biological')
self.redis.lpush('eventdisaster_variety', 'blizzard')
self.redis.lpush('eventdisaster_variety', 'chemical')
self.redis.lpush('eventdisaster_variety', 'civil unrest')
self.redis.lpush('eventdisaster_variety', 'cold snap ')
self.redis.lpush('eventdisaster_variety', 'creature infestation')
self.redis.lpush('eventdisaster_variety', 'crop failure')
self.redis.lpush('eventdisaster_variety', 'cyclone')
self.redis.lpush('eventdisaster_variety', 'displaced population')
self.redis.lpush('eventdisaster_variety', 'drought')
self.redis.lpush('eventdisaster_variety', 'earthquake')
self.redis.lpush('eventdisaster_variety', 'electrical storm')
self.redis.lpush('eventdisaster_variety', 'epidemic')
self.redis.lpush('eventdisaster_variety', 'explosion')
self.redis.lpush('eventdisaster_variety', 'famine')
self.redis.lpush('eventdisaster_variety', 'flash flood')
self.redis.lpush('eventdisaster_variety', 'flood')
self.redis.lpush('eventdisaster_variety', 'gamma ray burst')
self.redis.lpush('eventdisaster_variety', 'genocide')
self.redis.lpush('eventdisaster_variety', 'geomagnetic storm')
self.redis.lpush('eventdisaster_variety', 'heatwave')
self.redis.lpush('eventdisaster_variety', 'impact event')
self.redis.lpush('eventdisaster_variety', 'insect infestation')
self.redis.lpush('eventdisaster_variety', 'land slip')
self.redis.lpush('eventdisaster_variety', 'limnic eruption')
self.redis.lpush('eventdisaster_variety', 'magical')
self.redis.lpush('eventdisaster_variety', 'massive storm')
self.redis.lpush('eventdisaster_variety', 'meteor strike')
self.redis.lpush('eventdisaster_variety', 'mudflow')
self.redis.lpush('eventdisaster_variety', 'mudslide')
self.redis.lpush('eventdisaster_variety', 'plague')
self.redis.lpush('eventdisaster_variety', 'riots')
self.redis.lpush('eventdisaster_variety', 'rock fall')
self.redis.lpush('eventdisaster_variety', 'rockslide')
self.redis.lpush('eventdisaster_variety', 'rock topple')
self.redis.lpush('eventdisaster_variety', 'sinkhole')
self.redis.lpush('eventdisaster_variety', 'tarrasque')
self.redis.lpush('eventdisaster_variety', 'tornado')
self.redis.lpush('eventdisaster_variety', 'tsunami')
self.redis.lpush('eventdisaster_variety', 'violent storm')
self.redis.lpush('eventdisaster_variety', 'volcano')
self.redis.lpush('eventdisaster_variety', 'wildfire ')
self.redis.lpush('eventdisaster_variety', 'wind storm ')
   



