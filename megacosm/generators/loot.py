#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging
import random

import json
import magicitem
import mundaneitem
import gem
import artwork
import currency
import potion

class Loot(Generator):
    """ Generate several items for a larger treasure. """

    def __init__(self, redis, features={}):
        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)

        self.name['full'] = self.kind_description.pop('name')

        for treasuretype in self.kind_description:

            if getattr(self, 'loot_'+treasuretype+'_roll') <= self.kind_description[treasuretype]:
                self.kind_description[treasuretype]=True
                delattr(self, 'loot_'+treasuretype+'_chance')
                delattr(self, 'loot_'+treasuretype+'_roll')
                delattr(self, treasuretype+'_chance')
                treasuredetails=getattr(self, treasuretype)
                setattr(self, treasuretype+'_count', random.randint(treasuredetails['min'], treasuredetails['max']))
                setattr(self, treasuretype+'_text',getattr(self, treasuretype )['name'] )
                treasurecount=[]
                if treasuretype ==  'gem':
                    for _ in range( getattr(self, treasuretype+'_count')):
                        treasurecount.append( gem.Gem(self.redis, {'seed':random.randint(1,10000000)})  )
                elif treasuretype ==  'mundaneitem':
                    for _ in range( getattr(self, treasuretype+'_count')):
                        treasurecount.append( mundaneitem.MundaneItem(self.redis, {'seed':random.randint(1,10000000)})  )
                elif treasuretype ==  'currency':
                    for _ in range( getattr(self, treasuretype+'_count')):
                        treasurecount.append( currency.Currency(self.redis, {'seed':random.randint(1,10000000)})  )
                elif treasuretype ==  'artwork':
                    for _ in range( getattr(self, treasuretype+'_count')):
                        treasurecount.append( artwork.Artwork(self.redis, {'seed':random.randint(1,10000000)})  )
# Can't add potion until magic item is broken up FIXME
#                elif treasuretype ==  'potion':
#                    for _ in range( getattr(self, treasuretype+'_count')):
#                        treasurecount.append( potion.Potion(self.redis, {'seed':random.randint(1,10000000)})  )
                


                setattr(self, treasuretype, treasurecount )
            else:
                self.kind_description[treasuretype]=False
                delattr(self, 'loot_'+treasuretype+'_chance')
                delattr(self, 'loot_'+treasuretype+'_roll')
                delattr(self, treasuretype+'_chance')
                delattr(self, treasuretype)

# "name":"small chest",         "gem":80,  "currency":80,   "art":40,  "mundane":40,  "potion":50,  "scroll":50,  "armor":50,  "weapon":5



