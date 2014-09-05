#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from planet import Planet
from star import Star
import json
import logging
import random


class StarSystem(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.generate_stars()
        self.generate_planet()

    def generate_stars(self):
        """ Do stuff"""

        self.stars = []

        positions = self.redis.lrange('starposition', 0, -1)

        for starId in xrange(self.starcount['count']):
            random.shuffle(positions)
            self.stars.append(Star(self.redis, {'pos': json.loads(positions.pop(0))}))

    def generate_planet(self):
        """ Do stuff"""
        self.planet = Planet(self.redis)
