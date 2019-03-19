FROM python:3-alpine

COPY requirements.txt /

RUN apk update && apk upgrade && apk add postgresql-dev && apk add build-base
RUN pip install -r ./requirements.txt --no-cache-dir

 
