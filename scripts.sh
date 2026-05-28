#!/bin/bash

TAG="latest"

while getopts "t:" opt; do
  case $opt in
    t) TAG=$OPTARG ;;
  esac
done

echo "Building with tag: $TAG"

docker compose build
docker compose up -d