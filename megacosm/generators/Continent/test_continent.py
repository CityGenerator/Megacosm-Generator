#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Continent import Continent
from megacosm.generators.Country import Country
import unittest
import fakeredis

from fixtures import business, npc, region, motivation, phobia, city, organization, leader, country, continent


class TestContinent(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)

        continent.import_fixtures(self)
        country.import_fixtures(self)
        leader.import_fixtures(self)
        npc.import_fixtures(self)
        motivation.import_fixtures(self)
        phobia.import_fixtures(self)
        organization.import_fixtures(self)
        region.import_fixtures(self)
        city.import_fixtures(self)
        business.import_fixtures(self)
        self.redis.lpush('npc_race', 'gnome')

    def tearDown(self):
        """ Clean up any changes from the last run. """
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
