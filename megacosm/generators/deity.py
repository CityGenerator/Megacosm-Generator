#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Deities are basically NPCs with portfolios and followers.  """

import json
import logging
import random
from megacosm.generators.npc import NPC
from megacosm.generators.sect import Sect


class Deity(NPC):

    """ Generate a god for your world"""

    def __init__(self, redis, features={}):
        NPC.__init__(self, redis, features, 'npc')
        self.logger = logging.getLogger(__name__)

        self.generate_features('deity')

        self.select_portfolio()

    def add_sects(self):  # TODO make this more like countries for continents
        """ each portfolio item except the largest domain can have a sect"""

        if not hasattr(self, 'sects'):
            self.sects = []

        # ignore the primary domain and shuffle the rest

        sectdomains = self.portfolios[1:]
        random.shuffle(sectdomains)

        # Note that the sectchance is inversely proportional to unity-
        # The more unity, the less chance of fracturing

        sectchance = 100 - self.deity_unity_roll

        # give each domain a chance to have a sect, but each success lowers the
        # chance for the next one. A fractured church with many domains could
        # have many different sects.

        for domain in sectdomains:
            sectroll = random.randint(1, 100)
            if sectchance >= sectroll:
                sect = Sect(self.redis, {'deity': self, 'domain': domain})
                self.sects.append(sect)
                sectchance = sectchance / 2
        #Ensure the deity is set.
        for sect in self.sects:
            sect.deity = self

    def select_portfolio(self):
        #FIXME : Currently points are static values rather than ranges.
        """ Use the deity's importance to determine how many portfolios it rules over.
            First we detmine the Deities importance, which can range from 21 to 1. This
            number determines how many "portfolios" it rules over. Portfolios range
            from 16 points to 1 point; the higher the number, the more generic the portfolio.
            Good and evil are 16 points each, while amphibians are only one point.
            This can lead to the following gods:
                - Chronos, major deity, 21 points: Time(8), Death(8), Obedience(4), Anger(1)
                - Frogos, quazi deity, 1 point: Amphibians(1)
        """

        # Danger, each assigned portfolio reduces this point count.
        points = int(self.importance['points'])

        powerlevels = self.redis.lrange('portfolio_level', 0, -1)

        # Only set portfolio array if it's empty.
        if not hasattr(self, 'portfolios'):
            self.portfolios = []

        #Loop removing points each time.
        while points > 0:

            # Grab the highest power level available the first time, then a random one after that.
            powerlevel = int(powerlevels.pop())

            # Check to make sure this deity has the points to buy at that power level
            if powerlevel <= points:


                # get all the domains at the current powerlevel

                portfolios = self.redis.zrevrangebyscore('portfolio_domain', powerlevel, powerlevel)

                # shuffle them in python rather than redis to ensure repeatability.

                random.shuffle(portfolios)

                # While we can support this power level, lets use it until we can't.

                while powerlevel <= points and len(portfolios) > 0:

                    # pop a new portfolio off the list.
                    newdomain = json.loads(portfolios.pop())

                    # make sure our powerlevel is still what we expect

                    powerlevel = int(newdomain['score'])  # TODO is this still needed??

                    # append the new domain to our deity's list

                    self.portfolios.append(newdomain)

                    # subtract our new domain's power level from our available points

                    points = points - powerlevel

                # shuffle the remaining power levels
                # insert that power level at the back of the list; chances are we won't need it again.
                random.shuffle(powerlevels)
                powerlevels.insert(0, powerlevel)
