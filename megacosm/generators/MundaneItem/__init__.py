#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators.Generator import Generator
import logging


class MundaneItem(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        if not hasattr(self, 'text'):

            # TODO move this to the data file
            # self.text=self.render_template("{{params.quality['name']|article}}
            #               {{params.kind}}, {{params.repair['name']}}")

            self.kind = self.render_template(self.kind)
            self.text = self.render_template(self.template)
        self.text = self.text[0].capitalize() + self.text[1:]

    def __str__(self):
        return self.kind
