#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Star
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser
import os
from config import TestConfiguration


class TestStar(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_creation(self):
        """  """

        star = Star(self.redis)


