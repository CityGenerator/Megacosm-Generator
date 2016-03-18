def import_fixtures(self):

    self.redis.lpush('drink_appearance', 'amber')
    self.redis.lpush('drink_type', 'broth')
    self.redis.lpush('drink_flavor', 'spice')
    self.redis.lpush('drink_flavor_strength', 'overpowering')
    self.redis.zadd('drink_price', '{"name":"lavishly priced",     "score":100  }',100)
    self.redis.zadd('drink_rarity', '{"name":"unique",      "score":100  }',100)
    self.redis.zadd('drink_volume', '{"name":"in excess",     "score":100    }',100)
    self.redis.lpush('drink_feel', 'sticky')
    self.redis.lpush('drink_template', 'You sip {{params.appearance|article}} {{params.type}} that is {{params.rarity["name"]}} to {{params.region.name.fullname}}. It has a {{params.flavor_strength}} flavor of {{params.flavor}}, and feels {{params.feel}} on the tongue.')

    self.redis.lpush('drink_flavor_strength', 'faint')
