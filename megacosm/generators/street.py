#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Generate a street"""
import logging
from megacosm.generators.generator import Generator
from megacosm.generators.name import Name

class Street(Generator):
    """ Generate a street."""
    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        self.name = Name(self.redis, 'street')

    def __str__(self):
        return self.name.fullname.title()
