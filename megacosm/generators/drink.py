#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The Drink is a tasty beverage found at your local tavern."""

import logging
from megacosm.generators.generator import Generator
from megacosm.generators.npc import NPC
from megacosm.generators.region import Region


class Drink(Generator):
    """ Drink has a creator and a region. """
    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'creator'):
            setattr(self, 'creator', NPC(self.redis))
        if not hasattr(self, 'region'):
            setattr(self, 'region', Region(self.redis))

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text
