#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Cuisine
from megacosm.generators import Region
from megacosm.generators import NPC
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestCuisine(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=fakeredis.FakeRedis()

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

        self.redis.lpush('cuisine_template', 'words go here.')

    def test_random_cuisine(self):
        """  """
        cuisine = Cuisine(self.redis)
        self.assertEqual('Words go here.', cuisine.text)

    def test_static_cuisine(self):
        """  """
        creator=NPC(self.redis)
        region = Region(self.redis)

        cuisine = Cuisine(self.redis,{ 'creator':creator, 'region':region, 'text': 'Tacos.' } )
        self.assertEqual('Tacos.', cuisine.text)
        self.assertEqual(creator, cuisine.creator)
        self.assertEqual(region, cuisine.region)
        self.assertEqual("Tacos.", str(cuisine))
