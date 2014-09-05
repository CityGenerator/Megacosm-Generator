#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from npc import NPC
from jinja2.environment import Environment
from megacosm.util import Filters
import logging


class MagicItem(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.generate_features(self.kind)

        self.npc = NPC(redis)

        self.build_creator()

        text = self.render_template(self.name_template)
        self.name = self.render_template(text)

    def build_creator(self):
        environment = Environment()
        environment.filters['article'] = Filters.select_article
        environment.filters['pluralize'] = Filters.select_pluralize
        template = environment.from_string(self.creator_template)

        self.creator = template.render(npc=self.npc)


# TODO needs real testing!

# TODO move FILTER additions to generator
# TODO same with template rendering
