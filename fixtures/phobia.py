#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('phobia_template',
                     'You have {{params.strength["name"]}} {{params.kind_description["name"]}}, '+
                     'which is a fear of {{params.kind_description["description"]}}.')
    self.redis.zadd('phobia_strength', {'{"name":"moderate",  "score":100    }': 100})
    self.redis.lpush('phobia_kind', 'ablutophobia')
    self.redis.hset('phobia_kind_description', 'ablutophobia',
                    '{"name":"Ablutophobia",       "description":"washing or bathing" }')
