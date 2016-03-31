#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('country_right', 'appointment')
    self.redis.zadd('country_age', '{ "name":"ancient",        "score":100    }', 100)
    self.redis.zadd('country_aggression', '{"name":"timid",        "score":100    }', 100)
    self.redis.zadd('country_approval', '{ "name":"revere",         "score":100    }', 100)
    self.redis.zadd('country_corruption', '{ "name":"incorruptible",   "score":100    }', 100)
    self.redis.zadd('country_economic', '{"name":"conservative",     "score":100   }', 100)
    self.redis.zadd('country_efficiency', '{ "name":"ruthlessly effective",               "score":100    }', 100)
    self.redis.zadd('country_influence', '{ "name":"thriving",              "score":100    }', 100)
    self.redis.zadd('country_military', '{"name":"bloodthirsty",         "score":100    }', 100)
    self.redis.zadd('country_regiondetails',
                    '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
    self.redis.zadd('country_reputation', '{"name":"revered",     "score":100    }', 100)
    self.redis.zadd('country_size', '{"name":"micro",    "mincities":1,   "maxcities":2,    "score":100    }', 100)
    self.redis.zadd('country_social', '{"name":"authoritarian",       "score":100   }', 100)
    self.redis.zadd('country_theology', '{ "name":"is used to control the populace",   "score":100    }', 100)
    self.redis.zadd('country_unity', '{ "name":"rallies behind its leaders",        "score":100    }', 100)

    self.redis.lpush('countryname_fullname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.lpush('countryname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('countryname_formalname_template', '{{params.fullname}}')


    self.redis.lpush('countryname_title', 'Central')
    self.redis.lpush('countryname_pre', 'Af')
    self.redis.lpush('countryname_root', 'kil')

