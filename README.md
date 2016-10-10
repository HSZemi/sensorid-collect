sensorid-collect
================

Collection and identification of sensor data from sensorid. Also: Preprocessing.


Collection
----------

*The app "Sensorid" provides the sensor readings for this step*

    application/logcollector.py <directory>

logcollector.py listens on port 54321 for incoming data transmissions and stores the data in the given directory.

The data is organized in the scheme data/SENSOR_NAME/log-TIMESTAMP.csv.

Command line arguments may set host and port to other values.

Preprocessing
-------------

    application/processData.py <directory>

There are 3 preprocessing steps, called via command line arguments:
  * --classes: create an auxiliary file that matches sensor names to sensor classes
  * --unify: merge the data from the csv files into a unified data structure
  * --extract: extract feature vectors from the unified data structure and store them

The three steps can be called individually or alltogether with the command line switch -a / --all

In the end, the feature vectors are used for classification and hence identification.


Classification
--------------

    application/test.py <directory>

Loads the data from directory/normalizeddata.json and directory/enhancedsensors.json.

For each sensor type, randomly selects a subset of the data for training and trains a classifier.

Classifies the rest of the data and calculates a success rate.

Prints statistics about the data and the success rate.

Command line arguments may modify training set size and the area from which training data stems.

Command line arguments may specify output files for the statistics as csv file or cdf data for each sensor.

A Command line argument may determine the subset of features used (where 1 is just the first feature, 
2 the first two features, and so on).


Identification
--------------

*The app "Sensorid-test" provides the feature vectors for this step and receives the prediction*

    application/testinterface.py <directory>

Reads the prepared feature vectors and prepares classifiers for the different sensor types from the directory.

Listens on port 54322 for incoming feature vectors, gets a prediction from the corresponding classifier, and returns the prediction to the requesting client.

Command line arguments may set host and port to other values.

A Command line argument may determine the subset of features used (where 1 is just the first feature, 
2 the first two features, and so on).
