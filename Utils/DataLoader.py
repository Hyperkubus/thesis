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

def loadData(type):
    data = pd.read_csv("Data/Datasets/"+type+".csv", dtype=dtype)
    features = data.iloc[:, 1:17]
    targets = data.iloc[:, -1]
    return features, targets

def hex2string(hex):
    return bytes.fromhex(hex).decode('utf-8')