#

# This dish is ______ to the region
ZADD cuisine_rarity   5 {"name":"rare",        "score":5    }
ZADD cuisine_rarity  10 {"name":"strange",     "score":10   }
ZADD cuisine_rarity  20 {"name":"uncommon",    "score":20   }
ZADD cuisine_rarity  30 {"name":"familiar",    "score":30   }
ZADD cuisine_rarity  40 {"name":"ordinary",    "score":40   }
ZADD cuisine_rarity  60 {"name":"common",      "score":60   }
ZADD cuisine_rarity  70 {"name":"limited",     "score":70   }
ZADD cuisine_rarity  80 {"name":"isolated",    "score":80   }
ZADD cuisine_rarity  90 {"name":"native",      "score":90   }
ZADD cuisine_rarity  95 {"name":"exclusive",   "score":95   }
ZADD cuisine_rarity 100 {"name":"unique",      "score":100  }

# Travelers consider the dish spice_ and presentation to the eye_. Portions are usually size
ZADD cuisine_spice   5 {"name":"bland",     "score":5    }
ZADD cuisine_spice  30 {"name":"mild",      "score":30   }
ZADD cuisine_spice  70 {"name":"peppery",   "score":70   }
ZADD cuisine_spice  95 {"name":"fiery",     "score":95   }
ZADD cuisine_spice 100 {"name":"spicy",     "score":100  }

# The dish is ________ to the eye
ZADD cuisine_presentation   5 {"name":"ugly",           "score":5    }
ZADD cuisine_presentation  30 {"name":"unsightly",      "score":30   }
ZADD cuisine_presentation  70 {"name":"plain",          "score":70   }
ZADD cuisine_presentation  80 {"name":"pleasing",       "score":80   }
ZADD cuisine_presentation  95 {"name":"interesting",    "score":95   }
ZADD cuisine_presentation 100 {"name":"beautiful",      "score":100  }

# and seen as ____
ZADD cuisine_size   5 {"name":"tiny",           "score":5    }
ZADD cuisine_size  30 {"name":"small",          "score":30   }
ZADD cuisine_size  70 {"name":"sufficient",     "score":70   }
ZADD cuisine_size  80 {"name":"filling",        "score":80   }
ZADD cuisine_size  95 {"name":"large",          "score":95   }
ZADD cuisine_size 100 {"name":"gigantic",       "score":100  }
#Common folk consider it _____________
# popularity


self.redis.lpush('cuisine_method', 'baked ')
self.redis.lpush('cuisine_method', 'barbecued ')
self.redis.lpush('cuisine_method', 'blanched ')
self.redis.lpush('cuisine_method', 'boiled ')
self.redis.lpush('cuisine_method', 'braised ')
self.redis.lpush('cuisine_method', 'broiled ')
self.redis.lpush('cuisine_method', 'candied ')
self.redis.lpush('cuisine_method', 'canned ')
self.redis.lpush('cuisine_method', 'charred ')
self.redis.lpush('cuisine_method', 'cooked ')
self.redis.lpush('cuisine_method', 'creamed ')
self.redis.lpush('cuisine_method', 'deep-fried ')
self.redis.lpush('cuisine_method', 'fermented ')
self.redis.lpush('cuisine_method', 'frozen ')
self.redis.lpush('cuisine_method', 'fricasseed ')
self.redis.lpush('cuisine_method', 'fried ')
self.redis.lpush('cuisine_method', 'grilled ')
self.redis.lpush('cuisine_method', 'minced ')
self.redis.lpush('cuisine_method', 'mixed')
self.redis.lpush('cuisine_method', 'pickled ')
self.redis.lpush('cuisine_method', 'poached ')
self.redis.lpush('cuisine_method', 'raw ')
self.redis.lpush('cuisine_method', 'roasted ')
self.redis.lpush('cuisine_method', 'salted ')
self.redis.lpush('cuisine_method', 'sauteed ')
self.redis.lpush('cuisine_method', 'scalded ')
self.redis.lpush('cuisine_method', 'simmered ')
self.redis.lpush('cuisine_method', 'slow-cooked ')
self.redis.lpush('cuisine_method', 'smoked ')
self.redis.lpush('cuisine_method', 'spiced ')
self.redis.lpush('cuisine_method', 'steamed ')
self.redis.lpush('cuisine_method', 'stewed ')
self.redis.lpush('cuisine_method', 'stir-fried ')
self.redis.lpush('cuisine_method', 'tempered ')

self.redis.lpush('cuisine_flavor', 'peppered ')
self.redis.lpush('cuisine_flavor', 'cashew ')
self.redis.lpush('cuisine_flavor', 'orange ')
self.redis.lpush('cuisine_flavor', 'garlic ')
self.redis.lpush('cuisine_flavor', 'teriyaki ')
self.redis.lpush('cuisine_flavor', 'hickory ')
self.redis.lpush('cuisine_flavor', 'curry ')
self.redis.lpush('cuisine_flavor', 'mint ')
self.redis.lpush('cuisine_flavor', 'rosemary ')
self.redis.lpush('cuisine_flavor', 'maple ')
self.redis.lpush('cuisine_flavor', 'sweet and sour ')
self.redis.lpush('cuisine_flavor', 'sweet and spicy ')
self.redis.lpush('cuisine_flavor', 'sour ')
self.redis.lpush('cuisine_flavor', 'shredded ')
self.redis.lpush('cuisine_flavor', 'lemon ')

self.redis.lpush('cuisine_dish', 'apple')
self.redis.lpush('cuisine_dish', 'basilisk')
self.redis.lpush('cuisine_dish', 'bear')
self.redis.lpush('cuisine_dish', 'beef')
self.redis.lpush('cuisine_dish', 'chicken')
self.redis.lpush('cuisine_dish', 'dog')
self.redis.lpush('cuisine_dish', 'eggplant')
self.redis.lpush('cuisine_dish', 'fish')
self.redis.lpush('cuisine_dish', 'ham')
self.redis.lpush('cuisine_dish', 'lamb')
self.redis.lpush('cuisine_dish', 'moose')
self.redis.lpush('cuisine_dish', 'owlbear')
self.redis.lpush('cuisine_dish', 'pork')
self.redis.lpush('cuisine_dish', 'potato')
self.redis.lpush('cuisine_dish', 'seal')
self.redis.lpush('cuisine_dish', 'snail')
self.redis.lpush('cuisine_dish', 'squid')
self.redis.lpush('cuisine_dish', 'tentacle ')
self.redis.lpush('cuisine_dish', 'veal')
self.redis.lpush('cuisine_dish', 'veggie')
self.redis.lpush('cuisine_dish', 'horse')
self.redis.lpush('cuisine_dish', 'clam')
self.redis.lpush('cuisine_dish', 'oyster')
self.redis.lpush('cuisine_dish', 'shrimp')
self.redis.lpush('cuisine_dish', 'frog')
self.redis.lpush('cuisine_dish', 'tiger')
self.redis.lpush('cuisine_dish', 'deer')
self.redis.lpush('cuisine_dish', 'elephant')
self.redis.lpush('cuisine_dish', 'cuttlefish')
self.redis.lpush('cuisine_dish', 'crayfish')
self.redis.lpush('cuisine_dish', 'eel')
self.redis.lpush('cuisine_dish', 'mudskipper')
self.redis.lpush('cuisine_dish', 'salmon')
self.redis.lpush('cuisine_dish', 'rat')
self.redis.lpush('cuisine_dish', 'mutton')
self.redis.lpush('cuisine_dish', 'mouse')
self.redis.lpush('cuisine_dish', 'rabbit')
self.redis.lpush('cuisine_dish', 'goose')
self.redis.lpush('cuisine_dish', 'zucchini')
self.redis.lpush('cuisine_dish', 'melon')
self.redis.lpush('cuisine_dish', 'cheese')
self.redis.lpush('cuisine_dish', 'duck')
self.redis.lpush('cuisine_dish', 'chevon')
self.redis.lpush('cuisine_dish', 'tomato')
self.redis.lpush('cuisine_dish', 'artichoke')
self.redis.lpush('cuisine_dish', 'onion')
self.redis.lpush('cuisine_dish', 'turnip')
self.redis.lpush('cuisine_dish', 'tofu')
self.redis.lpush('cuisine_dish', 'yogurt')

self.redis.lpush('cuisine_mealtype', 'wrap')
self.redis.lpush('cuisine_mealtype', 'casserole')
self.redis.lpush('cuisine_mealtype', 'crumble')
self.redis.lpush('cuisine_mealtype', 'pudding')
self.redis.lpush('cuisine_mealtype', 'pie')
self.redis.lpush('cuisine_mealtype', 'soup')
self.redis.lpush('cuisine_mealtype', 'cream soup')
self.redis.lpush('cuisine_mealtype', 'sandwich')
self.redis.lpush('cuisine_mealtype', 'on pasta')
self.redis.lpush('cuisine_mealtype', 'cake')
self.redis.lpush('cuisine_mealtype', 'mousse')
self.redis.lpush('cuisine_mealtype', 'pancakes')
self.redis.lpush('cuisine_mealtype', 'salad')
self.redis.lpush('cuisine_mealtype', 'on rice')
self.redis.lpush('cuisine_mealtype', 'on kale')
self.redis.lpush('cuisine_mealtype', 'with flatbread')
self.redis.lpush('cuisine_mealtype', 'porridge')

self.redis.lpush('cuisine_sauce', 'red')
self.redis.lpush('cuisine_sauce', 'white')
self.redis.lpush('cuisine_sauce', 'duck')
self.redis.lpush('cuisine_sauce', 'bean')
self.redis.lpush('cuisine_sauce', 'peanut')
self.redis.lpush('cuisine_sauce', 'chile')
self.redis.lpush('cuisine_sauce', 'tomato')
self.redis.lpush('cuisine_sauce', 'oyster')
self.redis.lpush('cuisine_sauce', 'lemon')
self.redis.lpush('cuisine_sauce', 'cream')
self.redis.lpush('cuisine_sauce', 'cheese')
self.redis.lpush('cuisine_sauce', 'mushroom')
self.redis.lpush('cuisine_sauce', 'tartar')
self.redis.lpush('cuisine_sauce', 'soy')
self.redis.lpush('cuisine_sauce', 'anchovy')
self.redis.lpush('cuisine_sauce', 'chocolate')
self.redis.lpush('cuisine_sauce', 'carmel')
self.redis.lpush('cuisine_sauce', 'fudge')
self.redis.lpush('cuisine_sauce', 'brown')

self.redis.lpush('cuisine_saucetype', 'broth')
self.redis.lpush('cuisine_saucetype', 'sauce')
self.redis.lpush('cuisine_saucetype', 'gravy')
self.redis.lpush('cuisine_saucetype', 'cream')

self.redis.lpush('cuisine_served', 'hot')
self.redis.lpush('cuisine_served', 'cold')
self.redis.lpush('cuisine_served', 'chilled')
self.redis.lpush('cuisine_served', 'luke warm')
self.redis.lpush('cuisine_served', 'at room temperature')

#<!-- regional, ethnic, racial or religious roots, historical -->
# Baked cashew squid pie  in red gravy, served hot
SET   cuisine_method_chance 70 
SET   cuisine_flavor_chance 30 

SET   cuisine_mealtype_chance 40 
SET   cuisine_sauce_chance 30 
SET   cuisine_served_chance 20 


self.redis.lpush('cuisine_template', '{%if params.method%}{{params.method}} {%endif%}{%if params.flavor%}{{params.flavor}} {%endif%}{{params.dish}}{%if params.mealtype%} {{params.mealtype}}{%endif%}{%if params.sauce%} in {{params.sauce}} {{params.saucetype}}{%endif%}{%if params.served%}, served {{params.served}}{%endif%} This dish is {{params.rarity[\'name\']}} to the {{params.region.name.fullname}}. Travelers consider the dish {{params.spice[\'name\']}} and {{params.presentation[\'name\']}} to the eye. Portions are usually {{params.size[\'name\']}}.')

# The above template is a mess, but here\'s what it makes....
#{%if params.method%}{{params.method}} {%endif%}
#{%if params.flavor%}{{params.flavor}} {%endif%}
#{{params.dish}}
#{%if params.mealtype%} {{params.mealtype}}{%endif%}
#{%if params.sauce%} in {{params.sauce}} {{params.saucetype}}{%endif%}
#{%if params.served%}, served {{params.served}}{%endif%}
#
