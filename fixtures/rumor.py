#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('rumor_belief', '{{params.believer}} wants to believe it.')
    self.redis.lpush('rumor_dangeroushobby', 'drunkenly arguing with people')
    self.redis.lpush('rumor_fearresult', 'fell to the ground, dead')
    self.redis.lpush('rumor_heardit', '{{params.source}} said')
    self.redis.lpush('rumor_location', 'old millhouse')
    self.redis.lpush('rumor_past', ' last year')
    self.redis.lpush('rumor_scarything', 'dragon')
    self.redis.lpush('rumor_stealth', 'quietly')
    self.redis.lpush('rumor_template',
                     '{{params.culprit}} {{params.stealth}} {{params.verbed}} {{params.victim}}{{params.past}}.')
    self.redis.lpush('rumor_truth', '(True.)')
    self.redis.lpush('rumor_verbed', 'maimed')

