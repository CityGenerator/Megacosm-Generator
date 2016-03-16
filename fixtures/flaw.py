def import_fixtures(self):
    self.redis.zadd('flaw_scope', '{ "name":"major"    , "score":100  }', 100)
    self.redis.zadd('flaw_quality', '{ "name":"poor"    , "score":100  }', 100)
    self.redis.lpush('flaw_allergy', 'horses')
    self.redis.lpush('flaw_enemytrait', 'vicious')
    self.redis.lpush('flaw_template', "You have {{params.scope['name']|article}} an allergy to {{params.allergy}}")

