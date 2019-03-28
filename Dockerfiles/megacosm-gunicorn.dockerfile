FROM python:3.7
MAINTAINER "Jesse Morgan <morgajel@gmail.com>
WORKDIR /app
#COPY megacosm log run.py requirements.txt /app/
COPY . /app
COPY config.py.example /app/config.py

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000
CMD [ "/usr/local/bin/python", "run.py"]
#CMD '/bin/bash'
#/var/www/megacosm.morgajel.net/.env/bin/gunicorn --pid /var/run/megacosm/pid --bind unix:/var/run/megacosm/socket  megacosm:app -w 2
