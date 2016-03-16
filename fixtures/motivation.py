def import_fixtures(self):
    self.redis.lpush('motivationacceptance_text', "to gain the respect of {{params.npc.sex['possessive']}} peers")
    self.redis.lpush('motivationfear_text', 'by {{params.npc.phobia.strength}} {{params.npc.phobia.kind}}.')
    self.redis.lpush('motivation_kind', 'acceptance')
    self.redis.lpush('motivation_kind', 'acceptance')

