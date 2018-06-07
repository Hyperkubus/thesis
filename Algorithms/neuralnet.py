#https://machinelearningmastery.com/binary-classification-tutorial-with-the-keras-deep-learning-library/

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.layers import Input, Dense
from keras.models import Model

def test(label, model, data, target):
    y_pred = model.predict(data)
    total = data.shape[0]
    cnt_fp = 0
    cnt_fn = 0
    mislabled = 0
    for i in range(0, y_pred.shape[0]):
        pred = round(y_pred[i, 0])
        if (pred != target[i]):
            cnt_fn += (pred == 0)
            cnt_fp += (pred == 1)
        mislabled = cnt_fn + cnt_fp
    print("keras %s: %d Mislabled: %d[%d|%d] (%f)" % (label, total, mislabled, cnt_fp, cnt_fn, mislabled / total))


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

encoder = LabelEncoder()
encoder.fit(trainData.iloc[:,-1])

data_train = trainData.iloc[:,1:15]
target_train = encoder.transform(trainData.iloc[:,-1])

data_validate = validateData.iloc[:,1:15]
target_validate = encoder.transform(validateData.iloc[:,-1])

data_test = testData.iloc[:,1:15]
target_test = encoder.transform(testData.iloc[:,-1])



inputs = Input(shape=(14,))
x = Dense(14, kernel_initializer='normal', activation='relu')(inputs)
x = Dense(7, kernel_initializer='normal', activation='relu')(x)
x = Dense(2, kernel_initializer='normal', activation='relu')(x)
predictions = Dense(1, kernel_initializer='normal', activation='sigmoid')(x)

model = Model(inputs=inputs,outputs=predictions)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(data_train,target_train,epochs=250,validation_data=(data_validate,target_validate))

model.save('neuralnet.h5')

test('train',model,data_train,target_train)
test('validate',model,data_validate,target_validate)
test('test',model,data_test,target_test)
