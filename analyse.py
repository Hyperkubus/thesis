from Algorithms.bayes import train as trainBayes
from Algorithms.bayes import test as testBayes
from Algorithms.dictionary import load as loadDict
from Algorithms.dictionary import test as testDict
from Algorithms.markov import train as trainMarkov
from Algorithms.markov import test as testMarkov
from Algorithms.neuralnet import train as trainNet
from Algorithms.neuralnet import test as testNet
from Algorithms.neuralnet import load as loadNet
from Utils.DataLoader import loadData
from sklearn.preprocessing import LabelEncoder
from keras.utils import plot_model
import matplotlib.pyplot as plt
import time
import pandas as pd
import sys
import subprocess

def h2s(s):
    return bytes.fromhex(s).decode('utf-8')

def kerasTest(subSet):
    data = subSet.iloc[:, 1:16]
    target = subSet['valid']
    startTime = time.time()
    testNet('Analyse(%d)' % (i), kerasModel, data, encoder.transform(target))
    runTime = time.time() - startTime
    return runTime

def bayesTest(subSet):
    data = subSet.iloc[:, 1:16]
    target = subSet['valid']
    startTime = time.time()
    testBayes('Analyse(%d)' % (i), bayesModel, data, target)
    runTime = time.time() - startTime
    return runTime

def markovTest(subSet):
    data = subSet['hex'].apply(h2s)
    target = subSet['valid']
    startTime = time.time()
    testMarkov('Analyse(%d)' % (i), markovModel, data, target)
    runTime = time.time() - startTime
    return runTime

def dictTest(subSet):
    data = subSet['hex'].apply(h2s)
    target = subSet['valid']
    startTime = time.time()
    testDict('Analyse(%d)' % (i), dictModel, data, target)
    runTime = time.time() - startTime
    return runTime

def old():
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

    count = sys.argv[1]

    data_train, target_train = loadData('train')
    data_validation, target_validation = loadData('train')
    data_test, target_test = loadData('train')

    kerasModel = loadNet('neuralnet.h5')
    plot_model(kerasModel, to_file='../Graphs/neural_net.png',show_shapes=True)
    dictModel = loadDict()
    bayesModel = trainBayes(data_train, target_train)
    markovModel = trainMarkov(trainData)

    encoder = LabelEncoder()
    encoder.fit(trainData.iloc[:, -1])

    dictTime = {}
    kerasTime = {}
    bayesTime = {}
    markovTime = {}

    '''
    for i in range(4,max(testData['len']+1)):
        subSet = testData[testData['len'] == i]
        subSet = subSet.reset_index()
        if len(subSet) < 1:
            continue
        print("Wordlength: ", i)
        dictTime[i] = dictTest(subSet)
        bayesTime[i] = bayesTest(subSet)
        kerasTime[i] = kerasTest(subSet)
        markovTime[i] = markovTest(subSet)
        exit()
    '''

    subSet = testData.iloc[:count,:]
    dictTime[count] = dictTest(subSet)
    bayesTime[count] = bayesTest(subSet)
    kerasTime[count] = kerasTest(subSet)
    markovTime[count] = markovTest(subSet)

    print('Dict',dictTime)
    print('Bayes',bayesTime)
    print('Keras',kerasTime)
    print('Markov',markovTime)

    '''
    lists = sorted(dictTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Dict')
    lists = sorted(markovTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Markov')
    lists = sorted(bayesTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Bayes')
    lists = sorted(kerasTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Keras')
    plt.legend(loc='best')
    plt.title("laufzeit")
    plt.savefig('../Graphs/cpu_time.png')
    plt.show()
    plt.close()
    plt.clf()
    
    lists = sorted(markovTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Markov')
    lists = sorted(bayesTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Bayes')
    lists = sorted(kerasTime.items())
    x,y = zip(*lists)
    plt.plot(x,y,label='Keras')
    plt.legend(loc='best')
    plt.title("laufzeit")
    plt.savefig('../Graphs/cpu_time_no_dict.png')
    plt.show()
    plt.close()
    plt.clf()
    '''

def analyse():
    data = subprocess.run("time python test_dict.py")
    print(data)

if __name__ == "__main__":
    analyse()