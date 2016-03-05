#!/usr/bin/env python
# -*- coding: utf-8 -*-

from continent import Continent
from generator import Generator
from moon import Moon
import logging
import random


class Planet(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        if hasattr(self,'continents'):
            self.continentcount=len(self.continents)

    def add_continents(self):
        """ Generate the continents for this planet"""

        # Ensure that we have a continents array

        if not hasattr(self, 'continents'):
            self.continents = []

        # Ensure that we have a target number of continents

        if not hasattr(self, 'continentcount'):
            self.continentcount = random.randint(1, 5)


        while len(self.continents) < self.continentcount:
            self.continents.append(Continent(self.redis, {'planet': self}))

    def add_moons(self):
        """ Generate a list of moons """

        if not hasattr(self, 'moons'):
            self.moons = []
        

        # Note that mooncount is a planet stat
        while len(self.moons) < self.mooncount['count']:
            self.moons.append(Continent(self.redis, {'planet': self}))

    def __str__(self):
        return self.name['full']
