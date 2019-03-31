#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Misfire import Misfire
import unittest

import fixtures
import fakeredis


class TestMisfire(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.misfire.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        self.redis.lpush('npc_race', 'gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_misfire(self):
        """  """
        misfire = Misfire(self.redis)
        print(misfire.text)
        self.assertNotEqual(misfire.text, '')
        self.assertEqual('%s' % misfire, misfire.text)

    def test_static_misfire_text(self):
        """  """
        misfire = Misfire(self.redis, {'text': 'you fail at life'})
        # Remember it capitalizes
        self.assertEqual('You fail at life', str(misfire))

    def test_misfire_data(self):
        misfire = Misfire(self.redis)
        total = self.redis.llen('misfire_template')
        for i in range(0, total):
            misfire.template = self.redis.lindex('misfire_template', i)
            print("%s\n" % misfire.template)
            results = misfire.render_template(misfire.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)
