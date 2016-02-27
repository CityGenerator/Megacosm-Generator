#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Event
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestEvent(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

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

