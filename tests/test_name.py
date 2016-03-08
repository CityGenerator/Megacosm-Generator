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
        self.redis.set("humanname_fullname_template", '["title"," ","first_pre","first_root","first_post", " ", "last_pre", "last_root", "last_post", " ", "trailer"]')
        self.redis.set("humanname_shortname_template", '["first_pre","first_root","first_post"]')
        self.redis.set("humanname_formalname_template", '["title"," ","last_pre","last_root","last_post"]')

        self.redis.set('humanname_first_pre_chance', '100')
        self.redis.set('humanname_first_root_chance', '100')
        self.redis.set('humanname_first_post_chance', '100')
        self.redis.set('humanname_last_pre_chance', '100')
        self.redis.set('humanname_last_root_chance', '100')
        self.redis.set('humanname_last_post_chance', '100')

        self.redis.lpush('humanname_first_pre', 'De')
        self.redis.lpush('humanname_first_root', 'Col')
        self.redis.lpush('humanname_first_post', 'tin')
        self.redis.lpush('humanname_last_pre', 'Mac')
        self.redis.lpush('humanname_last_root', 'Anton')
        self.redis.lpush('humanname_last_post', 'ard')

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
