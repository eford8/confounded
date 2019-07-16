#!/bin/bash

set -e

export data_dir="../data/input/"
bash mnist.sh
bash bladderbatch.sh
bash gse37199.sh
bash tcga.sh
