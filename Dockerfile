# $ docker build -t spunkybot .
# $ 
FROM python:2-slim
MAINTAINER "Alexander Kress <feedback@spunkybot.de>"
WORKDIR /usr/src/app
COPY  "." "/usr/src/app"
CMD [ "python", "./spunky.py" ]
