
from megacosm.generators import Business
from megacosm.generators import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from megacosm.util.Seeds import *

from config import TestConfiguration

class TestBusiness(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(TestConfiguration.REDIS_URL)
       
        self.seed=set_seed( '3' )

    def test_business(self):
        """  """
        business = Business(self.redis )

    def test_senses(self):
        """  """
        business = Business(self.redis, {'smell': 'stank', 'sight':'ugly blinds', 'sound': 'cries for help'} )
        self.assertNotEqual("%s"% (business), "" )


