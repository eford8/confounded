#!/bin/bash

set -e

printf "\033[0;32mCalculating MSE\033[0m\n"

out_path="/output/metrics/mse.csv"
in_dirs=$(ls -d /data/input/*)

python mse.py -i $in_dirs -o $out_path
