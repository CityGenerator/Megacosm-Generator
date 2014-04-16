
from util.Seeds import *
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


class TestSeeds(unittest.TestCase):

    def setUp(self):
        """  """
        
    def test_int_seeds(self):
        """  """
        seeds = set_seed( 17)
        self.assertEquals(17,seeds)


    def test_str_seeds(self):
        """  """
        seeds = set_seed( "22")
        self.assertEquals(22,seeds)

    def test_unicode_seeds(self):
        """  """
        seeds = set_seed( u"22")
        self.assertEquals(22,seeds)

    def test_int_invalid_high(self):
        """  """
        seeds = set_seed( 10000000000000)
        self.assertLessEqual(1,seeds)
        self.assertGreaterEqual(10000000,seeds)

    def test_int_invalid_low(self):
        """  """
        seeds = set_seed( -2)
        self.assertLessEqual(1,seeds)
        self.assertGreaterEqual(10000000,seeds)



    def test_string_invalid_high(self):
        """  """
        seeds = set_seed( '100000000000000000')
        self.assertLessEqual(1,seeds)
        self.assertGreaterEqual(10000000,seeds)

    def test_string_invalid_low(self):
        """  """
        seeds = set_seed( '-2')
        self.assertLessEqual(1,seeds)
        self.assertGreaterEqual(10000000,seeds)


    def test_string_invalid_value(self):
        """  """
        seeds = set_seed( 'herpderp')
        self.assertLessEqual(1,seeds)
        self.assertGreaterEqual(10000000,seeds)

    def test_none(self):
        """  """
        seeds = set_seed( None)
        self.assertLessEqual(1,seeds)
        self.assertGreaterEqual(10000000,seeds)



