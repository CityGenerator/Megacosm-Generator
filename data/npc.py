#

ZADD npc_sex 51   {"name":"female",     "pronoun":"she", "possessive":"her", "third-person":"her", "spouse":"husband", "score":51   }
ZADD npc_sex 100  {"name":"male",       "pronoun":"he", "possessive":"his",  "third-person":"him", "spouse":"wife",    "score":100  }

# Bob is a[n] ________ follower of Grabesh.
ZADD npc_piety   5 {"name":"noncommittal",  "score":5     }
ZADD npc_piety  10 {"name":"dispassionate", "score":10    }
ZADD npc_piety  20 {"name":"insincere",     "score":20    }
ZADD npc_piety  30 {"name":"inattentive",   "score":30    }
ZADD npc_piety  40 {"name":"dutiful",       "score":40    }
ZADD npc_piety  50 {"name":"pious",         "score":50    }
ZADD npc_piety  60 {"name":"devoted",       "score":60    }
ZADD npc_piety  70 {"name":"reverent",      "score":70    }
ZADD npc_piety  80 {"name":"devout",        "score":80    }
ZADD npc_piety  90 {"name":"passionate",    "score":90    }
ZADD npc_piety 100 {"name":"overzealous",   "score":100   }

#Bob is a human 
ZADD npc_age 5    {"name":"juvenile",       "score":5   }
ZADD npc_age 10   {"name":"adolescent",     "score":10  }
ZADD npc_age 20   {"name":"young",          "score":20  }
ZADD npc_age 40   {"name":"adult",          "score":40  }
ZADD npc_age 80   {"name":"middle-aged",    "score":80  }
ZADD npc_age 95   {"name":"elderly",        "score":95  }
ZADD npc_age 100  {"name":"ancient",        "score":100 }

# friends consider bob ________
ZADD npc_honor 5    {"name":"treacherous",   "score":5   }
ZADD npc_honor 10   {"name":"untrustworthy", "score":10  }
ZADD npc_honor 15   {"name":"dishonorable",  "score":15  }
ZADD npc_honor 20   {"name":"devious",       "score":20  }
ZADD npc_honor 30   {"name":"dishonest",     "score":30  }
ZADD npc_honor 40   {"name":"inconsistent",  "score":40  }
ZADD npc_honor 50   {"name":"dependable",    "score":50  }
ZADD npc_honor 60   {"name":"reliable",      "score":60  }
ZADD npc_honor 70   {"name":"honest",        "score":70  }
ZADD npc_honor 80   {"name":"credible",      "score":80  }
ZADD npc_honor 85   {"name":"faithful",      "score":85  }
ZADD npc_honor 90   {"name":"loyal",         "score":90  }
ZADD npc_honor 95   {"name":"trustworthy",   "score":95  }
ZADD npc_honor 100  {"name":"honorable",     "score":100 }

# When provoked, bob is 
ZADD npc_bravery 5    {"name":"chicken-hearted",   "score":5  }
ZADD npc_bravery 10   {"name":"spineless",   "score":10  }
ZADD npc_bravery 15   {"name":"cowardly",   "score":15  }
ZADD npc_bravery 20   {"name":"craven",   "score":20  }
ZADD npc_bravery 30   {"name":"faint-hearted",   "score":30  }
ZADD npc_bravery 40   {"name":"panicky",   "score":40  }
ZADD npc_bravery 50   {"name":"nervous",   "score":50  }
ZADD npc_bravery 60   {"name":"tough",   "score":60  }
ZADD npc_bravery 70   {"name":"intrepid",   "score":70  }
ZADD npc_bravery 80   {"name":"fearless",   "score":80  }
ZADD npc_bravery 85   {"name":"bold",   "score":85  }
ZADD npc_bravery 90   {"name":"unafraid",   "score":90  }
ZADD npc_bravery 95   {"name":"brave",   "score":95  }
ZADD npc_bravery 100  {"name":"heroic",   "score":100  }

ZADD npc_skill 5   {"name":"incompetent",   "score":5  }
ZADD npc_skill 10  {"name":"ineptly skilled",   "score":10  }
ZADD npc_skill 30  {"name":"poorly skilled",   "score":30  }
ZADD npc_skill 40  {"name":"mediocrely skilled",   "score":40  }
ZADD npc_skill 50  {"name":"reasonably skilled",   "score":50  }
ZADD npc_skill 70  {"name":"decently skilled",   "score":70  }
ZADD npc_skill 80  {"name":"skilled",   "score":80  }
ZADD npc_skill 90  {"name":"gifted",   "score":90  }
ZADD npc_skill 98  {"name":"impressively skilled",   "score":98  }
ZADD npc_skill 100 {"name":"legendarily skilled",   "score":100  }

ZADD npc_experience 5    {"name":"new",   "score":5  }
ZADD npc_experience 10   {"name":"naive",   "score":10  }
ZADD npc_experience 15   {"name":"green",   "score":15  }
ZADD npc_experience 20   {"name":"amateur",   "score":20  }
ZADD npc_experience 25   {"name":"fledgling",   "score":25  }
ZADD npc_experience 30   {"name":"inexperienced",   "score":30  }
ZADD npc_experience 35   {"name":"rookie",   "score":35  }
ZADD npc_experience 40   {"name":"trained",   "score":40  }
ZADD npc_experience 45   {"name":"capable",   "score":45  }
ZADD npc_experience 50   {"name":"qualified",   "score":50  }
ZADD npc_experience 55   {"name":"proficient",   "score":55  }
ZADD npc_experience 60   {"name":"average",   "score":60  }
ZADD npc_experience 65   {"name":"effective",   "score":65  }
ZADD npc_experience 70   {"name":"accomplished",   "score":70  }
ZADD npc_experience 75   {"name":"gifted",   "score":75  }
ZADD npc_experience 80   {"name":"adept",   "score":80  }
ZADD npc_experience 85   {"name":"worldly",   "score":85  }
ZADD npc_experience 90   {"name":"expert",   "score":90  }
ZADD npc_experience 95   {"name":"veteran",   "score":95  }
ZADD npc_experience 100  {"name":"grizzled",   "score":100  }

ZADD npc_strength 10     {"name":"weak",   "score":10  }
ZADD npc_strength 20     {"name":"shaky",   "score":20  }
ZADD npc_strength 30     {"name":"delicate",   "score":30  }
ZADD npc_strength 40     {"name":"inactive",   "score":40  }
ZADD npc_strength 60     {"name":"able-bodied",   "score":60  }
ZADD npc_strength 70     {"name":"strong",   "score":70  }
ZADD npc_strength 80     {"name":"sinewy",   "score":80  }
ZADD npc_strength 90     {"name":"powerful",   "score":90  }
ZADD npc_strength 100    {"name":"herculean",   "score":100  }

ZADD npc_endurance 10    {"name":"exhausted",   "score":10  }
ZADD npc_endurance 20    {"name":"unenergetic",   "score":20  }
ZADD npc_endurance 30    {"name":"lazy",   "score":30  }
ZADD npc_endurance 40    {"name":"lethargic",   "score":40  }
ZADD npc_endurance 60    {"name":"resistant",   "score":60  }
ZADD npc_endurance 70    {"name":"vital",   "score":70  }
ZADD npc_endurance 80    {"name":"fortified",   "score":80  }
ZADD npc_endurance 90    {"name":"resolute",   "score":90  }
ZADD npc_endurance 100   {"name":"unflagging",   "score":100  }

# Looking at his past, bob is _____ of his choices in the past
ZADD npc_satisfaction 10     {"name":"rueful",   "score":10  }
ZADD npc_satisfaction 20     {"name":"regretful",   "score":20  }
ZADD npc_satisfaction 30     {"name":"apologetic",   "score":30  }
ZADD npc_satisfaction 40     {"name":"repentant",   "score":40  }
ZADD npc_satisfaction 50     {"name":"remorseful",   "score":50  }
ZADD npc_satisfaction 60     {"name":"questioning",   "score":60  }
ZADD npc_satisfaction 70     {"name":"unrepentant",   "score":70  }
ZADD npc_satisfaction 80     {"name":"unashamed",   "score":80  }
ZADD npc_satisfaction 90     {"name":"accepting",   "score":90  }
ZADD npc_satisfaction 100    {"name":"satisfied",   "score":100  }

ZADD npc_agility 30      {"name":"clumsy",   "score":30  }
ZADD npc_agility 60      {"name":"average",   "score":60  }
ZADD npc_agility 100     {"name":"agile",   "score":100  }

ZADD npc_wisdom 10       {"name":"foolish",   "score":10  }
ZADD npc_wisdom 20       {"name":"obtuse",   "score":20  }
ZADD npc_wisdom 30       {"name":"careless",   "score":30  }
ZADD npc_wisdom 40       {"name":"indiscreet",   "score":40  }
ZADD npc_wisdom 50       {"name":"average",   "score":50  }
ZADD npc_wisdom 60       {"name":"keen",   "score":60  }
ZADD npc_wisdom 70       {"name":"astute",   "score":70  }
ZADD npc_wisdom 80       {"name":"thoughtful",   "score":80  }
ZADD npc_wisdom 90       {"name":"enlightened",   "score":90  }
ZADD npc_wisdom 100      {"name":"wise",   "score":100  }

ZADD npc_charisma 30     {"name":"obnoxious",   "score":30  }
ZADD npc_charisma 50     {"name":"off-putting",   "score":50  }
ZADD npc_charisma 60     {"name":"average",   "score":60  }
ZADD npc_charisma 80     {"name":"charming",   "score":80  }
ZADD npc_charisma 100    {"name":"inspiring",   "score":100  }

ZADD npc_intelligence 20    {"name":"dumb",   "score":20  }
ZADD npc_intelligence 40    {"name":"dimwitted",   "score":40  }
ZADD npc_intelligence 60    {"name":"average",   "score":60  }
ZADD npc_intelligence 80    {"name":"clever",   "score":80  }
ZADD npc_intelligence 100   {"name":"brilliant",   "score":100  }

# Strangers take one look and consider Sydney _________
ZADD npc_attractiveness   5 {"name":"hideous",      "score":5   }
ZADD npc_attractiveness  10 {"name":"repulsive",    "score":10  }
ZADD npc_attractiveness  20 {"name":"repellent",    "score":20  }
ZADD npc_attractiveness  30 {"name":"ugly",         "score":30  }
ZADD npc_attractiveness  40 {"name":"unattractive", "score":40  }
ZADD npc_attractiveness  50 {"name":"homely",       "score":50  }
ZADD npc_attractiveness  60 {"name":"average",      "score":60  }
ZADD npc_attractiveness  70 {"name":"cute",         "score":70  }
ZADD npc_attractiveness  80 {"name":"attractive",   "score":80  }
ZADD npc_attractiveness  90 {"name":"good-looking", "score":90  }
ZADD npc_attractiveness  95 {"name":"gorgeous",     "score":95  }
ZADD npc_attractiveness 100 {"name":"stunning",     "score":100 }
        
#Bob is ____________
ZADD npc_money 5    {"name":"destitute",        "score":5   }
ZADD npc_money 20   {"name":"poor",             "score":20  }
ZADD npc_money 40   {"name":"barely getting by","score":40  }
ZADD npc_money 80   {"name":"making ends meet", "score":80  }
ZADD npc_money 95   {"name":"well off",         "score":95  }
ZADD npc_money 100  {"name":"rich",             "score":100 }

# and is ________ with what he owns.
ZADD npc_generous  50  {"name":"stingy",        "score":50  }
ZADD npc_generous 100  {"name":"generous",     "score":100 }


#Many people would consider bob ___________
ZADD npc_luck 50   {"name":"unlucky",        "score":50  }
ZADD npc_luck 100  {"name":"lucky",          "score":100 }

#and  ____________ confident.
ZADD npc_confident 30   {"name":"not very",       "score":30  }
ZADD npc_confident 60   {"name":"somewhat",       "score":60  }
ZADD npc_confident 100  {"name":"incredibly",     "score":100 }


        
self.redis.lpush('npc_posessiondetail', 'was lost during the war')
self.redis.lpush('npc_posessiondetail', 'was stolen weeks ago')
self.redis.lpush('npc_posessiondetail', 'has great personal significance')
self.redis.lpush('npc_posessiondetail', 'was a gift from someone close')
self.redis.lpush('npc_posessiondetail', 'is always kept close')
self.redis.lpush('npc_posessiondetail', 'is kept safe at all times')
self.redis.lpush('npc_posessiondetail', 'was stolen from someone else')
self.redis.lpush('npc_posessiondetail', 'was hidden away')
self.redis.lpush('npc_posessiondetail', 'was a gift ')
self.redis.lpush('npc_posessiondetail', 'was a gift from a parent')
self.redis.lpush('npc_posessiondetail', 'was a gift from a mentor')
self.redis.lpush('npc_posessiondetail', 'was a gift from a lover')
self.redis.lpush('npc_posessiondetail', 'was a gift from a friend')
self.redis.lpush('npc_posessiondetail', 'was found on the ground recently')
self.redis.lpush('npc_posessiondetail', 'was found on the ground years ago')
self.redis.lpush('npc_posessiondetail', 'was found in a tavern months ago')
        
self.redis.lpush('npc_posession', 'jackknife')
self.redis.lpush('npc_posession', 'small trinket')
self.redis.lpush('npc_posession', 'bouncyball')
self.redis.lpush('npc_posession', 'lucky coin')
self.redis.lpush('npc_posession', 'ancestral weapon')
self.redis.lpush('npc_posession', 'family ring')
self.redis.lpush('npc_posession', 'ballbearing')
self.redis.lpush('npc_posession', 'small gem')
self.redis.lpush('npc_posession', 'whistle')
self.redis.lpush('npc_posession', 'throwing knife')
self.redis.lpush('npc_posession', 'flask')
self.redis.lpush('npc_posession', 'small flute')
self.redis.lpush('npc_posession', 'necklace')
self.redis.lpush('npc_posession', 'locket')
self.redis.lpush('npc_posession', 'yoyo')
self.redis.lpush('npc_posession', 'scarf')
self.redis.lpush('npc_posession', 'arrowhead')
self.redis.lpush('npc_posession', 'map')
self.redis.lpush('npc_posession', 'deck of cards')
self.redis.lpush('npc_posession', 'dagger')
self.redis.lpush('npc_posession', 'horn')
self.redis.lpush('npc_posession', 'horseshoe')
self.redis.lpush('npc_posession', 'kaleidoscope')
self.redis.lpush('npc_posession', 'holy symbol')
self.redis.lpush('npc_posession', 'broken sword hilt')
self.redis.lpush('npc_posession', 'lock of hair')

#If approached, bob will be
self.redis.lpush('npc_attitude', 'accusatory')
self.redis.lpush('npc_attitude', 'apologetic')
self.redis.lpush('npc_attitude', 'attentive')
self.redis.lpush('npc_attitude', 'authoritarian')
self.redis.lpush('npc_attitude', 'battle-ready')
self.redis.lpush('npc_attitude', 'belligerent')
self.redis.lpush('npc_attitude', 'boastful')
self.redis.lpush('npc_attitude', 'cautious')
self.redis.lpush('npc_attitude', 'chatty')
self.redis.lpush('npc_attitude', 'clumsy')
self.redis.lpush('npc_attitude', 'conspiratorial')
self.redis.lpush('npc_attitude', 'contrarian')
self.redis.lpush('npc_attitude', 'crude')
self.redis.lpush('npc_attitude', 'conniving')
self.redis.lpush('npc_attitude', 'cowed')
self.redis.lpush('npc_attitude', 'deluded')
self.redis.lpush('npc_attitude', 'drunken')
self.redis.lpush('npc_attitude', 'easily offended')
self.redis.lpush('npc_attitude', 'efficient')
self.redis.lpush('npc_attitude', 'egotistical')
self.redis.lpush('npc_attitude', 'embittered')
self.redis.lpush('npc_attitude', 'exhausted')
self.redis.lpush('npc_attitude', 'fashion conscious')
self.redis.lpush('npc_attitude', 'fatalistic')
self.redis.lpush('npc_attitude', 'flirtatious')
self.redis.lpush('npc_attitude', 'forbidding')
self.redis.lpush('npc_attitude', 'forgetful')
self.redis.lpush('npc_attitude', 'giddy')
self.redis.lpush('npc_attitude', 'gluttonous')
self.redis.lpush('npc_attitude', 'gossipy')
self.redis.lpush('npc_attitude', 'greedy')
self.redis.lpush('npc_attitude', 'grieving')
self.redis.lpush('npc_attitude', 'guarded')
self.redis.lpush('npc_attitude', 'guilty')
self.redis.lpush('npc_attitude', 'healthy')
self.redis.lpush('npc_attitude', 'helpful')
self.redis.lpush('npc_attitude', 'homesick')
self.redis.lpush('npc_attitude', 'idealistic')
self.redis.lpush('npc_attitude', 'impatient')
self.redis.lpush('npc_attitude', 'insecure')
self.redis.lpush('npc_attitude', 'intimidating')
self.redis.lpush('npc_attitude', 'intimidated')
self.redis.lpush('npc_attitude', 'jaded')
self.redis.lpush('npc_attitude', 'jesterly')
self.redis.lpush('npc_attitude', 'jolly')
self.redis.lpush('npc_attitude', 'lonely')
self.redis.lpush('npc_attitude', 'loud')
self.redis.lpush('npc_attitude', 'lovelorn')
self.redis.lpush('npc_attitude', 'melancholy')
self.redis.lpush('npc_attitude', 'mocking')
self.redis.lpush('npc_attitude', 'mopey')
self.redis.lpush('npc_attitude', 'nervous')
self.redis.lpush('npc_attitude', 'nihilistic')
self.redis.lpush('npc_attitude', 'nosy')
self.redis.lpush('npc_attitude', 'outlandish')
self.redis.lpush('npc_attitude', 'pacifistic')
self.redis.lpush('npc_attitude', 'patriotic')
self.redis.lpush('npc_attitude', 'patronizing')
self.redis.lpush('npc_attitude', 'pious')
self.redis.lpush('npc_attitude', 'prejudiced')
self.redis.lpush('npc_attitude', 'quiet')
self.redis.lpush('npc_attitude', 'resentful')
self.redis.lpush('npc_attitude', 'scattered')
self.redis.lpush('npc_attitude', 'self-obsessed')
self.redis.lpush('npc_attitude', 'shifty')
self.redis.lpush('npc_attitude', 'sickly')
self.redis.lpush('npc_attitude', 'skeptical')
self.redis.lpush('npc_attitude', 'smitten')
self.redis.lpush('npc_attitude', 'smug')
self.redis.lpush('npc_attitude', 'solemn')
self.redis.lpush('npc_attitude', 'spiteful')
self.redis.lpush('npc_attitude', 'territorial')
self.redis.lpush('npc_attitude', 'thick')
self.redis.lpush('npc_attitude', 'treasure-obsessed')
self.redis.lpush('npc_attitude', 'trusting')
self.redis.lpush('npc_attitude', 'unreliable')
self.redis.lpush('npc_attitude', 'vengeful')
self.redis.lpush('npc_attitude', 'violent')
self.redis.lpush('npc_attitude', 'gambling')
self.redis.lpush('npc_attitude', 'worrying')
self.redis.lpush('npc_attitude', 'xenophobic')
        
self.redis.lpush('npc_regret', 'was unable to save a loved one')
self.redis.lpush('npc_regret', 'didn\'t lie to protect a close friend')
self.redis.lpush('npc_regret', 'accidentally killed an innocent person')
self.redis.lpush('npc_regret', 'seriously injured a friend goofing around')
self.redis.lpush('npc_regret', 'ran away from home long ago')
self.redis.lpush('npc_regret', 'scared a child')
        
self.redis.lpush('npc_height', 'short')
self.redis.lpush('npc_height', 'average height')
self.redis.lpush('npc_height', 'tall')
        
self.redis.lpush('npc_build', 'frail')
self.redis.lpush('npc_build', 'thin')
self.redis.lpush('npc_build', 'skinny')
self.redis.lpush('npc_build', 'chubby')
self.redis.lpush('npc_build', 'stocky')
self.redis.lpush('npc_build', 'obese')

SET   npc_mark_chance 20
        
self.redis.lpush('npc_mark', 'mole')
self.redis.lpush('npc_mark', 'freckle')
self.redis.lpush('npc_mark', 'blemish')
self.redis.lpush('npc_mark', 'small scar')
self.redis.lpush('npc_mark', 'large scar')
self.redis.lpush('npc_mark', 'birth mark')
self.redis.lpush('npc_mark', 'tattoo')
self.redis.lpush('npc_mark', 'deformity')
        
self.redis.lpush('npc_mark_location', 'face')
self.redis.lpush('npc_mark_location', 'head')
self.redis.lpush('npc_mark_location', 'leg')
self.redis.lpush('npc_mark_location', 'arm')
self.redis.lpush('npc_mark_location', 'hand')
self.redis.lpush('npc_mark_location', 'shoulder')
self.redis.lpush('npc_mark_location', 'chest')
self.redis.lpush('npc_mark_location', 'throat')
        
self.redis.lpush('npc_complexion', 'fair')
self.redis.lpush('npc_complexion', 'flushed')
self.redis.lpush('npc_complexion', 'jaundiced')
self.redis.lpush('npc_complexion', 'florid')
self.redis.lpush('npc_complexion', 'dull')
self.redis.lpush('npc_complexion', 'sallow')
self.redis.lpush('npc_complexion', 'radiant')
self.redis.lpush('npc_complexion', 'pallid')
self.redis.lpush('npc_complexion', 'tanned')
self.redis.lpush('npc_complexion', 'flawless')
self.redis.lpush('npc_complexion', 'light')
self.redis.lpush('npc_complexion', 'dark')
self.redis.lpush('npc_complexion', 'muddled')
        
self.redis.lpush('npc_eye', 'beady')
self.redis.lpush('npc_eye', 'light')
self.redis.lpush('npc_eye', 'dark')
self.redis.lpush('npc_eye', 'clear')
self.redis.lpush('npc_eye', 'bloodshot')
self.redis.lpush('npc_eye', 'cross-eyed')
self.redis.lpush('npc_eye', 'deep-set')
self.redis.lpush('npc_eye', 'close-set')
self.redis.lpush('npc_eye', 'heavy')
self.redis.lpush('npc_eye', 'hollow')
self.redis.lpush('npc_eye', 'piggish')
self.redis.lpush('npc_eye', 'sunken')
self.redis.lpush('npc_eye', 'brooding')
self.redis.lpush('npc_eye', 'glazed')
self.redis.lpush('npc_eye', 'haunted')

# Bobbette is  _________
self.redis.lpush('npc_marriagestatus', 'engaged')
self.redis.lpush('npc_marriagestatus', 'married')
self.redis.lpush('npc_marriagestatus', 'divorced')
self.redis.lpush('npc_marriagestatus', 'widowed')

# Bob has 
ZADD npc_kill 40    {"name":"never killed",                     "score":20  }
ZADD npc_kill 80    {"name":"killed in self defense",           "score":40  }
ZADD npc_kill 90    {"name":"killed in the heat of the moment", "score":60  }
ZADD npc_kill 95    {"name":"killed to solve a problem",        "score":80  }
ZADD npc_kill 100   {"name":"killed without issue",             "score":100  }

# Bob suffers from
SET   npc_medical_condition_chance 10
self.redis.lpush('npc_medical_condition', 'blindness in one eye')
self.redis.lpush('npc_medical_condition', 'deafness in one ear')
self.redis.lpush('npc_medical_condition', 'irritable bowels')
self.redis.lpush('npc_medical_condition', 'eczema')
self.redis.lpush('npc_medical_condition', 'syphilis')
self.redis.lpush('npc_medical_condition', 'gout')
self.redis.lpush('npc_medical_condition', 'a limp')
self.redis.lpush('npc_medical_condition', 'clumsiness')
self.redis.lpush('npc_medical_condition', 'poor circulation')
self.redis.lpush('npc_medical_condition', 'color blindness')
self.redis.lpush('npc_medical_condition', 'shortsightedness')
self.redis.lpush('npc_medical_condition', 'depression')
self.redis.lpush('npc_medical_condition', 'social anxiety')
self.redis.lpush('npc_medical_condition', 'poor hygiene')
self.redis.lpush('npc_medical_condition', 'allergies')
self.redis.lpush('npc_medical_condition', 'asthma')
self.redis.lpush('npc_medical_condition', 'arthritis')
self.redis.lpush('npc_medical_condition', 'blood pressure')
self.redis.lpush('npc_medical_condition', 'a cancerous growth')
self.redis.lpush('npc_medical_condition', 'chronic pain')
self.redis.lpush('npc_medical_condition', 'the flu')
self.redis.lpush('npc_medical_condition', 'diabetes')
self.redis.lpush('npc_medical_condition', 'diabeetus')
self.redis.lpush('npc_medical_condition', 'consumption')
self.redis.lpush('npc_medical_condition', 'cataracts')
self.redis.lpush('npc_medical_condition', 'anxiety')
self.redis.lpush('npc_medical_condition', 'cold sores')
self.redis.lpush('npc_medical_condition', 'chronic illness')
self.redis.lpush('npc_medical_condition', 'constipation')
self.redis.lpush('npc_medical_condition', 'dementia')
self.redis.lpush('npc_medical_condition', 'diarrhea')
self.redis.lpush('npc_medical_condition', 'depression')
self.redis.lpush('npc_medical_condition', 'food poisoning')
self.redis.lpush('npc_medical_condition', 'gallstones')
self.redis.lpush('npc_medical_condition', 'hay fever')
self.redis.lpush('npc_medical_condition', 'migraines')
self.redis.lpush('npc_medical_condition', 'impotence')
self.redis.lpush('npc_medical_condition', 'insomnia')
self.redis.lpush('npc_medical_condition', 'jaundice')
self.redis.lpush('npc_medical_condition', 'lactose intolerance')
self.redis.lpush('npc_medical_condition', 'liver disease')
self.redis.lpush('npc_medical_condition', 'mental illness')
self.redis.lpush('npc_medical_condition', 'an STD')
self.redis.lpush('npc_medical_condition', 'the remnants of a stroke')
self.redis.lpush('npc_medical_condition', 'whooping cough')
self.redis.lpush('npc_medical_condition', 'flatulence')
self.redis.lpush('npc_medical_condition', 'sleepwalking')
self.redis.lpush('npc_medical_condition', 'night terrors')
self.redis.lpush('npc_medical_condition', 'stammer')
self.redis.lpush('npc_medical_condition', 'tone deafness')
self.redis.lpush('npc_medical_condition', 'an arrow to the knee')
        
    
#        <option          max="23" >Commoner
#	    <option min="24" max="35" >Expert
#	    <option min="36" max="43" >Warrior
#	    <option min="44" max="49" >Rogue
#	    <option min="50" max="52" >Barbarian
#	    <option min="53" max="55" >Monk
#	    <option min="56" max="59" >Bard
#	    <option min="60" max="65" >Cleric
#	    <option min="66" max="69" >Druid
#	    <option min="70" max="77" >Fighter
#	    <option min="78" max="83" >Adept
#	    <option min="84" max="87" >Sorcerer
#	    <option min="88" max="91" >Wizard
#	    <option min="92" max="95" >Aristocrat
#	    <option min="96" max="97" >Paladin
#	    <option min="99"          >Ranger
	
        
