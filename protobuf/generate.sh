#! /bin/bash

protoc -I=./ --python_out=../application --java_out=/home/zemanek/AndroidStudioProjects/sensorid/app/src/main/java/ ./SensorData.proto
mv ./SensorData.proto ./SensorData.proto.bak
cat ./SensorData.proto.bak | sed -e 's/de.hszemi.sensorid/de.hszemi.sensorid_test/g' -e 's/package sensorid/package sensorid_test/g' > ./SensorData.proto
protoc -I=./ --java_out=/home/zemanek/AndroidStudioProjects/sensorid-test/app/src/main/java/ ./SensorData.proto
protoc -I=./ --python_out=../application --java_out=/home/zemanek/AndroidStudioProjects/sensorid-test/app/src/main/java/ ./TestData.proto
rm ./SensorData.proto
mv ./SensorData.proto.bak ./SensorData.proto