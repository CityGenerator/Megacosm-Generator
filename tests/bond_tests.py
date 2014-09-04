
from megacosm.generators.Bond import Bond
from megacosm.generators.Motivation import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from megacosm.util.Seeds import *

from config import TestConfiguration

class TestBond(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(TestConfiguration.REDIS_URL)
        self.seed=set_seed( "3" )

    def test_random_bond(self):
        """  """
        bond = Bond(self.redis )
#        self.assertEqual(bond.text,'you')

    def test_bond_features(self):
        """  """
        bond = Bond(self.redis, {'you':'Jesse', 'other':'Will', 'either':'Tony', 'partyA':'Shaun', 'partyB':'Rich', 'template':"{{params.you}} {{params.other}} {{params.either}} {{params.partyA}} {{params.partyB}}", 'bond_when_roll':5, 'when':'Bob' })
        
        self.assertEqual(bond.text,'Bob, Jesse Will Tony Shaun Rich')





