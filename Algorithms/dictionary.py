import pandas as pd
import time
from Utils.DataLoader import hex2string
from sklearn.naive_bayes import GaussianNB

def train():
    start_time = time.time()
    dict = pd.read_csv("Data/dictionary.csv")
    runtime = time.time()-start_time
    print("Dictionary loaded with %d Entries and took %fs" % (dict.shape[0],runtime))
    return dict

def test(label, dictionary ,data, target):
    data = data['hex'].apply(hex2string)
    total = data.shape[0]
    start_time = time.time()
    y_pred = data.isin(dictionary)
    runtime = time.time()-start_time
    cnt_fp = 0
    cnt_fn = 0

    for i in range(0, y_pred.shape[0]):
        if (y_pred[i] != target[i]):
            cnt_fn += (y_pred[i] == 0)
            cnt_fp += (y_pred[i] == 1)
    mislabled = cnt_fn + cnt_fp
    print("bayes %s Total: %d Mislabled: %d[%d|%d] (%f%%) [took: %fs]" % (label, total, mislabled, cnt_fp, cnt_fn, 100*mislabled / total, runtime))
    return

def load():
    return pd.read_csv("../Data/dictionary.csv")
