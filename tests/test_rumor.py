#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Rumor, NPC
import unittest2 as unittest

import fakeredis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestRumor(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('rumor_template', '{{params.culprit}} {{params.stealth}} {{params.verbed}} {{params.victim}}{{params.past}}.')
        self.redis.lpush('rumor_truth', '(True.)')
        self.redis.lpush('rumor_heardit', '{{params.source}} said')
        self.redis.lpush('rumor_belief', '{{params.believer}} wants to believe it.')
        self.redis.lpush('rumor_dangeroushobby',  'drunkenly arguing with people')
        self.redis.lpush('rumor_fearresult', 'fell to the ground, dead')
        self.redis.lpush('rumor_scarything', 'dragon')
        self.redis.lpush('rumor_location', 'old millhouse')
        self.redis.lpush('rumor_past',' last year')
        self.redis.lpush('rumor_stealth', 'quietly')
        self.redis.lpush('rumor_verbed', 'maimed')

        self.redis.lpush('npc_race','gnome')
        self.redis.lpush('gnome_covering','skin')
        self.redis.set('gnome_details',  '{"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }')
        self.redis.set('skin_covertemplate', '{{params.skinkind}}, {{params.skincolor}} skin')
        self.redis.lpush('skin_skincolor','alabaster')
        self.redis.lpush('skin_skinkind', 'thick')
        self.redis.lpush('phobia_template', "You are afraid.")
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('motivationacceptance_text', 'to impress someone')
        self.redis.lpush('gnome_name_first_post', 'Tom')
        self.redis.lpush('gnome_name_last_pre', 'Gyro')

        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)


    def test_random_rumor(self):
        """  """
        rumor = Rumor(self.redis)
        self.assertEqual('Tom Gyro quietly maimed Tom Gyro last year.', rumor.text)

    def test_static_person(self):
        """  """
        npc = NPC(self.redis, {'fullname': 'baba'})
        rumor = Rumor(self.redis, {'victim': npc})
        self.assertEqual('Tom Gyro quietly maimed Tom Gyro last year.', rumor.text)

    def test_static_text(self):
        """  """
        rumor = Rumor(self.redis, {'text': 'really, this is static'})
        self.assertEqual('Really, this is static', rumor.text)

    def test_str(self):
        """ """
        rumor = Rumor(self.redis, {'text': 'really, this is static'})
        self.assertEqual('Really, this is static', str(rumor))
        
