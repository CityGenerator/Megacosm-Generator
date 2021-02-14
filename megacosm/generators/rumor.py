#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Rumors are a good way to start a new quest or add drama."""

import logging
from megacosm.generators.generator import Generator
from megacosm.generators.npc import NPC


class Rumor(Generator):
    """ While some rumors are based in fact, most aren't. """
    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        for person in ['victim', 'culprit', 'source', 'believer']:
            if not hasattr(self, person):
                setattr(self, person, NPC(self.redis).name.fullname)

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text
