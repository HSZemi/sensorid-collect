sensorid-collect
================

Collection and identification of sensor data from sensorid. Also: Preprocessing.


Collection
----------

*The app "Sensorid" provides the sensor readings for this step*

'''application/logcollector.py'''

logcollector.py listens on port 54321 for incoming data transmissions and stores the data in the directory 'application/data'.

The data is organized in the scheme data/SENSOR_NAME/log-TIMESTAMP.csv.


Preprocessing
-------------

'''application/processData.py <directory>'''

There are 3 preprocessing steps, called via command line arguments:
  * --classes: create an auxiliary file that matches sensor names to sensor classes
  * --unify: merge the data from the csv files into a unified data structure
  * --extract: extract feature vectors from the unified data structure and store them

The three steps can be called individually or alltogether with the command line switch -a / --all

In the end, the feature vectors are used for classification and hence identification.


Identification
--------------

*The app "Sensorid-test" provides the feature vectors for this step and receives the prediction*

'''application/testinterface.py'''

Reads the prepared feature vectors and prepares classifiers for the different sensor types.

Listens on port 54322 for incoming feature vectors, gets a prediction from the corresponding classifier, and returns the prediction to the requesting client.