#!/bin/bash

rm -f *.dat

for file in $(ls samples/**/*); do
        type=$(echo $file | cut -d"/" -f2)
        out_to=$(echo "times-$type-output.dat")
        echo "Executing shell sort with file $file outputing time in $out_to"; 
        python shell_sort.py "$file" >> $out_to 
done;
