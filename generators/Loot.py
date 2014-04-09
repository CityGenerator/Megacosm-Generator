
import random
import json
from generators.Generator import Generator
from generators.MagicItem import MagicItem
from generators.MundaneItem import MundaneItem
from generators.Gem import Gem
from generators.Artwork import Artwork
from generators.Currency import Currency
from util import Filters, Seeds


class Loot(Generator):
    def __init__(self, redis, features={}):

        # Redis is the source of all data.
        self.redis=redis

        # We use our class name as a key for redis
        namekey= self.__class__.__name__.lower()

        if 'seed' in features:
            self.seed=Seeds.set_seed(features['seed'])
        else:
            self.seed=Seeds.set_seed()

        # For naming conventions, we use "name"+classname+"stuff"
        self.name=self.generate_name('name'+namekey)

        # For each feature, set it as an attribute for this generator
        for feature, value in features.iteritems():
            # This bit of meta code saves soooo much hassle and getters/setters.
            # especially with testing.
            setattr( self, feature, value)

        self.generate_feature('loot','loot_kind')
        print self.__dict__
        for chance in [ "gem", "currency", "mundane", "potion", "scroll", "armor", "weapon", 'art']:
            if not hasattr(self, 'loot_'+chance+'_chance'):
                setattr(self,'loot_'+chance+'_chance', self.kind_description[chance])
        # This is the guts of the Generator...
        self.generate_features(namekey)

        if hasattr(self,'gem'):
            self.generate_gems()
        if hasattr(self,'currency'):
            self.generate_currencies()
        if hasattr(self,'mundane'):
            self.generate_mundaneitems()
        if hasattr(self,'art'):
            self.generate_art()

    def generate_mundaneitems(self):
            if not hasattr(self, 'mundane_count'):
                self.mundane_count=random.randint(self.mundane['min'], self.mundane['max'])
                self.mundaneitems=[]
                for i in range(self.mundane_count):
                    self.mundaneitems.append(MundaneItem(self.redis))

    def generate_art(self):
            if not hasattr(self, 'art_count'):
                self.art_count=random.randint(self.art['min'], self.art['max'])
                self.art=[]
                for i in range(self.art_count):
                    self.art.append(Artwork(self.redis))

    def generate_gems(self):
            if not hasattr(self, 'gem_count'):
                self.gem_count=random.randint(self.gem['min'], self.gem['max'])
                self.gems=[]
                for i in range(self.gem_count):
                    self.gems.append(Gem(self.redis))

    def generate_currencies(self):
            if not hasattr(self, 'currency_count'):
                self.currency_count=random.randint(self.currency['min'], self.currency['max'])
                self.currencies=[]
                for i in range(self.currency_count):
                    self.currencies.append(Currency(self.redis))

