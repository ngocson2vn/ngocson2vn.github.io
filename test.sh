#!/bin/sh

IMAGE=$1
echo IMAGE=$IMAGE

sh mkdockerize.sh $IMAGE `pwd`/sample > /dev/null 2>&1 &
sleep 15
cname=$(docker ps --format "{{.Names}}")
echo "Container name: $cname"

status=$(docker run --link $cname byrnedo/alpine-curl curl -sI http://$cname:8000/ | head -1 | awk '{print $2}')
echo "Status: $status"
if [ "$status" = "200" ]; then
  echo "PASSED"
else
  echo "FAILED"
  exit 1
fi
