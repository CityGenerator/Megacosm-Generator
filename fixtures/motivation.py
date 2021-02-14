#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('motivationacceptance_text', "to gain the respect of {{params.npc.sex['possessive']}} peers")
    self.redis.lpush('motivationfear_text', 'by {{params.npc.phobia.strength}} {{params.npc.phobia.kind}}.')
    self.redis.lpush('motivation_kind', 'acceptance')
    self.redis.lpush('motivation_kind', 'acceptance')

