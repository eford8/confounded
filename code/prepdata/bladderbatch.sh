#!/bin/bash

set -e

printf "\033[0;32mDownloading and tidying the bladderbatch dataset\033[0m\n"

data_dir=${data_dir:-"../data/"}
dest="${data_dir}/bladderbatch/"
out_csv="${dest}/bladderbatch.csv"

mkdir -p $dest

Rscript bladderbatch.R $out_csv
