#!/bin/bash

set -e

printf "\033[0;32mGenerating loss figure\033[0m\n"
printf "\033[0;32mThis is good code but bad data. Find a better dataset to get this data from.\033[0m\n"

mkdir -p "../data/output"

Rscript loss.R
