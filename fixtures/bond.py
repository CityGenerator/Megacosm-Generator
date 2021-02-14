#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""

    self.redis.lpush('bond_when', 'Way back when')
    self.redis.lpush('bond_template', '{{params.partyA}} amused {{params.partyB}} in an unusual way.')

