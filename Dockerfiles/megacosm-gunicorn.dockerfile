FROM python:3.7
MAINTAINER "Jesse Morgan <morgajel@gmail.com>
COPY requirements.txt ./
COPY config.py.example ./config.py
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "run.py"]
