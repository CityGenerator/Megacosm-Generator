#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from leader import Leader
from name import Name
import logging


class Organization(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'leader'):
            self.leader = Leader(self.redis)

        if not hasattr(self, 'text'):
            self.text = self.render_template(self.template)
        self.name=Name(self.redis, 'organization', {'leader':self.leader})

