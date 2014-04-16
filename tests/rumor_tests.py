
from generators.Rumor import Rumor
from generators.Motivation import Motivation
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
        self.seed=set_seed( "3" )

    def test_random_rumor(self):
        """  """
        rumor = Rumor(self.redis )

