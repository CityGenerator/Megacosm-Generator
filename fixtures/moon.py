#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.zadd('moon_size', {'{  "name":"massive", "multiplier":0.8 , "score":100  }': 100})
    self.redis.zadd('moon_color', {'{  "name":"dull brown", "color":"0x876e4b" , "score":100  }': 100})
    self.redis.lpush('moonname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('moonname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('moonname_formalname_template', '{{params.fullname}}')
    self.redis.lpush('moonname_pre', 'Hima')
    self.redis.lpush('moonname_root', 'la')
    self.redis.lpush('moonname_post', 'se')
