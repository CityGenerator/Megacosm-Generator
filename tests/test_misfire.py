#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Misfire
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestMisfire(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_misfire(self):
        """  """
        misfire = Misfire(self.redis)
        print misfire.text
        self.assertNotEqual(misfire.text, '')
        self.assertEqual('%s' % misfire, misfire.text)

    def test_misfire_data(self):
        misfire = Misfire(self.redis)
        total = self.redis.llen('misfire_template')
        for i in range(0, total):
            misfire.template = self.redis.lindex('misfire_template', i)
            print "%s\n" % misfire.template
            results = misfire.render_template(misfire.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)
