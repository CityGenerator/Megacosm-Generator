#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Wanted import Wanted
from megacosm.generators.NPC import NPC
import unittest
import fixtures
import fakeredis


class TestWanted(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.wanted.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)

        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_wanted(self):
        """  """
        wanted = Wanted(self.redis)
        self.assertEquals('underground', wanted.lastseen)

    def test_wanted_static_npc(self):
        """  """
        npc = NPC(self.redis)
        wanted = Wanted(self.redis, {'npc':npc})
        self.assertEquals(npc, wanted.npc)

    def test_wanted_str(self):
        """  """
        wanted = Wanted(self.redis)
        self.assertEquals("Wanted: Tom Gyro", str(wanted))
