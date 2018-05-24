# Thesis

This repository will contain all the code for my bachelors thesis.

## comands for datacleanup:

```sh
 # splitt merged data at whitespace
 cat 000_merged.txt | sed -E -e 's/[[:blank:]]+/\n/g' > 001_split.txt
 # remove empty lines
 grep . 001_split.txt > 002_noEmptylines.txt
 # sort
 sort 002_noEmptylines.txt > 003_sorted.txt
 # remove duplicates
 cat 003_sorted.txt | uniq > 004_uniq.txt
 # remove everything with no letter
 sed -e '/[a-zA-Z]/!d' 004_uniq.txt > 005_atleastoneletter.txt
 # call strings
 strings 005_atleastoneletter.txt > 006_strings.txt
 # split up enumerations
 sed 's/,/\n/' 006_strings.txt > 007_splitEnums.txt
 # strip all non letter symbols from start
 sed 's/^[^[:alpha:]]\+//' 007_splitEnums.txt > 008_startingAlpha.txt
 # strip all non letter symbols from end
 sed 's/[^[:alpha:]]\+$//' 008_startingAlpha.txt > 009_trimNonAlpha.txt
 # sort once more
 sort 009_trimNonAlpha.txt >  010_trimNonAlpha.sorted.txt
 # remove duplicates once more
 cat 010_trimNonAlpha.sorted.txt | uniq > 011_uniq.txt
 # run strings once more
 strings 011_uniq.txt > 012_strings.txt
```

## featureExtractor.py

featureExtractor.py extracts all the features to be used by our algorithms

## datasetSplitter.py

datasetSplitter.py splits our extracted features into train, validation and test datasets