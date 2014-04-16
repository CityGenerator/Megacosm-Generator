
from generators.Motivation import Motivation
from generators.NPC import NPC
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestMotivation(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(url)
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


