def import_fixtures(self):

#FIXME
#TODO throw an error if leader_kind doesn't already exist.

#    self.redis.lpush('leader_kind', 'absolutemonarchy')
    self.redis.lpush('leaderabsolutemonarchy_leader', 'king')
    self.redis.hset('leader_kind_description', 'absolutemonarchy', '{ "scope":"country"   }')
    self.redis.hset('leaderabsolutemonarchy_leader_description', 'king', '{ "male":"King",    "female":"Queen"     }')

    self.redis.hset('leaderabsolutemonarchy_leader_description', 'emperor', '{ "male":"Emperor", "female":"Empress"   }')


#    self.redis.lpush('leader_kind', 'guild')
    self.redis.lpush('leaderguild_leader', 'guildmaster')
    self.redis.hset('leader_kind_description', 'guild', '{ "scope":"organization"   }')
    self.redis.hset('leaderguild_leader_description', 'guildmaster', '{ "male":"Guildmaster",    "female":"Guildmaster"     }')

#    self.redis.lpush('leader_kind', 'magistrate')
    self.redis.lpush('leadermagistrate_leader', 'magistrate')
    self.redis.hset('leader_kind_description', 'magistrate', '{ "scope":"city"   }')
    self.redis.hset('leadermagistrate_leader_description', 'magistrate', '{ "male":"Magistrate",      "female":"Magistrate"      }')

