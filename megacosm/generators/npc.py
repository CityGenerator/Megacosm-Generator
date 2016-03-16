#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import motivation
import phobia
from name import Name
import json
import logging
import random


class NPC(Generator):

    def __init__(self, redis, features={}, namekey=None):

        Generator.__init__(self, redis, features, namekey)
        self.logger = logging.getLogger(__name__)

        if self.race not in self.redis.lrange('npc_race', 0, -1):
            raise Exception(' %s is not a valid race and has no associated data' % self.race)
        self.generate_features(self.race)
        self.generate_features(self.covering)
        self.coveringtext = self.render_template(self.covertemplate)

        self.details = json.loads(self.details)

        self.name=Name(self.redis, self.race)

        if hasattr(self, 'subrace'):
            self.race = self.subrace_description['subrace'].lower()

        if not hasattr(self, 'phobia'):
            self.phobia = phobia.Phobia(self.redis )

        if not hasattr(self, 'motivation'):
            self.motivation = motivation.Motivation(self.redis, {'npc': self})

    def __str__(self):
        return self.name.fullname
