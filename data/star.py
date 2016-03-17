# TODO we need to create a stat list


self.redis.zadd('star_size', '{ "name":"tiny",       "multiplier":0.5, "score":5  }', '5')
self.redis.zadd('star_size', '{ "name":"small",      "multiplier":0.8, "score":10  }', '10')
self.redis.zadd('star_size', '{ "name":"average",    "multiplier":1.0, "score":65  }', '65')
self.redis.zadd('star_size', '{ "name":"large",      "multiplier":1.5, "score":85  }', '85')
self.redis.zadd('star_size', '{ "name":"massive",    "multiplier":3.0, "score":100  }', '100')


self.redis.zadd('star_color', '{ "name":"blue",   "color":"0x4699ca", "luminosity":0.6, "score":10  }', '10')
self.redis.zadd('star_color', '{ "name":"white",  "color":"0xffffff", "luminosity":0.5, "score":30  }', '30')
self.redis.zadd('star_color', '{ "name":"yellow", "color":"0xffff79", "luminosity":0.4, "score":70  }', '70')
self.redis.zadd('star_color', '{ "name":"orange", "color":"0xff8f37", "luminosity":0.3, "score":85  }', '85')
self.redis.zadd('star_color', '{ "name":"red",    "color":"0xff0000", "luminosity":0.2, "score":100  }', '100')



# The lack of underscore prevents it from getting sucked in as a feature
self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":4  }')
self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":-4 }')
self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":-4, "z":4  }')
self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":-4, "z":-4 }')


