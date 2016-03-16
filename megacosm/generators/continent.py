#!/usr/bin/env python
# -*- coding: utf-8 -*-

from country import Country
from generator import Generator
from name import Name
import logging
import random


class Continent(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        # If we're passing in a list of countries, we're hard-setting the country count.
        if hasattr(self,'countries'):
            self.countrycount=len(self.countries)

        if not hasattr(self,'name'):
            self.name=Name(self.redis, 'continent')

        # set a random count
        if not hasattr(self, 'countrycount'):
            self.countrycount = random.randint(self.countrydetails['mincount'], self.countrydetails['maxcount'])

    def add_countries(self):
        """ add countries to the continent"""

        if not hasattr(self, 'countries'):
            self.countries = []
        while len(self.countries) < self.countrycount :
            self.countries.append(Country(self.redis, {'continent': self}))

    def __str__(self):
        return self.name.fullname
