#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.MundaneItem import MundaneItem
import unittest2 as unittest
import fakeredis
from config import TestConfiguration
import fixtures


class TestMundaneItem(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.mundaneitem.import_fixtures(self)

    def test_random_mundaneitem(self):
        """  """
        mundaneitem = MundaneItem(self.redis)
        self.assertEqual('An excellent wool tunic that is in pristine condition', mundaneitem.text)
        self.assertEqual('wool tunic', str(mundaneitem))


    def test_static_mundaneitem_kind(self):
        """  """
        mundaneitem = MundaneItem(self.redis, {'kind':'glass marble'})
        self.assertEqual('An excellent glass marble that is in pristine condition', mundaneitem.text)
        self.assertEqual('glass marble', str(mundaneitem))


    def test_static_mundaneitem_text(self):
        """  """
        mundaneitem = MundaneItem(self.redis, {'text': 'the jaberwokey hides among us'})
        self.assertEqual('The jaberwokey hides among us', mundaneitem.text)
        self.assertEqual('wool tunic', str(mundaneitem))

