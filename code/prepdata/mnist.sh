#!/bin/bash

set -e

printf "\033[0;32mDownloading the MNIST dataset\033[0m\n"

dest="${data_dir}/mnist"
raw_csv=/tmp/raw.csv
tidy_csv="${dest}/unadjusted.csv"
batched_csv="${dest}/noisy.csv"

wget https://pjreddie.com/media/files/mnist_test.csv -O $raw_csv

printf "\033[0;32mTidying the MNIST dataset\033[0m\n"

python mnist.py $raw_csv $tidy_csv
python artificial_batch.py $tidy_csv $batched_csv
