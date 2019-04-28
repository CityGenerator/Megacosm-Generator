#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Event import Event
import unittest
import fakeredis
from fixtures import event

class TestEvent(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        event.import_fixtures(self)
    def tearDown(self):
        self.redis.flushall()

    def test_random_event(self):
        """  """
        event = Event(self.redis)
        self.assertNotEquals('', event.text)
        self.assertNotEquals('', event.magnitude['name'])
        self.assertNotEquals('', event.kind)
        self.assertNotEquals('', event.variety)
        self.assertIn('to the people in the area', event.template)
        self.assertIn(event.kind, event.text)
        self.assertNotEqual('', str(event) )

    def test_static_event_kind(self):
        """  """
        event = Event(self.redis,{'magnitude':'trivial', 'kind':'festival'})
        self.assertNotEquals('', event.text)
        self.assertIn(event.variety, ['a religious','a trade'])

    def test_static_event_text(self):
        """  """
        event = Event(self.redis,{'text':'Foo Bar'})
        self.assertEqual('Foo Bar', event.text)

