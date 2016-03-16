#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Flaw
import unittest2 as unittest

import fakeredis
import fixtures
from config import TestConfiguration


class TestFlaw(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.flaw.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_random_flaw(self):
        """  """
        flaw = Flaw(self.redis)
        self.assertNotEquals('', flaw.text)
    def test_static_text(self):
        """  """
        flaw = Flaw(self.redis,{'text':'You are a loser.'})
        self.assertEquals('You are a loser.', str(flaw))
