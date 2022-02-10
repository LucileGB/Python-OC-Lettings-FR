#!/bin/bash

set -e

if [ "$CIRCLE_BRANCH" == "master" ]; then
    TAG=$CIRCLE_BUILD_NUM;
if [ "$CIRCLE_BRANCH" != "master" ]; then
        TAG="latest"

fidocker login --username $DOCKER_USER --password $DOCKER_PASS
docker build -t shardlabs/app:$TAG .
docker push shardlabs/app:$TAG
