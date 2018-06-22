import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm


dtype = {
            '': int,
            'len': int,
            'cnt_alpha': int,
            'cnt_nonAlpha': int,
            'alpha_to_special': float,
            'cnt_vowel': int,
            'cnt_consonant': int,
            'vowel_to_consonant': float,
            'entropy': float,
            'entropy_ideal': float,
            'emtropy_percentage': float,
            'fleschkincaid': float,
            'smog': float,
            'dalechall': float,
            'gunningfog': float,
            'sybl': float,
            'hex': str,
            'valid': bool
    }
datasetPOS = pd.read_csv("../Data/features.csv", dtype=dtype)
datasetNEG = pd.read_csv("../Data/features.neg.csv", dtype=dtype)

datapoints = [
    ["Wordlaenge",52],
    ["Alphabetische_Zeichen",50],
    ["Sonderzeichen",50],
    ["Zeichen_Verhältniss",101],
    ["Vokale",50],
    ["Konsonanten",50],
    ["Vokale_Konsonanten",101],
    ["Entropie",101],
    ["Ideale_Entropie",101],
    ["Entropie_Prozentual",101],
    ["fleschkincaid",100],
    ["smog",100],
    ["dalechall",100],
    ["gunningfog",100],
    ["Silben",10],
]

for i in range(0,15): #[0,3,6,9,10,11,12,13]:
    print(i)
    max = float(np.nanmax(datasetNEG.iloc[:,i]))
    bin_a = int(max)
    max = float(np.nanmax(datasetPOS.iloc[:,i]))
    bin_b = int(max)
    bins = datapoints[i][1] # 'auto' #max(bin_a,bin_b)
    print(datapoints[i][0], bin_a, bin_b, bins)
    plt.figure()
    plt.hist([datasetNEG.iloc[:,i]],bins, histtype='step', label='Irrelevant')
    plt.hist([datasetPOS.iloc[:,i]],bins, histtype='step', label='Relevant')
    #plt.hist(data[:,i],bins, histtype='step')
    plt.title(datapoints[i][0])
    plt.legend(loc='best')
    plt.savefig('../Graphs/'+datapoints[i][0]+'.png')
    plt.close()
    plt.clf()

    plt.figure()
    plt.hist([datasetNEG.iloc[:,i]],bins, histtype='step', label='Irrelevant')
    plt.hist([datasetPOS.iloc[:,i]],bins, histtype='step', label='Relevant')
    #plt.hist(data[:,i],bins, histtype='step')
    plt.title(datapoints[i][0]+" (log-scale)")
    plt.legend(loc='best')
    plt.yscale('log', nonposy='clip')
    plt.savefig('../Graphs/'+datapoints[i][0]+'_log.png')
    plt.close()
    plt.clf()
'''
    weights_a = np.ones_like(datasetNEG.iloc[:, i]) / float(len(datasetNEG.iloc[:, i]))
    weights_b = np.ones_like(datasetPOS.iloc[:, i]) / float(len(datasetPOS.iloc[:, i]))
    print(datapoints[i][0], np.nanmax(weights_a), np.nanmax(weights_b))
    plt.figure()
    plt.hist([datasetNEG.iloc[:,i]], bins, weights=[weights_a], histtype='step', label='Irrelevant')
    plt.hist([datasetPOS.iloc[:,i]], bins, weights=[weights_b], histtype='step', label='Relevant')
    #plt.hist(data[:, i], bins, weights=weights_b, histtype='step')
    plt.title(datapoints[i][0]+" (normalized)")
    plt.legend(loc='best')
    plt.savefig('../Graphs/' + datapoints[i][0] + '.norm.png')
    plt.close()
    plt.clf()'''