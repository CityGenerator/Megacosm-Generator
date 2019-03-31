#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Artwork import Artwork
from megacosm.generators.Gem import Gem
from megacosm.generators.Deity import Deity
import unittest
import fixtures
import fakeredis


class TestArtwork(unittest.TestCase):
    """ Test the Artwork Class"""
    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.artwork.import_fixtures(self)
        fixtures.gem.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.deity.import_fixtures(self)
        self.redis.lpush('npc_race', 'gnome')
    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_random_artwork(self):
        """ Create a random piece of artwork and ensure it has everything it needs. """
        artwork = Artwork(self.redis)
        self.assertEqual("A ceremonial bronze spear with a emerald in the pommel", artwork.text)
        self.assertEqual("A ceremonial bronze spear with a emerald in the pommel", str(artwork))

    def test_artwork_static_features(self):
        """ Test overriding many of the features """
        artwork = Artwork(self.redis, {
            'metal': 'gold',
            'kind': 'weapon',
            'subkind': 'blowdart',
            'template': 'template {{params.metal}} {{params.deity.name.shortname}}',
            })
        self.assertEqual('weapon', artwork.kind)
        self.assertEqual('blowdart', artwork.subkind)
        self.assertEqual('Template gold Tom', artwork.text)
        self.assertEqual('Template gold Tom', str(artwork))

    def test_artwork_non_features(self):
        """ Test the deity and gem to ensure they work as expected. """
        gem = Gem(self.redis)
        deity = Deity(self.redis)
        artwork = Artwork(self.redis, {
            'gem':gem,
            'deity':deity,
            'template': "{{params.gem}} {{params.deity}}",
            })

        self.assertEqual('Chipped green emerald, costly Tom Gyro', artwork.text)
        self.assertEqual('Chipped green emerald, costly Tom Gyro', str(artwork))

    def test_artwork_text(self):
        """  Ensure that the text is capitalized like a sentence."""
        artwork = Artwork(self.redis, {
            'text': 'something'
            })

        self.assertEqual('Something', artwork.text)
        self.assertEqual('Something', str(artwork))

