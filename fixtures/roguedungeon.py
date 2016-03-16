def import_fixtures(self):
    self.redis.hset('roguedungeonroom_kind_description', 'audiencechamber', '{ "name":"audience chamber",   "description":""   }')
    self.redis.lpush('roguedungeonroom_kind', 'audiencechamber')
    self.redis.lpush('roguedungeon_theme', 'fortress')
    self.redis.zadd('roguedungeon_build', '{"name":"dungeon and caves",    "score": 100  }', 100)
    self.redis.zadd('roguedungeon_refinement', '{"name":"dungeon",                             "score": 100  }', 100)
    self.redis.zadd('roguedungeon_room_count', '{"name":"lots",       "minsize":25, "maxsize":50,  "score": 100  }', 100)
    self.redis.zadd('roguedungeon_room_size', '{"name":"gigantic", "minsize":3,  "maxsize":20,   "score": 100  }', 100)
    self.redis.zadd('roguedungeon_size', '{"name":"gigantic", "minsize":60, "maxsize":60,   "score": 100  }', 100)

