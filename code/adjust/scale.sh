#!/bin/bash

set -e

printf "\033[0;32mAdjusting the data with a linear scaler\033[0m\n"

Rscript adjust.R "/data/input/mnist/noisy.csv" -a scale -b Batch
Rscript adjust.R "/data/input/bladderbatch/bladderbatch.csv" -a scale -b batch
Rscript adjust.R "/data/input/gse37199/gse37199.csv" -a scale -b plate
Rscript adjust.R "/data/input/tcga/tcga.csv" -a scale -b CancerType
