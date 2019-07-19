#!/bin/bash

set -e

printf "\033[0;32mAdjusting the data with Confounded\033[0m\n"

# We also save a log for our loss chart
#confounded /data/input/mnist/noisy.csv -b Batch -f /data/metrics/mnist_confounded_log.csv
#confounded /data/input/bladderbatch/bladderbatch.csv -b batch
#confounded /data/input/gse37199/gse37199.csv -b plate
confounded /data/input/tcga/tcga.csv -b CancerType
