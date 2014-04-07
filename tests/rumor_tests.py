
from generators.Rumor import Rumor
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestRumor(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
#        self.seed=set_seed( "3" )

    def test_random_rumor(self):
        """  """
        rumor = Rumor(self.redis )
        print rumor.text
#        self.assertEqual(rumor.text,'you')

#    def test_rumor_features(self):
#        """  """
#        rumor = Rumor(self.redis, {'you':'Jesse', 'other':'Will', 'either':'Tony', 'partyA':'Shaun', 'partyB':'Rich', 'template':"{{params.you}} {{params.other}} {{params.either}} {{params.partyA}} {{params.partyB}}", 'rumor_when_roll':5, 'when':'Bob' })
#        
#        self.assertEqual(rumor.text,'Bob, Jesse Will Tony Shaun Rich')

