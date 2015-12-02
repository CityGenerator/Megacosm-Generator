#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Elixir
import unittest2 as unittest

import redis
from config import TestConfiguration

class TestDrink(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_elixir(self):
        """ """
        elixir = Elixir(self.redis)
        self.assertNotEqual('', elixir.name)

    def test_elixir_template(self):
        """ """
        elixir = Elixir(self.redis, {
            'type' : 'ale',
            'taste' : 'rubbery',
            'container' : 'bowl',
            'template' :  'template {{params.taste}} {{params.container}}'
        })

        self.assertEqual('Template rubbery bowl', elixir.text)
        self.assertEqual('Template rubbery bowl', "%s" % elixir)

    def test_elixir_text(self):
        """  """
        potion = Elixir(self.redis, {
            'text': 'something'
            })

        self.assertEqual('Something', potion.text)
        self.assertEqual('Something', "%s" % potion)

    def test_elixir_data(self):
        elixir = Elixir(self.redis)
        total = self.redis.llen('elixir_template')
        for i in range(0, total):
            elixir.template = self.redis.lindex('elixir_template', i)
            results = elixir.render_template(elixir.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)