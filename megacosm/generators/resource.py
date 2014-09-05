#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from region import Region
import logging


class Resource(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        del self.name

        if not hasattr(self, 'place'):
            self.place = Region(self.redis)

        self.subkind = self.kind + '_' + self.rand_value(self.kind + '_kind')

        self.generate_features(self.subkind)

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text


