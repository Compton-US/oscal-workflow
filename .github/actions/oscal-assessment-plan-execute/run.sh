#!/bin/sh -l

# chmod +x run.sh

cat $1

time=$(date)
echo "::set-output name=time::$time"

location=$(pwd)
echo "::set-output name=location::$location"
