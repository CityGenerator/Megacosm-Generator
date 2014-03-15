
from generators.Business import Business
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestBusiness(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
        self.seed=set_seed( '3' )

    def test_races(self):
        """  """
        business = Business(self.redis )


if __name__ == '__main__':
    unittest.main()




