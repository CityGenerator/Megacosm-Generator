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
json_data.close()


#pprint(data)
for feature in data:
    if (feature.find("_chance") != -1 ):
        server.set('worldname'+feature, data[feature])
    else:
        featureset=data[feature]
        server.ltrim('worldname'+feature, 0, 0 )
        server.lpush('worldname'+feature, *featureset)

    
print server.llen('worldnamepost') 
#print server.srandmember('worldnamepre')+server.srandmember('worldnameroot')+server.srandmember('worldnamepost')




