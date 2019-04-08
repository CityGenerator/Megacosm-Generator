#!/usr/bin/env python3
import fakeredis
import redis
import os

class BaseConfiguration(object):
    # Statement for enabling the development environment
    DEBUG = False
    LOG_PATH = 'data/logging.json'

    REDIS = redis.Redis(host="localhost", port=6379, decode_responses=True, encoding=u'utf-8')


class ProductionConfiguration(BaseConfiguration):
    # Statement for enabling the development environment
    DEBUG = False


class DevConfiguration(BaseConfiguration):
    # Statement for enabling the development environment
    DEBUG = True


class IntegrationTestConfiguration(BaseConfiguration):
    # Statement for enabling the development environment
    DEBUG = True

class TestConfiguration(BaseConfiguration):
    # Statement for enabling the development environment
    DEBUG = True
    REDIS = fakeredis.FakeRedis(decode_responses=True)

class DockerConfiguration(BaseConfiguration):
    # Statement for enabling the development environment
    if 'REDISHOST' not in os.environ or 'REDISPORT' not in os.environ:
        raise Exception("missing Redis ENV values!")
    REDIS = redis.Redis(host=os.environ['REDISHOST'],
                      port=os.environ['REDISPORT'],
                      decode_responses=True, encoding=u'utf-8'
                      )
