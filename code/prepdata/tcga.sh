#!/bin/bash

set -e

printf "\033[0;32mDownloading the TCGA dataset\033[0m\n"

data_dir=${data_dir:-"../data/"}
dest="${data_dir}/tcga/"
rnaseq="${dest}/rnaseq.tsv.gz"
mutations="${dest}/mutations.tsv.gz"
labels="${dest}/labels.tsv.gz"
final="${dest}/tcga.csv"

mkdir -p $dest

if [ ! -f $rnaseq ]; then
    wget https://osf.io/7xjdn/download -O $rnaseq
fi
if [ ! -f $mutations ]; then
    wget https://osf.io/na3rp/download -O $mutations
fi
if [ ! -f $labels ]; then
    wget https://osf.io/frxv6/download -O $labels
fi

printf "\033[0;32mTidying the TCGA dataset\033[0m\n"

python tcga.py $rnaseq $mutations $labels $final
