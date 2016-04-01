#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.zadd('starsystem_starcount', '{ "name":"binary star",  "count":2, "score":100  }', 100.0)

