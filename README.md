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

## Algorithms

Model |Data      |Total|Mislabeld|FalsePositive|FalseNegative|PercentageFalse|PercentageFN
------|----------|-----|---------|-------------|-------------|---------------|------------
Dict  |train     |39862|10794    |0            |10794        |27.08%         | 100
Dict  |validation|9966 |2718     |0            |2718         |27.27%         | 100
Dict  |test      |12458|3400     |1            |3399         |27.29%         |~100
Bayes |train     |39862|3184     |323          |2861         |7.98%          |  90
Bayes |validation|9966 |779      |79           |700          |7.81%          |  90
Bayes |test      |12458|1025     |110          |915          |8.22%          |  89
Markov|train     |39862|110      |110          |0            |2.76%          |   0
Markov|validate  |9966 |150      |29           |121          |1.51%          |  80
Markov|test      |12458|173      |43           |130          |1.39%          |  75
nohidd|train     |39862|1308     |748          |560          |3.28%          |  43
nohidd|validate  |9966 |338      |194          |144          |3.39%          |  43
nohidd|test      |12458|412      |263          |149          |3.31%          |  36


# Analysis

verschiedene Eingabegroessen testen
Testdaten grössen

Model | CPUtime test() | Memory Usage (inc. Train) |
------|----------------|---------------------------|
Dict  | 511.00s        | 132 Mb                    |
Bayes |   1.55s        | 121 Mb                    |
Markov|   2.69s        |  79 Mb                    |
Keras |   1.97s        | 252 Mb                    |