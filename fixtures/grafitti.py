
def import_fixtures(self):
    self.redis.lpush('grafitti_template', 'The following message is written in {{params.language}} with {{params.material}}: "{{params.message}}"')
    self.redis.lpush('grafitti_language', 'Gnomish')
    self.redis.lpush('grafitti_hero', 'warrior')
    self.redis.lpush('grafitti_monster', 'mimic')
    self.redis.lpush('grafitti_loss', 'a leg')
    self.redis.lpush('grafitti_stare', 'the leader')
    self.redis.lpush('grafitti_threatcount', '1')
    self.redis.lpush('grafitti_message', 'The {{params.hero}} tried to protect us, but was too late...')
    self.redis.lpush('grafitti_signature', 'with a hand print.')
    self.redis.lpush('grafitti_age', 'less than a day old.')
    self.redis.lpush('grafitti_material', 'slime')

