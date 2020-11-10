FROM python:3.6.8-jessie

WORKDIR /app

RUN apt-get -y update
    && apt-get -y upgrade
    && apt-get install -y mysql-client

RUN pip install --upgrade pip

COPY . /app

ENV PYTHONUNBUFFERED=1

RUN pip3 install -r requirements.txt

EXPOSE 8080

USER 1000
ENTRYPOINT ["/app/docker/python/entrypoint.sh"]
