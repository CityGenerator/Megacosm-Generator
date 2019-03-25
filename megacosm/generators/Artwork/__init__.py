#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Artwork will generate several type of artwork. """
import logging
from megacosm.generators.Gem import Gem
from megacosm.generators.Deity import Deity
from megacosm.generators.Generator import Generator
#from pprint import pprint

class Artwork(Generator):
    """Generate an exquisite piece of artwork."""

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        self.generate_features('artwork'+self.kind)

        if not hasattr(self, 'gem'):
            setattr(self, 'gem', Gem(self.redis))
        if not hasattr(self, 'deity'):
            setattr(self, 'deity', Deity(self.redis))

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text
