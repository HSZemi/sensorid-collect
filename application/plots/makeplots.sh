#! /bin/bash

./generate_plot_data.py
gnuplot rotation.plot
convert out-a.png out-b.png +append sensor_traces_rotation_comparison.png

