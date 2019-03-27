#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Generator import Generator
from megacosm.generators.NPC import NPC
import logging


class Grafitti(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'npc'):
            setattr(self, 'npc', NPC(self.redis))

        if not hasattr(self, 'npcname'):
            setattr(self, 'npcname', self.npc.name.shortname)
        if not hasattr(self, 'npcprofession'):
            setattr(self, 'npcprofession', self.npc.profession)

        if not hasattr(self, 'text'):
            if hasattr(self, 'signature'):
                self.template = self.template + ' The message is signed ' + getattr(self, 'signature')
            if hasattr(self, 'age'):
                self.template = self.template + " You'd guess the message is " + getattr(self, 'age')

            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text

