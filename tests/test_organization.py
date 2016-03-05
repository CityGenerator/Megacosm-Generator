#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Organization
import unittest2 as unittest
from megacosm.generators import Leader
import fakeredis
from config import TestConfiguration


class TestOrganization(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('organization_kind', 'crime ring')
        self.redis.lpush('organization_powertype', 'gambling')
        self.redis.lpush('organization_identification', 'with difficulty')
        self.redis.zadd('organization_age', '{"name":"ancient",       "score":100  }', 100)
        self.redis.zadd('organization_legal', '{"name":"legitimate",   "score":100   }', 100)
        self.redis.zadd('organization_violence', '{"name":"passive",       "score":100  }', 100)
        self.redis.zadd('organization_morale', '{"name":"encouraged",          "score":100  }', 100)
        self.redis.zadd('organization_leadership', '{ "name":"strong",     "score":100 }', 100)
        self.redis.zadd('organization_structure', '{ "name":"rigidly",    "score":100 }', 100)
        self.redis.zadd('organization_stability', '{ "name":"are rock solid",     "score":100 }', 100)
        self.redis.zadd('organization_adaptability', '{"name":"stay ahead of new development",    "score":100  }', 100)
        self.redis.zadd('organization_regulation', '{ "name":"strictly enforced",  "score":100 }', 100)
        self.redis.zadd('organization_rules', '{ "name":"rigidly",    "score":100 }', 100)
        self.redis.zadd('organization_failure', '{ "name":"better guidance and training",  "score":100 }', 100)
        self.redis.zadd('organization_teamwork', '{ "name":"as a well oiled machine",         "score":100 }', 100)
        self.redis.zadd('organization_visibility', '{ "name":"well known",            "score":100 }', 100)
        self.redis.zadd('organization_size', '{ "name":"world",       "score":100 }', 100)
        self.redis.zadd('organization_entry', '{"name":"impossible",      "score":100  }', 100)
        self.redis.lpush('organization_template', "{{params.leader.name['firstname']}}'s {{params.kind|title}}")
        self.redis.lpush('name_organizationpre', 'Yak')
        self.redis.lpush('name_organizationroot', 'u')
        self.redis.lpush('name_organizationpost', 'gua')
        self.redis.lpush('name_organizationtrailer', 'Dragons')
        self.redis.lpush('npc_race','gnome')
        self.redis.lpush('gnome_covering','skin')
        self.redis.set('gnome_details',  '{"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }')
        self.redis.set('skin_covertemplate', '{{params.skinkind}}, {{params.skincolor}} skin')
        self.redis.lpush('skin_skincolor','alabaster')
        self.redis.lpush('skin_skinkind', 'thick')
        self.redis.lpush('phobia_template', "You are afraid.")
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('motivationacceptance_text', 'to impress someone')
        self.redis.lpush('gnome_name_first_post', 'Tom')
        self.redis.lpush('gnome_name_last_pre', 'Gyro')
        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)
        self.redis.lpush('leader_kind', 'absolutemonarchy')
        self.redis.hset('leader_kind_description', 'absolutemonarchy', '{ "scope":"country"   }')
        self.redis.lpush('leaderabsolutemonarchy_leader', 'king')
        self.redis.hset('leaderabsolutemonarchy_leader_description', 'king', '{ "male":"King",    "female":"Queen"     }')
        self.redis.zadd('country_regiondetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
        self.redis.zadd('npc_sex', '{"name":"male",       "pronoun":"he", "possessive":"his",  "third-person":"him", "spouse":"wife",    "score":100  }', 100)

    def tearDown(self):
        self.redis.flushall()

    def test_random_organization(self):
        """  """
        organization = Organization(self.redis)
        self.assertNotEquals('', organization.text)
        self.assertIsInstance(organization.leader, Leader)

    def test_static_organization(self):
        """  """
        leader = Leader(self.redis)
        organization = Organization(self.redis,{'leader': leader, 'text':"boooyah"})
        self.assertEquals(leader, organization.leader)
        self.assertEquals("boooyah", organization.text)
