#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Flaw
from megacosm.generators import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser
import os
from megacosm.util.Seeds import *

from config import TestConfiguration


class TestFlaw(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

#        self.seed=set_seed( "3" )

    def test_random_flaw(self):
        """  """

        flaw = Flaw(self.redis)
        print flaw.text


