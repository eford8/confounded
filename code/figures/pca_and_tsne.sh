#!/bin/bash

set -e

printf "\033[0;32mGenerating PCA and t-SNE figures\033[0m\n"

Rscript pca_and_tsne.R
