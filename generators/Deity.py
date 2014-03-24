
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from generators.Sect import  Sect

class Deity(Generator):
    """ Generate a god for your world"""
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.generate_avatar()
        self.generate_favored_stat()
        self.select_portfolio()


    def generate_favored_stat(self):
        """ Select a single stat and make that favored by the deity. """
        # TODO change removal of sex to favoring men or women
        avatarstats=self.avatar.stats

        # removing sex because "Gobo favors sex" just doesn't sound right
        avatarstats.remove('sex')

        random.shuffle(avatarstats)
        self.favored_stat=avatarstats.pop()

    def generate_avatar(self):
        """ Many features of a god are determined by their avatar."""

        # Theoretically Deity could be a child class of NPC, but I couldn't make it mesh.
        self.avatar=NPC(self.redis)

        # Steal the name for simplicity, leave the rest as avatar traits
        self.name=self.avatar.name


    def add_sects(self): #TODO make this more like countries for continents
        """ each portfolio item except the largest domain can have a sect"""
        if not hasattr(self, 'sect'):
            self.sects=[]

        # ignore the primary domain and shuffle the rest
        sectdomains=self.portfolios[1:]
        random.shuffle(sectdomains)

        # Note that the sectchance is inversely proportional to unity-
        # The more unity, the less chance of fracturing
        sectchance=100-self.deity_unity_roll
        # give each domain a chance to have a sect, but each success lowers the 
        # chance for the next one. A fractured church with many domains could
        # have many different sects.
        for domain in sectdomains:
            sectroll=random.randint(1,100)
            if sectchance >= sectroll: 
                sect= Sect(self.redis, {'deity':self,'domain':domain})
                self.sects.append(sect)
                sectchance=sectchance/2

    
    def select_portfolio(self):
        """  use the deity's importance to determine how many portfolios it has. """

        points=int(self.importance['points'])

        # domains are split up by power level; the more valuable, the higher the power
        # Values currently include: 16, 8, 6, 5, 4, 3, 2, 1
        powerlevels=self.redis.lrange('portfolio_level',0,-1)

        # Only set this if it's empty.
        if not hasattr(self, 'portfolios'):
            self.portfolios=[]

        # Danger, each assigned domain reduces the point count.
        while points>0:
            # Grab the highest power level available
            powerlevel=int(powerlevels.pop())
            # Check to make sure this deity has the points to buy at that power level
            if powerlevel <= points:
                # shuffle the remaining power levels
                # insert that power level at the back of the list; chances are we won't need it again.
                random.shuffle(powerlevels)
                powerlevels.insert(0,powerlevel)
                
                # get all the domains at the current powerlevel
                portfolios=self.redis.zrevrangebyscore('portfolio_domain', powerlevel,powerlevel)
                #shuffle them in python rather than redis to ensure repeatability.
                random.shuffle(portfolios)
                # While we can support this power level, lets use it until we can't.
                while powerlevel <= points :
                    # pop a new portfolio off the list.
                    newdomain=json.loads(portfolios.pop())

                    # make sure our powerlevel is still what we expect
                    powerlevel=int(newdomain['score']) #TODO is this still needed??

                    # append the new domain to our deity's list
                    self.portfolios.append(newdomain)

                    # subtract our new domain's power level from our available points
                    points=points- powerlevel
            #else:
                #print "can't support powerlevel",powerlevel,"with",points,"points"

