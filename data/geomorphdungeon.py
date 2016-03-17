#

self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"1",     "tiles":1,    "score": 25   }', '5')
self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"2",     "tiles":2,    "score": 30   }', '30')
self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"3",     "tiles":3,    "score": 50   }', '50')
self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"4",     "tiles":4,    "score": 70   }', '70')
self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"5",     "tiles":5,    "score": 90   }', '90')
self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"6",     "tiles":6,   "score": 100  }', '100')



self.redis.zadd('geomorphdungeon_gridheight', '{"name":"1",    "tiles":1,    "score": 25   }', '5')
self.redis.zadd('geomorphdungeon_gridheight', '{"name":"2",    "tiles":2,    "score": 35   }', '35')
self.redis.zadd('geomorphdungeon_gridheight', '{"name":"3",    "tiles":3,    "score": 90   }', '90')
self.redis.zadd('geomorphdungeon_gridheight', '{"name":"4",    "tiles":4,    "score": 100  }', '100')

# solid chance means 1 in ____ chance that a side is solid. lower the solid chance number, 
# higher the chance of a solid, the more segmentation
self.redis.zadd('geomorphdungeon_segmentation', '{"name":"none",       "solidchance":1000,     "score": 20   }', '20')
self.redis.zadd('geomorphdungeon_segmentation', '{"name":"a little",   "solidchance":4,        "score": 80   }', '80')
self.redis.zadd('geomorphdungeon_segmentation', '{"name":"a lot",      "solidchance":3,        "score": 90   }', '90')
self.redis.zadd('geomorphdungeon_segmentation', '{"name":"most",       "solidchance":1,        "score": 95   }', '95')
self.redis.zadd('geomorphdungeon_segmentation', '{"name":"all",        "solidchance":0,        "score": 100  }', '100')



self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"0%",    "offset":0.0,  "score":20  }', '20')
self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"20%",   "offset":0.2,  "score":40  }', '40')
self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"40%",   "offset":0.4,  "score":50  }', '50')
self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"50%",   "offset":0.5,  "score":60  }', '60')
self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"60%",   "offset":0.6,  "score":80  }', '80')
self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"80%",   "offset":0.8,  "score":100 }', '100')
