
from generators.Legend import Legend
from generators.Motivation import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestLegend(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
#        self.seed=set_seed( "3" )

    def test_random_legend(self):
        """  """
        legend = Legend(self.redis )
        print legend.text
        self.assertNotEqual(legend.text,'')


if __name__ == '__main__':
    unittest.main()




