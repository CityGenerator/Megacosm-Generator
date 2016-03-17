#

self.redis.lpush('legend_lastseen', 'was last seen years ago')
self.redis.lpush('legend_lastseen', 'disappeared after an attack by bandits')
self.redis.lpush('legend_lastseen', 'was stolen from a locked vault')
self.redis.lpush('legend_lastseen', 'has been lost for ages')
self.redis.lpush('legend_lastseen', 'mysteriously disappeared')
self.redis.lpush('legend_lastseen', 'was never recovered')
self.redis.lpush('legend_lastseen', 'hasn\'t reappeared in years')
        
self.redis.lpush('legend_ability', 'make people cry')
self.redis.lpush('legend_ability', 'cause others to fall asleep')
self.redis.lpush('legend_ability', 'dominate others')
self.redis.lpush('legend_ability', 'summon angels')
self.redis.lpush('legend_ability', 'summon demons')
self.redis.lpush('legend_ability', 'grant wishes')
self.redis.lpush('legend_ability', 'solve any riddle')
self.redis.lpush('legend_ability', 'answer any question')
self.redis.lpush('legend_ability', 'find any item')
self.redis.lpush('legend_ability', 'disappear on its own')
self.redis.lpush('legend_ability', 'speak for itself')
self.redis.lpush('legend_ability', 'make someone speak the truth')
self.redis.lpush('legend_ability', 'move on its own accord')
        
self.redis.lpush('legend_abilitytype', 'power')
self.redis.lpush('legend_abilitytype', 'ability')
self.redis.lpush('legend_abilitytype', 'capability')
self.redis.lpush('legend_abilitytype', 'knack')
        
self.redis.lpush('legend_reputation', 'legendary')
self.redis.lpush('legend_reputation', 'magical')
self.redis.lpush('legend_reputation', 'special')
self.redis.lpush('legend_reputation', 'unique')
self.redis.lpush('legend_reputation', 'cursed')
self.redis.lpush('legend_reputation', 'possessed')
        
self.redis.lpush('legend_object', 'harp')
self.redis.lpush('legend_object', 'mirror')
self.redis.lpush('legend_object', 'ring')
self.redis.lpush('legend_object', 'rake')
self.redis.lpush('legend_object', 'throne')
self.redis.lpush('legend_object', 'crown')
self.redis.lpush('legend_object', 'tiara')
self.redis.lpush('legend_object', 'amulet')
self.redis.lpush('legend_object', 'hat')
self.redis.lpush('legend_object', 'bedpan')
self.redis.lpush('legend_object', 'sceptre')
self.redis.lpush('legend_object', 'trident')
self.redis.lpush('legend_object', 'helmet')
self.redis.lpush('legend_object', 'brooch')
self.redis.lpush('legend_object', 'sandwich')
self.redis.lpush('legend_object', 'lasso')
self.redis.lpush('legend_object', 'quill')
self.redis.lpush('legend_object', 'fiddle')
self.redis.lpush('legend_object', 'goose')
self.redis.lpush('legend_object', 'cat')
self.redis.lpush('legend_object', 'painting')
self.redis.lpush('legend_object', 'coin')
self.redis.lpush('legend_object', 'key')
self.redis.lpush('legend_object', 'cauldron')
self.redis.lpush('legend_object', 'apple')
self.redis.lpush('legend_object', 'beans')
self.redis.lpush('legend_object', 'needle')
self.redis.lpush('legend_object', 'shoes')
self.redis.lpush('legend_object', 'rose')
self.redis.lpush('legend_object', 'jug')
self.redis.lpush('legend_object', 'deck of cards')
self.redis.lpush('legend_object', 'bag of beans')
        
self.redis.lpush('legend_bait', 'sneeze three times')
self.redis.lpush('legend_bait', 'offer you sweets')
self.redis.lpush('legend_bait', 'ask for your help')
self.redis.lpush('legend_bait', 'ask a favor of you')
        
self.redis.lpush('legend_trap', 'sell you into slavery')
self.redis.lpush('legend_trap', 'eat you')
self.redis.lpush('legend_trap', 'carry you away')
self.redis.lpush('legend_trap', 'imprison you')
self.redis.lpush('legend_trap', 'turn you into a mouse')
self.redis.lpush('legend_trap', 'give you a gift if you are nice')
self.redis.lpush('legend_trap', 'banish you if you are cruel')
self.redis.lpush('legend_trap', 'steal your soul')
        
self.redis.lpush('legend_monster', 'Pooka')
self.redis.lpush('legend_monster', 'witch')
self.redis.lpush('legend_monster', 'hag')
self.redis.lpush('legend_monster', 'Boogyman')
self.redis.lpush('legend_monster', 'old woman')
self.redis.lpush('legend_monster', 'old man')
        
self.redis.lpush('legend_who', 'They')
self.redis.lpush('legend_who', 'Some')
self.redis.lpush('legend_who', 'Folks')
self.redis.lpush('legend_who', 'Villagers')
self.redis.lpush('legend_who', 'Commoners')
self.redis.lpush('legend_who', 'People')
        
self.redis.lpush('legend_wander', 'roamed')
self.redis.lpush('legend_wander', 'wandered')
self.redis.lpush('legend_wander', 'hunted')
self.redis.lpush('legend_wander', 'haunted')
self.redis.lpush('legend_wander', 'stalked')
self.redis.lpush('legend_wander', 'frequented')
self.redis.lpush('legend_wander', 'lingered in')
        
SET   legend_stopit_chance 10
self.redis.lpush('legend_stopit', 'unless you flee')
self.redis.lpush('legend_stopit', 'unless you complete a quest')
self.redis.lpush('legend_stopit', 'unless you return a lost possession')
self.redis.lpush('legend_stopit', 'unless you offer a sacrifice')
self.redis.lpush('legend_stopit', 'unless you offer your most valued possession')
self.redis.lpush('legend_stopit', 'unless you pay a tribute')
self.redis.lpush('legend_stopit', 'unless you answer a riddle')
        
SET   legend_drawn_chance 30
self.redis.lpush('legend_drawn', 'and was drawn towards misbehaving children')
self.redis.lpush('legend_drawn', 'and was drawn towards murderers')
self.redis.lpush('legend_drawn', 'and was drawn towards those that have killed innocents')
self.redis.lpush('legend_drawn', 'and was drawn towards thieves')
self.redis.lpush('legend_drawn', 'and was drawn towards acts of greed')
self.redis.lpush('legend_drawn', 'and was drawn towards those that wronged others')
        
SET   legend_when_chance 40
self.redis.lpush('legend_when', 'at dusk')
self.redis.lpush('legend_when', 'on gloomy days')
self.redis.lpush('legend_when', 'on rainy days')
self.redis.lpush('legend_when', 'before dawn')
self.redis.lpush('legend_when', 'once a year')
self.redis.lpush('legend_when', 'every six years')
self.redis.lpush('legend_when', 'during a full moon')
self.redis.lpush('legend_when', 'during a red moon')
self.redis.lpush('legend_when', 'when the moon is new')
self.redis.lpush('legend_when', 'during the summer solstice')
self.redis.lpush('legend_when', 'when the wind blows from the north')
self.redis.lpush('legend_when', 'when the wind blows from the south')
self.redis.lpush('legend_when', 'when the wind blows from the east')
self.redis.lpush('legend_when', 'when the wind blows from the west')
        
self.redis.lpush('legend_detect', 'hear')
self.redis.lpush('legend_detect', 'see')
self.redis.lpush('legend_detect', 'touch')
self.redis.lpush('legend_detect', 'face')
self.redis.lpush('legend_detect', 'caught')
self.redis.lpush('legend_detect', 'confront')
        
self.redis.lpush('legend_badfate', 'will be driven mad')
self.redis.lpush('legend_badfate', 'will be killed')
self.redis.lpush('legend_badfate', 'will be eaten alive')
self.redis.lpush('legend_badfate', 'will die within 24 hours')
self.redis.lpush('legend_badfate', 'will be stricken blind')
self.redis.lpush('legend_badfate', 'will be stricken deaf')
self.redis.lpush('legend_badfate', 'will never be seen again')
        
self.redis.lpush('legend_area', 'countryside')
self.redis.lpush('legend_area', 'town')
self.redis.lpush('legend_area', 'world')
self.redis.lpush('legend_area', 'woods')
self.redis.lpush('legend_area', 'field')
self.redis.lpush('legend_area', 'region')
self.redis.lpush('legend_area', 'swamps')
self.redis.lpush('legend_area', 'fields')
self.redis.lpush('legend_area', 'streets')
        
self.redis.lpush('legend_hero', 'a hero named {{params.npc.name.fullname}}')
self.redis.lpush('legend_hero', 'a {{params.npc.race}} named {{params.npc.name.fullname}}')
self.redis.lpush('legend_hero', 'a {{params.npc.behavior}} {{params.npc.race}} named {{params.npc.name.fullname}}')
self.redis.lpush('legend_hero', '{{params.npc.name.fullname}} the {{params.npc.race}}')
        
self.redis.lpush('legend_badguy', 'a {{params.badguytype}} named {{params.villain.name.fullname}}')
self.redis.lpush('legend_badguy', 'an evil {{params.badguytype}} named {{params.villain.name.fullname}}')
self.redis.lpush('legend_badguy', '{{params.villain.name.fullname}} the {{params.badguytype}}')
        
self.redis.lpush('legend_badguytype', 'dragon')
self.redis.lpush('legend_badguytype', 'minotaur')
self.redis.lpush('legend_badguytype', 'wizard')
self.redis.lpush('legend_badguytype', 'monster')
self.redis.lpush('legend_badguytype', 'serial killer')
self.redis.lpush('legend_badguytype', 'murderer')
self.redis.lpush('legend_badguytype', 'demon')
self.redis.lpush('legend_badguytype', 'devil')
self.redis.lpush('legend_badguytype', 'cyclops')
self.redis.lpush('legend_badguytype', 'ghoul')
self.redis.lpush('legend_badguytype', 'spirit')
self.redis.lpush('legend_badguytype', 'lich')
self.redis.lpush('legend_badguytype', 'vampire')
        
self.redis.lpush('legend_badaction', 'destroyed a nearby village')
self.redis.lpush('legend_badaction', 'took over the town')
self.redis.lpush('legend_badaction', 'kidnapped a princess')
self.redis.lpush('legend_badaction', 'took a hostage and demanded a ransom')
self.redis.lpush('legend_badaction', 'slayed a local hero')
self.redis.lpush('legend_badaction', 'stole a priceless heirloom')
        

self.redis.lpush('legend_storytime', 'Long, long ago')
self.redis.lpush('legend_storytime', 'Long, long ago in a city far, far away')
self.redis.lpush('legend_storytime', 'A long time ago')
self.redis.lpush('legend_storytime', 'Many years ago')
self.redis.lpush('legend_storytime', 'Once upon a time')
self.redis.lpush('legend_storytime', 'In the olden days')
self.redis.lpush('legend_storytime', 'In the days of yore')
self.redis.lpush('legend_storytime', 'Some time ago')
self.redis.lpush('legend_storytime', 'In times past')
self.redis.lpush('legend_storytime', 'In times gone by')
self.redis.lpush('legend_storytime', 'Long ago')
self.redis.lpush('legend_storytime', 'In days gone by')
self.redis.lpush('legend_storytime', 'Years ago')
self.redis.lpush('legend_storytime', 'In olden times')
self.redis.lpush('legend_storytime', 'Way back when')
        
self.redis.lpush('legend_virtue', 'a clever idea')
self.redis.lpush('legend_virtue', 'a crazy idea')
self.redis.lpush('legend_virtue', 'one brave person')
self.redis.lpush('legend_virtue', 'gumption')
self.redis.lpush('legend_virtue', 'never giving up')
self.redis.lpush('legend_virtue', 'never losing hope')
self.redis.lpush('legend_virtue', 'never trusting another {{params.badguytype}}')
        
self.redis.lpush('legend_chumps', 'the villagers')
self.redis.lpush('legend_chumps', 'the constable')
self.redis.lpush('legend_chumps', 'the townsfolk')
self.redis.lpush('legend_chumps', 'the royals')
        
self.redis.lpush('legend_goodstart', 'lived happily')
self.redis.lpush('legend_goodstart', 'lived in peace')
self.redis.lpush('legend_goodstart', 'thrived')
self.redis.lpush('legend_goodstart', 'lived in harmony')
        
self.redis.lpush('legend_goodstatus', 'always nice')
self.redis.lpush('legend_goodstatus', 'good')
self.redis.lpush('legend_goodstatus', 'quiet')
self.redis.lpush('legend_goodstatus', 'peaceful')
        
SET   legend_victory_chance 50
self.redis.lpush('legend_victory', 'and was killed in the process')
self.redis.lpush('legend_victory', 'and rescued the hostages')
self.redis.lpush('legend_victory', 'and rescued {{params.location.name.fullname}}')
        
self.redis.lpush('legend_results', 'defeated {{params.villain.name.fullname}}')
self.redis.lpush('legend_results', 'killed the {{params.badguytype}}')
self.redis.lpush('legend_results', 'tricked {{params.villain.name.fullname}}')
self.redis.lpush('legend_results', 'banished {{params.villain.name.fullname}}')
        
self.redis.lpush('legend_planaction', 'by killing the {{params.badguytype}} while {{params.villain.sex[\'pronoun\']}} slept')
self.redis.lpush('legend_planaction', 'by making a wager with {{params.villain.name.fullname}}')
self.redis.lpush('legend_planaction', 'by causing a distraction while others struck')
self.redis.lpush('legend_planaction', 'by using magic to banish it')
        
self.redis.lpush('legend_plan', 'a plan to trick the {{params.badguytype}}')
self.redis.lpush('legend_plan', 'an idea to slay the {{params.badguytype}}')
self.redis.lpush('legend_plan', 'the thought to slay the {{params.badguytype}}')
        
self.redis.lpush('legend_talent', 'a skilled storyteller')
self.redis.lpush('legend_talent', 'a valiant knight')
self.redis.lpush('legend_talent', 'an expert bowman')
self.redis.lpush('legend_talent', 'a sneaky thief')
        
    
self.redis.lpush('legend_caughtfailing', 'failed miserably')
self.redis.lpush('legend_caughtfailing', 'didn\'t get close')
self.redis.lpush('legend_caughtfailing', 'were caught')
        
    
self.redis.lpush('legend_failedresolution', 'stop the {{params.badguytype}}')
self.redis.lpush('legend_failedresolution', 'kill {{params.villain.name.fullname}}')
        


#LPUSH legend_template  Legends tell of {{params.npc.name.fullname}}\'s {{params.object |title}}, {{params.reputation | article}} {{params.object}} with the {{params.abilitytype}} to {{params.ability}}.  It  {{params.lastseen}}.

self.redis.lpush('legend_template', '{{params.storytime}}, {{params.badguytype |article }} named {{params.villain.name.fullname}} {{params.wander}} the {{params.area}} {{params.when}} {{params.drawn}}. {{params.who}} say that if you {{params.detect}} {{params.villain.sex[\'third-person\']}}, you {{params.badfate}} {{params.stopit}}.')
#LPUSH legend_template  {{params. USE infl = Lingua.EN.Inflect; -}}{{params.storytime}}, {{params.  infl.A( imaginarymonster )}} {{params.wander}} the {{params.area}}{{params.when}}{{params.drawn}}. {{params.who}} say that the {{params.imaginarymonster}} will {{params.baityou}}, then {{params.trapyou}}.


#LPUSH legend_template  Legend says that {{params.storytime}}, a {{params.person or critter}}
#
#Legends tell of a Pooka that haunts the city. They will try to trick you into coming outside, then carry you away.
#Legends tell of the children of Lir, who were turned into swans by a jealous stepmother,
#Legends tell of saint Patrick, who was kidnapped and sold as a slave as a child, and once freed spent his life converting others.
#Legends tell of a warrior named Finn Maccool. He caught a magic salmon and gained great knowledge from eating it.
#Legends tell of a lost city named Atlantis that was lost under the waves in a great cataclysm.
#Legends tell of a god named Loki, who played horrible jokes on people.
#Legends tell of an alley that appears and disappears and contains horrors within it.
#Legends tell of a bad place, where a scary monster does bad things and hoards treasure.
#Legends tell of an old woman who can grant your wish at a horrible price
#Legends tell of a woman who wanders the streets at night wearing a white dress and steals children who are still awake
#Legends tell of a ghost who haunts a place, and townsfolk do something to keep her at bay.
#Legends tell of a young woman who fell in love with someone, and bad things happened.
#Legends say that many years ago, something happened that was bad, and when the prophecy is complete it will happen again.
#Legends tell of a demon called a succubus that tricked men into siring children with them.
#Legends tell of a lost tribe of people that will one day return.
#Legends tell of a fountain of youth that has the power to make you younger. It is guarded by a serpent.
#Legends tell of a wandering jew who taunted jesus and was cursed to walk the earth forever.
#Legends tell of a the only female pope of the catholic church. She was killed.
#Legends tell of a hero named Robin Hood, who robbed from the rich and stole from the poor.
#Legends tell of a magical chalice that possed miraculous powers. It was lost long ago.
#Legends tell of a king long ago who united the lands.
#Legends tell of a king who made a declaration that worked out poorly and cost him dearly.
#Legends tell of a prince who was banished for something bad, then came back to redeem himself.
#Legends tell of two brothers who were raised by a wolf and did something amazing, like found a city.
#Legends tell of a small creature that slowly grew larger and eventually terrorized the countryside.
#Legends tell of a boy who met a unicorn and befriended it.
#Legends tell of a boy who saved a lion and it later saved him.
#Legends tell of a hero who rescued a damsel from a monster.
#Legends tell of a giant with the head of a bull that was trapped in a maze.
#Legends tell of a man who traveled to a dangerous place to rescue his wife and faced a monster.
#
#Legends tell of Dagda\'s harp, a magical item said to possess the power to make people cry. It was stolen and lost for the ages

        
    



