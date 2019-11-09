FROM redis:5
LABEL maintainer="Jesse Morgan <morgajel@gmail.com>"
WORKDIR /app
#COPY megacosm log run.py requirements.txt /app/
COPY ./data /app


CMD [ "redis-server" ]
#RUN cat /app/* | redis-cli --pipe
EXPOSE 6379


