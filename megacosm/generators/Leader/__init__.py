#!/usr/bin/env python
# -*- coding: utf-8 -*-
from megacosm.generators.NPC import NPC

from megacosm.generators import Country
from megacosm.generators import City
from megacosm.generators import Organization
import logging
# from pprint import pprint


class Leader(NPC):

    """ Generate a god for your world"""

    def __init__(self, redis, features=None):
        NPC.__init__(self, redis, features, 'npc')
        self.logger = logging.getLogger(__name__)

        self.generate_features('leader')

        self.generate_features('leader' + self.scope)
        # generate self.kind from scope; scope.kind = absolutemonarchy
        self.generate_features('leader' + self.kind)
        # generate self.leader from leaderabsolutemonarchy_leader
        # generate leader.description from leaderabsolutemonarchy_leader_description
        if not hasattr(self,'location'):
            if self.scope == 'country':
                self.location = Country.Country(self.redis, {'leader': self})
            elif self.scope == 'city':
                self.location = City.City(self.redis, {'leader': self})
            elif self.scope == 'organization':
                self.location = Organization.Organization(self.redis, {'leader': self})
            else:
                self.location =Organization.Organization(self.redis, {'leader': self})
                self.scope='organization'

        self.name.title = self.leader_description[self.sex['name']]
        # re-render the name with the title.
        self.name.render()
