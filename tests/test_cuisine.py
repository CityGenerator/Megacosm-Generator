#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Cuisine import Cuisine
from megacosm.generators.Region import Region
from megacosm.generators.NPC import NPC
import unittest

import fakeredis
from config import TestConfiguration
import fixtures

class TestCuisine(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis=fakeredis.FakeRedis(decode_responses=True)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.cuisine.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')


    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_random_cuisine(self):
        """  """
        cuisine = Cuisine(self.redis)
        print(cuisine.text)
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
