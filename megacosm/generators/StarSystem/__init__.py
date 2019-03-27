#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A starsystem contains one or more stars """

import json
import logging
import random
from megacosm.generators.Generator import Generator
from megacosm.generators.Planet import Planet
from megacosm.generators.Star import Star


class StarSystem(Generator):
    """ "Generate some stars and planets."""
    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        self.generate_stars()
        self.generate_planet()

    def generate_stars(self):
        """ generate our stars first."""

        self.stars = []
        positions = self.redis.lrange('starposition', 0, -1)

        for starId in xrange(self.starcount['count']):
            random.shuffle(positions)
            self.stars.append(Star(self.redis, {'pos': json.loads(positions.pop(0))}))

    def generate_planet(self):
        """ Generate a planet"""
        #TODO this should be an array, right?
        self.planet = Planet(self.redis)

    def __str__(self):
        return self.stars[0].name.shortname+" System"
