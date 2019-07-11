#!/bin/bash

dest="../data/mnist/"
raw_csv="${dest}/raw.csv"
tidy_csv="${dest}/unadjusted.csv"
batched_csv="${dest}/noisy.csv"

mkdir -p $dest

if [ ! -f $raw_csv ]; then
    wget https://pjreddie.com/media/files/mnist_test.csv -O $raw_csv
fi

python mnist.py $raw_csv $tidy_csv
python artificial_batch.py $tidy_csv $batched_csv
