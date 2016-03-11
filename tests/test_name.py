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
        self.redis.lpush('humanname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}}{{params.first_post}} {{params.last_pre}}{{params.last_root}}{{params.last_post}} {{params.trailer}}')
        self.redis.lpush('humanname_shortname_template', '{{params.first_pre}}{{params.first_root}}{{params.first_post}}')
        self.redis.lpush('humanname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}{{params.last_post}}')
        self.redis.lpush('humanname_first_pre', 'Dru')
        self.redis.lpush('humanname_first_root', 'cil')
        self.redis.lpush('humanname_first_post', 'la')
        self.redis.lpush('humanname_last_pre', 'La')
        self.redis.lpush('humanname_last_root', 'Sal')
        self.redis.lpush('humanname_last_post', 'vae')

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """
        name = Name(self.redis, 'human')
        self.assertEqual('Drucilla LaSalvae', str(name.fullname))
        self.assertEqual('Drucilla', str(name.shortname))
        self.assertEqual('LaSalvae', str(name.formalname))
        self.assertEqual('Drucilla Lasalvae', str(name))

    def test_missing_fullname_template(self):
        self.redis.delete('humanname_fullname_template')
        with self.assertRaisesRegexp(LookupError, "fullname_template not found for human"):
            name = Name(self.redis, 'human')
    def test_additional_title(self):
        """  """
        self.redis.lpush('humanname_title', 'Lord')
        name = Name(self.redis, 'human')
        self.assertEqual('Lord Drucilla LaSalvae', name.fullname)

    def test_staticadditional_title(self):
        """  """
        name = Name(self.redis, 'human', {'title': 'Poobah', "first_pre":"Blah"})
        self.assertEqual('Poobah Blahcilla LaSalvae', name.fullname)
        self.assertEqual('Poobah Blahcilla Lasalvae', str(name))

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
