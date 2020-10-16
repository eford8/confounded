#!/bin/bash

set -e

numSample="$1"
numRandomFeatures="$2"
numRedundantFeatures="$3"
numInformativeFeatures="$4"
bash simulate_expression.sh "$numSample" "$numRandomFeatures" "$numRedundantFeatures" "$numInformativeFeatures"
#bash mnist.sh
#bash bladderbatch.sh
#bash gse37199.sh
#bash tcga.sh
