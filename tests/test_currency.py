#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Currency
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestCurrency(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_currency(self):
        """  """

        currency = Currency(self.redis)
        self.assertNotEquals('', currency.name)
