#!/bin/bash

export data_dir="../data/metrics/"

bash ./mse.sh
bash ./mmd.sh
bash ./classify.sh
