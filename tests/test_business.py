#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Business
import unittest2 as unittest

import redis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestBusiness(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

        self.seed = set_seed('3')

    def test_business(self):
        """  """
        business = Business(self.redis)
        self.assertNotEqual('', business.name)

    def test_senses(self):
        """  """

        business = Business(self.redis, {'smell': 'stank', 'sight': 'ugly blinds', 'sound': 'cries for help'})
        self.assertNotEqual('%s' % business, '')
