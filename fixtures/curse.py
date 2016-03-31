#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.hset('curse_kind_description', 'bezerker',
                    '{"name":"bezerker", "description":"causes intermittent, uncontrollable rage in the victim"  }')
    self.redis.zadd('curse_duration', '{"name":"last a lifetime",       "score":100 }', 100)
    self.redis.lpush('curse_kind', 'bezerker')
    self.redis.lpush('curse_removal', 'performing an epic task')
    self.redis.lpush('curse_template',
                     'The {{params.kind_description["name"]|title}} Curse {{params.kind_description["description"]}},'+
                     ' and can only be undone by {{params.removal}}. Untreated, the effects of the curse '+
                     '{{params.duration["name"]}}.')
