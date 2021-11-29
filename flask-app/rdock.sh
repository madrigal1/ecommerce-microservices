#!/usr/bin/env bash

docker-compose up -d db
sudo chown -R $USER /home/gokulkurup/root/Microservices-python/flask-app/.dbdata/
docker-compose up --build
