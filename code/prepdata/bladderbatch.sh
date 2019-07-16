#!/bin/bash

set -e

printf "\033[0;32mDownloading and tidying the bladderbatch dataset\033[0m\n"

dest="${data_dir}/bladderbatch"
out_csv="${dest}/bladderbatch.csv"

Rscript bladderbatch.R $out_csv
