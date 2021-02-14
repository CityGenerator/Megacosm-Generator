#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import MundaneItem
import unittest2 as unittest

from pprint import pprint

import redis
from config import IntegrationTestConfiguration


class TestMundaneItemIntegration(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(IntegrationTestConfiguration.REDIS_URL)

    def tearDown(self):
        """Tear stuff Down."""
        #self.redis.flushall()

    def test_kinds(self):
        """  """
        for kind in self.redis.lrange('mundaneitem_kind',0,-1):
            print "kind: "+kind
            for template in self.redis.lrange('mundaneitem_template',0,-1):
                print "template: "+template
                mundaneitem = MundaneItem(self.redis, {'kind':kind, 'template':template} )
                rendered_kind= mundaneitem.render_template(kind)
                self.assertEqual(rendered_kind, str(mundaneitem.kind))

                self.assertNotIn('{', str(mundaneitem))
                self.assertNotIn('}', str(mundaneitem))
                self.assertNotIn('params', str(mundaneitem))

