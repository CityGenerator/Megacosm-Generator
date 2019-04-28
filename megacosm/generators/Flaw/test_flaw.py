#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Flaw import Flaw
import unittest

import fakeredis
from fixtures import flaw


class TestFlaw(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
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
