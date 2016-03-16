#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Artwork, Gem
import unittest2 as unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestArtwork(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.artwork.import_fixtures(self)
        fixtures.gem.import_fixtures(self)
    def tearDown(self):
        self.redis.flushall()

    def test_random_artwork(self):
        """  """
        artwork = Artwork(self.redis)
        self.assertNotEqual('', artwork.text)

    def test_artwork_features(self):
        """  """
        artwork = Artwork(self.redis, {
            'metal': 'metal',
            'weapon': 'weapon',
            'item': 'item',
            'item_material': 'material',
            'item_decoration': 'decoration',
            'jewelry': 'jewelry',
            'cloth_item': 'clothitem',
            'cloth_material': 'clothmaterial',
            'template': 'template {{params.metal}}',
            })
        self.assertEqual('Template metal', artwork.text)
        self.assertEqual('Template metal', "%s" % artwork)

    def test_artwork_non_features(self):
        """  """
        artwork = Artwork(self.redis, {
            'gem': Gem(self.redis, {'kind_description': {'name': 'ruby', 'color': ['red']}}),
            'template': "{{params.gem.kind_description['name']}}",
            })

        self.assertEqual('Ruby', artwork.text)
        self.assertEqual('Ruby', "%s" % artwork)

    def test_artwork_text(self):
        """  """
        artwork = Artwork(self.redis, {
            'text': 'something'
            })

        self.assertEqual('Something', artwork.text)
        self.assertEqual('Something', "%s" % artwork)

    def test_artwork_data(self):
        artwork = Artwork(self.redis)
        total = self.redis.llen('artwork_template')
        for i in range(0, total):
            artwork.template = self.redis.lindex('artwork_template', i)
            results = artwork.render_template(artwork.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)
