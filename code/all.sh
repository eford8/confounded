#!/bin/bash

set -e

cd prepdata
bash all.sh
exit
cd ../

cd adjust
bash all.sh
cd ../

cd metrics
bash all.sh
cd ../

cd figures
bash all.sh
cd ../
