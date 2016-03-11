#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import NPC, Phobia, Motivation
import unittest2 as unittest
import fakeredis
from megacosm.util.Seeds import set_seed
from config import TestConfiguration

class TestNPC(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis()
        self.redis.zadd( 'npc_sex', '{"name":"female",     "pronoun":"she", "possessive":"her", "third-person":"her", "spouse":"husband", "score":51   }', 100);
        self.redis.zadd('npc_piety','{"name":"overzealous",   "score":100   }',100)
        self.redis.zadd('npc_age','{"name":"ancient",        "score":100 }',100)
        self.redis.zadd('npc_honor','{"name":"honorable",     "score":100 }',100)
        self.redis.zadd('npc_bravery','{"name":"heroic",   "score":100  }',100)
        self.redis.zadd('npc_skill','{"name":"legendarily skilled",   "score":100  }',100)
        self.redis.zadd('npc_experience','{"name":"grizzled",   "score":100  }',100)
        self.redis.zadd('npc_strength','{"name":"herculean",   "score":100  }',100)
        self.redis.zadd('npc_endurance','{"name":"unflagging",   "score":100  }',100)
        self.redis.zadd('npc_satisfaction','{"name":"satisfied",   "score":100  }',100)
        self.redis.zadd('npc_agility','{"name":"agile",   "score":100  }',100)
        self.redis.zadd('npc_wisdom','{"name":"wise",   "score":100  }',100)
        self.redis.zadd('npc_charisma','{"name":"inspiring",   "score":100  }',100)
        self.redis.zadd('npc_intelligence','{"name":"brilliant",   "score":100  }',100)
        self.redis.zadd('npc_attractiveness','{"name":"stunning",     "score":100 }',100)
        self.redis.zadd('npc_money','{"name":"rich",             "score":100 }',100)
        self.redis.zadd('npc_generous','{"name":"generous",     "score":100 }',100)
        self.redis.zadd('npc_luck','{"name":"lucky",          "score":100 }',100)
        self.redis.zadd('npc_confident','{"name":"incredibly",     "score":100 }',100)
        self.redis.zadd('npc_kill','{"name":"killed without issue",             "score":100  }',100)
        self.redis.lpush('npc_posessiondetail','was lost during the war')
        self.redis.lpush('npc_posession','jackknife')
        self.redis.lpush('npc_attitude','cautious')
        self.redis.lpush('npc_regret','scared a child')
        self.redis.lpush('npc_height','short')
        self.redis.lpush('npc_build','thin')
        self.redis.lpush('npc_mark','mole')
        self.redis.lpush('npc_mark_location','face')
        self.redis.lpush('npc_complexion','dull')
        self.redis.lpush('npc_eye','beady')
        self.redis.lpush('npc_profession','actor')
        self.redis.lpush('npc_emotion','angry')
        self.redis.lpush('npc_marriagestatus','divorced')
        self.redis.lpush('npc_modeical_condition','gout')
        self.redis.lpush('fur_covertemplate','fur cover template')
        self.redis.lpush('fur_furcolor','blue')
        self.redis.lpush('fur_furkind','soft')
        self.redis.lpush('skin_covertemplate','skin cover template')
        self.redis.lpush('skin_skincolor','red')
        self.redis.lpush('skin_skinkind','scabby')
        self.redis.lpush('scale_covertemplate','scale cover template')
        self.redis.lpush('scale_scalecolor','silver')
        self.redis.lpush('scale_scalekind','flaky')
        self.redis.lpush('feather_covertemplate','feather cover template')
        self.redis.lpush('feather_feathercolor','white')
        self.redis.lpush('feather_featherkind','thin')
    
        self.redis.lpush('phobia_template', "You are afraid.")
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('motivationacceptance_text', 'to impress someone')
    
        #Details for Humans
        self.redis.set('human_details', '{"name": "Human",  "size": "medium",  "description": "quick growth and adaptability"}')
        self.redis.lpush('human_covering','skin')
        self.redis.lpush('humanname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}}{{params.first_post}} {{params.last_pre}}{{params.last_root}}{{params.last_post}} {{params.trailer}}')
        self.redis.lpush('humanname_shortname_template', '{{params.first_pre}}{{params.first_root}}{{params.first_post}}')
        self.redis.lpush('humanname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}{{params.last_post}}')
   
 
        self.redis.lpush('humanname_first_pre', 'Dru')
        self.redis.lpush('humanname_first_root', 'cil')
        self.redis.lpush('humanname_first_post', 'la')
        self.redis.lpush('humanname_last_pre', 'La')
        self.redis.lpush('humanname_last_root', 'Sal')
        self.redis.lpush('humanname_last_post', 'vae')
    
        #Details for Kobolds
        self.redis.set( 'kobold_details', '{"name": "Kobold",     "size": "small",   "description": "their small stature and cowardice"}')
        self.redis.lpush('kobold_covering','skin')
        self.redis.lpush('koboldname_first_root', 'Kole')
        self.redis.lpush('koboldname_fullname_template', '{{params.title}} {{params.first_root}}{{params.first_post}} {{params.trailer}}')
        self.redis.lpush('koboldname_shortname_template', '{{params.first_root}}')
        self.redis.lpush('koboldname_formalname_template', '{{params.title}} {{params.first_root}}')
 
        self.redis.set('kobold_subrace_chance',100)
        self.redis.lpush('kobold_subrace', 'aquatic')
    
        self.redis.hset('kobold_subrace_description', 'aquatic', '{"subrace": "Aquatic Kobold",   "description": "" }')

    def tearDown(self):
        self.redis.flushall()

    def test_generated_race(self):
        """  """
	# only human is in the npc_race array
	self.redis.lpush('npc_race','human')

        npc = NPC(self.redis)
        self.assertEqual('human', npc.race)
        npc = NPC(self.redis, {})
        self.assertEqual('human', npc.race)

    def test_races(self):
        """  """
	self.redis.lpush('npc_race','kobold')

        npc = NPC(self.redis, {'race': 'kobold'})
        self.assertIn('kobold', npc.race)
        self.assertEqual('Kole',npc.name.fullname)

        with self.assertRaisesRegexp(Exception, 'turkeys is not a valid race and has no associated data'):
            npc = NPC(self.redis, {'race': 'turkeys'})

    def test_race_details(self):
        """  """
	self.redis.lpush('npc_race','human')

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')

        self.assertEqual(npc.details['name'], 'Human')
        self.assertEqual(npc.details['size'], 'medium')
        self.assertEqual(npc.details['description'], 'quick growth and adaptability')

    def test_names(self):
        """  """
	self.redis.lpush('npc_race','human')
	self.redis.lpush('humanname_title', 'Lady')
	self.redis.lpush('humanname_trailer', 'Esq.')

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')
        self.assertEqual('Lady Drucilla LaSalvae Esq.',npc.name.fullname)
        self.assertEqual('Lady Drucilla LaSalvae Esq.',str(npc))

    def test_phobias(self):
        """ Test NPC Phobias """
	#Our Static Phobia
	phobia = Phobia(self.redis)
	self.redis.lpush('npc_race','human')

        npc = NPC(self.redis, {'race':'human'})
        self.assertNotEqual('',npc.race)
        self.assertNotEqual('',npc.phobia.text)
	#This should be random, not our static
        self.assertNotEqual(phobia ,npc.phobia)
        self.assertEqual('You are afraid.',npc.phobia.text)


        npc = NPC(self.redis, {'race':'human','phobia':phobia})
	#This should be our static Phobia
        self.assertEqual(phobia ,npc.phobia)
        self.assertEqual('You are afraid.',npc.phobia.text)


    def test_motivations(self):
        """ Test NPC Motivations """
	#Our Static Motivation
	self.redis.lpush('npc_race','human')
	self.redis.lpush('npc_race','kobold')

	motivation = Motivation(self.redis)

        npc = NPC(self.redis, {'race':'human'})
        self.assertNotEqual('',npc.race)
        self.assertNotEqual('',npc.motivation.text)
	#This should be random, not our static
        self.assertNotEqual(motivation ,npc.motivation)
        self.assertEqual('to impress someone',npc.motivation.text)

        npc = NPC(self.redis, {'race':'human','motivation':motivation})
	#This should be our static Motivation
        self.assertEqual(motivation ,npc.motivation)
        self.assertEqual('to impress someone',npc.motivation.text)

