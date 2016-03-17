
# I heard that Bob ______ Frank
self.redis.lpush('rumor_verbed', 'blackmailed')
self.redis.lpush('rumor_verbed', 'bribed')
self.redis.lpush('rumor_verbed', 'cheated')
self.redis.lpush('rumor_verbed', 'extorted')
self.redis.lpush('rumor_verbed', 'insulted')
self.redis.lpush('rumor_verbed', 'kidnapped')
self.redis.lpush('rumor_verbed', 'maimed')
self.redis.lpush('rumor_verbed', 'murdered')
self.redis.lpush('rumor_verbed', 'patronized')
self.redis.lpush('rumor_verbed', 'robbed')
self.redis.lpush('rumor_verbed', 'screwed')
self.redis.lpush('rumor_verbed', 'stole from')
self.redis.lpush('rumor_verbed', 'torched')

#  Bob ____________ cheated Frank
self.redis.lpush('rumor_stealth', 'flagrantly')
self.redis.lpush('rumor_stealth', 'secretly')
self.redis.lpush('rumor_stealth', 'quietly')
self.redis.lpush('rumor_stealth', 'publicly')

SET   rumor_past_chance 30
# Note that "past" is used in several templates.
# and yes, the double space is needed to parse properly. Fugly, I know.
self.redis.lpush('rumor_past', 'yesterday')
self.redis.lpush('rumor_past', 'the day before last')
self.redis.lpush('rumor_past', 'several days ago')
self.redis.lpush('rumor_past', 'last week')
self.redis.lpush('rumor_past', 'last month')
self.redis.lpush('rumor_past', 'last year')
self.redis.lpush('rumor_past', 'several years ago')

# A creepy place where a thing was seen
# a ghost was spotted out at the __________
self.redis.lpush('rumor_location', 'old millhouse')
self.redis.lpush('rumor_location', 'empty riverbed')
self.redis.lpush('rumor_location', 'caves to the north')
self.redis.lpush('rumor_location', 'abandoned farmhouse outside of town')
self.redis.lpush('rumor_location', 'ancient ruins')

# They say a[n] ________ guards it
self.redis.lpush('rumor_scarything', 'ghost')
self.redis.lpush('rumor_scarything', 'witch')
self.redis.lpush('rumor_scarything', 'mummy')
self.redis.lpush('rumor_scarything', 'werewolf')
self.redis.lpush('rumor_scarything', 'dinosaur')
self.redis.lpush('rumor_scarything', 'demon')
self.redis.lpush('rumor_scarything', 'dragon')
self.redis.lpush('rumor_scarything', 'ghoul')
self.redis.lpush('rumor_scarything', 'three headed hound')
self.redis.lpush('rumor_scarything', 'venomous serpent')

# bob saw the ghost and __________
self.redis.lpush('rumor_fearresult', 'fled in terror')
self.redis.lpush('rumor_fearresult', 'was killed')
self.redis.lpush('rumor_fearresult', 'was stricken dumb')
self.redis.lpush('rumor_fearresult', 'was nearly killed')
self.redis.lpush('rumor_fearresult', 'was gravely injured')
self.redis.lpush('rumor_fearresult', 'fell to the ground, dead')
self.redis.lpush('rumor_fearresult', 'ran home as fast as possible')

# Bob went missing and was last seen _____________.
self.redis.lpush('rumor_dangeroushobby', 'seeking revenge')
self.redis.lpush('rumor_dangeroushobby', 'trying to earn some quick coin')
self.redis.lpush('rumor_dangeroushobby', 'trying to win a bet')
self.redis.lpush('rumor_dangeroushobby', 'threaten a mysterious stranger')
self.redis.lpush('rumor_dangeroushobby', 'working for a new employer who suddenly skipped town.')
self.redis.lpush('rumor_dangeroushobby', 'drunkenly arguing with people')
self.redis.lpush('rumor_dangeroushobby', 'chasing something into the woods')

SET   rumor_belief_chance 30
self.redis.lpush('rumor_belief', '{{params.believer}} believes it.')
self.redis.lpush('rumor_belief', '{{params.believer}} doesn\'t believe it.')
self.redis.lpush('rumor_belief', '{{params.believer}} wants to believe it.')
self.redis.lpush('rumor_belief', '{{params.believer}} doesn\'t want to believe it.')

SET   rumor_heardit_chance 30
self.redis.lpush('rumor_heardit{{params.source}}', 'heard')
self.redis.lpush('rumor_heardit{{params.source}}', 'said')

SET   rumor_truth_chance 30
self.redis.lpush('rumor_truth', '(True.)')
self.redis.lpush('rumor_truth', '(False.)')
self.redis.lpush('rumor_truth', '(Unknown.)')
self.redis.lpush('rumor_truth', '(Mistaken.)')

self.redis.lpush('rumor_template', '{{params.culprit}} {{params.stealth}} {{params.verbed}} {{params.victim}}{{params.past}}.')
self.redis.lpush('rumor_template', '{{params.scarything|article}} was spotted out by the {{params.location}}{{params.past}}. {{params.victim}} saw it and {{params.fearresult}}.')
self.redis.lpush('rumor_template', 'there\'s a hidden treasure at the {{params.location}} for anyone stupid enough to go after it. They say {{params.scarything|article}} guards it.')
self.redis.lpush('rumor_template', '{{params.victim}} went missing{{params.past}} and was last seen {{params.dangeroushobby}}, never to be seen again.')


# FIXME change stupid enough to a variable
# for anyone brave enough, stupid enough, etc.
