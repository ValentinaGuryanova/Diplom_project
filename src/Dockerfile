#FROM ubuntu:latest
#LABEL authors="gurya"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .