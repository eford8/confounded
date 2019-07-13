#!/bin/bash

out_dir="${data_dir}:-../data/metrics"
out_path="${out_dir}/mmd.csv"
in_dirs=$(ls -d ../data/input/*)

mkdir -p $out_dir

python mmd.py -i $in_dirs -o $out_path
