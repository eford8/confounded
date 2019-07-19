#!/bin/bash

set -e

printf "\033[0;32mDownloading the TCGA dataset\033[0m\n"

dest="${data_dir}/tcga"
medium="${data_dir}/tcga_medium"
small="${data_dir}/tcga_small"
rnaseq="/tmp/rnaseq.tsv.gz"
mutations="/tmp/mutations.tsv.gz"
labels="/tmp/labels.tsv.gz"
final="${dest}/tcga.csv"

# This gets the TCGA RNA-Seq dataset
wget -O /tmp/GSE62944_RAW.tar "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file"
cd /tmp
tar -xvf GSE62944_RAW.tar
rm GSE62944_RAW.tar
mv GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz rnaseq.tsv.gz
python /prepdata/transpose_matrix.py rnaseq.tsv.gz rnaseq2.tsv.gz
python /prepdata/tcga_expression.py rnaseq2.tsv.gz $rnaseq

### Old version. Only has RNA-Seq data for ~300 genes
###wget https://osf.io/7xjdn/download -O $rnaseq

cd /prepdata

wget https://osf.io/na3rp/download -O $mutations
wget https://osf.io/frxv6/download -O $labels

printf "\033[0;32mTidying the TCGA dataset\033[0m\n"

python tcga.py $rnaseq $mutations $labels $final

# Do the subsampling stuff
mkdir -p $medium
mkdir -p $small
Rscript tcga_sampling.R
