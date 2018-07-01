from sklearn.naive_bayes import GaussianNB
import pickle
import time

def train(data,target):
    data = data.drop('hex',1)
    start_time = time.time()
    gnb = GaussianNB()
    gnb.fit(data.values, target.values)
    runtime = time.time()-start_time
    print("Bayes Trained on %d Entries and took %fs" % (data.shape[0],runtime))
    pickle.dump(gnb,open('bayes.pkl',"wb"))
    return gnb

def test(label,gnb,data,target):
    data = data.drop('hex',1)
    start_time = time.time()
    y_pred = gnb.predict(data)
    runtime = time.time()-start_time
    total = target.shape[0]
    cnt_fp = 0
    cnt_fn = 0
    for i in range(0, y_pred.shape[0]):
        if (y_pred[i] != target[i]):
            cnt_fn += (y_pred[i] == 0)
            cnt_fp += (y_pred[i] == 1)
    mislabled = cnt_fn + cnt_fp
    print("bayes %s Total: %d Mislabled: %d[%d|%d] (%f%%) [took: %fs]" % (label, total, mislabled, cnt_fp, cnt_fn, 100*mislabled / total, runtime))
    return

def load(path):
    return pickle.load(open(path,"rb"))