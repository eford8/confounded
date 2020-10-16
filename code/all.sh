    !/bin/bash

set -e


for sampleSize in 100 200 300
do
    for codeSize in 20
    do
        cd prepdata
        bash all.sh $sampleSize 800 175 25 
        cd ../

        cd adjust
        bash all.sh $codeSize "sigmoid"
        cd ../

        cd metrics 
        bash all.sh $sampleSize 25 $codeSize "sigmoid"
        cd ../

        cd prepdata
        bash all.sh $sampleSize 950 40 10
        cd ../

        cd adjust
        bash all.sh $codeSize "sigmoid"
        cd ../

        cd metrics 
        bash all.sh $sampleSize 10 $codeSize "sigmoid"
        cd ../

        cd prepdata
        bash all.sh $sampleSize 990 8 2
        cd ../

        cd adjust
        bash all.sh $codeSize "sigmoid"
        cd ../

        cd metrics 
        bash all.sh $sampleSize 2 $codeSize "sigmoid"
        cd ../
    done
done

   

    #cd figures
    #bash all.sh
    #cd ../
