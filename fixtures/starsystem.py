def import_fixtures(self):
    self.redis.zadd('starsystem_starcount',  '{ "name":"binary star",  "count":2, "score":100  }',100.0)

