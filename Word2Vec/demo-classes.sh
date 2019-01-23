#!/usr/bin/env bash
#make
#if [ ! -e text8 ]; then
#  wget http://mattmahoney.net/dc/text8.zip -O text8.gz
#  gzip -d text8.gz -f
#fi
time ./word2vec -train "/Users/anirudhprabhu/PycharmProjects/AnE-Extractor/Data/processed_copy.txt.out" -output classes.txt -cbow 1 -size 1000 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -iter 15 -classes 50
sort classes.txt -k 2 -n > Processed_Clus.txt
echo The word classes were saved to file classes.sorted.txt

