#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import StarSystem,Planet, Star
import unittest2 as unittest
import fixtures
import fakeredis
from mock import Mock, patch, MagicMock

from config import TestConfiguration


class TestStarSystem(unittest.TestCase):

    def setUp(self):
    	self.redis = fakeredis.FakeRedis()
        fixtures.starsystem.import_fixtures(self)
        fixtures.star.import_fixtures(self)
        fixtures.planet.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """
        starsystem = StarSystem(self.redis)
        self.assertTrue(starsystem.planet)
        self.assertEqual(2, len(starsystem.stars))
        self.assertEqual('Krojel System', str(starsystem))

