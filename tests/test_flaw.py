#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Flaw
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestFlaw(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_flaw(self):
        """  """
        flaw = Flaw(self.redis)
        self.assertNotEquals('', flaw.text)
