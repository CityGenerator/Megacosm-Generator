#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Generators package
"""

from jinja2.environment import Environment
from megacosm.util import Filters
from megacosm.util import Seeds
import json
import logging
import random
from pprint import pprint

# TODO:
# Description - The long version of text.  Should be a full sentence or two describing the object.
# Abbr - The short version. It should answer "You see ___."
#    e.g. "A ring", "Drebak", "Marthok, Goddess of Light", "Lichenstien", "the Mongo brewhouse", a" red moon",
#         "the Ibiwan Curse", "King Leopold", "a clear day"


class Generator(object):

    """ An abstracted Generator that all generators are based from """

    def __init__(self, redis, features=None, namekey=None):
        self.logger = logging.getLogger(__name__)

        if features is None:
            features = {}
        # Redis is the source of all data.

        self.redis = redis
        self.pipeline = self.redis.pipeline

        # We use our class name as a key for redis

        if namekey is None:
            namekey = self.__class__.__name__.lower()
        # see if we have a seed to use, otherwise generate a new one.

        if 'seed' in features:
            self.seed = Seeds.set_seed(features['seed'])
        else:
            self.seed = Seeds.set_seed()
        self.logger.debug('new generator %s with seed %i', namekey, self.seed)

        # For naming conventions, we use "name"+classname+"stuff"

#        self.name = Name(self.redis, namekey)

        # For each feature, set it as an attribute for this generator

        for (feature, value) in features.items():

            # This bit of meta code saves soooo much hassle and getters/setters.
            # especially with testing.

            setattr(self, feature, value)

        # This is the guts of the Generator...

        self.generate_features(namekey)

    def generate_features(self, namekey):
        """ Given a namekey, add those features to this object."""

        # find all keys matching our namekey

        self.logger.debug('Generating features for %s with seed %i', namekey, self.seed)
        for key in self.redis.keys("%s_*" % namekey):
            if key.endswith("_description"):
                continue
            self.generate_feature(namekey, key)

    def generate_feature(self, namekey, key):
        if self.redis.exists("%s_chance" % key):
            # make sure the value is not already set, then grab it.

            if not hasattr(self, "%s_chance" % key):
                setattr(self, "%s_chance" % key, int(self.redis.get("%s_chance" % key)))

            # check to see if you have a preset roll; if not, roll 1-100

            if not hasattr(self, "%s_roll" % key):
                setattr(self, "%s_roll" % key, random.randint(1, 100))

            # if the roll is greater than the chance, you have failed, and don't get to use this stat.
            # Go to the next entry in the for loop.

            if int(getattr(self, "%s_roll" % key)) > getattr(self, "%s_chance" % key):
                return
            # FIXME Note that there is no condition for a seperate chance and roll;
            # i.e. a 1% chance of something happening, then a separate d100 roll to determine effect.

        # #########################################################################################
        # Provided you had no associated _chance or that you succeeded on the chance roll, you can
        # Move on to actually setting the value.

        # Most features don't need the namekey on the front since it's redundant
        # so we shorten the name for brevity.
        featurename = str(key).replace("%s_" % namekey, '')

        keytype = self.redis.type(key)
        if keytype == 'zset':
            # Zset means it's a 1-100 stat;
            if not hasattr(self, featurename):
                setattr(self, featurename, Generator.select_by_roll(self, key))
        elif keytype == 'string':
            # string means it's a simple value that plugs right in
            if not hasattr(self, featurename):
                setattr(self, featurename, self.redis.get(key))
        elif keytype == 'list':
            # List gets a bit tricky; select a value, then see if it has an associated description
            # If feature isn't set, grab a rand value from the list.

            if not hasattr(self, featurename):
                featurevalue = Generator.rand_value(self, key)
                setattr(self, featurename, featurevalue)

            # if the description hasn't been set and exists in redis.
            if not hasattr(self, featurename + '_description'):
                desc_text = ""
                try:
                    desc_text = self.redis.hmget("%s_description" % key, getattr(self, featurename))[0]
                    if desc_text is not None:
                        featurevalue = json.loads(desc_text)
                        setattr(self, featurename + '_description', featurevalue)
                except ValueError:
                    self.logger.critical("JSON parsing error: Couldn't read json %s", desc_text)
                    raise ValueError("JSON parsing error: Couldn't read json", desc_text)
        else:
            raise RuntimeError("%s(%s) is an unsupported keytype" % (key,keytype))


    def rand_value(self, key):
        """ Select a Random Value from the list matching the key in redis. """

        try:
            total = self.redis.llen(key)
            value = self.redis.lindex(key, random.randint(0, total - 1))
            return value
        except Exception:
            raise Exception("the key (%s) doesn't appear to exist or isn't a list (%s)." % (key, self.redis.type(key)))

    def select_by_roll(self, key):
        """ Using roll, select the closest matching score from key in Redis. """

        if "%s_roll" % key not in self.__dict__:
            setattr(self, "%s_roll" % key, random.randint(1, 100))

        roll = max(1, min(getattr(self, "%s_roll" % key), 100))
        if self.redis.type(key) == 'none':
            raise ValueError('The key %s does not exist.' % key)
        elif self.redis.type(key) != 'zset':
            raise TypeError('The key %s is not a zset; the type is %s.' % (key, self.redis.type(key)))
        rollvalue = None
        try:
            rollvalue = self.redis.zrangebyscore(key, roll, 100, 0, 1)
            if not rollvalue:
                raise LookupError('The key (%s) appears to be empty for a roll of %s- This should never happen.' %
                                  (key, roll))
            return json.loads(rollvalue[0])
        except ValueError:
            raise ValueError("JSON parsing error: Couldn't read json", rollvalue[0])

    def render_template(self, template):
        """ Renders a given template using itself."""

        environment = Environment()
        environment.filters['article'] = Filters.select_article
        environment.filters['pluralize'] = Filters.select_pluralize
        environment.filters['conjunction'] = Filters.select_conjunction
        environment.filters['plural_verb'] = Filters.select_plural_verb
        environment.filters['plural_adj'] = Filters.select_plural_adj

        template = environment.from_string(template)

        return template.render(params=self)

    def dump_vars(self):
        pprint(vars(self))
        return vars(self)
