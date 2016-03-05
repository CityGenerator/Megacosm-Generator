#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging


class Region(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

    def __str__(self):
        return '%s' % (self.name['full'])

# TODO start a separate fork for cities and enable this with the new class
#    def add_cities(self):
#        """ add cities to the region"""
#        if not hasattr(self, 'cities'):
#            self.cities=[]
#        for cityid in xrange(self.citycount):
#            self.city.append( City(self.redis,{'region':self} ) )
