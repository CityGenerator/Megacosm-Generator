#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('cityname_fullname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.lpush('cityname_shortname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('cityname_formalname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')

    self.redis.lpush('cityname_fullname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.lpush('cityname_shortname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('cityname_formalname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.zadd('city_size',
                    {'{ "name":"capitol", "minpop":"30001", "maxpop":"80000", "min_density":"240",'+
                    ' "max_density":"40000", "min_dist":3,  "max_dist":14 }': 100})
    self.redis.zadd('city_happiness', {' { "name":"estatic",     "score":100   }': 100})
    self.redis.zadd('city_health', {' { "name":"vigorous",       "score":100   }': 100})
    self.redis.zadd('city_age', {' { "name":"ancient",           "score":100    }': 100})
    self.redis.zadd('city_terrain', {'{ "name": "jagged",         "score":100   }': 100})
    self.redis.zadd('city_pollution', {'{ "name": "squalid",      "score":100  }': 100})
    self.redis.zadd('city_moral', {'{ "name": "virtuous",         "score":100   }': 100})
    self.redis.zadd('city_order', {'{ "name": "honorable",         "score":100   }': 100})
    self.redis.zadd('city_tolerance', {'{ "name": "love",                        "score":100   }': 100})
    self.redis.zadd('city_economy', {'{ "name": "lively",                        "score":100   }': 100})
    self.redis.zadd('city_military', {'{ "name": "reverent",                     "score":100   }': 100})
    self.redis.zadd('city_magic', {'{ "name": "growing",                         "score":100   }': 100})
    self.redis.zadd('city_education', {'{ "name": "wonderful",                   "score":100   }': 100})
    self.redis.zadd('city_authority', {'{ "name": "is very authoritarian",       "score":100   }': 100})
    self.redis.zadd('city_crime', {'{ "name": "unheard of",                      "score":100   }': 100})

    self.redis.lpush('city_shape', 'octagonal')
    self.redis.lpush('city_gatheringplace', 'adventurersguild')

    self.redis.lpush('cityname_title', 'Alta')
    self.redis.lpush('cityname_pre', 'De')
    self.redis.lpush('cityname_root', 'Allen')
    self.redis.lpush('cityname_post', 'tle')
    self.redis.lpush('cityname_trailer', 'Gate')

