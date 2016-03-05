#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Event
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestEvent(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('event_magnitude', '{  "name":"of dire importance",            "score":100      }', 100)

        self.redis.lpush('eventfestival_variety', 'a trade')
        self.redis.lpush('eventdisaster_variety', 'animal infestation')
        self.redis.lpush('event_kind', 'disaster')
        self.redis.lpush('event_template', "{{params.variety }} {{params.kind}}, which is {{params.magnitude['name']}} to the people in the area.")

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

