#!/usr/bin/zsh

TIMEFMT='%J   %U  user %S system %P cpu %*E total'$'\n'\
'avg shared (code):         %X KB'$'\n'\
'avg unshared (data/stack): %D KB'$'\n'\
'total (sum):               %K KB'$'\n'\
'max memory:                %M MB'$'\n'\
'page faults from disk:     %F'$'\n'\
'other page faults:         %R'

#declare -a tests=("test_none.py" "test_dict.py" "test_bayes.py" "test_markov.py" "test_keras.py")
declare -a tests=("test_none.py")
declare -a size=("1" "10" "100" "500" "1000" "2000" "2500" "5000" "7500" "10000" "15000" "20000" "25000" "50000" "75000" "100000" "150000" "200000" "250000")
for t in "${size[@]}"
do
    for i in "${tests[@]}"
    do
        echo "$i $t"
        time python $i $t >/dev/null
    done
done