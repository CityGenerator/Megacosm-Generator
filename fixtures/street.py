#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('streetname_title', 'new')
    self.redis.lpush('streetname_root', 'alba')
    self.redis.lpush('streetname_trailer', 'byway')
    self.redis.lpush('streetname_fullname_template', '{{params.title}} {{params.root}} {{params.trailer}}')
    self.redis.lpush('streetname_shortname_template', '{{params.root}} {{params.trailer}}')
    self.redis.lpush('streetname_formalname_template', '{{params.fullname}}')
    self.redis.lpush('street_kind', 'road')
    self.redis.lpush('street_material', 'pavingstone')
    self.redis.zadd('street_age', '{ "name":"ancient",         "score":100   }', 100)
    self.redis.zadd('street_crime', '{"name":"unheard of",                                     "score":100  }', 100)
    self.redis.zadd('street_economy', '{"name":"lively",                                         "score":100  }', 100)
    self.redis.zadd('street_important', '{ "name":"primary",    "score":100   }', 100)
    self.redis.zadd('street_moral', '{"name":"virtuous",                                    "score":100  }', 100)
    self.redis.zadd('street_order', '{"name":"honorable",                                         "score":100  }', 100)
    self.redis.zadd('street_pollution', '{"name":"squalid",        "score":100 }', 100)
    self.redis.zadd('street_popularity', '{ "name":"popular",    "score":100   }', 100)
    self.redis.zadd('street_repair', '{ "name":"pristine",            "score":100   }', 100)
    self.redis.zadd('street_scope', '{ "name":"country",     "score":100   }', 100)
    self.redis.zadd('street_size', '{ "name":"wide",             "score":100   }', 100)
    self.redis.zadd('street_terrain', '{"name":"jagged",      "score":100 }', 100)
    self.redis.zadd('street_tolerance', '{"name":"love",                                         "score":100  }', 100)

