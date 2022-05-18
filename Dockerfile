FROM ubuntu:latest

MAINTAINER zeldegiz

ADD dynamicli dynamicli
WORKDIR dynamicli

RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip \
&& apt-get install -y libpcap0.8 && pip3 install -r requirements.txt
