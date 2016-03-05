#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Planet, Continent, Moon
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestPlanet(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('planet_size', '{"name":"massive",  "multiplier":2.0,  "score":100   } ', 100)
        self.redis.zadd('planet_temp', '{"name":"unbearably hot",  "multiplier":1.5,  "score":100   } ', 100)
        self.redis.zadd('planet_atmosphere', '{"name":"dense",    "opacity":0.99,  "score":100   } ', 100)
        self.redis.zadd('planet_wind', '{"name":"overwhelming", "multiplier":1.5,  "score":100   } ', 100)
        self.redis.zadd('planet_day', '{"name":"long",        "minhour":51,     "maxhour":100,  "score":100   } ', 100)
        self.redis.zadd('planet_year', '{"name":"long"     ,  "score":100   } ', 100)
        self.redis.zadd('planet_civilization', '{"name":"thriving"    ,  "score":100   } ', 100)
        self.redis.zadd('planet_precipitation', '{"name":"excessive", "multiplier":1.5 ,  "score":100   } ', 100)
        self.redis.zadd('planet_mooncount', '{"name":"quadruple moon",   "count":4,  "score":100   } ', 100)
        self.redis.zadd('planet_technology', '{"name":"Contemporary Age", "description":"being similar to our own",           "score":100   } ', 100)
        self.redis.zadd('moon_size', '{  "name":"massive", "multiplier":0.8 , "score":100  }', 100)
        self.redis.zadd('moon_color', '{  "name":"dull brown", "color":"0x876e4b" , "score":100  }', 100)
        self.redis.zadd('continent_countrydetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
        self.redis.lpush('name_planetpre', 'Ae')
        self.redis.lpush('name_planetroot', 'boo')
        self.redis.lpush('name_planetpost', 'ris')

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """
        planet=Planet(self.redis)
        planet.add_continents()
        planet.add_moons()
        self.assertEquals('Aebooris', str(planet))
        self.assertNotEquals(None, planet.continents)
        self.assertNotEquals(None, planet.moons)

    def test_static_continents(self):
        """  """
        continenta=Continent(self.redis)
        continentb=Continent(self.redis)
        planet=Planet(self.redis, {'continents':[continenta, continentb] })
        planet.add_continents()
        self.assertNotEquals('Aebooris', planet.name)

    def test_static_continentcount(self):
        """  """
        continenta=Continent(self.redis)
        continentb=Continent(self.redis)
        planet=Planet(self.redis, {'continents':[continenta, continentb], 'continentcount':4 })
        self.assertEqual(len(planet.continents), 2)
        self.assertEqual(planet.continentcount, 2)
        planet.continentcount=4
        planet.add_continents()
        self.assertEqual(len(planet.continents), 4)


    def test_static_moons(self):
        """  """
        moona=Moon(self.redis)
        moonb=Moon(self.redis)
        planet=Planet(self.redis, {'moons':[moona, moonb] })
        planet.add_moons()
        self.assertNotEquals('', planet.name)

