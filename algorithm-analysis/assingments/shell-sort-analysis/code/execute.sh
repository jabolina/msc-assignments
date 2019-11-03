#!/bin/bash

chmod +x run_ss.sh
chmod +x generate_samples.sh
chmod +x gen_graphs.sh

printf "Starting samples generation:\n\n"
./generate_samples.sh

printf "Running shell sort on generated files:\n\n"
./run_ss.sh

print "Plotting graphs\n"
./gen_graphs.sh

echo "Finished."
