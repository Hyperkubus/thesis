import pandas as pd

dtype = {
        '': int,                        # 0
        'len': int,                     # 1
        'cnt_alpha': int,               # 2
        'cnt_nonAlpha': int,            # 3
        'alpha_to_special': float,      # 4
        'cnt_vowel': int,               # 5
        'cnt_consonant': int,           # 6
        'vowel_to_consonant': object,   # 7
        'entropy': float,               # 8
        'entropy_ideal': float,         # 9
        'emtropy_percentage': float,    #10
        'fleschkincaid': float,         #11
        'smog': float,                  #12
        'dalechall': float,             #13
        'gunningfog': float,            #14
        'sybl': int,                    #15
        'hex': str,                     #16
        'valid': bool                   #17
}

data = pd.read_csv("Data/Datasets/test.csv", dtype=dtype)
single = data.iloc[:1,:]
data = single

for i in [1,10,100,500,1000,1500,2000,2500,5000,7500,10000,15000,20000,25000,50000,75000,100000,150000,200000,250000]:
    while (data.shape[0] < i):
        data = pd.concat((data,single.iloc[:1,:]))
    data.to_csv('./Data/Datasets/%06d.csv' % i)