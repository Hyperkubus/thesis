import pandas as pd
from sklearn.naive_bayes import GaussianNB

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

gnb = GaussianNB()
gnb.fit(data_train.values, target_train.values)

y_pred = gnb.predict(data_train)
total = data_train.shape[0]
cnt_fp = 0
cnt_fn = 0
for i in range(0,y_pred.shape[0]):
    if(y_pred[i] != target_train[i]):
        cnt_fn += (y_pred[i]==0)
        cnt_fp += (y_pred[i]==1)
mislabled = cnt_fn+cnt_fp
print("Train Total: %d Mislabled: %d[%d|%d] (%f)" % (total,mislabled,cnt_fp,cnt_fn,mislabled/total))

y_pred = gnb.predict(data_validate)
total = data_validate.shape[0]
cnt_fp = 0
cnt_fn = 0
for i in range(0,y_pred.shape[0]):
    if(y_pred[i] != target_validate[i]):
        cnt_fn += (y_pred[i]==0)
        cnt_fp += (y_pred[i]==1)
mislabled = cnt_fn+cnt_fp
print("Validation Total: %d Mislabled: %d[%d|%d] (%f)" % (total,mislabled,cnt_fp,cnt_fn,mislabled/total))

y_pred = gnb.predict(data_test)
total = data_test.shape[0]
cnt_fp = 0
cnt_fn = 0
for i in range(0,y_pred.shape[0]):
    if(y_pred[i] != target_test[i]):
        cnt_fn += (y_pred[i]==0)
        cnt_fp += (y_pred[i]==1)
mislabled = cnt_fn+cnt_fp
print("Test Total: %d Mislabled: %d[%d|%d] (%f)" % (total,mislabled,cnt_fp,cnt_fn,mislabled/total))