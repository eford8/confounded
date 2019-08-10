#!/bin/bash

set -e

printf "\033[0;32mAdjusting the data with Confounded\033[0m\n"

# We also save a log for our loss chart
confounded /data/mnist/unadjusted.csv -o /data/mnist/confounded.csv -b Batch --learning-rate 0.0001 -f /output/metrics/mnist_confounded_log.csv
exit
##confounded /data/mnist/unadjusted.csv -b Batch --learning-rate 0.001  -f /output/metrics/mnist_confounded_log2.csv

confounded /data/bladderbatch/unadjusted.csv -o /data/bladderbatch/confounded.csv -b batch
confounded /data/gse37199/unadjusted.csv -o /data/gse37199/confounded.csv -b plate

confounded /data/tcga/unadjusted.csv -o /data/tcga/confounded.csv -b CancerType
confounded /data/tcga_medium/unadjusted.csv -o /data/tcga_medium/confounded.csv -b CancerType
confounded /data/tcga_small/unadjusted.csv -o /data/tcga_small/confounded.csv -b CancerType
