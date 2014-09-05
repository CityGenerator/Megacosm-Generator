#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Legend
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestLegend(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_legend(self):
        """  """
        legend = Legend(self.redis)
        self.assertNotEqual('', legend.text)
