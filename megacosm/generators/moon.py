#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from name import Name
import logging


class Moon(Generator):

    def __init__(self, server, features={}):
        Generator.__init__(self, server, features)
        self.logger = logging.getLogger(__name__)
        self.name=Name(self.redis, 'moon')
    def __str__(self):
        return self.name.fullname.title()
