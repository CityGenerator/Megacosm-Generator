#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('starname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('starname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('starname_formalname_template', '{{params.fullname}}')
    self.redis.lpush('starname_pre', 'Kro')
    self.redis.lpush('starname_root', 'j')
    self.redis.lpush('starname_post', 'el')
    self.redis.zadd('star_size', {'{ "name":"massive",    "multiplier":3.0, "score":100  }': 100})
    self.redis.zadd('star_color', {'{ "name":"red",    "color":"0xff0000", "luminosity":0.2, "score":100  }': 100})


    self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":4  }')
    self.redis.lpush('starposition', '{"name": "companion2",    "x":-150,    "y":-4,  "z":4  }')
