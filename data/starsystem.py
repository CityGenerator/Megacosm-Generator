#
#TODO add a stat

self.redis.zadd('starsystem_starcount', '{ "name":"single star",  "count":1, "score":70  }', '70')
self.redis.zadd('starsystem_starcount', '{ "name":"binary star",  "count":2, "score":95  }', '95')
self.redis.zadd('starsystem_starcount', '{ "name":"trinary star", "count":3, "score":100  }', '100')

