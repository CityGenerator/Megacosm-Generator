def import_fixtures(self):
    self.redis.lpush('continentname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('continentname_shortname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('continentname_formalname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
    self.redis.zadd('continent_civilization', '{"name":"thriving"    ,  "score":100   }',100)
    self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
    self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }',100)
    self.redis.zadd('continent_size', '{"name":"massive",  "multiplier":2.0,  "score":100   }',100)
    self.redis.zadd('continent_technology', ' {"name":"Contemporary Age", "score":100   }',100)

    self.redis.lpush('continentname_title', 'West')
    self.redis.lpush('continentname_pre', 'As')
    self.redis.lpush('continentname_root', 'bar')
    self.redis.lpush('continentname_post', 'ca')


