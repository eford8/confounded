#!/bin/bash

dest="../data/gse37199/"
raw="${dest}/raw/"
raw_loc="${raw}/raw.tar.gz"
expression_tsv="${raw}/GSE37199_Expression_BatchUnadjusted.txt.gz"
clinical_tsv="${raw}/GSE37199_Clinical.txt"
out_csv="${dest}/gse37199.csv"

mkdir -p $raw

if [ ! -f $raw_loc ]; then
    wget https://osf.io/av3yt/download -O $raw_loc
fi
tar -zxvf $raw_loc -C $raw

python gse37199.py $expression_tsv $clinical_tsv $out_csv
