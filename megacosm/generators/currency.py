#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Gold, Silver and Copper are boring currencies; this spices them up a bit. """

import logging
import random
from megacosm.generators.generator import Generator
from megacosm.generators.npc import NPC
from megacosm.generators.name import Name


class Currency(Generator):

    """ Define a currency to be used in your game """

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'count'):
            self.count = random.randint(self.amount['min'], self.amount['max'])
        if not hasattr(self, 'name'):
            self.name = Name(self.redis, 'currency')

        # Double parse the template to fill in templated template values.

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text
