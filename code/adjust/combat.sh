#!/bin/bash

Rscript combat.R "../data/input/mnist/noisy.csv" -b Batch
Rscript combat.R "../data/input/bladderbatch/bladderbatch.csv" -b batch
Rscript combat.R "../data/input/gse37199/gse37199.csv" -b plate
Rscript combat.R "../data/input/tcga/tcga.csv" -b CancerType
