import random
import re
def set_seed(seed=None):

    #Make sure it's an Integer

    # What if the seed is empty? Lets make a new one!
    MAXSEED=100000
    MINSEED=1


    if ( type(seed) == str or type(seed) == unicode ) and seed.isdigit():
        seed=int(seed)

    if  type(seed) != int  or  seed < MINSEED or seed > MAXSEED :
        seed=random.randint(MINSEED,MAXSEED)

    random.seed(float(seed))
    return seed
