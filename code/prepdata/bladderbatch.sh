#!/bin/bash

data_dir=${data_dir:-"../data/"}
dest="${data_dir}/bladderbatch/"
out_csv="${dest}/bladderbatch.csv"

mkdir -p $dest

Rscript bladderbatch.R $out_csv
