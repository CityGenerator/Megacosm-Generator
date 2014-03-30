
from generators.Deity import Deity
from generators.Motivation import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestDeity(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
        self.seed=set_seed( '3' )

    def test_deity(self):
        """  """
        deity = Deity(self.redis )

    def test_deity_sects(self):
        """  """
        deity = Deity(self.redis, {'deity_unity_roll': 100, 'deity_importance_roll':100} )
        deity.add_sects()
        self.assertEqual(len(deity.sects),0)

        deity = Deity(self.redis, {'deity_unity_roll': 0, 'deity_importance_roll':100} )
        deity.add_sects()
        self.assertGreaterEqual(len(deity.sects),1)


if __name__ == '__main__':
    unittest.main()




