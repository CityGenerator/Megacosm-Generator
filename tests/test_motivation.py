#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Motivation
from megacosm.generators import NPC
import unittest2 as unittest
import fixtures
import fakeredis

from config import TestConfiguration


class TestMotivation(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_motivation(self):
        """  """

        motivation = Motivation(self.redis)
        self.assertNotEqual(motivation.text, '')

    def test_motivation_w_npc(self):
        """  """

        npc = NPC(self.redis)
        motivation = Motivation(self.redis, {'npc': npc})
        self.assertNotEqual(motivation.text, '')
        self.assertEqual(motivation.npc, npc)
        self.assertNotEqual('%s' % motivation, '')

    def test_motivation_w_fear(self):
        """  """

        npc = NPC(self.redis)
        motivation = Motivation(self.redis, {'npc': npc, 'kind': 'fear'})
        self.assertNotEqual(motivation.text, '')
        self.assertEqual(motivation.npc, npc)
        self.assertNotEqual('%s' % motivation, '')
