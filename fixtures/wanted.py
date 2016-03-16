
def import_fixtures(self):
    self.redis.lpush('wanted_by', 'Regional Authorities')
    self.redis.lpush('wanted_condition', 'proof of death')
    self.redis.lpush('wanted_crime', 'Desecration')
    self.redis.lpush('wanted_headline', 'Notice:')
    self.redis.lpush('wanted_lastseen', 'underground')
    self.redis.lpush('wanted_reward', '10 gold')
    self.redis.lpush('wanted_title', '"Loathsome"')
    self.redis.lpush('wanted_warning', 'has killed before')

