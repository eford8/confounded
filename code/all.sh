#!/bin/bash

set -e

cd prepdata
bash all.sh
cd ../
exit

cd adjust
bash all.sh
cd ../
exit

cd metrics
bash all.sh
cd ../

cd figures
bash all.sh
cd ../