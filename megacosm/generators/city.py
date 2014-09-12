#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from business import Business
from npc import NPC
import region
import random
import logging


class City(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        if not hasattr(self, 'region'):
            self.region = region.Region(self.redis)

        self.gatheringplace=Business(self.redis, {'kind': 'bus_'+self.gatheringplace})

        self.citizen=NPC(self.redis)

        self.calculate_population()

    def calculate_population(self):
        self.population_estimate = random.randint(int(self.size['minpop']), int(self.size['maxpop']))
        self.population_density = random.randint(int(self.size['min_density']), int(self.size['max_density']))

    def __str__(self):
        return '%s' % (self.name['full'])
