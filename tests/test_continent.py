#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Continent,Country
import unittest2 as unittest
from pprint import pprint
import fakeredis
from config import TestConfiguration
import fixtures

class TestContinent(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()

        fixtures.continent.import_fixtures(self)
        fixtures.country.import_fixtures(self)
        fixtures.leader.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.organization.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.city.import_fixtures(self)
        fixtures.business.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')
    def tearDown(self):
        self.redis.flushall()

    def test_random_continent(self):
        """  """
        continent = Continent(self.redis)
        continent.add_countries()
        self.assertGreaterEqual(len(continent.countries), 0)

    def test_continent_countryCount(self):
        """  """
        continent = Continent(self.redis, {'countrycount': 25})
        continent.add_countries()
        self.assertEqual(len(continent.countries), 25)
    def test_continent_pass_countries(self):
        """  """
        countrya=Country(self.redis)
        countryb=Country(self.redis)
        countryc=Country(self.redis)
        continent = Continent(self.redis, {'countries':[countrya,countryb,countryc] })
        continent.add_countries()
        self.assertEqual(len(continent.countries), 3)
        self.assertIn(countrya,continent.countries)
        self.assertIn(countryb,continent.countries)
        self.assertIn(countryc,continent.countries)
        continent.countrycount=5
        continent.add_countries()
        self.assertEqual(len(continent.countries), 5)
        self.assertIn(countrya,continent.countries)
        self.assertIn(countryb,continent.countries)
        self.assertIn(countryc,continent.countries)



    def test_continent_str(self):
        continent = Continent(self.redis)
        self.assertEqual('West Asbarca', str(continent)) 
