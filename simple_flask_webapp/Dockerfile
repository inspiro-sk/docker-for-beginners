FROM ubuntu:18.04

RUN apt-get upgrade && apt-get update
RUN apt-get install -y python python-pip
RUN pip install flask

COPY app.py /opt/app.py
COPY /templates/index.html /opt/templates/index.html

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
