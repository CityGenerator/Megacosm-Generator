#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Legend, NPC
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestLegend(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis()
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
        self.redis.lpush('legend_template','Once upon a time, the end.')

    def tearDown(self):
        self.redis.flushall()

    def test_random_legend(self):
        """  """
        legend = Legend(self.redis)
        self.assertEqual('Once upon a time, the end.', str(legend))

    def test_legend_static_npc(self):
        """  """
        npc=NPC(self.redis)
        legend = Legend(self.redis, {'npc':npc, 'villain':npc})
        self.assertNotEqual('', legend.text)

    def test_legend_static_text(self):
        """  """
        legend = Legend(self.redis, {'text':'something spooky'})
        self.assertNotEqual('something spooky', str(legend))
