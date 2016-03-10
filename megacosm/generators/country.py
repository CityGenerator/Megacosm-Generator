#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from region import Region
from name import Name
import logging
import random


class Country(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'regioncount'):
            self.regioncount = random.randint(self.regiondetails['mincount'], self.regiondetails['maxcount'])
        if not hasattr(self, 'name'):
            self.name = Name(self.redis, 'country')

    def add_regions(self):
        """ add regions to the country"""

        if not hasattr(self, 'regions'):
            self.regions = []
            for regionid in xrange(self.regioncount):
                self.regions.append(Region(self.redis, {'country': self}))

    def __str__(self):
        return '%s with %s regions' % (self.name.fullname, self.regioncount)

