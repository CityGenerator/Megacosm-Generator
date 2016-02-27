#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Organization
import unittest2 as unittest
from megacosm.generators import Leader
import redis
from config import TestConfiguration


class TestOrganization(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

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
