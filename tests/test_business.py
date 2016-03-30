#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import Business, NPC
import unittest2 as unittest
import fakeredis
from mock import Mock
from config import TestConfiguration
from pprint import pprint
import json
import fixtures

class TestBusiness(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.business.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')




    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_business(self):
        """  """
        business = Business(self.redis)
        self.assertNotEqual('', business.name)
        self.assertNotEqual('', str(business))

    def test_senses(self):
        """  """
        business = Business(self.redis, {'smell': 'stank', 'sight': 'ugly blinds', 'sound': 'cries for help'})
        pprint(vars(business.name))
        self.assertEqual("Angry Axe Hall", str(business))

    def test_maxfloors(self):
        """  """
        self.redis.set('bus_adventurersguild_maxfloors', None)
        business = Business(self.redis)
        self.assertEqual("Angry Axe Hall", str(business))
        self.assertEqual(1, business.maxfloors)

    def test_business_params(self):
        """  """
        dummyuser = Mock(NPC)
        business = Business(self.redis,
                            {'owner': dummyuser, 'patroncount': 3, 'trailer': 'a place', 'maxfloors': 2, 'floor': 1})
        self.assertEqual("Angry Axe A Place", str(business))

    def test_business_data(self):

        stats = ['status', 'size', 'popularity', 'reputation', 'price', 'age', 'neighborhood']
        for stat in stats:
            results = self.redis.zrangebyscore('business_'+stat, 0, 100, withscores=True)
            for (result, score) in results:
                resultobj = json.loads(result)
                self.assertEquals(score, resultobj['score'])
