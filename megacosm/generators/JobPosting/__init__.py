#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Business import Business
from megacosm.generators.Generator import Generator
from megacosm.generators.NPC import NPC
import logging


class JobPosting(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        for field in ['contact', 'npc']:
            if not hasattr(self, field):
                setattr(self, field, NPC(self.redis))
        if not hasattr(self, 'business'):
            setattr(self, 'business', Business(self.redis))

        if not hasattr(self, 'text'):

            for field in ['hook', 'request']:
                if hasattr(self, field):
                    self.template = getattr(self, field) + ' ' + self.template

            for field in ['requirement', 'disclaimer', 'payment']:
                if hasattr(self, field):
                    self.template = self.template + ' ' + getattr(self, field)

            self.template = self.template + ' Contact ' + self.contact.name.fullname
            self.template = self.template + ' at the ' + self.business.name.fullname
            if hasattr(self, 'detail'):
                self.template = self.template + ' ' + self.detail

            self.template += '.'

            self.text = self.render_template(self.template)
            self.text = self.render_template(self.text)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.text
