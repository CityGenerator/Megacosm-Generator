#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Motivation
from megacosm.generators import NPC
import unittest2 as unittest

import fakeredis

from config import TestConfiguration


class TestMotivation(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('motivationacceptance_text', "to gain the respect of {{params.npc.sex['possessive']}} peers")
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
        self.redis.zadd('npc_sex', '{"name":"male",       "pronoun":"he", "possessive":"his",  "third-person":"him", "spouse":"wife",    "score":100  }', 100)
        self.redis.lpush('motivationfear_text', 'by {{params.npc.phobia.strength}} {{params.npc.phobia.kind}}.')

    def tearDown(self):
        self.redis.flushall()

    def test_random_motivation(self):
        """  """

        motivation = Motivation(self.redis)
        self.assertNotEqual(motivation.text, '')

    def test_motivation_w_npc(self):
        """  """

        npc = NPC(self.redis)
        motivation = Motivation(self.redis, {'npc': npc})
        self.assertNotEqual(motivation.text, '')
        self.assertEqual(motivation.npc, npc)
        self.assertNotEqual('%s' % motivation, '')

    def test_motivation_w_fear(self):
        """  """

        npc = NPC(self.redis)
        motivation = Motivation(self.redis, {'npc': npc, 'kind': 'fear'})
        self.assertNotEqual(motivation.text, '')
        self.assertEqual(motivation.npc, npc)
        self.assertNotEqual('%s' % motivation, '')
