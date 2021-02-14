#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('planetname_fullname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.lpush('planetname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('planetname_formalname_template', '{{params.fullname}}')
    self.redis.lpush('planetname_pre', 'Ab')
    self.redis.lpush('planetname_root', 'so')
    self.redis.lpush('planetname_post', 'bah')
    self.redis.zadd('planet_size', '{"name":"massive",  "multiplier":2.0,  "score":100   } ', 100)
    self.redis.zadd('planet_temp', '{"name":"unbearably hot",  "multiplier":1.5,  "score":100   } ', 100)
    self.redis.zadd('planet_atmosphere', '{"name":"dense",    "opacity":0.99,  "score":100   } ', 100)
    self.redis.zadd('planet_wind', '{"name":"overwhelming", "multiplier":1.5,  "score":100   } ', 100)
    self.redis.zadd('planet_day', '{"name":"long",        "minhour":51,     "maxhour":100,  "score":100   } ', 100)
    self.redis.zadd('planet_year', '{"name":"long"     ,  "score":100   } ', 100)
    self.redis.zadd('planet_civilization', '{"name":"thriving"    ,  "score":100   } ', 100)
    self.redis.zadd('planet_precipitation', '{"name":"excessive", "multiplier":1.5 ,  "score":100   } ', 100)
    self.redis.zadd('planet_mooncount', '{"name":"quadruple moon",   "count":4,  "score":100   } ', 100)
    self.redis.zadd('planet_technology',
                    '{"name":"Contemporary Age", "description":"being similar to our own", "score":100 } ', 100)
