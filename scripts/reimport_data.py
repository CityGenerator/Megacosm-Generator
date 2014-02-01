import redis
import ConfigParser, os
import json
import sys
from pprint import pprint


config = ConfigParser.RawConfigParser()
config.read('configs/config.ini')

url = config.get('redis', 'url')

server=redis.from_url(url)

json_data=open('data/worldnames.json')
data = json.load(json_data)

#pprint(data)
for feature in data:
    if (feature.find("_chance") != -1 ):
        server.set('worldname'+feature, data[feature])
    else:
        featurelist=data[feature]
        server.sadd('worldname'+feature, *featurelist)

    
 
print server.srandmember('worldnamepre')+server.srandmember('worldnameroot')+server.srandmember('worldnamepost')



json_data.close()

