import random

def set_seed(seed):

    #Make sure it's an Integer

    # What if the seed is empty? Lets make a new one!
    if (seed is None):
        seed=random.randint(1,100000)

    random.seed(float(seed))
    return seed
