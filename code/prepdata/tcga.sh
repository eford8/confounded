#!/bin/bash

set -e

printf "\033[0;32mDownloading the TCGA dataset\033[0m\n"

dest="${data_dir}/tcga"
rnaseq="/tmp/rnaseq.tsv.gz"
mutations="/tmp/mutations.tsv.gz"
labels="/tmp/labels.tsv.gz"
final="${dest}/tcga.csv"

wget https://osf.io/7xjdn/download -O $rnaseq
wget https://osf.io/na3rp/download -O $mutations
wget https://osf.io/frxv6/download -O $labels

printf "\033[0;32mTidying the TCGA dataset\033[0m\n"

python tcga.py $rnaseq $mutations $labels $final
