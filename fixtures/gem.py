
def import_fixtures(self):
    self.redis.zadd('gem_amount',  '{ "name":"a single",  "min":1, "max":100, "score":100  }',100.0)
    self.redis.zadd('gem_value',  '{ "name":"costly", "score":100  }',100.0)
    self.redis.zadd('gem_saturation',  '{ "name":"blanched", "score":100  }',100.0)
    self.redis.zadd('gem_quality',  '{ "name":"chipped", "score":100  }',100.0)
    self.redis.hset('gem_kind_description', 'emerald', '{ "name":"emerald", "color":["green"] }')
    self.redis.lpush('gem_kind', 'emerald')
    self.redis.lpush('gem_template', 'A Gem Template')

