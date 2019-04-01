FROM python:3.7
MAINTAINER "Jesse Morgan <morgajel@gmail.com>
WORKDIR /app
#COPY megacosm log run.py requirements.txt /app/
COPY . /app
COPY config.py.example /app/config.py
EXPOSE 8000

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

#CMD [ "/usr/local/bin/python", "run.py"]
#CMD '/bin/bash'
CMD ["gunicorn", "megacosm:app", "-w", "4" ]
