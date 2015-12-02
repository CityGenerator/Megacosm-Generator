#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Potion
import unittest2 as unittest

import redis
from config import TestConfiguration

class TestDrink(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_potion(self):
        """ """
        potion = Potion(self.redis)
        self.assertNotEqual('', potion.name)

    def test_potion_template(self):
        """ """
        potion = Potion(self.redis, {
            'type' : 'ale',
            'taste' : 'rubbery',
            'container' : 'bowl',
            'template' :  'template {{params.taste}} {{params.container}}'
        })

        self.assertEqual('Template rubbery bowl', potion.text)
        self.assertEqual('Template rubbery bowl', "%s" % potion)

    def test_potion_text(self):
        """  """
        potion = Potion(self.redis, {
            'text': 'something'
            })

        self.assertEqual('Something', potion.text)
        self.assertEqual('Something', "%s" % potion)

    def test_potion_data(self):
        potion = Potion(self.redis)
        total = self.redis.llen('potion_template')
        for i in range(0, total):
            potion.template = self.redis.lindex('potion_template', i)
            results = potion.render_template(potion.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)