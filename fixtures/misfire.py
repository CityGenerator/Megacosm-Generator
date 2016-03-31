#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('misfire_template', '{{params.target}} grow a pair of small horns (2 in each) on the forehead, which contrasts with skin color.  A remove curse may remove them.')

