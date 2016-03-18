#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Weather
import unittest2 as unittest
import fakeredis
from config import TestConfiguration
import fixtures
from pprint import pprint
class TestWeather(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.weather.import_fixtures(self)

    def test_random_weather(self):
        """  """
        weather = Weather(self.redis)
        self.assertEqual('unbearably hot', str(weather))
        self.assertEqual('Right now it is unbearably hot outside, with hurricane-force winds. It is heavily sleeting at the moment. There are cumulus clouds in the sky above. A downburst is approaching, and will hit in the early evening.', weather.text)

    def test_static_weather_text(self):
        """  """
        weather = Weather(self.redis, {'text': 'It is super hot.'})
        self.assertEqual('unbearably hot', str(weather))
        pprint(weather.text)
        self.assertEqual('It is super hot.', weather.text)
