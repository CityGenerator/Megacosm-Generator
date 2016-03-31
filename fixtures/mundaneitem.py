#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.zadd('mundaneitem_quality', '{"name":"excellent", "score":100 }', 100)
    self.redis.zadd('mundaneitem_repair', '{"name":"in pristine condition",     "score":100 }', 100)
    self.redis.lpush('mundaneitem_kind', 'wool tunic')
    self.redis.lpush( 'mundaneitem_metal', 'copper')

    self.redis.lpush( 'mundaneitem_template', '{{params.quality["name"]|article}} {{params.kind}} that is {{params.repair["name"]}}')
