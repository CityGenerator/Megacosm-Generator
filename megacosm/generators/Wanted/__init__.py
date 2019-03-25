#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Generator import Generator
from megacosm.generators.NPC import NPC
import logging


class Wanted(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        for person in ['npc', 'victim']:
            if not hasattr(self, person):
                setattr(self, person, NPC(self.redis))

        self.headline = self.render_template(self.headline)
        self.lastseen = self.render_template(self.lastseen)
    def __str__(self):
        return "Wanted: %s" %  self.npc.name.fullname
