#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('jobposting_class', 'warrior')
    self.redis.lpush('jobposting_critter', 'carnivorous butterflies')
    self.redis.lpush('jobposting_detail', 'if intrigued')
    self.redis.lpush('jobposting_disclaimer', 'Length of job expected to be short.')
    self.redis.lpush('jobposting_duration', 'few weeks')
    self.redis.lpush('jobposting_favor', 'companion or two')
    self.redis.lpush('jobposting_hazardlocation', 'my business')
    self.redis.lpush('jobposting_hook', 'Looking for something new?')
    self.redis.lpush('jobposting_item', 'keg')
    self.redis.lpush('jobposting_magicuser', 'witch/warlock')
    self.redis.lpush('jobposting_payment', 'Will reward you with valuable information.')
    self.redis.lpush('jobposting_rarelanguage', 'abyssal')
    self.redis.lpush('jobposting_request', 'Wanted:')
    self.redis.lpush('jobposting_requirement', 'Serious inquiries only.')
    self.redis.lpush('jobposting_skill', 'boxing')
    self.redis.lpush('jobposting_subject', 'local lore')
    self.redis.lpush('jobposting_supplies', 'eye of newt')
    self.redis.lpush('jobposting_template',
                     '{{params.npc.name.fullname}} has been kidnapped! Generous payment for safe return.')
    self.redis.lpush('jobposting_testitem', 'cheese')
    self.redis.lpush('jobposting_valuedpossession', 'house')
    self.redis.lpush('jobposting_title', 'Uncle')

