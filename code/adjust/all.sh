#!/bin/bash

set -e
codeSize="$1"
scaler="$2"
bash ./scale.sh
bash ./combat.sh
bash ./confounded.sh $codeSize $scaler
