#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Govt import Govt
from megacosm.generators.Country import Country
from megacosm.generators.City import City
import unittest

import fakeredis
from fixtures import govt, city, region, country, organization, business, leader, npc, motivation, phobia


class TestGovt(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        govt.import_fixtures(self)
        city.import_fixtures(self)
        region.import_fixtures(self)
        country.import_fixtures(self)
        organization.import_fixtures(self)
        business.import_fixtures(self)
        leader.import_fixtures(self)
        npc.import_fixtures(self)
        motivation.import_fixtures(self)
        phobia.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_govt(self):
        """  """
        govt = Govt(self.redis)
        self.assertEqual('far longer than should be allowed', govt.age['name'])
    def test_static_body(self):
        """  """
        country=Country(self.redis)
        govt = Govt(self.redis,{'body':country})
        self.assertIn('Central Afkil', str(govt.body))
        self.assertEqual(type(govt.body), Country)

    def test_static_body_country(self):
        """  """
        govt = Govt(self.redis,{'kind':'country'})
        self.assertIn('Central Afkil', str(govt.body))
        self.assertEqual(type(govt.body), Country)

    def test_str(self):
        """  """
        govt = Govt(self.redis,{'kind':'country'})
        self.assertIn('absolute monarchy', str(govt))


    def test_static_body_tacos(self):
        """  What happens if you pass in an unsupported kind? it defaults to country."""
        govt = Govt(self.redis,{'kind':'tacos'})
        self.assertIn('Central Afkil', str(govt.body))
        self.assertEqual(type(govt.body), Country)


    def test_static_body_city(self):
        """  """
        self.redis.lpush('govt_kind', 'city')
        self.redis.hset('govtcity_govttype_description', 'councilmanager', '{ "name":"council/manager", "description":"things are run by a council, which selects a manager for administrative tasks"}')
        self.redis.lpush('govtcity_govttype', 'councilmanager')

        govt = Govt(self.redis,{'kind':'city'})
        self.assertIn('Alta DeAllentle Gate', str(govt.body))
        self.assertEqual(type(govt.body), City)

