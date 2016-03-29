#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Artwork
import unittest2 as unittest

from pprint import pprint

import redis
from config import IntegrationTestConfiguration


class TestArtworkIntegration(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(IntegrationTestConfiguration.REDIS_URL)

    def tearDown(self):
        """Tear stuff Down."""
        #self.redis.flushall()

    def test_kinds(self):
        """  """
        for kind in self.redis.lrange('artwork_kind',0,-1):
            print "kind: "+kind
            for template in self.redis.lrange('artwork'+kind+'_template',0,-1):
                print "template: "+template
                artwork = Artwork(self.redis, {'kind':kind, 'template':template} )
                self.assertEqual(kind, str(artwork.kind))

                self.assertNotIn('{', str(artwork))
                self.assertNotIn('}', str(artwork))
                self.assertNotIn('params', str(artwork))
            for subkind in self.redis.lrange('artwork'+kind+'_subkind',0,-1):
                print "template: "+template
                artwork = Artwork(self.redis, {'kind':kind, 'subkind':subkind} )
                self.assertEqual(kind, str(artwork.kind))
                self.assertNotIn(kind, str(artwork))
                self.assertIn(subkind, str(artwork))

                self.assertNotIn('{', str(artwork))
                self.assertNotIn('}', str(artwork))
                self.assertNotIn('params', str(artwork))
