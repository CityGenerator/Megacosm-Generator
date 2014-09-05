
from megacosm.generators.Motivation import Motivation
from megacosm.generators.NPC import NPC
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from megacosm.util.Seeds import *

from config import TestConfiguration

class TestMotivation(unittest.TestCase):

    def setUp(self):
        self.redis=redis.from_url(TestConfiguration.REDIS_URL)        
#        self.seed=set_seed( "3" )

    def test_random_motivation(self):
        """  """
        motivation = Motivation(self.redis )
        self.assertNotEqual(motivation.text,'')

    def test_motivation_w_npc(self):
        """  """
        npc=NPC(self.redis)
        motivation = Motivation(self.redis, { 'npc':npc } )
        self.assertNotEqual(motivation.text,'')
        self.assertEqual(motivation.npc,npc)
        self.assertNotEqual("%s" % (motivation),'')


