#!/bin/bash

set -e

printf "\033[0;32mDownloading the GSE37199 dataset\033[0m\n"

data_dir=${data_dir:-"../data/"}
dest="${data_dir}/gse37199/"
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

printf "\033[0;32mTidying the GSE37199 dataset\033[0m\n"

python gse37199.py $expression_tsv $clinical_tsv $out_csv
