#!/bin/bash

set -e

printf "\033[0;32mAdjusting the data with a linear scaler\033[0m\n"

Rscript combat.R "/data/input/mnist/noisy.csv" -a scale -b Batch
#Rscript combat.R "../data/input/bladderbatch/bladderbatch.csv" -a scale -b batch
#Rscript combat.R "../data/input/gse37199/gse37199.csv" -a scale -b plate
#Rscript combat.R "../data/input/tcga/tcga.csv" -a scale -b CancerType
