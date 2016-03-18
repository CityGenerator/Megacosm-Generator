#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Cuisine
from megacosm.generators import Region
from megacosm.generators import NPC
import unittest2 as unittest

import fakeredis
from config import TestConfiguration
import fixtures

class TestCuisine(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=fakeredis.FakeRedis()
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.cuisine.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')


    def tearDown(self):
        self.redis.flushall()

    def test_random_cuisine(self):
        """  """
        cuisine = Cuisine(self.redis)
        print cuisine.text
        self.assertEqual('Scalded orange dog salad in chile gravy, served luke warm This dish is unique to the . Travelers consider the dish spicy and beautiful to the eye. Portions are usually large.', cuisine.text)

    def test_static_cuisine(self):
        """  """
        creator=NPC(self.redis)
        region = Region(self.redis)

        cuisine = Cuisine(self.redis,{ 'creator':creator, 'region':region, 'text': 'Tacos.' } )
        self.assertEqual('Tacos.', cuisine.text)
        self.assertEqual(creator, cuisine.creator)
        self.assertEqual(region, cuisine.region)
        self.assertEqual("Tacos.", str(cuisine))
