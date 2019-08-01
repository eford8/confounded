#!/bin/bash

set -e

printf "\033[0;32mAdjusting the data with ComBat\033[0m\n"

#Rscript adjust.R "/data/input/mnist/noisy.csv" -b Batch
Rscript adjust.R /data/bladderbatch/unadjusted.csv /data/bladderbatch/combat.csv -b batch
#Rscript adjust.R "/data/input/gse37199/gse37199.csv" -b plate
#Rscript adjust.R "/data/input/tcga/tcga.csv" -b CancerType
#Rscript adjust.R "/data/input/tcga_medium/tcga_medium.csv" -b CancerType
#Rscript adjust.R "/data/input/tcga_small/tcga_small.csv" -b CancerType
