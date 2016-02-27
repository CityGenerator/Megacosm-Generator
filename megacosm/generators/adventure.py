#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import npc
import logging


class Adventure(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        self.generate_features('adventure' + self.kind)

        if not hasattr(self, 'villain'):
            self.villain = npc.NPC(self.redis)
        if not hasattr(self, 'ally'):
            self.ally = npc.NPC(self.redis)

        self.hook = self.render_template(self.hook)

    def __str__(self):
        return self.hook

