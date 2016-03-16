#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from organization import Organization
#from city import City
#from country import Country
import country, city, organization
from npc import NPC
from name import Name
import logging
from pprint import pprint

class Leader(NPC):

    """ Generate a god for your world"""

    def __init__(self, redis, features={}):
        NPC.__init__(self, redis, features, 'npc')
        self.logger = logging.getLogger(__name__)

        self.generate_features('leader')
        #generates self.scope = "country"

        self.generate_features('leader' + self.scope)
        # generate self.kind from scope; scope.kind = absolutemonarchy
        self.generate_features('leader' + self.kind)
        # generate self.leader from leaderabsolutemonarchy_leader
        # generate leader.description from leaderabsolutemonarchy_leader_description

        if self.scope == 'country':
            self.location = country.Country(self.redis, {'leader': self})
        elif self.scope == 'city':
            self.location = city.City(self.redis, {'leader': self})
        elif self.scope == 'organization':
            self.location = organization.Organization(self.redis, {'leader': self})
        else:
            self.location = organization.Organization(self.redis, {'leader': self})
            self.scope='organization'

        self.name.title = self.leader_description[self.sex['name']]
        #re-render the name with the title.
        self.name.render()
