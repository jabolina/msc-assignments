#!/bin/bash

rm -rf graphs/*

for data in $(ls *.dat); do
        echo "Generating graph for $data";
        title=$(echo $data | cut -d"-" -f2)
        gnuplot -c plot.gnu "graphs/$title.png" $data $title
done;
