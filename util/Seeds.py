import random
import re
def set_seed(seed):

    #Make sure it's an Integer

    # What if the seed is empty? Lets make a new one!
    if seed is None  or re.search("\D", seed) or  int(seed) <1 or int(seed) > 100000:
        seed=random.randint(1,100000)

    random.seed(float(seed))
    return seed
