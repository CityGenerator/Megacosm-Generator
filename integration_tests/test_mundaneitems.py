#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Test the Mundane Items against live data in redis to ensure the MundaneItems data is valid/behaves."""

import unittest
from megacosm.generators.MundaneItem import MundaneItem
from config import IntegrationTestConfiguration


class TestMundaneItemIntegration(unittest.TestCase):

    def setUp(self):
        self.redis = IntegrationTestConfiguration.REDIS

    def tearDown(self):
        """Tear stuff Down."""
        self.redis.flushall()

    def test_kinds(self):
        """  """
        for kind in self.redis.lrange('mundaneitem_kind', 0, -1):
            print("kind: %s" % kind)
            for template in self.redis.lrange('mundaneitem_template', 0, -1):
                print("template: %s" % template)
                mundaneitem = MundaneItem(self.redis, {'kind': kind, 'template': template})
                rendered_kind = mundaneitem.render_template(kind)
                self.assertEqual(rendered_kind, str(mundaneitem.kind))

                self.assertNotIn('{', str(mundaneitem))
                self.assertNotIn('}', str(mundaneitem))
                self.assertNotIn('params', str(mundaneitem))
