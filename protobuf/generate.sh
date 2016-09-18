#! /bin/bash

protoc -I=./ --python_out=../logcollector --java_out=../../app/src/main/java/ ./SensorData.proto