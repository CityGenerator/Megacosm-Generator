
from megacosm.generators import Misfire
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from megacosm.util.Seeds import *

from config import TestConfiguration

class TestMisfire(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(TestConfiguration.REDIS_URL)
#        self.seed=set_seed( "3" )

    def test_random_misfire(self):
        """  """
        misfire = Misfire(self.redis )
        print misfire.text
        self.assertNotEqual(misfire.text,'')
        self.assertEqual("%s" % (misfire),   misfire.text)


