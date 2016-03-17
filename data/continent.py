
# East Amoro is a _______ continent
self.redis.zadd('continent_size', '{"name":"tiny",      "multiplier":0.4,  "score":5   }', '5')
self.redis.zadd('continent_size', '{"name":"small",     "multiplier":0.7,  "score":10   }', '10')
self.redis.zadd('continent_size', '{"name":"average",   "multiplier":1.0,  "score":65   }', '65')
self.redis.zadd('continent_size', '{"name":"large",     "multiplier":1.5,  "score":85   }', '85')
self.redis.zadd('continent_size', '{"name":"massive",  "multiplier":2.0,  "score":100   }  ', '100')

# East Amoro is a _______ continent with ______ civilization.
self.redis.zadd('continent_civilization', '{"name":"crude"       ,  "score":5   }', '5')
self.redis.zadd('continent_civilization', '{"name":"scattered"   ,  "score":10   }', '10')
self.redis.zadd('continent_civilization', '{"name":"moderate"    ,  "score":90   }', '90')
self.redis.zadd('continent_civilization', '{"name":"prosperous"  ,  "score":95   }', '95')
self.redis.zadd('continent_civilization', '{"name":"thriving"    ,  "score":100   }', '100')

# Most civilized areas in  East Amoro have _________ technology
self.redis.zadd('continent_technology', '{"name":"Stone Age",        "score":5   }', '5')
self.redis.zadd('continent_technology', '{"name":"Bronze Age",       "score":10   }', '10')
self.redis.zadd('continent_technology', '{"name":"Iron Age",         "score":15   }', '15')
self.redis.zadd('continent_technology', '{"name":"Ancient Age",      "score":20   }', '20')
self.redis.zadd('continent_technology', '{"name":"Middle Age",       "score":90   }', '90')
self.redis.zadd('continent_technology', '{"name":"Modern Age",       "score":95   }', '95')
self.redis.zadd('continent_technology', '{"name":"Contemporary Age", "score":100   }', '100')

# The continent has ________ known countries:
self.redis.zadd('continent_countrydetails', '{"name":"a single",     "score":10,  "mincount":1,   "maxcount":1   }', '10')
self.redis.zadd('continent_countrydetails', '{"name":"a couple",     "score":20,  "mincount":2,   "maxcount":2   }', '20')
self.redis.zadd('continent_countrydetails', '{"name":"several",      "score":90,  "mincount":3,   "maxcount":6   }', '90')
self.redis.zadd('continent_countrydetails', '{"name":"many",         "score":95,  "mincount":6,   "maxcount":11  }', '95')
self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  } ', '100')

