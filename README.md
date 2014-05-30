[![Coverage Status](https://coveralls.io/repos/CityGenerator/Megacosm-Generator/badge.png?branch=develop)](https://coveralls.io/r/CityGenerator/Megacosm-Generator?branch=develop) 
[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/CityGenerator/megacosm-generator/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

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
    ./Start
    # View the app in your browser at http://127.0.0.1:8000/
```

After that, you just need to use this:

```bash
    source env/bin/activate
    ./Start
```

To try your unit tests, run 

```bash
    nosetests
```

