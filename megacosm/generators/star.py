#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A Star may light up the sky above your world."""

import logging
from megacosm.generators.generator import Generator
from megacosm.generators.name import Name


class Star(Generator):
    """ A simple star, nothing fancy. """
    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.name = Name(self.redis, 'star')

    def __str__(self):
        return self.name.shortname
