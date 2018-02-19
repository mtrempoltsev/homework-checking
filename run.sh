#!/bin/bash

cp data/$1/* $2
docker build -t $3 $2 > /dev/null
docker run --stop-timeout=5 $3

exit 0
