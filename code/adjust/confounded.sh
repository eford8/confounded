#!/bin/bash

set -e

printf "\033[0;32mAdjusting the data with Confounded\033[0m\n"

docker run -it \
    -v $(pwd)/../data/input/bladderbatch/:/confounded/data/bladderbatch \
    jdayton3/confounded data/bladderbatch/bladderbatch.csv -b batch
docker run -it \
    -v $(pwd)/../data/input/gse37199/:/confounded/data/gse37199 \
    jdayton3/confounded data/gse37199/gse37199.csv -b plate
docker run -it \
    -v $(pwd)/../data/input/mnist/:/confounded/data/mnist \
    -v $(pwd)/../data/metrics/:/confounded/data/log \
    jdayton3/confounded data/mnist/noisy.csv -b Batch \
    -f data/log/log.csv # save a log for our loss chart
docker run -it \
    -v $(pwd)/../data/input/tcga/:/confounded/data/tcga \
    jdayton3/confounded data/tcga/tcga.csv -b CancerType
