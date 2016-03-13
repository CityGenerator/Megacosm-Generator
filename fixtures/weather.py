def import_fixtures(self):

    self.redis.lpush('weather_cloud', 'cumulus')
    self.redis.lpush('weather_storm', 'downburst')
    self.redis.lpush('weather_time', 'in the early evening')
    self.redis.zadd('weather_precipitation', '{ "name":"heavily",    "score":100     }', 100)
    self.redis.zadd('weather_temp', '{ "name":"unbearably hot",   "score":100     }', 100)
    self.redis.zadd('weather_wind', '{ "name":"hurricane-force",  "score":100     }', 100)

