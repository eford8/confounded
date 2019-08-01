#!/bin/bash

set -e

printf "\033[0;32mCalculating MMD\033[0m\n"

out_path="/output/metrics/mmd.csv"
in_dirs=$(ls -d /data/input/*)

python mmd.py -i $in_dirs -o $out_path
