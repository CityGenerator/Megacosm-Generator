#

#If a when is selected, it\'s tacked on to the front of a sentence.
SET   bond_when_chance 50
self.redis.lpush('bond_when', 'Recently')
self.redis.lpush('bond_when', 'Yesterday')
self.redis.lpush('bond_when', 'Long long ago')
self.redis.lpush('bond_when', 'In the past')
self.redis.lpush('bond_when', 'Years ago')
self.redis.lpush('bond_when', 'When it was most needed')
self.redis.lpush('bond_when', 'At one time')
self.redis.lpush('bond_when', 'On one occasion')
self.redis.lpush('bond_when', 'Way back when')


# params.partyA and params.partyB could be You or a Name, random.shuffle([\'you\',\'npc\'])
# either could be... either party. Other is the other.
self.redis.lpush('bond_template', '{{params.partyA}} accepted {{params.partyB}} despite obvious failings. Which failing was the hardest?')
self.redis.lpush('bond_template', '{{params.partyA}} admired {{params.partyB}} secretly. Any idea why?')
self.redis.lpush('bond_template', '{{params.partyA}} advised {{params.partyB}} incorrectly. What were the consequences?')
self.redis.lpush('bond_template', '{{params.partyA}} advised {{params.partyB}} correctly. What were the consequences?')
self.redis.lpush('bond_template', '{{params.partyA}} agreed with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} alerted {{params.partyB}} to impending danger.')
self.redis.lpush('bond_template', '{{params.partyA}} amused {{params.partyB}} in an unusual way.')
self.redis.lpush('bond_template', '{{params.partyA}} annoyed {{params.partyB}} in an unusual way.')
self.redis.lpush('bond_template', '{{params.partyA}} argued with {{params.partyB}} at the worst possible moment.')
self.redis.lpush('bond_template', '{{params.partyA}} accidentally led to the arrest of {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} attacked {{params.partyB}} over an unpaid bill long ago. Some think {{params.either}} still harbors a grudge.')
self.redis.lpush('bond_template', '{{params.you}} and {{params.other}} battled on opposite sides of a conflict.')
self.redis.lpush('bond_template', '{{params.you}} and {{params.other}} belonged to the same group.')
self.redis.lpush('bond_template', '{{params.you}} and {{params.other}} burned an enemy\'s house down.')
self.redis.lpush('bond_template', '{{params.partyA}} bet against {{params.partyB}} and lost.')
self.redis.lpush('bond_template', '{{params.partyA}} bet against {{params.partyB}} and won.')
self.redis.lpush('bond_template', '{{params.partyA}} bet against {{params.partyB}} and cheated to win.')
self.redis.lpush('bond_template', '{{params.partyA}} and {{params.partyB}} camped together recently.')
self.redis.lpush('bond_template', '{{params.partyA}} challenged {{params.partyB}} to a duel to the death, then backed out.')
self.redis.lpush('bond_template', '{{params.partyA}} tampered with a jury for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} charged a bear with a chicken wing to defend {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} chased a wild boar for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} cheated {{params.partyB}} at poker.')
self.redis.lpush('bond_template', '{{params.partyA}} choked {{params.partyB}} in a brawl.')
self.redis.lpush('bond_template', '{{params.partyA}} claimed to have given {{params.partyB}} something of value.')
self.redis.lpush('bond_template', '{{params.partyA}} cleaned soiled armor for {{params.partyB}} losing a bet.')
self.redis.lpush('bond_template', '{{params.partyA}} collected a bounty on {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} commanded {{params.partyB}} in battle.')
self.redis.lpush('bond_template', '{{params.partyA}} competed for a prize with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} confessed to a crime {{params.partyB}} committed.')
self.redis.lpush('bond_template', '{{params.partyA}} confused {{params.partyB}} with a bizarre story.')
self.redis.lpush('bond_template', '{{params.partyA}} corrected {{params.partyB}} in front of royalty.')
self.redis.lpush('bond_template', '{{params.partyA}} coughed blood on {{params.partyB}} after a battle.')
self.redis.lpush('bond_template', '{{params.partyA}} counted on {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} covered for {{params.partyB}} to prevent an execution.')
self.redis.lpush('bond_template', '{{params.partyA}} literally crawled over broken glass for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} crossed a raging river to help {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} cried openly in front of {{params.partyB}} about a dark secret.')
self.redis.lpush('bond_template', '{{params.partyA}} found a cure for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} danced with the devil to save {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} dared {{params.partyB}} to do something stupid - ending in arrest, fines and community service.')
self.redis.lpush('bond_template', '{{params.partyA}} deceived {{params.partyB}} in an appalling way.')
self.redis.lpush('bond_template', '{{params.partyA}} delayed {{params.partyB}}, resulting in the death of a loved one.')
self.redis.lpush('bond_template', '{{params.partyA}} delivered crushing news to {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} depended on {{params.partyB}} to come through. {{params.partyB|capitalize}} did.')
self.redis.lpush('bond_template', '{{params.partyA}} depended on {{params.partyB}} to come through. {{params.partyB|capitalize}} didn\'t.')
self.redis.lpush('bond_template', '{{params.partyA}} deserted {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} destroyed a cursed item to save {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} disarmed {{params.partyB}} in an embarrassing sparring session.')
self.redis.lpush('bond_template', '{{params.partyA}} discovered the deep, dark secret that {{params.partyB}} hid.')
self.redis.lpush('bond_template', '{{params.partyA}} discovered that {{params.partyB}} lied about something critical.')
self.redis.lpush('bond_template', '{{params.partyA}} divided the loot improperly with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} dragged {{params.partyB}} somewhere dangerous.')
self.redis.lpush('bond_template', '{{params.partyA}} had a prophetic dream about {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} dressed up in drag to save {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} dropped {{params.partyB}} down a well by accident.')
self.redis.lpush('bond_template', '{{params.partyA}} nearly drowned trying to save {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} earned {{params.partyB}} an undeserved reputation.')
self.redis.lpush('bond_template', '{{params.partyA}} educated {{params.partyB}} on the birds and the bees.')
self.redis.lpush('bond_template', '{{params.partyA}} embarrassed {{params.partyB}} in front of royalty.')
self.redis.lpush('bond_template', '{{params.partyA}} employed {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} emptied a bottle that belonged to {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} encouraged {{params.partyB}} to do something brave, despite the paralyzing fear.')
self.redis.lpush('bond_template', '{{params.partyA}} enjoyed traveling with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} entered into an agreement with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} entertained {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} escaped with {{params.partyB}} from certain death.')
self.redis.lpush('bond_template', '{{params.partyA}} examined an injury {{params.partyB}} would rather forget.')
self.redis.lpush('bond_template', '{{params.partyA}} thought of excuses for {{params.partyB}} when they were needed.')
self.redis.lpush('bond_template', '{{params.partyA}} expected better of {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} explained things in small words for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} faced {{params.partyB}} in single combat.  {{params.either |capitalize}} lost.')
self.redis.lpush('bond_template', '{{params.partyA}} faced {{params.partyB}} in single combat.  {{params.either |capitalize}} won.')
self.redis.lpush('bond_template', '{{params.partyA}} failed in a way that {{params.partyB}} will never forget.')
self.redis.lpush('bond_template', '{{params.partyA}} fenced an item for {{params.partyB}} once.')
self.redis.lpush('bond_template', '{{params.partyA}} fetched help when {{params.partyB}} got stuck.')
self.redis.lpush('bond_template', '{{params.partyA}} fired {{params.partyB}} on a previous job.')
self.redis.lpush('bond_template', '{{params.partyA}} fixed a bet with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} followed {{params.partyB}} into the wrong brothel.')
self.redis.lpush('bond_template', '{{params.partyA}} unknowingly fooled {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} forced {{params.partyB}} into a bad situation.')
self.redis.lpush('bond_template', '{{params.partyA}} formed an incorrect option of {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} found {{params.partyB}} on the verge of death.')
self.redis.lpush('bond_template', '{{params.partyA}} accidentally framed {{params.partyB}} for murder.')
self.redis.lpush('bond_template', '{{params.partyA}} accidentally framed {{params.partyB}} for theft.')
self.redis.lpush('bond_template', '{{params.partyA}} frightened small children and blamed {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} glued a fork to {{params.partyB}} in a prank gone horribly wrong.')
self.redis.lpush('bond_template', '{{params.partyA}} guaranteed good behavior from {{params.partyB}} in return for leniency.')
self.redis.lpush('bond_template', '{{params.partyA}} guarded treasure that {{params.partyB}} unsuccessfully tried to steal.')
self.redis.lpush('bond_template', '{{params.partyA}} guarded treasure that {{params.partyB}} successfully to stole.')
self.redis.lpush('bond_template', '{{params.partyA}} guided {{params.partyB}} into danger.')
self.redis.lpush('bond_template', '{{params.partyA}} harassed {{params.partyB}} for amusement.')
self.redis.lpush('bond_template', '{{params.partyA}} inadvertently harmed someone and {{params.partyB}} took the blame.')
self.redis.lpush('bond_template', '{{params.partyA}} hated {{params.partyB}} at first sight.')
self.redis.lpush('bond_template', '{{params.partyA}} swore to haunt {{params.partyB}} if {{params.partyA}} died.')
self.redis.lpush('bond_template', '{{params.partyA}} healed {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} helped {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} hooked {{params.partyB}} with a fish hook by accident.')
self.redis.lpush('bond_template', '{{params.partyA}} hoped to never see {{params.partyB}} again.')
self.redis.lpush('bond_template', '{{params.partyA}} hovered over every decision {{params.partyB}} made.')
self.redis.lpush('bond_template', '{{params.partyA}} hugged {{params.partyB}} inappropriately.')
self.redis.lpush('bond_template', '{{params.partyA}} hummed to drive {{params.partyB}} crazy.')
self.redis.lpush('bond_template', '{{params.partyA}} liked to hunt with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} often felt hurried by {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} identified {{params.partyB}} as the person responsible for an unsolved crime.')
self.redis.lpush('bond_template', '{{params.partyA}} ignored {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} imagined {{params.partyB}} without clothing by accident.')
self.redis.lpush('bond_template', '{{params.partyA}} impressed {{params.partyB}} with a quick wit.')
self.redis.lpush('bond_template', '{{params.partyA}} included {{params.partyB}} so {{params.partyB}} wouldn\'t feel bad.')
self.redis.lpush('bond_template', '{{params.partyA}} influenced {{params.partyB}} in a good way.')
self.redis.lpush('bond_template', '{{params.partyA}} influenced {{params.partyB}} in a bad way.')
self.redis.lpush('bond_template', '{{params.partyA}} informed {{params.partyB}} of an approaching assassin.')
self.redis.lpush('bond_template', '{{params.partyA}} drugged {{params.partyB}} for kicks.')
self.redis.lpush('bond_template', '{{params.partyA}} injured {{params.partyB}} intentionally.')
self.redis.lpush('bond_template', '{{params.partyA}} injured {{params.partyB}} unintentionally.')
self.redis.lpush('bond_template', '{{params.partyA}} instructed {{params.partyB}} on how to play the spoons.')
self.redis.lpush('bond_template', '{{params.partyA}} intended to turn {{params.partyB}} into the authorities.')
self.redis.lpush('bond_template', '{{params.partyA}} interrupted {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} introduced {{params.partyB}} to a bad influence.')
self.redis.lpush('bond_template', '{{params.partyA}} invented a wondrous item which {{params.partyB}} destroyed.')
self.redis.lpush('bond_template', '{{params.partyA}} invited {{params.partyB}} to the wrong party.')
self.redis.lpush('bond_template', '{{params.partyA}} irritated {{params.partyB}} less than {{params.partyB}} would like to admit.')
self.redis.lpush('bond_template', '{{params.partyA}} judged {{params.partyB}} too quickly.')
self.redis.lpush('bond_template', '{{params.partyA}} kicked {{params.partyB}} in the groin.')
self.redis.lpush('bond_template', '{{params.partyA}} nearly killed {{params.partyB}}, and {{params.partyB}} knew it.')
self.redis.lpush('bond_template', '{{params.partyA}} knocked {{params.partyB}} out.')
self.redis.lpush('bond_template', '{{params.partyA}} learned not to trust {{params.partyB}} so easily.')
self.redis.lpush('bond_template', '{{params.partyA}} lied to {{params.partyB}} about something and got caught.')
self.redis.lpush('bond_template', '{{params.partyA}} liked {{params.partyB}} a lot more before "the incident".')
self.redis.lpush('bond_template', '{{params.partyA}} locked {{params.partyB}} in the bottom of a privy.')
self.redis.lpush('bond_template', '{{params.partyA}} managed to irritate {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} murdered someone to protect {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} murdered someone to frame {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} nailed {{params.partyB}} to a tree.')
self.redis.lpush('bond_template', '{{params.partyA}} took notes for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} obtained treasure for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} offended {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} offered help to {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} opened doors for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} did business with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} owed {{params.partyB}} a favor. It\'s still owed.')
self.redis.lpush('bond_template', '{{params.partyA}} owned {{params.partyB}} as a slave.')
self.redis.lpush('bond_template', '{{params.partyA}} painted {{params.partyB}} in a bad light.')
self.redis.lpush('bond_template', '{{params.partyA}} parked carriages for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} parted ways with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} paused to chat with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} pecked {{params.partyB}} on the cheek.')
self.redis.lpush('bond_template', '{{params.partyA}} peeped when {{params.partyB}} changed.')
self.redis.lpush('bond_template', '{{params.partyA}} performed heroic deeds for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} picked on {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} pined for the fjords with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} placed {{params.partyB}} on a pedestal.')
self.redis.lpush('bond_template', '{{params.partyA}} planted evidence to frame {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} played mind-games with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} poked fun at {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} polished the knobs for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} popped pills with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} poured wine for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} practiced the magic arts with {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} permitted {{params.partyB}} to live in the basement.')
self.redis.lpush('bond_template', '{{params.partyA}} permitted {{params.partyB}} to live in the attic.')
self.redis.lpush('bond_template', '{{params.partyA}} permitted {{params.partyB}} to live in the shed.')
self.redis.lpush('bond_template', '{{params.partyA}} preached to {{params.partyB}} about religion. ')
self.redis.lpush('bond_template', '{{params.partyA}} gave {{params.partyB}} a gift.')
self.redis.lpush('bond_template', '{{params.partyA}} read poetry to {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} preceded {{params.partyB}} in the family tree.')
self.redis.lpush('bond_template', '{{params.partyA}} pressed {{params.partyB}} to take action.')
self.redis.lpush('bond_template', '{{params.partyA}} printed libelous pamphlets about {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} produced {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} promised the world to {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} provided {{params.partyB}} with something crucial.')
self.redis.lpush('bond_template', '{{params.partyA}} provided {{params.partyB}} with something useless.')
self.redis.lpush('bond_template', '{{params.partyA}} provided {{params.partyB}} with the cure.')
self.redis.lpush('bond_template', '{{params.partyA}} pulled practical jokes on {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} pumped water for {{params.partyB}}.')
self.redis.lpush('bond_template', '{{params.partyA}} pushed {{params.partyB}} over a cliff.')
self.redis.lpush('bond_template', '{{params.partyA}} feared what {{params.partyB}} would become.')
self.redis.lpush('bond_template', '{{params.partyA}} didn\'t tell {{params.partyB}} about the prophecy.')
        
# These were never resolved.    
#    <reason>
#        <where>
#            <option>Where did this happen?
#            <option>
#        
#        <what>
#			<option>What were the details?
#			<option>What lead to this?
#			<option>What happened?
#			<option>What is missing?
#			<option>What was the reason?
#			<option>What will they do?
#        
#        <when>
#            <option>
#            <option>
#        
#        <how>
#			<option>How?
#			<option>How come?
#			<option>How did you stop them?
#        
#        <application>
#            <option>
#            <option>
#        
#        <analysis>
#            <option>
#            <option>
#        
#        <synthesis> 
#            <option>
#            <option>
#        
#        <evaluation>
#            <option>
#            <option>
#        
#    



