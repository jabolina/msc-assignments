#!/usr/local/bin/gnuplot --persist

set terminal png size 1366,768;
set output ARG1;
set title ARG3;
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1;
plot ARG2 with linespoints linestyle 1
