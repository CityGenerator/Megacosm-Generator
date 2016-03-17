#

ZADD roguedungeon_size  25 {"name":"tiny",     "minsize":20, "maxsize":20,   "score": 25   }
ZADD roguedungeon_size  65 {"name":"small",    "minsize":30, "maxsize":30,   "score": 65   }
ZADD roguedungeon_size  90 {"name":"medium",   "minsize":40, "maxsize":40,   "score": 90   }
ZADD roguedungeon_size  97 {"name":"large",    "minsize":50, "maxsize":50,   "score": 97   }
ZADD roguedungeon_size 100 {"name":"gigantic", "minsize":60, "maxsize":60,   "score": 100  }



ZADD roguedungeon_room_count  25 {"name":"few",        "minsize":3,  "maxsize":5,   "score": 25   }
ZADD roguedungeon_room_count  65 {"name":"several",    "minsize":5,  "maxsize":10,  "score": 65   }
ZADD roguedungeon_room_count  90 {"name":"many",       "minsize":10, "maxsize":25,  "score": 90   }
ZADD roguedungeon_room_count 100 {"name":"lots",       "minsize":25, "maxsize":50,  "score": 100  }



ZADD roguedungeon_room_size  25 {"name":"tiny",     "minsize":3,  "maxsize":4,    "score": 25   }
ZADD roguedungeon_room_size  65 {"name":"small",    "minsize":3,  "maxsize":10,   "score": 65   }
ZADD roguedungeon_room_size  90 {"name":"medium",   "minsize":3,  "maxsize":15,   "score": 90   }
ZADD roguedungeon_room_size 100 {"name":"gigantic", "minsize":3,  "maxsize":20,   "score": 100  }


ZADD roguedungeon_build  25 {"name":"natural caves",        "score": 25   }
ZADD roguedungeon_build  65 {"name":"dungeon",              "score": 65   }
ZADD roguedungeon_build 100 {"name":"dungeon and caves",    "score": 100  }


ZADD roguedungeon_refinement  25 {"name":"natural caves",                       "score": 25   }
ZADD roguedungeon_refinement  25 {"name":"natural caves with smoothed floors",  "score": 25   }
ZADD roguedungeon_refinement  25 {"name":"widened caves",                       "score": 25   }
ZADD roguedungeon_refinement  65 {"name":"dungeon and caves",                   "score": 65   }
ZADD roguedungeon_refinement 100 {"name":"dungeon",                             "score": 100  }


self.redis.lpush('roguedungeon_theme', 'elvish')
self.redis.lpush('roguedungeon_theme', 'human')
self.redis.lpush('roguedungeon_theme', 'royal')
self.redis.lpush('roguedungeon_theme', 'fiendish')
self.redis.lpush('roguedungeon_theme', 'dwarven')
self.redis.lpush('roguedungeon_theme', 'goblin')
self.redis.lpush('roguedungeon_theme', 'gnomish')
self.redis.lpush('roguedungeon_theme', 'storage')
self.redis.lpush('roguedungeon_theme', 'deathtrap')
self.redis.lpush('roguedungeon_theme', 'prison')
self.redis.lpush('roguedungeon_theme', 'laboratory')
self.redis.lpush('roguedungeon_theme', 'tomb')
self.redis.lpush('roguedungeon_theme', 'lair')
self.redis.lpush('roguedungeon_theme', 'ruins')
self.redis.lpush('roguedungeon_theme', 'mines')
self.redis.lpush('roguedungeon_theme', 'decorated')
self.redis.lpush('roguedungeon_theme', 'crypts')
self.redis.lpush('roguedungeon_theme', 'fortress')
self.redis.lpush('roguedungeon_theme', 'dreamworld')
self.redis.lpush('roguedungeon_theme', 'underworld')
self.redis.lpush('roguedungeon_theme', 'hideout')


# Room 7: ________

self.redis.lpush('roguedungeonroom_kind', 'abandoned')
self.redis.lpush('roguedungeonroom_kind', 'animalpen')
self.redis.lpush('roguedungeonroom_kind', 'antechamber')
self.redis.lpush('roguedungeonroom_kind', 'armory')
self.redis.lpush('roguedungeonroom_kind', 'arsenal')
self.redis.lpush('roguedungeonroom_kind', 'assemblage')
self.redis.lpush('roguedungeonroom_kind', 'audiencechamber')
self.redis.lpush('roguedungeonroom_kind', 'audiencehall')
self.redis.lpush('roguedungeonroom_kind', 'aviary')
self.redis.lpush('roguedungeonroom_kind', 'banquethall')
self.redis.lpush('roguedungeonroom_kind', 'barracks')
self.redis.lpush('roguedungeonroom_kind', 'bath')
self.redis.lpush('roguedungeonroom_kind', 'bedroom')
self.redis.lpush('roguedungeonroom_kind', 'bestiary')
self.redis.lpush('roguedungeonroom_kind', 'chantry')
self.redis.lpush('roguedungeonroom_kind', 'chapel')
self.redis.lpush('roguedungeonroom_kind', 'cistern')
self.redis.lpush('roguedungeonroom_kind', 'classroom')
self.redis.lpush('roguedungeonroom_kind', 'closet')
self.redis.lpush('roguedungeonroom_kind', 'collapsedroom')
self.redis.lpush('roguedungeonroom_kind', 'combatpit')
self.redis.lpush('roguedungeonroom_kind', 'commandroom')
self.redis.lpush('roguedungeonroom_kind', 'conjuringroom')
self.redis.lpush('roguedungeonroom_kind', 'courtroom')
self.redis.lpush('roguedungeonroom_kind', 'crypt')
self.redis.lpush('roguedungeonroom_kind', 'diningroom')
self.redis.lpush('roguedungeonroom_kind', 'divinationroom')
self.redis.lpush('roguedungeonroom_kind', 'dormitory')
self.redis.lpush('roguedungeonroom_kind', 'dressingroom')
self.redis.lpush('roguedungeonroom_kind', 'exerciseroom')
self.redis.lpush('roguedungeonroom_kind', 'forge')
self.redis.lpush('roguedungeonroom_kind', 'foyer')
self.redis.lpush('roguedungeonroom_kind', 'gallery')
self.redis.lpush('roguedungeonroom_kind', 'gameroom')
self.redis.lpush('roguedungeonroom_kind', 'grandhall')
self.redis.lpush('roguedungeonroom_kind', 'greathall')
self.redis.lpush('roguedungeonroom_kind', 'guardroom')
self.redis.lpush('roguedungeonroom_kind', 'hall')
self.redis.lpush('roguedungeonroom_kind', 'harem')
self.redis.lpush('roguedungeonroom_kind', 'kennel')
self.redis.lpush('roguedungeonroom_kind', 'kitchen')
self.redis.lpush('roguedungeonroom_kind', 'laboratory')
self.redis.lpush('roguedungeonroom_kind', 'lair')
self.redis.lpush('roguedungeonroom_kind', 'larder')
self.redis.lpush('roguedungeonroom_kind', 'library')
self.redis.lpush('roguedungeonroom_kind', 'lounge')
self.redis.lpush('roguedungeonroom_kind', 'maproom')
self.redis.lpush('roguedungeonroom_kind', 'meditationchamber')
self.redis.lpush('roguedungeonroom_kind', 'mine')
self.redis.lpush('roguedungeonroom_kind', 'monster')
self.redis.lpush('roguedungeonroom_kind', 'museum')
self.redis.lpush('roguedungeonroom_kind', 'naturalroom')
self.redis.lpush('roguedungeonroom_kind', 'observatory')
self.redis.lpush('roguedungeonroom_kind', 'office')
self.redis.lpush('roguedungeonroom_kind', 'pantry')
self.redis.lpush('roguedungeonroom_kind', 'personalroom')
self.redis.lpush('roguedungeonroom_kind', 'pool')
self.redis.lpush('roguedungeonroom_kind', 'prayer')
self.redis.lpush('roguedungeonroom_kind', 'prison')
self.redis.lpush('roguedungeonroom_kind', 'prisoncell')
self.redis.lpush('roguedungeonroom_kind', 'privy')
self.redis.lpush('roguedungeonroom_kind', 'receptionroom')
self.redis.lpush('roguedungeonroom_kind', 'refectory')
self.redis.lpush('roguedungeonroom_kind', 'riftbridgeroom')
self.redis.lpush('roguedungeonroom_kind', 'robingroom')
self.redis.lpush('roguedungeonroom_kind', 'salon')
self.redis.lpush('roguedungeonroom_kind', 'secretroom')
self.redis.lpush('roguedungeonroom_kind', 'sentrypost')
self.redis.lpush('roguedungeonroom_kind', 'shrine')
self.redis.lpush('roguedungeonroom_kind', 'sittingroom')
self.redis.lpush('roguedungeonroom_kind', 'smithy')
self.redis.lpush('roguedungeonroom_kind', 'solarium')
self.redis.lpush('roguedungeonroom_kind', 'stable')
self.redis.lpush('roguedungeonroom_kind', 'statue')
self.redis.lpush('roguedungeonroom_kind', 'stockade')
self.redis.lpush('roguedungeonroom_kind', 'storageroom')
self.redis.lpush('roguedungeonroom_kind', 'storeroom')
self.redis.lpush('roguedungeonroom_kind', 'study')
self.redis.lpush('roguedungeonroom_kind', 'summoning')
self.redis.lpush('roguedungeonroom_kind', 'temple')
self.redis.lpush('roguedungeonroom_kind', 'throneroom')
self.redis.lpush('roguedungeonroom_kind', 'toilet')
self.redis.lpush('roguedungeonroom_kind', 'tomb')
self.redis.lpush('roguedungeonroom_kind', 'torturechamber')
self.redis.lpush('roguedungeonroom_kind', 'trainingroom')
self.redis.lpush('roguedungeonroom_kind', 'trappedroom')
self.redis.lpush('roguedungeonroom_kind', 'trashroom')
self.redis.lpush('roguedungeonroom_kind', 'treasureroom')
self.redis.lpush('roguedungeonroom_kind', 'trophyroom')
self.redis.lpush('roguedungeonroom_kind', 'vault')
self.redis.lpush('roguedungeonroom_kind', 'verticalcavern')
self.redis.lpush('roguedungeonroom_kind', 'waitingroom')
self.redis.lpush('roguedungeonroom_kind', 'warroom')
self.redis.lpush('roguedungeonroom_kind', 'well')
self.redis.lpush('roguedungeonroom_kind', 'workpit')
self.redis.lpush('roguedungeonroom_kind', 'workroom')
self.redis.lpush('roguedungeonroom_kind', 'workshop')




HSET roguedungeonroom_kind_description abandoned         { "name":"abandoned",          "description":""   }
HSET roguedungeonroom_kind_description animalpen         { "name":"animal pen",         "description":""   }
HSET roguedungeonroom_kind_description antechamber       { "name":"antechamber",        "description":""   }
HSET roguedungeonroom_kind_description armory            { "name":"armory",             "description":""   }
HSET roguedungeonroom_kind_description arsenal           { "name":"arsenal",            "description":""   }
HSET roguedungeonroom_kind_description assemblage        { "name":"assemblage",         "description":""   }
HSET roguedungeonroom_kind_description audiencechamber   { "name":"audience chamber",   "description":""   }
HSET roguedungeonroom_kind_description audiencehall      { "name":"audience hall",      "description":""   }
HSET roguedungeonroom_kind_description aviary            { "name":"aviary",             "description":""   }
HSET roguedungeonroom_kind_description banquethall       { "name":"banquet hall",       "description":""   }
HSET roguedungeonroom_kind_description barracks          { "name":"barracks",           "description":""   }
HSET roguedungeonroom_kind_description bath              { "name":"bath",               "description":""   }
HSET roguedungeonroom_kind_description bedroom           { "name":"bedroom",            "description":""   }
HSET roguedungeonroom_kind_description bestiary          { "name":"bestiary",           "description":""   }
HSET roguedungeonroom_kind_description chantry           { "name":"chantry",            "description":""   }
HSET roguedungeonroom_kind_description chapel            { "name":"chapel",             "description":""   }
HSET roguedungeonroom_kind_description cistern           { "name":"cistern",            "description":""   }
HSET roguedungeonroom_kind_description classroom         { "name":"classroom",          "description":""   }
HSET roguedungeonroom_kind_description closet            { "name":"closet",             "description":""   }
HSET roguedungeonroom_kind_description collapsedroom     { "name":"collapsed room",     "description":""   }
HSET roguedungeonroom_kind_description combatpit         { "name":"combat pit",         "description":""   }
HSET roguedungeonroom_kind_description commandroom       { "name":"command room",       "description":""   }
HSET roguedungeonroom_kind_description conjuringroom     { "name":"conjuring room",     "description":""   }
HSET roguedungeonroom_kind_description courtroom         { "name":"courtroom",          "description":""   }
HSET roguedungeonroom_kind_description crypt             { "name":"crypt",              "description":""   }
HSET roguedungeonroom_kind_description diningroom        { "name":"diningroom",         "description":""   }
HSET roguedungeonroom_kind_description divinationroom    { "name":"divination room",    "description":""   }
HSET roguedungeonroom_kind_description dormitory         { "name":"dormitory",          "description":""   }
HSET roguedungeonroom_kind_description dressingroom      { "name":"dressing room",      "description":""   }
HSET roguedungeonroom_kind_description exerciseroom      { "name":"exercise room",      "description":""   }
HSET roguedungeonroom_kind_description forge             { "name":"forge",              "description":""   }
HSET roguedungeonroom_kind_description foyer             { "name":"foyer",              "description":""   }
HSET roguedungeonroom_kind_description gallery           { "name":"gallery",            "description":""   }
HSET roguedungeonroom_kind_description gameroom          { "name":"game room",          "description":""   }
HSET roguedungeonroom_kind_description grandhall         { "name":"grandhall",          "description":""   }
HSET roguedungeonroom_kind_description greathall         { "name":"greathall",          "description":""   }
HSET roguedungeonroom_kind_description guardroom         { "name":"guard room",         "description":""   }
HSET roguedungeonroom_kind_description hall              { "name":"hall",               "description":""   }
HSET roguedungeonroom_kind_description harem             { "name":"harem",              "description":""   }
HSET roguedungeonroom_kind_description kennel            { "name":"kennel",             "description":""   }
HSET roguedungeonroom_kind_description kitchen           { "name":"kitchen",            "description":""   }
HSET roguedungeonroom_kind_description laboratory        { "name":"laboratory",         "description":""   }
HSET roguedungeonroom_kind_description lair              { "name":"lair",               "description":""   }
HSET roguedungeonroom_kind_description larder            { "name":"larder",             "description":""   }
HSET roguedungeonroom_kind_description library           { "name":"library",            "description":""   }
HSET roguedungeonroom_kind_description lounge            { "name":"lounge",             "description":""   }
HSET roguedungeonroom_kind_description maproom           { "name":"map room",           "description":""   }
HSET roguedungeonroom_kind_description meditationchamber { "name":"meditation chamber", "description":""   }
HSET roguedungeonroom_kind_description mine              { "name":"mine",               "description":""   }
HSET roguedungeonroom_kind_description monster           { "name":"monster",            "description":""   }
HSET roguedungeonroom_kind_description museum            { "name":"museum",             "description":""   }
HSET roguedungeonroom_kind_description naturalroom       { "name":"natural room",       "description":""   }
HSET roguedungeonroom_kind_description observatory       { "name":"observatory",        "description":""   }
HSET roguedungeonroom_kind_description office            { "name":"office",             "description":""   }
HSET roguedungeonroom_kind_description pantry            { "name":"pantry",             "description":""   }
HSET roguedungeonroom_kind_description personalroom      { "name":"personal room",      "description":""   }
HSET roguedungeonroom_kind_description pool              { "name":"pool",               "description":""   }
HSET roguedungeonroom_kind_description prayer            { "name":"prayer",             "description":""   }
HSET roguedungeonroom_kind_description prison            { "name":"prison",             "description":""   }
HSET roguedungeonroom_kind_description prisoncell        { "name":"prison cell",        "description":""   }
HSET roguedungeonroom_kind_description privy             { "name":"privy",              "description":""   }
HSET roguedungeonroom_kind_description receptionroom     { "name":"reception room",     "description":""   }
HSET roguedungeonroom_kind_description refectory         { "name":"refectory",          "description":""   }
HSET roguedungeonroom_kind_description riftbridgeroom    { "name":"rift/bridge room",   "description":""   }
HSET roguedungeonroom_kind_description robingroom        { "name":"robing room",        "description":""   }
HSET roguedungeonroom_kind_description salon             { "name":"salon",              "description":""   }
HSET roguedungeonroom_kind_description secretroom        { "name":"secret room",        "description":""   }
HSET roguedungeonroom_kind_description sentrypost        { "name":"sentry post",        "description":""   }
HSET roguedungeonroom_kind_description shrine            { "name":"shrine",             "description":""   }
HSET roguedungeonroom_kind_description sittingroom       { "name":"sitting room",       "description":""   }
HSET roguedungeonroom_kind_description smithy            { "name":"smithy",             "description":""   }
HSET roguedungeonroom_kind_description solarium          { "name":"solarium",           "description":""   }
HSET roguedungeonroom_kind_description stable            { "name":"stable",             "description":""   }
HSET roguedungeonroom_kind_description statue            { "name":"statue",             "description":""   }
HSET roguedungeonroom_kind_description stockade          { "name":"stockade",           "description":""   }
HSET roguedungeonroom_kind_description storageroom       { "name":"storage room",       "description":""   }
HSET roguedungeonroom_kind_description storeroom         { "name":"store room",         "description":""   }
HSET roguedungeonroom_kind_description strongroom        { "name":"strong room",        "description":""   }
HSET roguedungeonroom_kind_description study             { "name":"study",              "description":""   }
HSET roguedungeonroom_kind_description summoning         { "name":"summoning",          "description":""   }
HSET roguedungeonroom_kind_description temple            { "name":"temple",             "description":""   }
HSET roguedungeonroom_kind_description throneroom        { "name":"throne room",        "description":""   }
HSET roguedungeonroom_kind_description toilet            { "name":"toilet",             "description":""   }
HSET roguedungeonroom_kind_description tomb              { "name":"tomb",               "description":""   }
HSET roguedungeonroom_kind_description torturechamber    { "name":"torture chamber",    "description":""   }
HSET roguedungeonroom_kind_description trainingroom      { "name":"training room",      "description":""   }
HSET roguedungeonroom_kind_description trappedroom       { "name":"trapped room",       "description":""   }
HSET roguedungeonroom_kind_description trashroom         { "name":"trash room",         "description":""   }
HSET roguedungeonroom_kind_description treasureroom      { "name":"treasure room",      "description":""   }
HSET roguedungeonroom_kind_description trophyroom        { "name":"trophy room",        "description":""   }
HSET roguedungeonroom_kind_description vault             { "name":"vault",              "description":""   }
HSET roguedungeonroom_kind_description verticalcavern    { "name":"vertical cavern",    "description":""   }
HSET roguedungeonroom_kind_description waitingroom       { "name":"waiting room",       "description":""   }
HSET roguedungeonroom_kind_description warroom           { "name":"war room",           "description":""   }
HSET roguedungeonroom_kind_description well              { "name":"well",               "description":""   }
HSET roguedungeonroom_kind_description workpit           { "name":"work pit",           "description":""   }
HSET roguedungeonroom_kind_description workroom          { "name":"work room",          "description":""   }
HSET roguedungeonroom_kind_description workshop          { "name":"workshop",           "description":""   }


