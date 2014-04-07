[![Coverage Status](https://coveralls.io/repos/CityGenerator/Megacosm-Generator/badge.png?branch=develop)](https://coveralls.io/r/CityGenerator/Megacosm-Generator?branch=develop) 

Megacosm-Generator
==================

A tool for creating fantasy campaign settings, including maps, regions, flags, cities, NPCs, businesses, legends, lore and more.

# Set Up The Dev Environment

* make sure you have python 2.7
* make sure you have python's virtualenv installed
* set up Redis or (have access to one, like redistogo).


On the first run, do the following:

```bash

    # create a virtual env
    virtualenv env

    # activate the env
    source env/bin/activate

    # install the requirements
    pip install -r requirements.txt

    # copy the example config into place and configure it
    cp data/config.ini.example data/config.ini

    # Load your data
    python scripts/reimport_data.py

    # start the server
    python megacosm.py
```

After that, you just need to use this:

```bash
    source env/bin/activate
    python megacosm.py
```

To try your unit tests, run 

```bash
    nosetests tests/
```

