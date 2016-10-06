#! /bin/bash

# get test data for all four datasets

#./processData.py -a --silent data.set1
#./processData.py -a --silent data.set2
#./processData.py -a --silent data.set3
#./processData.py -a --silent data.set4

./test.py --csv set1-13.csv --limitfeatures 13 --silent data.set1
./test.py --csv set2-13.csv --limitfeatures 13 --silent data.set2
./test.py --csv set3-13.csv --limitfeatures 13 --silent data.set3
./test.py --csv set4-13.csv --limitfeatures 13 --silent data.set4

./test.py --csv set1-all.csv --silent data.set1
./test.py --csv set2-all.csv --silent data.set2
./test.py --csv set3-all.csv --silent data.set3
./test.py --csv set4-all.csv --silent data.set4
