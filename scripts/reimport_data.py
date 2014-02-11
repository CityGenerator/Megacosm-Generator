#!/usr/bin/python

import redis
import ConfigParser, os
import glob
import sys
from pprint import pprint


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')

url = config.get('redis', 'url')

server=redis.from_url(url)
pipe=server.pipeline()


linenumber=0
for filename in glob.glob("data/*.data") :
    raw_data=open(filename)
    for line in raw_data:
        linenumber+=1
        line=line.rstrip()
        if line:
            print line
            if line.startswith('#'):
                continue;
            else:
                command, args = line.split(' ',1)
                command=command.upper()
                if command == 'SET':
                    key,value=args.split(' ',1)
                    pipe.set(key,value)
                elif command == "LPUSH":
                    key,value=args.split(' ',1)
                    pipe.lpush(key,value)
                elif command == "ZADD":
                    key,score,value=args.split(' ',2)
                    print score
                    pipe.zadd(key,value,score)
                elif command == "DEL":
                    pipe.delete(args)
                else:
                    print "I have no idea what ",line,"is."
                    raise Exception("line #%s in %s: %s is an unsupported command." % (linenumber, filename, command) )
    raw_data.close()

pipe.execute()


print server.type('starnamepre')



