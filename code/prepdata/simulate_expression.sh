#!/bin/bash

set -e

printf "\033[0;32mPreparing a simulated gene-expression dataset\033[0m\n"
numSamples="$1"
numRandomFeatures="$2"
numRedundantFeatures="$3"
numInformativeFeatures="$4"
python simulate_expression.py /data/simulated_expression/unadjusted1.csv "$numSamples" "$numRandomFeatures" "$numRedundantFeatures" "$numInformativeFeatures"