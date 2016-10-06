#! /bin/bash

../test.py --silent --cdf data-cdf-limit-5.dat --limittraining 0.5 --limitfeatures 13 ../data.set2
../test.py --silent --cdf data-cdf-nolimit-5.dat --limittraining 1 --limitfeatures 13 ../data.set2

../test.py --silent --cdf data-cdf-limit-10.dat --limittraining 0.5 --limitfeatures 13 --default-training-size 10 ../data.set2
../test.py --silent --cdf data-cdf-nolimit-10.dat --limittraining 1 --limitfeatures 13 --default-training-size 10 ../data.set2

gnuplot cdfs.plot
