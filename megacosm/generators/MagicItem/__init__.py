#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Generator import Generator
from megacosm.generators.NPC import NPC
from megacosm.generators.Curse import Curse
from jinja2.environment import Environment
from megacosm.util import Filters
import logging
import random


class MagicItem(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.generate_features(self.kind)

        if not hasattr(self, 'npc'):
            self.npc = NPC(redis)

        self.curse_chance_roll = random.randint(1, 100);
        if not hasattr(self, 'curse') and self.curse_chance_roll < self.curse_chance :
            self.curse = Curse(redis)

        self.creator = self.render_template(self.creator_template)

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template).title()

    def __str__(self):
        return self.text
# TODO needs real testing!

