
#kind of Governments

# This government has been in power

self.redis.zadd('govt_age', '{ "name":"for a short time",                  "score":10       }', '10')
self.redis.zadd('govt_age', '{ "name":"for mere hours",                    "score":20       }', '20')
self.redis.zadd('govt_age', '{ "name":"for mere days",                     "score":30       }', '30')
self.redis.zadd('govt_age', '{ "name":"for a few months",                  "score":40       }', '40')
self.redis.zadd('govt_age', '{ "name":"for years",                         "score":50       }', '50')
self.redis.zadd('govt_age', '{ "name":"for several years",                 "score":60       }', '60')
self.redis.zadd('govt_age', '{ "name":"for many years",                    "score":70       }', '70')
self.redis.zadd('govt_age', '{ "name":"for decades",                       "score":80       }', '80')
self.redis.zadd('govt_age', '{ "name":"for several decades",               "score":90       }', '90')
self.redis.zadd('govt_age', '{ "name":"far longer than should be allowed", "score":100      }', '100')

self.redis.zadd('govt_reputation', '{ "name":"despised",   "score":10       }', '10')
self.redis.zadd('govt_reputation', '{ "name":"hated",      "score":20       }', '20')
self.redis.zadd('govt_reputation', '{ "name":"feared",     "score":30       }', '30')
self.redis.zadd('govt_reputation', '{ "name":"ridiculed",  "score":40       }', '40')
self.redis.zadd('govt_reputation', '{ "name":"mocked",     "score":50       }', '50')
self.redis.zadd('govt_reputation', '{ "name":"praised",    "score":60       }', '60')
self.redis.zadd('govt_reputation', '{ "name":"loved",      "score":70       }', '70')
self.redis.zadd('govt_reputation', '{ "name":"respected",  "score":80       }', '80')
self.redis.zadd('govt_reputation', '{ "name":"honored",    "score":90       }', '90')
self.redis.zadd('govt_reputation', '{ "name":"revered",    "score":100      }', '100')
       
self.redis.zadd('govt_opposition', '{ "name":"no visible", "score":10       }', '10')
self.redis.zadd('govt_opposition', '{ "name":"secret",     "score":20       }', '20')
self.redis.zadd('govt_opposition', '{ "name":"minor",      "score":30       }', '30')
self.redis.zadd('govt_opposition', '{ "name":"peaceful",   "score":40       }', '40')
self.redis.zadd('govt_opposition', '{ "name":"open",       "score":50       }', '50')
self.redis.zadd('govt_opposition', '{ "name":"public",     "score":60       }', '60')
self.redis.zadd('govt_opposition', '{ "name":"strong",     "score":70       }', '70')
self.redis.zadd('govt_opposition', '{ "name":"hostile",    "score":80       }', '80')
self.redis.zadd('govt_opposition', '{ "name":"forceful",   "score":90       }', '90')
self.redis.zadd('govt_opposition', '{ "name":"violent",    "score":100      }', '100')
        
self.redis.zadd('govt_corruption', '{ "name":"the epitome corruption",                    "score":5       }', '5')
self.redis.zadd('govt_corruption', '{ "name":"corrupt and nefarious",                    "score":10       }', '10')
self.redis.zadd('govt_corruption', '{ "name":"willing to look the other way for the right price",    "score":15       }', '15')
self.redis.zadd('govt_corruption', '{ "name":"crooked",                                  "score":20       }', '20')
self.redis.zadd('govt_corruption', '{ "name":"on the take",                              "score":25       }', '25')
self.redis.zadd('govt_corruption', '{ "name":"underhanded",                              "score":30       }', '30')
self.redis.zadd('govt_corruption', '{ "name":"unethical",                                "score":35       }', '35')
self.redis.zadd('govt_corruption', '{ "name":"disreputable",                             "score":40       }', '40')
self.redis.zadd('govt_corruption', '{ "name":"equitable",                                "score":45       }', '45')
self.redis.zadd('govt_corruption', '{ "name":"reasonable",                               "score":50       }', '50')
self.redis.zadd('govt_corruption', '{ "name":"fair",                                     "score":55       }', '55')
self.redis.zadd('govt_corruption', '{ "name":"honest",                                   "score":60       }', '60')
self.redis.zadd('govt_corruption', '{ "name":"principled",                               "score":65       }', '65')
self.redis.zadd('govt_corruption', '{ "name":"decent",                                   "score":70       }', '70')
self.redis.zadd('govt_corruption', '{ "name":"resolute",                                 "score":75       }', '75')
self.redis.zadd('govt_corruption', '{ "name":"honorable",                                "score":80       }', '80')
self.redis.zadd('govt_corruption', '{ "name":"trustworthy",                              "score":85       }', '85')
self.redis.zadd('govt_corruption', '{ "name":"upright",                                  "score":90       }', '90')
self.redis.zadd('govt_corruption', '{ "name":"virtuous",                                 "score":95       }', '95')
self.redis.zadd('govt_corruption', '{ "name":"incorruptible",                            "score":100      }', '100')
       
self.redis.zadd('govt_approval', '{ "name":"despised",                                   "score":10       }', '10')
self.redis.zadd('govt_approval', '{ "name":"hated",                                      "score":20       }', '20')
self.redis.zadd('govt_approval', '{ "name":"feared",                                     "score":30       }', '30')
self.redis.zadd('govt_approval', '{ "name":"ridiculed",                                  "score":40       }', '40')
self.redis.zadd('govt_approval', '{ "name":"mocked",                                     "score":50       }', '50')
self.redis.zadd('govt_approval', '{ "name":"praised",                                    "score":60       }', '60')
self.redis.zadd('govt_approval', '{ "name":"loved",                                      "score":70       }', '70')
self.redis.zadd('govt_approval', '{ "name":"respected",                                  "score":80       }', '80')
self.redis.zadd('govt_approval', '{ "name":"honored",                                    "score":90       }', '90')
self.redis.zadd('govt_approval', '{ "name":"revered",                                    "score":100      }', '100')
       
self.redis.zadd('govt_efficiency', '{ "name":"the pinnacle of inefficiency",              "score":5       }', '5')
self.redis.zadd('govt_efficiency', '{ "name":"incapable of even simple tasks",           "score":10       }', '10')
self.redis.zadd('govt_efficiency', '{ "name":"clearly incompetent",                      "score":15       }', '15')
self.redis.zadd('govt_efficiency', '{ "name":"horribly inefficient",                     "score":20       }', '20')
self.redis.zadd('govt_efficiency', '{ "name":"sloppy and disorganized",                  "score":25       }', '25')
self.redis.zadd('govt_efficiency', '{ "name":"inept and inadequate",                     "score":30       }', '30')
self.redis.zadd('govt_efficiency', '{ "name":"slipshod",                                 "score":35       }', '35')
self.redis.zadd('govt_efficiency', '{ "name":"minimally competent",                      "score":40       }', '40')
self.redis.zadd('govt_efficiency', '{ "name":"somewhat capable",                          "score":45       }', '45')
self.redis.zadd('govt_efficiency', '{ "name":"adequate",                                 "score":50       }', '50')
self.redis.zadd('govt_efficiency', '{ "name":"satisfactory",                             "score":55       }', '55')
self.redis.zadd('govt_efficiency', '{ "name":"mostly sufficient",                        "score":60       }', '60')
self.redis.zadd('govt_efficiency', '{ "name":"surprisingly decent",                      "score":65       }', '65')
self.redis.zadd('govt_efficiency', '{ "name":"effective overall",                        "score":70       }', '70')
self.redis.zadd('govt_efficiency', '{ "name":"on the ball",                              "score":75       }', '75')
self.redis.zadd('govt_efficiency', '{ "name":"efficient",                                "score":80       }', '80')
self.redis.zadd('govt_efficiency', '{ "name":"shrewd",                                   "score":85       }', '85')
self.redis.zadd('govt_efficiency', '{ "name":"surprisingly skillful",                    "score":90       }', '90')
self.redis.zadd('govt_efficiency', '{ "name":"magnificently organized",                  "score":95       }', '95')
self.redis.zadd('govt_efficiency', '{ "name":"ruthlessly effective",                     "score":100      }', '100')
    
        
self.redis.zadd('govt_influence', '{ "name":"negligible",          "score":5       }', '5')
self.redis.zadd('govt_influence', '{ "name":"dwindling rapidly",  "score":10       }', '10')
self.redis.zadd('govt_influence', '{ "name":"wilting",            "score":15       }', '15')
self.redis.zadd('govt_influence', '{ "name":"wasting away",       "score":20       }', '20')
self.redis.zadd('govt_influence', '{ "name":"shrinking",          "score":25       }', '25')
self.redis.zadd('govt_influence', '{ "name":"declining",          "score":30       }', '30')
self.redis.zadd('govt_influence', '{ "name":"receding",           "score":35       }', '35')
self.redis.zadd('govt_influence', '{ "name":"consistent",         "score":40       }', '40')
self.redis.zadd('govt_influence', '{ "name":"steady",             "score":45       }', '45')
self.redis.zadd('govt_influence', '{ "name":"lasting",            "score":50       }', '50')
self.redis.zadd('govt_influence', '{ "name":"enduring",           "score":55       }', '55')
self.redis.zadd('govt_influence', '{ "name":"steadfast",          "score":60       }', '60')
self.redis.zadd('govt_influence', '{ "name":"unwavering",         "score":65       }', '65')
self.redis.zadd('govt_influence', '{ "name":"broadening",         "score":70       }', '70')
self.redis.zadd('govt_influence', '{ "name":"improving",          "score":75       }', '75')
self.redis.zadd('govt_influence', '{ "name":"spreading",          "score":80       }', '80')
self.redis.zadd('govt_influence', '{ "name":"growing",            "score":85       }', '85')
self.redis.zadd('govt_influence', '{ "name":"maturing",           "score":90       }', '90')
self.redis.zadd('govt_influence', '{ "name":"flourishing",        "score":95       }', '95')
self.redis.zadd('govt_influence', '{ "name":"thriving",           "score":100       }', '100')
        
self.redis.zadd('govt_unity', '{ "name":"turns against itself",                             "score":10       }', '10')
self.redis.zadd('govt_unity', '{ "name":"is eager to point fingers",                        "score":20       }', '20')
self.redis.zadd('govt_unity', '{ "name":"gives up their freedom in exchange for security",  "score":30       }', '30')
self.redis.zadd('govt_unity', '{ "name":"flees for the hills",                              "score":40       }', '40')
self.redis.zadd('govt_unity', '{ "name":"cowers in fear",                                   "score":50       }', '50')
self.redis.zadd('govt_unity', '{ "name":"squabbles amongst themselves",                     "score":60       }', '60')
self.redis.zadd('govt_unity', '{ "name":"stages ineffective protests",                      "score":70       }', '70')
self.redis.zadd('govt_unity', '{ "name":"overcomes their differences",                      "score":80       }', '80')
self.redis.zadd('govt_unity', '{ "name":"comes together and fights as one",                 "score":90       }', '90')
self.redis.zadd('govt_unity', '{ "name":"rallies behind its leaders",                       "score":100       }', '100')
        
self.redis.zadd('govt_theology', '{ "name":"is strictly forbidden on pain of death",                              "score":5       }', '5')
self.redis.zadd('govt_theology', '{ "name":"is forbidden",                                                       "score":10       }', '10')
self.redis.zadd('govt_theology', '{ "name":"will get you in trouble",                                            "score":15       }', '15')
self.redis.zadd('govt_theology', '{ "name":"is unwelcome",                                                       "score":20       }', '20')
self.redis.zadd('govt_theology', '{ "name":"is unregulated",                                                     "score":25       }', '25')
self.redis.zadd('govt_theology', '{ "name":"is taxed heavily",                                                   "score":30       }', '30')
self.redis.zadd('govt_theology', '{ "name":"is tightly regulated by the government",                             "score":35       }', '35')
self.redis.zadd('govt_theology', '{ "name":"is viewed as a nuisance",                                            "score":40       }', '40')
self.redis.zadd('govt_theology', '{ "name":"is practiced behind closed doors",                                   "score":45       }', '45')
self.redis.zadd('govt_theology', '{ "name":"is left to the people",                                              "score":50       }', '50')
self.redis.zadd('govt_theology', '{ "name":"is common place",                                                    "score":55       }', '55')
self.redis.zadd('govt_theology', '{ "name":"is unregulated and diverse, making it a melting pot of many faiths", "score":60       }', '60')
self.redis.zadd('govt_theology', '{ "name":"enjoys many legal benefits",                                         "score":65       }', '65')
self.redis.zadd('govt_theology', '{ "name":"is widespread",                                                      "score":70       }', '70')
self.redis.zadd('govt_theology', '{ "name":"is sanctioned by the government",                                    "score":75       }', '75')
self.redis.zadd('govt_theology', '{ "name":"is limited to a single deity",                                       "score":80       }', '80')
self.redis.zadd('govt_theology', '{ "name":"plays a central role in the lawmaking process",                      "score":85       }', '85')
self.redis.zadd('govt_theology', '{ "name":"controlled by the government",                                       "score":90       }', '90')
self.redis.zadd('govt_theology', '{ "name":"is sacred, and the words of the gods are law",                       "score":95       }', '95')
self.redis.zadd('govt_theology', '{ "name":"is used to control the populace",                                    "score":100       }', '100')


self.redis.lpush('govt_kind', 'country')


self.redis.hset('govtcountry_govttype_description', 'absolutemonarchy', '{ "name":"absolute monarchy",            "description":"the monarch rules unhindered"  }')
self.redis.hset('govtcountry_govttype_description', 'authoritarian', '{ "name":"authoritarian government",     "description":"state authority is imposed onto many aspects of citizens\' lives"  }')
self.redis.hset('govtcountry_govttype_description', 'commonwealth', '{ "name":"commonwealth",                 "description":"state authority is founded on law and united by a compact of the people for the common good"  }')
self.redis.hset('govtcountry_govttype_description', 'communist', '{ "name":"communist government",         "description":"the state plans and controls the economy and a single party holds power"  }')
self.redis.hset('govtcountry_govttype_description', 'constitutional', '{ "name":"constitutional government",    "description":"an authoritative document sets forth the system of fundamental laws and limits of that government"  }')
self.redis.hset('govtcountry_govttype_description', 'democracy', '{ "name":"democracy",                    "description":"the supreme power is retained by the people, but is exercised through a system of representation"  }')
self.redis.hset('govtcountry_govttype_description', 'dictatorship', '{ "name":"dictatorship",                 "description":"the ruler or small clique wield absolute power (not restricted by a constitution or laws)"  }')
self.redis.hset('govtcountry_govttype_description', 'ecclesiastical', '{ "name":"ecclesiastical government",    "description":"the government administrated by a church."  }')
self.redis.hset('govtcountry_govttype_description', 'emirate', '{ "name":"emirate",                      "description":"the supreme power is in the hands of an emir, who may be an absolute overlord with constitutionally limited authority"  }')
self.redis.hset('govtcountry_govttype_description', 'federation', '{ "name":"federation",                   "description":"sovereign power is formally divided between a central authority and a number of constituent regions"  }')
self.redis.hset('govtcountry_govttype_description', 'monarchy', '{ "name":"monarchy",                     "description":"the supreme power is lodged in the hands of a monarch who reigns with constitutionally limited authority"  }')
self.redis.hset('govtcountry_govttype_description', 'oligarchy', '{ "name":"oligarchy",                    "description":"control is exercised by a small group of individuals whose authority generally is based on wealth or power"  }')
self.redis.hset('govtcountry_govttype_description', 'parliamentary', '{ "name":"parliamentary government",     "description":"members are nominated to their positions by a parliament and can be dissolved by the parliament if it can no longer function"  }')
self.redis.hset('govtcountry_govttype_description', 'republic', '{ "name":"republic",                     "description":"the people\'s elected representatives, not the people themselves, vote on legislation."  }')
self.redis.hset('govtcountry_govttype_description', 'theocracy', '{ "name":"theocracy",                    "description":"a deity is recognized as the supreme civil ruler, but the deity\'s laws are interpreted by ecclesiastical authorities"  }')
self.redis.hset('govtcountry_govttype_description', 'totalitarian', '{ "name":"totalitarian government",      "description":"the government subordinates individuals by controlling all political and economic matters, as well as the attitudes, values, and beliefs"  }')
            
self.redis.lpush('govtcountry_govttype', 'absolutemonarchy            ')
self.redis.lpush('govtcountry_govttype', 'authoritarian               ')
self.redis.lpush('govtcountry_govttype', 'commonwealth                ')
self.redis.lpush('govtcountry_govttype', 'communist                   ')
self.redis.lpush('govtcountry_govttype', 'constitutional              ')
self.redis.lpush('govtcountry_govttype', 'democracy                   ')
self.redis.lpush('govtcountry_govttype', 'dictatorship                ')
self.redis.lpush('govtcountry_govttype', 'ecclesiastical              ')
self.redis.lpush('govtcountry_govttype', 'emirate                     ')
self.redis.lpush('govtcountry_govttype', 'federation                  ')
self.redis.lpush('govtcountry_govttype', 'monarchy                    ')
self.redis.lpush('govtcountry_govttype', 'oligarchy                   ')
self.redis.lpush('govtcountry_govttype', 'parliamentary               ')
self.redis.lpush('govtcountry_govttype', 'republic         ')
self.redis.lpush('govtcountry_govttype', 'theocracy        ')
self.redis.lpush('govtcountry_govttype', 'totalitarian     ')

            
self.redis.lpush('govt_kind', 'city')

#Detroit is governed through a[n] __________, where ____________________.
self.redis.hset('govtcity_govttype_description', 'councilmanager', '{ "name":"council/manager", "description":"things are run by a council, which selects a manager for administrative tasks"}')
self.redis.hset('govtcity_govttype_description', 'mayorcouncil', '{ "name":"mayor/council",   "description":"a mayor handles executive tasks, while a council handles legislative tasks"}')
self.redis.hset('govtcity_govttype_description', 'commission', '{ "name":"commission",      "description":"commissioners manage specific executive affairs"}')
self.redis.hset('govtcity_govttype_description', 'townmeeting', '{ "name":"town meeting",    "description":"everyone can be heard"}')
self.redis.hset('govtcity_govttype_description', 'magistrate', '{ "name":"magistrate",      "description":"representative appointed by the nation\'s leaders governs"}')

self.redis.lpush('govtcity_govttype', 'councilmanager')
self.redis.lpush('govtcity_govttype', 'mayorcouncil')
self.redis.lpush('govtcity_govttype', 'commission')
self.redis.lpush('govtcity_govttype', 'townmeeting')
self.redis.lpush('govtcity_govttype', 'magistrate')

SET govt_influencereason_chance 50
self.redis.lpush('govt_influencereason', 'riots in the region')
self.redis.lpush('govt_influencereason', 'food shortages in the region')
self.redis.lpush('govt_influencereason', 'racial tensions')
self.redis.lpush('govt_influencereason', 'a thwarted assassination attempt')

#    <feature>
#
#        <right>
#            <option>by forgery</option>
#            <option>by divine will</option>
#            <option>by consensus</option>
#            <option>by constitution</option>
#            <option>by hereditary succession</option>
#            <option>by election</option>
#            <option>by appointment</option>
#            <option>by force</option>
#            <option>by revolution</option>
#            <option>by foreign imposition</option>
#        </right>
#    
#    
#        <maintained><!-- and that power is maintained __________ -->
#            <option >through the tip of a sword</option>
#            <option >through random violence</option>
#            <option >through the ignorance of the plebeian society</option>
#            <option >through vague threats and a constant state of fear</option>
#            <option >through financial oppression</option>
#            <option >by secret police raiding homes in the dead of night</option>
#            <option >by strict laws and corrupt guards</option>
#            <option >by strict laws and incorruptible guards</option>
#            <option >by draconian laws and underpaid guards</option>
#            <option >through spying and assassination</option>
#            <option >through a fair and just legal system</option>
#            <option >through the writ of law</option>
#            <option >through a knowledgeable and just populace</option>
#            <option >through vague promises and a constant state of hope</option>
#            <option >through sheer willpower</option>
#            <option >through the acclaim of the nobles</option>
#            <option >by unwavering supporters</option>
#            <option >through the support of merchant groups</option>
#        </maintained>
#    
#    </feature>
#
#    <govtypes> 
#
#
#
#
#
#
#
#
