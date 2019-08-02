#!/bin/bash

set -e

printf "\033[0;32mCalculating classification accuracy\033[0m\n"

#in_dirs=$(ls -d /data/*)
in_dirs=$(ls -d /data/bladderbatch)
out_path1="/output/metrics/batch_classification.csv"
out_path2="/output/metrics/true_classification.csv"

python classify.py -i $in_dirs -o $out_path1 -p $out_path2
