#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Artwork, Gem
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestArtwork(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('artwork_metal', 'bronze')
        self.redis.lpush('artwork_weapon', 'dagger')
        self.redis.lpush('artwork_item', 'harp')
        self.redis.lpush('artwork_item_material', 'ivory')
        self.redis.lpush('artwork_item_decoration', 'bear')
        self.redis.lpush('artwork_jewelry', 'ring')
        self.redis.lpush('artwork_cloth_item', 'glove')
        self.redis.lpush('artwork_cloth_material', 'silk')
        self.redis.lpush('artwork_template', "a necklace of {{params.gem.size}} {{params.gem.kind_description['name']|pluralize(2)}}")

        self.redis.zadd('gem_amount',  '{ "name":"a single",  "min":1, "max":100, "score":100  }',100.0)
        self.redis.zadd('gem_value',  '{ "name":"costly", "score":100  }',100.0)
        self.redis.zadd('gem_saturation',  '{ "name":"blanched", "score":100  }',100.0)
        self.redis.zadd('gem_quality',  '{ "name":"chipped", "score":100  }',100.0)
        self.redis.hset('gem_kind_description', 'emerald', '{ "name":"emerald", "color":["green"] }')
        self.redis.lpush('gem_kind', 'emerald')
        self.redis.lpush('gem_template', 'A Gem Template')

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
