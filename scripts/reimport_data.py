import redis
import ConfigParser, os
import json
import sys
from pprint import pprint


config = ConfigParser.RawConfigParser()
config.read('configs/config.ini')

url = config.get('redis', 'url')

server=redis.from_url(url)

def load_names(dataname,data):
    print "loading",dataname
    for feature in data:
        if (feature.find("_chance") != -1 ):
            server.set(dataname+feature, data[feature])
            print "    ",feature,":",server.get(dataname+feature) 
        else:
            featureset=data[feature]
            server.ltrim(dataname+feature, 0, 0 )
            server.lpush(dataname+feature, *featureset)
            print "    ",feature,":",server.llen(dataname+feature) 





for dataname in ['world','star','moon']:
    json_data=open('data/'+dataname+'name.json')
    data = json.load( json_data )
    load_names(dataname+'name',data)
    json_data.close()

