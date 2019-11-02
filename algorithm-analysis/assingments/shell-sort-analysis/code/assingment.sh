#!/bin/zsh

declare -a types=("random" "repeated" "ordered")

for type in "${types[@]}"; do
        for i in $(seq 10 20); do
                size=$((2**$i))
                echo "Generating $type array of size: $size"
                python generator.py $type $size "samples/file-$size-random"
        done
done
