#!/usr/bin/zsh

TIMEFMT='%Mmb'

declare -a tests=("test_dict.py" "test_bayes.py" "test_markov.py" "test_keras.py")
declare -a size=("1" "10" "50" "100" "200" "300" "500" "750" "1000" "2000" "3000" "5000")
for t in "${size[@]}"
do
    for i in "${tests[@]}"
    do
        echo "$i $t"
        time python $i $t >/dev/null
    done
done