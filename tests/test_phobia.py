#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Phobia
import unittest2 as unittest
import fakeredis
import fixtures
from config import TestConfiguration


class TestPhobia(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.phobia.import_fixtures(self)


    def tearDown(self):
        self.redis.flushall()
        
    def test_random_phobia(self):
        """  """
        phobia = Phobia(self.redis)
        self.assertEquals('You have moderate Ablutophobia, which is a fear of washing or bathing.', str(phobia))

    def test_static_text(self):
        """  """
        phobia = Phobia(self.redis, {'text': 'You have Tacophobia, which is a fear of tacos.'})
        self.assertEquals('You have Tacophobia, which is a fear of tacos.', str(phobia))

