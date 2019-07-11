#!/bin/bash

dest="../data/bladderbatch/"
out_csv="${dest}/bladderbatch.csv"

mkdir -p $dest

Rscript bladderbatch.R $out_csv
