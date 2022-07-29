#!/bin/sh -l

# chmod +x run.sh



model=$(cat $1)
echo "::set-output name=model::$model"

time=$(date)
echo "::set-output name=time::$time"

location=$(pwd)
echo "::set-output name=location::$location"
