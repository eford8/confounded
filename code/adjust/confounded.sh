#!/bin/bash

docker run -it \
    -v $(pwd)/../data/input/bladderbatch/:/confounded/data/bladderbatch \
    jdayton3/confounded data/bladderbatch/bladderbatch.csv -b batch
docker run -it \
    -v $(pwd)/../data/input/gse37199/:/confounded/data/gse37199 \
    jdayton3/confounded data/gse37199/gse37199.csv -b plate
docker run -it \
    -v $(pwd)/../data/input/mnist/:/confounded/data/mnist \
    jdayton3/confounded data/mnist/noisy.csv -b Batch
docker run -it \
    -v $(pwd)/../data/input/tcga/:/confounded/data/tcga \
    jdayton3/confounded data/tcga/tcga.csv -b CancerType
