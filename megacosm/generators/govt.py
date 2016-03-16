#!/usr/bin/env python
# -*- coding: utf-8 -*-

from country import Country
from city import City
from generator import Generator
import logging

#FIXME: Governments should support various bodies to govern, and it should be based on govt_kind.
#FIXME: This needs be WAAAY more strict on error handling.

class Govt(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        self.generate_features('govt' + self.kind)

        if not hasattr(self, 'body'):
            # TODO this should have an if statement on kind and also do cities
            if self.kind == 'city':
                self.body = City(self.redis)
            elif self.kind == 'country':
                self.body = Country(self.redis)
            else: 
                self.body = Country(self.redis)
