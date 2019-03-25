#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.zadd('geomorphdungeon_decorationoffset', {'{"name":"80%",   "offset":0.8,  "score":100 }': 100})
    self.redis.zadd('geomorphdungeon_gridheight', {'{"name":"4",    "tiles":4,    "score": 100  }': 100})
    self.redis.zadd('geomorphdungeon_gridwidth', {'{"name":"6",     "tiles":6,   "score": 100  }': 100})
    self.redis.zadd('geomorphdungeon_segmentation', {'{"name":"all",        "connection_chance":100,    "score": 100  }': 100})
    self.redis.lpush('geomorph_type_0', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }')
    self.redis.lpush('geomorph_type_1', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }')
    self.redis.lpush('geomorph_type_2', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }')
    self.redis.lpush('geomorph_type_3', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }')
    self.redis.lpush('geomorph_type_4', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }')
    self.redis.lpush('geomorph_type_5', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }')

