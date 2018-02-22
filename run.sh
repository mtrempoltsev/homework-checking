#!/bin/bash

cp data/$1/* $2
docker build -t $3 $2 > /dev/null
id=$(docker run -d -v /$2/out:/out $3)
docker stop -t=5 ${id} > /dev/null
docker container rm ${id} > /dev/null

cat /$2/out/out.txt

exit 0
