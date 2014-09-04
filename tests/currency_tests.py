
from megacosm.generators.Currency import Currency
from megacosm.generators.Motivation import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from megacosm.util.Seeds import *


from config import TestConfiguration

class TestCurrency(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(TestConfiguration.REDIS_URL)        
#        self.seed=set_seed( "3" )

    def test_random_currency(self):
        """  """
        currency = Currency(self.redis )
        print currency.text



