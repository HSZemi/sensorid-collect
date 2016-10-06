set terminal pdf size 9,8 linewidth 5
set output 'cdfs.pdf'

set xlabel "success rate";

set key inside top left autotitle columnhead

set multiplot layout 2, 2 title "CDFs for testing data from different rotations" font ",14"
set tmargin 3

set title "Using 5 random samples over all four rotations for training"
plot "data-cdf-nolimit-5.dat" using 0:1 with lines, "" using 0:2 with lines, "" using 0:3 with lines, "" using 0:4 with lines, "" using 0:5 with lines, "" using 0:6 with lines, "" using 0:7 with lines

set title "Using 5 random samples over two rotations for training"
plot "data-cdf-limit-5.dat" using 0:1 with lines, "" using 0:2 with lines, "" using 0:3 with lines, "" using 0:4 with lines, "" using 0:5 with lines, "" using 0:6 with lines, "" using 0:7 with lines

set title "Using 10 random samples over all four rotations for training"
plot "data-cdf-nolimit-10.dat" using 0:1 with lines, "" using 0:2 with lines, "" using 0:3 with lines, "" using 0:4 with lines, "" using 0:5 with lines, "" using 0:6 with lines, "" using 0:7 with lines

set title "Using 10 random samples over two rotations for training"
plot "data-cdf-limit-10.dat" using 0:1 with lines, "" using 0:2 with lines, "" using 0:3 with lines, "" using 0:4 with lines, "" using 0:5 with lines, "" using 0:6 with lines, "" using 0:7 with lines