FROM python:3.7
LABEL MAINTAINER="Jesse Morgan <morgajel@gmail.com>"
WORKDIR /app
COPY ./megacosm/ /app/megacosm/
COPY config.py logging.conf requirements.txt /app/
EXPOSE 8000

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

#CMD [ "/usr/local/bin/python", "run.py"]
#CMD '/bin/bash'
CMD ["gunicorn", "megacosm:app", "-w", "4",  "--log-config", "/app/logging.conf", "-b", ":8000" ]
