#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Deity import Deity
from megacosm.generators.Sect import Sect
import unittest

import fakeredis
from fixtures import npc, motivation, phobia, deity, sect


class TestDeity(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        npc.import_fixtures(self)
        motivation.import_fixtures(self)
        phobia.import_fixtures(self)
        deity.import_fixtures(self)
        sect.import_fixtures(self)
        self.redis.lpush('npc_race', 'gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_deity(self):
        """  """
        deity = Deity(self.redis)
        self.assertNotEqual('', deity.name)

    def test_deity_sects(self):
        """  """
        deity = Deity(self.redis, {'deity_unity_roll': 100, 'deity_importance_roll': 100})
        deity.add_sects()
        self.assertEqual(len(deity.sects), 0)

        deity = Deity(self.redis, {'deity_unity_roll': 0, 'deity_importance_roll': 100})
        deity.add_sects()
        self.assertGreaterEqual(len(deity.sects), 1)

        sect=Sect(self.redis)
        wrongdeity=sect.deity
        deity = Deity(self.redis, {'sects':[sect]})
        self.assertIsNot(deity, wrongdeity)
        deity.add_sects()
        self.assertIs(deity, sect.deity)

        self.assertGreaterEqual(len(deity.sects), 1)

    def test_deity_portfolios(self):
        """  """

        deity = Deity(self.redis, {'portfolios':['tacos','burritos']})
        deity.add_sects()
        self.assertIn( 'tacos', deity.portfolios )
