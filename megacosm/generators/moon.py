#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging


class Moon(Generator):

    def __init__(self, server, features={}):
        Generator.__init__(self, server, features)
        self.logger = logging.getLogger(__name__)


