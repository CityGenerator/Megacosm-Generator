#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Country import Country
from megacosm.generators.Region import Region
import unittest
import fakeredis
from fixtures import business, npc, region, motivation, phobia, city, organization, leader, country, continent


class TestCountry(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        country.import_fixtures(self)
        leader.import_fixtures(self)
        continent.import_fixtures(self)
        region.import_fixtures(self)
        npc.import_fixtures(self)
        phobia.import_fixtures(self)
        motivation.import_fixtures(self)
        city.import_fixtures(self)
        business.import_fixtures(self)
        organization.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_random_country(self):
        """  """
        country = Country(self.redis)
        self.assertNotEqual('', country.name)

    def test_country_region_count(self):
        """  """
        country = Country(self.redis, {'regioncount': 25})
        country.add_regions()
        self.assertNotEqual('', country.name)

        self.assertEqual(25, len(country.regions))

    def test_country_region(self):
        """  """
        regiona=Region(self.redis)
        regionb=Region(self.redis)
        country = Country(self.redis, {'regions': [regiona,regionb]})
        self.assertEqual(2, len(country.regions))
        country.add_regions()
        self.assertEqual(2, len(country.regions))


    def test_country_region_str(self):
        """  """
        country = Country(self.redis, {'regioncount': 25})
        country.add_regions()
        self.assertEqual('Central Afkil',str(country))
        self.assertEqual(25,len(country.regions))

