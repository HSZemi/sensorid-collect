set terminal png size 1000,2000
set output 'out-a.png'

set pointsize 0.1;
set xrange [-500000000.0:5500000000.0];
#set yrange [-3:14];
#set yrange [-80:140];
set yrange [-1:1];
set xlabel "time / ns";
set ylabel "sensor value"

#
# Gnuplot version 5.0 demo of multiplot auto-layout capability
#
#
set multiplot layout 4, 2 title "Nexus 6 , device 5+7, sensor Invensense Linear Acceleration" font ",14"
set tmargin 4
set title "Nexus6x05-0"
plot "Nexus6x05-0-a.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-0-a.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-0-a.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-0"
plot "Nexus6x07-0-a.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-0-a.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-0-a.dat" using 1:4 with points pointtype 1 title 'z';
#
set title "Nexus6x05-1"
plot "Nexus6x05-1-a.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-1-a.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-1-a.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-1"
plot "Nexus6x07-1-a.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-1-a.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-1-a.dat" using 1:4 with points pointtype 1 title 'z';
#
set title "Nexus6x05-2"
plot "Nexus6x05-2-a.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-2-a.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-2-a.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-2"
plot "Nexus6x07-2-a.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-2-a.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-2-a.dat" using 1:4 with points pointtype 1 title 'z';
#
set title "Nexus6x05-3"
plot "Nexus6x05-3-a.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-3-a.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-3-a.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-3"
plot "Nexus6x07-3-a.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-3-a.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-3-a.dat" using 1:4 with points pointtype 1 title 'z';
#
unset multiplot
#
#
#
set terminal png size 1000,2000
set output 'out-b.png'

set pointsize 0.1;
set xrange [-500000000.0:5500000000.0];
#set yrange [-3:14];
set yrange [-80:100];
#set yrange [-1:1];
set xlabel "time / ns";

#
# Gnuplot version 5.0 demo of multiplot auto-layout capability
#
#
set multiplot layout 4, 2 title "Nexus 6, device 5+7, sensor Invensense Magnetometer" font ",14"
set tmargin 4
set title "Nexus6x05-0"
plot "Nexus6x05-0-b.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-0-b.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-0-b.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-0"
plot "Nexus6x07-0-b.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-0-b.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-0-b.dat" using 1:4 with points pointtype 1 title 'z';
#
set title "Nexus6x05-1"
plot "Nexus6x05-1-b.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-1-b.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-1-b.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-1"
plot "Nexus6x07-1-b.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-1-b.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-1-b.dat" using 1:4 with points pointtype 1 title 'z';
#
set title "Nexus6x05-2"
plot "Nexus6x05-2-b.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-2-b.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-2-b.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-2"
plot "Nexus6x07-2-b.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-2-b.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-2-b.dat" using 1:4 with points pointtype 1 title 'z';
#
set title "Nexus6x05-3"
plot "Nexus6x05-3-b.dat" using 1:2 with points pointtype 5 title 'x', "Nexus6x05-3-b.dat" using 1:3 with points pointtype 5 title 'y', "Nexus6x05-3-b.dat" using 1:4 with points pointtype 5 title 'z';
#
set title "Nexus6x07-3"
plot "Nexus6x07-3-b.dat" using 1:2 with points pointtype 1 title 'x', "Nexus6x07-3-b.dat" using 1:3 with points pointtype 1 title 'y', "Nexus6x07-3-b.dat" using 1:4 with points pointtype 1 title 'z';
#
unset multiplot
#
#
#


