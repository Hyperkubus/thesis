import pandas as pd
from sklearn.naive_bayes import GaussianNB

def test(label, dictionary ,data, target):
    total = data.shape[0]
    cnt_fp = 0
    cnt_fn = 0
    for i in range(len(data)):
        pred = (str(data[i]) in dictionary.values)
        if (pred != target[i]):
            cnt_fn += (target[i] == 1)
            cnt_fp += (target[i] == 0)
        print("%i/%i" % (i, total))
    mislabled = cnt_fn + cnt_fp
    print("Dict %s: %d Mislabled: %d[%d|%d] (%f)" % (label ,total, mislabled, cnt_fp, cnt_fn, mislabled / total))
    return

def hex2string(hex):
    return bytes.fromhex(hex).decode('utf-8')

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

dictionary = pd.read_csv("../Data/dictionary.csv")

trainData = pd.read_csv("../Data/Datasets/train.csv", dtype=dtype)
validateData = pd.read_csv("../Data/Datasets/validate.csv", dtype=dtype)
testData = pd.read_csv("../Data/Datasets/test.csv", dtype=dtype)

trainTarget = trainData['valid']
trainData = trainData['hex'].apply(hex2string)
validateTarget = validateData['valid']
validateData = validateData['hex'].apply(hex2string)
testTarget = testData['valid']
testData = testData['hex'].apply(hex2string)

test('train',dictionary,trainData,trainTarget)
test('validate',dictionary,validateData,validateTarget)
test('test',dictionary,testData,testTarget)