#!/bin/sh -l

# chmod +x run.sh

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"