def import_fixtures(self):
    self.redis.lpush('dungeonname_fullname_template', '{{params.descriptor}} {{params.place}} of the {{params.thingtype}} of {{params.thing}}')
    self.redis.lpush('dungeonname_shortname_template', 'The {{params.place}}')
    self.redis.lpush('dungeonname_formalname_template', '{{params.fullname}}')

    self.redis.lpush('dungeonname_place', 'panopticon')
    self.redis.lpush('dungeonname_descriptor', 'lost')
    self.redis.lpush('dungeonname_thingtype', 'king')
    self.redis.lpush('dungeonname_thing', 'chaos')
