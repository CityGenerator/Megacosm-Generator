#ubiquity - Where can you find it? anywhere? just here?
# This resource is _________ to this particular region,
self.redis.zadd('resource_ubiquity', '{  "name":"very specific",      "score":50        }', '50')
self.redis.zadd('resource_ubiquity', '{  "name":"not specific",       "score":100       }', '100')
    
#Utility -  Level of Usefulness; Wool sweaters are not as useful in the tropics.
# which many consider ____________.
self.redis.zadd('resource_utility', '{  "name":"useless",         "score":50       }', '50')
self.redis.zadd('resource_utility', '{  "name":"useful",          "score":100      }', '100')

#Value- what do people consider this? (can be recalculated rather than randomly selected)
# slippers are often seen as a _______ resource.
self.redis.zadd('resource_value', '{  "name":"inexpensive",         "score":50       }', '50')
self.redis.zadd('resource_value', '{  "name":"valuable",          "score":100      }', '100')

#Competition -  How available is the resource for the region? the country? is this place the sole supplier? Is there a trade war?
#Competition in the frog market is ____
self.redis.zadd('resource_competition', '{  "name":"negligible",         "score":50       }', '50')
self.redis.zadd('resource_competition', '{  "name":"fierce",             "score":100      }', '100')

#Management - Is any effort being put in place to artificially control the production?
# And are ________ managed
self.redis.zadd('resource_management', '{  "name":"poorly",         "score":50       }', '50')
self.redis.zadd('resource_management', '{  "name":"well",           "score":100      }', '100')
       
# Depletion -  the amount of stuff left
# The deep mines are ___________.
self.redis.zadd('resource_depletion', '{  "name":"nearly-empty",         "score":50       }', '50')
self.redis.zadd('resource_depletion', '{  "name":"bountiful",           "score":100      }', '100')

# export region -  where does it get exported
# the fruit crops are exported  ___________.
self.redis.zadd('resource_exportregion', '{  "name":"to neighboring cities",         "score":50       }', '50')
self.redis.zadd('resource_exportregion', '{  "name":"across the continent",           "score":100      }', '100')

self.redis.lpush('resource_kind', 'naturalresource')
self.redis.lpush('resource_kind', 'laborresource')


self.redis.lpush('resource_template', '"{{params.place.name.fullname}} is known for its {{params.name_type}} {{params.name}} which {{params.method}} {{params.product}}. This resource is {{params.ubiquity[\'name\']}} to the region. Many consider the {{params.product}} {{params.utility[\'name\']}}, and are regardless seen as a {{params.value[\'name\']}} resource. Competition in the {{params.product}} market is {{params.competition[\'name\']}}, and the {{params.name}} resource as a whole are {{params.management[\'name\']}} managed."')



# Types of labor
# skilled labor
# unskilled labor
# slave labor
# manual labor
# volunteer labor
# free labor
# child labor
# 
