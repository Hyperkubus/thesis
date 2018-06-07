import numpy as np
import pandas as pd
import binascii

def train(string, model=None):
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

def validate(string, model):
    string = " "+string
    for i in range(len(string)-1):
        letter = string[i].encode('utf-8').hex()
        nextletter = string[i+1].encode('utf-8').hex()
        if(not model[letter].__contains__(nextletter)):
            return False
    return True

def test(label, markov, data, target):
    mislabled = 0
    cnt_fn = 0
    cnt_fp = 0
    for i in range(data.shape[0]):
        pred = validate(data[i], markov)
        if (pred != target[i]):
            cnt_fn += (pred == 0)
            cnt_fp += (pred == 1)
            mislabled += 1
    print("Markov %s: %d Mislabled: %d[%d|%d] (%f)" % (label, target.shape[0], mislabled, cnt_fp, cnt_fn, mislabled / target.shape[0]))
    return

def hex2string(hex):
    return str(bytes.fromhex(hex))


dtype = {
        '': int,
        'len': int,
        'cnt_alpha': int,
        'cnt_nonAlpha': int,
        'alpha_to_special': float,
        'cnt_vowel': int,
        'cnt_consonant': int,
        'vowel_to_consonant': object,
        'entropy': float,
        'entropy_ideal': float,
        'emtropy_percentage': float,
        'fleschkincaid': float,
        'smog': float,
        'dalechall': float,
        'gunningfog': float,
        'sybl': int,
        'hex': str,
        'valid': bool
}

trainData = pd.read_csv("../Data/Datasets/train.csv", dtype=dtype)
validateData = pd.read_csv("../Data/Datasets/validate.csv", dtype=dtype)
testData = pd.read_csv("../Data/Datasets/test.csv", dtype=dtype)

trainTarget = trainData['valid']
trainData = trainData.sort_values('valid')
trainData = trainData['hex'].apply(hex2string)
trainValidation = trainData
trainData = trainData.iloc[(int(len(trainData)/2+1)):-1]
trainData = trainData.reset_index(drop=True)
validateTarget = validateData['valid']
validateData = validateData['hex'].apply(hex2string)
testTarget = testData['valid']
testData = testData['hex'].apply(hex2string)

model = None

print("training...")
for i in range(trainData.shape[0]):
    model = train(trainData[i],model)
    print("%d/%d" % (i, trainData.shape[0]))

test('train',model,trainData,trainTarget)
test('validate',model,validateData,validateTarget)
test('test',model,testData,testTarget)