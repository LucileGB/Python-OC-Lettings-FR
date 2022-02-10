#!/bin/bash

set -e

if [ "$CIRCLE_BRANCH" == "master" ]; then
    TAG=$CIRCLE_BUILD_NUM;
elif [ "$CIRCLE_BRANCH" != "master" ]; then
        TAG="latest"

docker login --username $DOCKER_USER --password $DOCKER_PASS
docker build -t lgarrigoux/oc_lettings:$TAG .
docker push lgarrigoux/oc_lettings:$TAG
