#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging


class Weather(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
