#!/bin/bash

set -e

bash overview_and_network.sh
bash loss.sh
bash pca_and_tsne.sh
bash mse_mmd_classification.sh
bash mnist.sh
