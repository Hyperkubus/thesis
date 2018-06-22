#https://machinelearningmastery.com/binary-classification-tutorial-with-the-keras-deep-learning-library/

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.layers import Input, Dense
from keras.models import Model, load_model
import time

def train(data,target,validationData,validationTarget):
    data = data.drop('hex',1)
    validationData = validationData.drop('hex',1)
    inputs = Input(shape=(15,))
    #x = Dense(15, kernel_initializer='normal', activation='relu')(inputs)
    #x = Dense(10, kernel_initializer='normal', activation='relu')(x)
    #x = Dense(5, kernel_initializer='normal', activation='relu')(x)
    #predictions = Dense(1, kernel_initializer='normal', activation='sigmoid')(x)
    predictions = Dense(1, kernel_initializer='normal', activation='sigmoid')(inputs)

    model = Model(inputs=inputs, outputs=predictions)
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    model.fit(data, target, epochs=25, validation_data=(validationData, validationTarget))

    return model

def load(path):
    return load_model(path)

def test(label, model, data, target):
    data = data.drop('hex',1)
    start_time = time.time()
    y_pred = model.predict(data)
    runtime = time.time()-start_time
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
    print("bayes %s Total: %d Mislabled: %d[%d|%d] (%f%%) [took: %fs]" % (label, total, mislabled, cnt_fp, cnt_fn, 100*mislabled / total, runtime))
    return


def __main__():
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
    encoder.fit(trainData.iloc[:, -1])

    data_train = trainData.iloc[:, 1:16]
    target_train = encoder.transform(trainData.iloc[:, -1])

    data_validate = validateData.iloc[:, 1:16]
    target_validate = encoder.transform(validateData.iloc[:, -1])

    data_test = testData.iloc[:, 1:16]
    target_test = encoder.transform(testData.iloc[:, -1])

    model = train(data_train,target_train,data_validate,target_validate)

    model.save('neuralnet.new.h5')

    test('train',model,data_train,target_train)
    test('validate',model,data_validate,target_validate)
    test('test',model,data_test,target_test)
