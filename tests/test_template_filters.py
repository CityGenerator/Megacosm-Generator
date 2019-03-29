#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."
#

import megacosm
from flask_testing import TestCase
import fakeredis
import fixtures
from megacosm import template_filters

class MegacosmFlaskTestCast(TestCase):

    def create_app(self):
        """ """
        app = megacosm.create_app('config.TestConfiguration')
        app.debug = True
        return app

    def setUp(self):
        megacosm.app.config['REDIS'] = fakeredis.FakeRedis(decode_responses=True)
        self.app = megacosm.app.test_client()
        self.redis = megacosm.app.config['REDIS']

    ################################################################

    def test_select_uppercase(self):
        self.assertEquals('DOG', template_filters.select_uppercase('dog'))
        self.assertEquals('APPLE?', template_filters.select_uppercase('Apple?'))
        self.assertEquals('HOUR.!', template_filters.select_uppercase('HOUR.!'))

    ################################################################

    def test_select_article(self):
        self.assertEquals('a dog', template_filters.select_article('dog'))
        self.assertEquals('an apple', template_filters.select_article('apple'))
        self.assertEquals('an hour', template_filters.select_article('hour'))

    ################################################################

    def test_select_pluralize(self):
        self.assertEquals('dogs', template_filters.select_pluralize('dog', 0))
        self.assertEquals('dog', template_filters.select_pluralize('dog', 1))
        self.assertEquals('dogs', template_filters.select_pluralize('dog', 2))
        self.assertEquals('classes', template_filters.select_pluralize('class', 0))
        self.assertEquals('class', template_filters.select_pluralize('class', 1))
        self.assertEquals('classes', template_filters.select_pluralize('class', 2))

    ################################################################

    def test_select_conjunction(self):
        self.assertEquals('a', template_filters.select_conjunction(['a']))
        self.assertEquals('a and b', template_filters.select_conjunction(['a', 'b']))
        self.assertEquals('a, b, and c', template_filters.select_conjunction(['a', 'b', 'c']))
        self.assertEquals('a, b, c, and d', template_filters.select_conjunction(['a', 'b', 'c', 'd']))

    ################################################################

    def test_select_plural_verb(self):
        self.assertEquals('were', template_filters.select_plural_verb('was', 0))
        self.assertEquals('was', template_filters.select_plural_verb('was', 1))
        self.assertEquals('were', template_filters.select_plural_verb('was', 2))

    ################################################################

    def test_select_plural_adj(self):
        self.assertEquals('some', template_filters.select_plural_adj('a', 0))
        self.assertEquals('a', template_filters.select_plural_adj('a', 1))
        self.assertEquals('some', template_filters.select_plural_adj('a', 2))

        self.assertEquals('these', template_filters.select_plural_adj('this', 0))
        self.assertEquals('this', template_filters.select_plural_adj('this', 1))
        self.assertEquals('these', template_filters.select_plural_adj('this', 2))

        self.assertEquals('those', template_filters.select_plural_adj('that', 0))
        self.assertEquals('that', template_filters.select_plural_adj('that', 1))
        self.assertEquals('those', template_filters.select_plural_adj('that', 2))

        self.assertEquals('our', template_filters.select_plural_adj('my', 0))
        self.assertEquals('my', template_filters.select_plural_adj('my', 1))
        self.assertEquals('our', template_filters.select_plural_adj('my', 2))

