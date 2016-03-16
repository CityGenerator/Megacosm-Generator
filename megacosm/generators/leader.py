#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from organization import Organization
#from city import City
#from country import Country
import country, city, organization
from npc import NPC
from name import Name
import logging


class Leader(NPC):

    """ Generate a god for your world"""

    def __init__(self, redis, features={}):
        NPC.__init__(self, redis, features, 'npc')
        self.logger = logging.getLogger(__name__)

        self.generate_features('leader')
        self.generate_features('leader' + self.kind)
        if not hasattr( self, 'location'):
            if self.kind_description['scope'] == 'country':
                self.location = country.Country(self.redis, {'leader': self})
            elif self.kind_description['scope'] == 'city':
                self.location = city.City(self.redis, {'leader': self})
            elif self.kind_description['scope'] == 'organization':
                self.location = organization.Organization(self.redis, {'leader': self})
            else:
                self.location = organization.Organization(self.redis, {'leader': self})
                self.kind_description['scope']='organization'

        self.name.title = self.leader_description[self.sex['name']]
        #re-render the name with the title.
        self.name.render()
