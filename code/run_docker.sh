#! /bin/bash

set -e

image=srp33/confounded-paper:version1

docker build -t $image .

mkdir -p data/input/mnist data/input/bladderbatch data/input/gse37199 data/input/tcga
mkdir -p data/metrics

docker run -i -t --rm \
  -v $(pwd)/data:/data \
  $image
