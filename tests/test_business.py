#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Business import Business
from megacosm.generators.NPC import NPC
import unittest
import fakeredis
import fixtures


class TestBusiness(unittest.TestCase):
    """ Test various features of the Business class """
    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.business.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        self.redis.lpush('npc_race', 'gnome')

    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_business(self):
        """ Test a simple random business """
        business = Business(self.redis)
        self.assertEqual('Angry Axe Hall', str(business.name))
        self.assertEqual('Angry Axe Hall', str(business))
        self.assertGreaterEqual(10, business.patroncount)
        self.assertLessEqual(1, business.patroncount)
        self.assertGreaterEqual(2, business.floor)
        self.assertLessEqual(1, business.floor)
        self.assertEqual(2, business.maxfloors)

    def test_senses(self):
        """ Verify that all three senses exist. """
        senses = {'smell': 'stank', 'sight': 'ugly blinds', 'sound': 'cries for help'}
        business = Business(self.redis, senses)
        # pprint(vars(business.name))
        self.assertEqual("Angry Axe Hall", str(business))
        self.assertEqual('you smell stank', business.smell)
        self.assertEqual('you see ugly blinds', business.sight)
        self.assertEqual('you hear cries for help', business.sound)

    def test_no_maxfloors(self):
        """  Ensure the number of floors if there's no max"""
        self.redis.delete('bus_adventurersguild_maxfloors')
        business = Business(self.redis)
        self.assertEqual("Angry Axe Hall", str(business))
        self.assertEqual(1, business.maxfloors)

    def test_business_params(self):
        """ Test various Features and ensure they do good things."""
        owner = NPC(self.redis)
        features = {'owner': owner, 'patroncount': 20, 'trailer': 'a place', 'maxfloors': 100, 'floor': 4}
        business = Business(self.redis, features)
        self.assertEqual(100, business.maxfloors)

        for feature in features.keys():
            self.assertEqual(features[feature], getattr(business, feature))

        self.assertEqual("Angry Axe A Place", str(business))
        self.assertGreaterEqual(100, business.floor)
        self.assertLessEqual(1, business.floor)
