def import_fixtures(self):
    self.redis.zadd( 'sect_acceptance','{"name":"saintly",  "score":100   }',100)

