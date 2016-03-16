#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import deity
import logging
import random


class Sect(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'deity'):
            self.deity = deity.Deity(redis)

        if not hasattr(self, 'domain'):
            portfolio = self.deity.portfolios
            random.shuffle(portfolio)
            self.domain = portfolio[0]
        self.name="sect name placeholder"

# TODO this should have an __str__; is it using the text->template pattern?
