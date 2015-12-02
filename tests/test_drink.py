#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Drink
import unittest2 as unittest

import redis
from config import TestConfiguration

class TestDrink(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_drink(self):
        """ """
        drink = Drink(self.redis)
        self.assertNotEqual('', drink.name)

    def test_drink_template(self):
        """ """
        drink = Drink(self.redis, {
            'color' : 'ale',
            'flavor' : 'sour',
            'appearance' : 'ruby',
            'strength' : 'aggressive',
            'template' :  'template {{params.flavor}} {{params.type}}'
        })

        self.assertEqual('Template sour ale', drink.text)
        self.assertEqual('Template sour ale', "%s" % drink)


    def test_drink_text(self):
        """  """
        drink = Drink(self.redis, {
            'text': 'something'
            })

        self.assertEqual('Something', drink.text)
        self.assertEqual('Something', "%s" % drink)

    def test_artwork_data(self):
        drink = Drink(self.redis)
        total = self.redis.llen('drink_template')
        for i in range(0, total):
            drink.template = self.redis.lindex('drink_template', i)
            results = drink.render_template(drink.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)