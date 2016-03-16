def import_fixtures(self):

    self.redis.lpush('bond_when', 'Way back when')
    self.redis.lpush('bond_template', '{{params.partyA}} amused {{params.partyB}} in an unusual way.')

