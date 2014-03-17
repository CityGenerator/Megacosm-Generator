
from generators.Moon import Moon
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestMoon(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
#        self.seed=set_seed( "3" )

    def test_random_moon(self):
        """  """
        moon = Moon(self.redis )
        self.assertNotEqual(moon.color,'')
        self.assertNotEqual(moon.size,'')


if __name__ == '__main__':
    unittest.main()




