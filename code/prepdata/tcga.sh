#!/bin/bash

dest="../data/tcga/"
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

python tcga.py $rnaseq $mutations $labels $final
