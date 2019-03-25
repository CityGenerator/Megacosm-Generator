FROM python:3.7
LABEL maintainer="Jesse Morgan <morgajel@gmail.com>"
ENV REDISHOST="localhost"
ENV REDISPORT="6379"

WORKDIR /app
#COPY megacosm log run.py requirements.txt /app/
COPY . /app
COPY config.py.example /app/config.py

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

CMD /usr/local/bin/python reimport_data.py --redishost $REDISHOST --redisport $REDISPORT
#CMD '/bin/bash'
#/var/www/megacosm.morgajel.net/.env/bin/gunicorn --pid /var/run/megacosm/pid --bind unix:/var/run/megacosm/socket  megacosm:app -w 2
