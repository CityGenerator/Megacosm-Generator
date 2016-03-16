#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Planet, Continent, Moon
import unittest2 as unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestPlanet(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        fixtures.planet.import_fixtures(self)
        fixtures.moon.import_fixtures(self)
        fixtures.continent.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """
        planet=Planet(self.redis)
        planet.add_continents()
        planet.add_moons()
        self.assertEquals('Absobah', str(planet))
        self.assertNotEquals(None, planet.continents)
        self.assertNotEquals(None, planet.moons)

    def test_static_continents(self):
        """  """
        continenta=Continent(self.redis)
        continentb=Continent(self.redis)
        planet=Planet(self.redis, {'continents':[continenta, continentb] })
        planet.add_continents()
        self.assertNotEquals('Absobah', planet.name)

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

