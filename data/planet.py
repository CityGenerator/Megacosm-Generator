# Planet details

self.redis.zadd('planet_size', '{"name":"tiny",      "multiplier":0.4,  "score":5   } ', '5')
self.redis.zadd('planet_size', '{"name":"small",     "multiplier":0.7,  "score":10   } ', '10')
self.redis.zadd('planet_size', '{"name":"average",   "multiplier":1.0,  "score":65   } ', '65')
self.redis.zadd('planet_size', '{"name":"large",     "multiplier":1.5,  "score":85   } ', '85')
self.redis.zadd('planet_size', '{"name":"massive",  "multiplier":2.0,  "score":100   } ', '100')

self.redis.zadd('planet_temp', '{"name":"unbearably cold", "multiplier":0.5,  "score":5   } ', '5')
self.redis.zadd('planet_temp', '{"name":"freezing",        "multiplier":0.6,  "score":10   } ', '10')
self.redis.zadd('planet_temp', '{"name":"cold",            "multiplier":0.7,  "score":15   } ', '15')
self.redis.zadd('planet_temp', '{"name":"cool",            "multiplier":0.8,  "score":20   } ', '20')
self.redis.zadd('planet_temp', '{"name":"mild",            "multiplier":0.9,  "score":30   } ', '30')
self.redis.zadd('planet_temp', '{"name":"ideal",           "multiplier":1.0,  "score":70   } ', '70')
self.redis.zadd('planet_temp', '{"name":"pleasant",        "multiplier":1.1,  "score":80   } ', '80')
self.redis.zadd('planet_temp', '{"name":"warm",            "multiplier":1.2,  "score":85   } ', '85')
self.redis.zadd('planet_temp', '{"name":"hot",             "multiplier":1.3,  "score":90   } ', '90')
self.redis.zadd('planet_temp', '{"name":"sweltering",      "multiplier":1.4,  "score":95   } ', '95')
self.redis.zadd('planet_temp', '{"name":"unbearably hot",  "multiplier":1.5,  "score":100   } ', '100')
                              
self.redis.zadd('planet_atmosphere', '{"name":"thin",     "opacity":0.01,  "score":5   } ', '5')
self.redis.zadd('planet_atmosphere', '{"name":"meager",   "opacity":0.10,  "score":10   } ', '10')
self.redis.zadd('planet_atmosphere', '{"name":"slight",   "opacity":0.30,  "score":25   } ', '25')
self.redis.zadd('planet_atmosphere', '{"name":"average",  "opacity":0.50,  "score":75   } ', '75')
self.redis.zadd('planet_atmosphere', '{"name":"thick",    "opacity":0.70,  "score":85   } ', '85')
self.redis.zadd('planet_atmosphere', '{"name":"heavy",    "opacity":0.90,  "score":95   } ', '95')
self.redis.zadd('planet_atmosphere', '{"name":"dense",    "opacity":0.99,  "score":100   } ', '100')


self.redis.zadd('planet_wind', '{"name":"dead",         "multiplier":0.5,  "score":5   } ', '5')
self.redis.zadd('planet_wind', '{"name":"soft",         "multiplier":0.7,  "score":10   } ', '10')
self.redis.zadd('planet_wind', '{"name":"slight",       "multiplier":0.9,  "score":25   } ', '25')
self.redis.zadd('planet_wind', '{"name":"breezy",       "multiplier":1.0,  "score":75   } ', '75')
self.redis.zadd('planet_wind', '{"name":"gusty",        "multiplier":1.1,  "score":85   } ', '85')
self.redis.zadd('planet_wind', '{"name":"heavy",        "multiplier":1.3,  "score":95   } ', '95')
self.redis.zadd('planet_wind', '{"name":"overwhelming", "multiplier":1.5,  "score":100   } ', '100')

self.redis.zadd('planet_day', '{"name":"short",       "minhour":10,     "maxhour":15 ,  "score":5   } ', '5')
self.redis.zadd('planet_day', '{"name":"swift",       "minhour":16,     "maxhour":20 ,  "score":10   } ', '10')
self.redis.zadd('planet_day', '{"name":"average",     "minhour":21,     "maxhour":40 ,  "score":90   } ', '90')
self.redis.zadd('planet_day', '{"name":"slow",        "minhour":40,     "maxhour":50 ,  "score":95   } ', '95')
self.redis.zadd('planet_day', '{"name":"long",        "minhour":51,     "maxhour":100,  "score":100   } ', '100')

self.redis.zadd('planet_year', '{"name":"short"    ,  "score":5   } ', '5')
self.redis.zadd('planet_year', '{"name":"swift"    ,  "score":10   } ', '10')
self.redis.zadd('planet_year', '{"name":"average"  ,  "score":90   } ', '90')
self.redis.zadd('planet_year', '{"name":"slow"     ,  "score":95   } ', '95')
self.redis.zadd('planet_year', '{"name":"long"     ,  "score":100   } ', '100')

self.redis.zadd('planet_civilization', '{"name":"crude"       ,  "score":5   } ', '5')
self.redis.zadd('planet_civilization', '{"name":"scattered"   ,  "score":10   } ', '10')
self.redis.zadd('planet_civilization', '{"name":"moderate"    ,  "score":90   } ', '90')
self.redis.zadd('planet_civilization', '{"name":"prosperous"  ,  "score":95   } ', '95')
self.redis.zadd('planet_civilization', '{"name":"thriving"    ,  "score":100   } ', '100')

self.redis.zadd('planet_precipitation', '{"name":"scarce",    "multiplier":0.5 ,  "score":10   } ', '10')
self.redis.zadd('planet_precipitation', '{"name":"rare",      "multiplier":0.8 ,  "score":30   } ', '30')
self.redis.zadd('planet_precipitation', '{"name":"common",    "multiplier":0.9 ,  "score":55   } ', '55')
self.redis.zadd('planet_precipitation', '{"name":"plentiful", "multiplier":1.1 ,  "score":85   } ', '85')
self.redis.zadd('planet_precipitation', '{"name":"abundant",  "multiplier":1.2 ,  "score":95   } ', '95')
self.redis.zadd('planet_precipitation', '{"name":"excessive", "multiplier":1.5 ,  "score":100   } ', '100')

# Details for moons.

self.redis.zadd('planet_mooncount', '{"name":"no moons",         "count":0,  "score":10   } ', '10')
self.redis.zadd('planet_mooncount', '{"name":"single moon",      "count":1,  "score":70   } ', '70')
self.redis.zadd('planet_mooncount', '{"name":"double moon",      "count":2,  "score":95   } ', '95')
self.redis.zadd('planet_mooncount', '{"name":"triple moon",      "count":3,  "score":97   } ', '97')
self.redis.zadd('planet_mooncount', '{"name":"quadruple moon",   "count":4,  "score":100   } ', '100')


# Most of this planet appears to be in the Stone Age, which is known for 
self.redis.zadd('planet_technology', '{"name":"Stone Age",        "description":"implements made of stone",          "score":5   } ', '5')
self.redis.zadd('planet_technology', '{"name":"Bronze Age",       "description":"implements of copper and bronze",    "score":10   } ', '10')
self.redis.zadd('planet_technology', '{"name":"Iron Age",         "description":"implements of iron and steel",       "score":15   } ', '15')
self.redis.zadd('planet_technology', '{"name":"Ancient Age",      "description":"advances in engineering",            "score":20   } ', '20')
self.redis.zadd('planet_technology', '{"name":"Middle Age",       "description":"advances in weaponry",               "score":90   } ', '90')
self.redis.zadd('planet_technology', '{"name":"Modern Age",       "description":"advances in science",                "score":95   } ', '95')
self.redis.zadd('planet_technology', '{"name":"Contemporary Age", "description":"being similar to our own",           "score":100   } ', '100')




#    <atmosphere reason_chance=\'50\' > <!-- The sky is _________[, partially due to ______ high in the atmosphere].-->
#        <option          max="40" color="blue">
#            <reason>water vapor</reason>
#        </option>
#        <option min="41" max="45" color="white">
#            <reason>clouds</reason>
#            <reason>pollution</reason>
#        </option>
#        <option min="46" max="50" color="gray">
#            <reason>clouds</reason>
#            <reason>pollution</reason>
#        </option>
#        <option min="51" max="55" color="brown">
#            <reason>pollution</reason>
#            <reason>noxious fumes</reason>
#            <reason>dust</reason>
#        </option>
#        <option min="56" max="60" color="red">
#            <reason>noxious fumes</reason>
#            <reason>dust</reason>
#        </option>
#        <option min="61" max="65" color="pink">
#            <reason>noxious fumes</reason>
#            <reason>dust</reason>
#        </option>
#        <option min="66" max="70" color="green">
#            <reason>noxious fumes</reason>
#            <reason>airborn plankton</reason>
#        </option>
#        <option min="71" max="75" color="yellow">
#            <reason>pollution</reason>
#            <reason>noxious fumes</reason>
#            <reason>dust</reason>
#        </option>
#        <option min="76" max="80" color="beige">
#            <reason>pollution</reason>
#            <reason>noxious fumes</reason>
#            <reason>dust</reason>
#        </option>
#        <option min="81" max="85" color="orange">
#            <reason>pollution</reason>
#            <reason>dust</reason>
#        </option>
#        <option min="86" max="90" color="purple">
#        </option>
#        <option min="91"          color="murky">
#            <reason>clouds</reason>
#            <reason>pollution</reason>
#            <reason>noxious fumes</reason>
#            <reason>dust</reason>
#        </option>
#    </atmosphere>
#
#
#
#
#    <year>
#        <option          max="10"  minday="5"      maxday="10" />
#        <option min="11" max="20"  minday="11"     maxday="100" />
#        <option min="21" max="30"  minday="101"    maxday="200" />
#        <option min="31" max="60"  minday="201"    maxday="400" />
#        <option min="61" max="82"  minday="401"    maxday="600" />
#        <option min="81" max="92"  minday="601"    maxday="800" />
#        <option min="93" max="93"  minday="801"    maxday="1000" />
#        <option min="94" max="94"  minday="1001"   maxday="2000" />
#        <option min="95" max="95"  minday="2001"   maxday="10000" />
#        <option min="96" max="96"  minday="10001"  maxday="50000" />
#        <option min="97" max="97"  minday="50001"  maxday="100000" />
#        <option min="98" max="98"  minday="100001" maxday="300000" />
#        <option min="99" max="99"  minday="300001" maxday="700000" />
#    </year>
#
#    
#            
#    </surface>
#
#

#    <smallstorms>
#        <option          max="10" >scarce</option>
#        <option min="10" max="31" >rare</option>
#        <option min="30" max="55" >common</option>
#        <option min="65" max="85" >plentiful</option>
#        <option min="86" max="95" >abundant</option>
#        <option min="96"          >excessive</option>
#    </smallstorms>
#
#    <clouds>
#        <option          max="10" >scarce</option>
#        <option min="10" max="31" >rare</option>
#        <option min="30" max="55" >common</option>
#        <option min="65" max="85" >plentiful</option>
#        <option min="86" max="95" >abundant</option>
#        <option min="96"          >excessive</option>
#    </clouds>
#

