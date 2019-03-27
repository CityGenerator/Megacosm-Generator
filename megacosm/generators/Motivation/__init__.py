#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Generator import Generator
from megacosm.generators import NPC
import logging


class Motivation(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        self.generate_features('motivation' + self.kind)

        if not hasattr(self, 'npc'):
            self.npc = NPC.NPC(self.redis, {'motivation': self})

        self.text = self.render_template(self.text)

    def __str__(self):
        return self.text
