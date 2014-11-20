#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging
import random

import magicitem
import mundaneitem
import gem
import artwork
import currency

class Loot(Generator):
    """ Generate several items for a larger treasure. """

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)


