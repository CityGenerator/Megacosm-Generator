import redis
import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('configs/config.ini')

url = config.get('redis', 'url')

server=redis.from_url(url)






