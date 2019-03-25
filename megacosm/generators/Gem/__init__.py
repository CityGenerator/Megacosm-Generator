#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Generator import Generator
import logging
import random


class Gem(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'count'):
            self.count = random.randint(self.amount['min'], self.amount['max'])

        if not hasattr(self, 'color'):
            self.color = random.choice(self.kind_description['color'])

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return '%s %s %s, %s' % (self.quality['name'], self.color, self.kind_description['name'], self.value['name'])
