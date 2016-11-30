FROM ubuntu:latest
MAINTAINER Adele Kapellusch <adelekoutia@gmail.com>
RUN apt-get update
RUN apt-get -y install sudo
RUN sudo apt-get -y install python
RUN sudo apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN apt-get install -y git
RUN pip install owslib
RUN pip install lxml
RUN apt-get install -y libxml2
RUN pip install git+https://github.com/USGS-CIDA/pyGDP.git@v1.3.1#egg=pyGDP
RUN git clone https://github.com/ksaxberg/final_teamAZ.git


