#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Name
import unittest2 as unittest

import fakeredis
from pprint import pprint
#from config import TestConfiguration

class TestName(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """
        name = Name(self.redis, 'human')
        self.assertEqual('DeColtin MacAntonard', str(name.fullname))
        self.assertEqual('DeColtin', str(name.shortname))
        self.assertEqual('MacAntonard', str(name.formalname))
        self.assertEqual('DeColtin MacAntonard', str(name))

    def test_missing_fullname_template(self):
        self.redis.delete('humanname_fullname_template')
        with self.assertRaisesRegexp(LookupError, "fullname_template not found for human"):
            name = Name(self.redis, 'human')
    def test_additional_title(self):
        """  """
        self.redis.lpush('humanname_title', 'Lord')
        name = Name(self.redis, 'human')
        self.assertEqual('Lord DeColtin MacAntonard', str(name))

    def test_staticadditional_title(self):
        """  """
        name = Name(self.redis, 'human', {'title': 'Poobah', "first_pre":"Blah"})
        self.assertEqual('Poobah BlahColtin MacAntonard', str(name))

    def test_static_nochancese(self):
        """  """
        self.redis.set('humanname_first_pre_chance', '0')
        self.redis.set('humanname_first_root_chance', '0')
        self.redis.set('humanname_first_post_chance', '0')
        self.redis.set('humanname_last_pre_chance', '0')
        self.redis.set('humanname_last_root_chance', '0')
        self.redis.set('humanname_last_post_chance', '0')
        name = Name(self.redis, 'human', {'title': 'Poobah', "first_pre":"Blah"})
        self.assertEqual('Poobah Blah', str(name))
