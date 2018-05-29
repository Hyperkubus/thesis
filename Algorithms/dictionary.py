import pandas as pd
from sklearn.naive_bayes import GaussianNB


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

total = trainData.shape[0]
cnt_fp = 0
cnt_fn = 0
for i in range(len(trainData)):
    pred = (str(trainData[i]) in dictionary.values)
    if(pred != trainTarget[i]):
        cnt_fn += (trainTarget[i]==1)
        cnt_fp += (trainTarget[i]==0)
mislabled = cnt_fn+cnt_fp
print("Dict Train: %d Mislabled: %d[%d|%d] (%f)" % (total,mislabled,cnt_fp,cnt_fn,mislabled/total))

total = validateData.shape[0]
cnt_fp = 0
cnt_fn = 0
for i in range(len(validateData)):
    pred = (str(validateData[i]) in dictionary.values)
    if(pred != validateTarget[i]):
        cnt_fn += (validateTarget[i]==1)
        cnt_fp += (validateTarget[i]==0)
mislabled = cnt_fn+cnt_fp
print("Dict Validate: %d Mislabled: %d[%d|%d] (%f)" % (total,mislabled,cnt_fp,cnt_fn,mislabled/total))

total = testData.shape[0]
cnt_fp = 0
cnt_fn = 0
for i in range(len(testData)):
    pred = (str(testData[i]) in dictionary.values)
    if(pred != testTarget[i]):
        cnt_fn += (testTarget[i]==1)
        cnt_fp += (testTarget[i]==0)
mislabled = cnt_fn+cnt_fp
print("Dict Test: %d Mislabled: %d[%d|%d] (%f)" % (total,mislabled,cnt_fp,cnt_fn,mislabled/total))