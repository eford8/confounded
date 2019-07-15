#!/bin/bash

set -e

printf "\033[0;32mCalculating MSE\033[0m\n"

out_dir="${data_dir}:-../data/metrics"
out_path="${out_dir}/mse.csv"
in_dirs=$(ls -d ../data/input/*)

mkdir -p $out_dir

python mse.py -i $in_dirs -o $out_path
