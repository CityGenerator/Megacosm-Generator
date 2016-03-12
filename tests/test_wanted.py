#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Wanted, NPC
import unittest2 as unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestWanted(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
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
