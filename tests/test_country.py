#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Country, Region
import unittest2 as unittest
import fakeredis
from config import TestConfiguration
import fixtures

class TestCountry(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.country.import_fixtures(self)
        fixtures.continent.import_fixtures(self)
        fixtures.region.import_fixtures(self)

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

