#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('dungeonname_fullname_template',
                     '{{params.descriptor}} {{params.place}} of the {{params.thingtype}} of {{params.thing}}')
    self.redis.lpush('dungeonname_shortname_template', 'The {{params.place}}')
    self.redis.lpush('dungeonname_formalname_template', '{{params.fullname}}')

    self.redis.lpush('dungeonname_place', 'panopticon')
    self.redis.lpush('dungeonname_descriptor', 'lost')
    self.redis.lpush('dungeonname_thingtype', 'king')
    self.redis.lpush('dungeonname_thing', 'chaos')
