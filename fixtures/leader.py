def import_fixtures(self):
    self.redis.hset('leaderabsolutemonarchy_leader_description', 'king', '{ "male":"King",    "female":"Queen"     }')
    self.redis.hset('leader_kind_description', 'absolutemonarchy', '{ "scope":"country"   }')
    self.redis.lpush('leaderabsolutemonarchy_leader', 'king')
    self.redis.lpush('leader_kind', 'absolutemonarchy')

