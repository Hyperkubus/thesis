import pandas as pd
from sklearn.naive_bayes import GaussianNB

def train(data,target):
    gnb = GaussianNB()
    gnb.fit(data_train.values, target_train.values)
    return gnb

def test(label,gnb,data,target):
    y_pred = gnb.predict(data)
    total = target.shape[0]
    cnt_fp = 0
    cnt_fn = 0
    for i in range(0, y_pred.shape[0]):
        if (y_pred[i] != target[i]):
            cnt_fn += (y_pred[i] == 0)
            cnt_fp += (y_pred[i] == 1)
    mislabled = cnt_fn + cnt_fp
    print("%s Total: %d Mislabled: %d[%d|%d] (%f)" % (label, total, mislabled, cnt_fp, cnt_fn, mislabled / total))
    return

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

data_train = trainData.iloc[:,1:15]
target_train = trainData.iloc[:,-1]

data_validate = validateData.iloc[:,1:15]
target_validate = validateData.iloc[:,-1]

data_test = testData.iloc[:,1:15]
target_test = testData.iloc[:,-1]

gnb = train(data_train, target_train)

test('train',gnb,data_train,target_train)
test('validate',gnb,data_validate,target_validate)
test('test',gnb,data_test,target_test)
