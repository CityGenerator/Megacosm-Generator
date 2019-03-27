#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A region usually contains several cities."""

import logging
from megacosm.generators.Generator import Generator
from megacosm.generators.Name import Name


class Region(Generator):
    """ Create a region to populate. """
    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.name = Name(self.redis, 'region')
    def __str__(self):
        return str(self.name.fullname).title()

# TODO start a separate fork for cities and enable this with the new class
#    def add_cities(self):
#        """ add cities to the region"""
#        if not hasattr(self, 'cities'):
#            self.cities=[]
#        for cityid in xrange(self.citycount):
#            self.city.append( City(self.redis,{'region':self} ) )
