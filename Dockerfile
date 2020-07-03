FROM python:rc

RUN mkdir /src
WORKDIR /src
COPY . /src/

ADD ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
