#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Continent,Country
import unittest2 as unittest
from pprint import pprint
import fakeredis
from config import TestConfiguration


class TestContinent(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('continent_size', '{"name":"massive",  "multiplier":2.0,  "score":100   }',100)
        self.redis.zadd('continent_civilization', '{"name":"thriving"    ,  "score":100   }',100)
        self.redis.zadd('continent_technology', ' {"name":"Contemporary Age", "score":100   }',100)
        self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }',100)

        self.redis.zadd('country_size', '{"name":"micro",    "mincities":1,   "maxcities":2,       "score":100    }', 100)
        self.redis.zadd('country_regiondetails','{"name":"a single",     "score":100,  "mincount":1,   "maxcount":1   }',100)

        self.redis.lpush('continentname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
        self.redis.lpush('continentname_shortname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
        self.redis.lpush('continentname_formalname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
        self.redis.lpush('countryname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
        self.redis.lpush('countryname_shortname_template', '{{params.fullname}}')
        self.redis.lpush('countryname_formalname_template', '{{params.fullname}}')


        self.redis.lpush('countryname_title', 'Central')
        self.redis.lpush('countryname_pre','Af')
        self.redis.lpush('countryname_root','kil')

        self.redis.lpush('continentname_title', 'West')
        self.redis.lpush('continentname_pre', 'As')
        self.redis.lpush('continentname_root', 'bar')
        self.redis.lpush('continentname_post', 'ca')

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
