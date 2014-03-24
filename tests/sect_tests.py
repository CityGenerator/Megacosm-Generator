
from generators.Sect import Sect
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestSect(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
#        self.seed=set_seed( "3" )

    def test_random_sect(self):
        """  """
        sect = Sect(self.redis )
        self.assertNotEqual(sect.domain,'')


if __name__ == '__main__':
    unittest.main()




