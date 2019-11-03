#!/bin/bash

declare -a types=("random" "repeated" "ordered")
rm -rf samples/*

for type in "${types[@]}"; do
        mkdir "samples/$type"

        for i in $(seq 10 25); do
                size=$((2**$i))
                echo "Generating $type array of size: $size"
                python generator.py $type $size "samples/$type/sample-$i"
        done
done
