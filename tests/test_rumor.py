#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Rumor import Rumor
from megacosm.generators.NPC import NPC
import unittest

import fakeredis
from megacosm.util.Seeds import set_seed
import fixtures
from config import TestConfiguration


class TestRumor(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.npc.import_fixtures(self)
        fixtures.rumor.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_rumor(self):
        """  """
        rumor = Rumor(self.redis)
        self.assertEqual('Tom Gyro quietly maimed Tom Gyro last year.', rumor.text)

    def test_static_person(self):
        """  """
        npc = NPC(self.redis, {'fullname': 'baba'})
        rumor = Rumor(self.redis, {'victim': npc})
        self.assertEqual('Tom Gyro quietly maimed Tom Gyro last year.', rumor.text)

    def test_static_text(self):
        """  """
        rumor = Rumor(self.redis, {'text': 'really, this is static'})
        self.assertEqual('Really, this is static', rumor.text)

    def test_str(self):
        """ """
        rumor = Rumor(self.redis, {'text': 'really, this is static'})
        self.assertEqual('Really, this is static', str(rumor))
        
