#

self.redis.zadd('magicitem_value', '{"name":"trivial magical item",  "score": 25   }', '25')
self.redis.zadd('magicitem_value', '{"name":"minor magical item",    "score": 65   }', '65')
self.redis.zadd('magicitem_value', '{"name":"medium magical item",   "score": 90   }', '90')
self.redis.zadd('magicitem_value', '{"name":"major magical item",    "score": 97   }', '97')
self.redis.zadd('magicitem_value', '{"name":"artifact",              "score": 100  }', '100')
        
# Foo is a quality greatsword that is _______ 
self.redis.zadd('magicitem_repair', '{"name":"broken",                    "score":5   }', '5')
self.redis.zadd('magicitem_repair', '{"name":"in disrepair",              "score":20  }', '20')
self.redis.zadd('magicitem_repair', '{"name":"intact",                    "score":60  }', '60')
self.redis.zadd('magicitem_repair', '{"name":"well maintained",           "score":80  }', '80')
self.redis.zadd('magicitem_repair', '{"name":"in pristine condition",     "score":100 }', '100')
        
self.redis.zadd('magicitem_strength', '{"name":"weak",         "score":20  }', '20')
self.redis.zadd('magicitem_strength', '{"name":"mediocre",     "score":40  }', '40')
self.redis.zadd('magicitem_strength', '{"name":"moderate",     "score":60  }', '60')
self.redis.zadd('magicitem_strength', '{"name":"strong",       "score":80  }', '80')
self.redis.zadd('magicitem_strength', '{"name":"powerful",     "score":100  }', '100')

# Foo is a ________ greatsword that is well maintained
self.redis.zadd('magicitem_quality', '{"name":"shoddy",   "score":20  }', '20')
self.redis.zadd('magicitem_quality', '{"name":"poor",     "score":40  }', '40')
self.redis.zadd('magicitem_quality', '{"name":"average",  "score":60  }', '60')
self.redis.zadd('magicitem_quality', '{"name":"good",     "score":80  }', '80')
self.redis.zadd('magicitem_quality', '{"name":"excellent","score":100 }', '100')
        
#        <location><!-- This ring can be found _________. -->
self.redis.lpush('magicitem_location', 'hidden on a corpse')
self.redis.lpush('magicitem_location', 'locked in a chest')
self.redis.lpush('magicitem_location', 'stashed in a crack in the wall')
self.redis.lpush('magicitem_location', 'forgotten on a shelf')
self.redis.lpush('magicitem_location', 'buried in a pile of refuse')
self.redis.lpush('magicitem_location', 'secreted away in a tomb')
self.redis.lpush('magicitem_location', 'buried in a nest')
self.redis.lpush('magicitem_location', 'hidden on a sage')

# The Good hammer _______ when ________ the hammer.
SET   magicitem_vibe_chance 40
self.redis.lpush('magicitem_vibe', 'makes you feel uncomfortable')
self.redis.lpush('magicitem_vibe', 'gives you feelings of power')
self.redis.lpush('magicitem_vibe', 'gives you feelings of might')

self.redis.lpush('magicitem_vibe_when', 'holding')
self.redis.lpush('magicitem_vibe_when', 'looking at')
self.redis.lpush('magicitem_vibe_when', 'approaching')
self.redis.lpush('magicitem_vibe_when', 'you look at')

        
#LPUSH magicitem_kind rings
#LPUSH magicitem_kind rods
#LPUSH magicitem_kind staves
#LPUSH magicitem_kind wands
#LPUSH magicitem_kind Wondrous Items

SET   magicitem_curse_chance 40


# Foo was created ___________ by a human named bob
self.redis.zadd('magicitem_age', '{"name":"recently",              "score":20  }', '20')
self.redis.zadd('magicitem_age', '{"name":"several months ago",    "score":40  }', '40')
self.redis.zadd('magicitem_age', '{"name":"several years ago",     "score":60  }', '60')
self.redis.zadd('magicitem_age', '{"name":"several decades ago",   "score":80  }', '80')
self.redis.zadd('magicitem_age', '{"name":"over a century ago",    "score":100 }', '100')

# this wand was created recently by _________
self.redis.lpush('magicitem_creator_template', '{{npc.race | article}}')
self.redis.lpush('magicitem_creator_template', '{{npc.race | article}} named {{npc.name.fullname}}')
self.redis.lpush('magicitem_creator_template', '{{npc.name.shortname}} the {{npc.race}}')
self.redis.lpush('magicitem_creator_template', '{{npc.attitude}} {{npc.race }} named {{npc.name.fullname}}')










