#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Country, Region
import unittest2 as unittest
import fakeredis
from config import TestConfiguration


class TestCountry(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('country_size', '{"name":"micro",    "mincities":1,   "maxcities":2,       "score":100    }', 100)
        self.redis.zadd('country_regiondetails','{"name":"a single",     "score":100,  "mincount":1,   "maxcount":1   }',100)


        self.redis.lpush('countryname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
        self.redis.lpush('countryname_shortname_template', '{{params.fullname}}')
        self.redis.lpush('countryname_formalname_template', '{{params.fullname}}')


        self.redis.lpush('countryname_title', 'Central')
        self.redis.lpush('countryname_pre','Af')
        self.redis.lpush('countryname_root','kil')

        self.redis.lpush('regionname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
        self.redis.lpush('regionname_shortname_template', '{{params.fullname}}')
        self.redis.lpush('regionname_formalname_template', '{{params.fullname}}')

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

