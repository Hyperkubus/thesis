import pprint
import numpy as np
import pandas as pd
import time
import binascii
import pickle
from Utils.DataLoader import hex2string

def cleanData(data):
    data = data['hex'].apply(hex2string)
    data = data.reset_index(drop=True)
    return data

def trainSingle(string, model=None):
    if(model == None):
        model = {}
    string = " "+string
    for i in range(len(string)):
        letter = string[i].encode('utf-8').hex()
        lastletter = string[i-1].encode('utf-8').hex()
        if(not model.keys().__contains__(letter)):
            model[letter] = []
        if(i>0):
            if(not model[lastletter].__contains__(letter)):
                model[lastletter].append(letter)
    return model

def train(data,target):
    model = {}
    data = data['hex'].apply(hex2string)
    data = pd.concat([data, target], axis=1)
    data = data[data['valid'] == True]
    data = data.reset_index(drop=True)
    data = data['hex']
    start_time = time.time()
    for i in range(data.shape[0]):
        model = trainSingle(data[i], model)
    runtime = time.time() - start_time
    print("Markov trained with %d Entries and took %fs" % (data.shape[0], runtime))
    pickle.dump(model,open('markov.pkl',"wb"))
    return model

def validate(string, model):
    string = " "+string
    for i in range(len(string)-1):
        letter = string[i].encode('utf-8').hex()
        nextletter = string[i+1].encode('utf-8').hex()
        if(not model[letter].__contains__(nextletter)):
            return False
    return True

def test(label, markov, data, target):
    data = cleanData(data)
    mislabled = 0
    cnt_fn = 0
    cnt_fp = 0
    cnt_0 = 0
    cnt_1 = 0
    time_start = time.time()
    for i in range(data.shape[0]):
        pred = validate(data[i], markov)
        cnt_0 += (pred == 0)
        cnt_1 += (pred == 1)
        if (pred != target[i]):
            cnt_fn += (pred == 0)
            cnt_fp += (pred == 1)
            mislabled += 1
    runtime = time.time()-time_start
    print("Markov %s Total: %d Mislabled: %d[%d|%d] (%f%%) [took: %fs]" % (label, data.shape[0], mislabled, cnt_fp, cnt_fn, 100*mislabled / data.shape[0], runtime))
    return

def load(path):
    return pickle.load(open(path,"rb"))