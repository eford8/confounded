#!/bin/bash

set -e

printf "\033[0;32mCalculating classification accuracy\033[0m\n"

batch_out_path="/output/metrics/batch_classification.csv"
true_out_path="/output/metrics/true_classification.csv"

rm -f ${batch_out_path} ${true_out_path}

# It doesn't make sense to measure true-class accuracy for bladderbatch because it is confounded with batch
#python classify.py -i /data/mnist -o ${batch_out_path} -c Batch
#python classify.py -i /data/mnist -o ${true_out_path} -c Digit
python classify.py -i /data/bladderbatch -o ${batch_out_path} -c batch
#python classify.py -i /data/gse37199 -o ${batch_out_path} -c plate
#python classify.py -i /data/gse37199 -o ${true_out_path} -c Stage
#python classify.py -i /data/tcga -o ${batch_out_path} -c CancerType
#python classify.py -i /data/tcga -o ${true_out_path} -c TP53_Mutated
