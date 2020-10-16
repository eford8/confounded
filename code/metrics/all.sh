#!/bin/bash

set -e

numSamples="$1"
numInformativeFeatures="$2"
codeSize="$3"
scaler="$4"
#bash ./mse.sh
#bash ./mmd.sh
bash ./classify.sh "$numSamples" "$numInformativeFeatures" "$codeSize" "$scaler"
