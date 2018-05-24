import numpy as np
import pandas as pd

data = pd.read_csv('Data/features.csv')
dataneg = pd.read_csv('Data/features.neg.csv')

data = data.sort_values(by=['len'])
data = data.assign(valid=True)
data = data.reset_index(drop=True)

dataneg = dataneg.sort_values(by=['len'])
dataneg = dataneg.assign(valid=False)
dataneg = dataneg.reset_index(drop=True)

if(data.shape != dataneg.shape):
    print("Data and DataNeg should have same shape")
    print(data.shape)
    print(dataneg.shape)
    exit()

data_80 = data[data.index % 5 != 0]  # Excludes every 5th row starting from 0
data_80 = data_80.reset_index(drop=True)
data_20 = data[data.index % 5 == 0]  # Selects every 5th raw starting from 0
data_20 = data_20.reset_index(drop=True)
data_80_80 = data_80[data_80.index % 5 != 0]  # Excludes every 5th row starting from 0
data_80_80 = data_80_80.reset_index(drop=True)
data_80_20 = data_80[data_80.index % 5 == 0]  # Selects every 5th raw starting from 0
data_80_20 = data_80_20.reset_index(drop=True)

dataneg_80 = dataneg[dataneg.index % 5 != 0]  # Excludes every 5th row starting from 0
dataneg_80 = dataneg_80.reset_index(drop=True)
dataneg_20 = dataneg[dataneg.index % 5 == 0]  # Selects every 5th raw starting from 0
dataneg_20 = dataneg_20.reset_index(drop=True)
dataneg_80_80 = dataneg_80[dataneg_80.index % 5 != 0]  # Excludes every 5th row starting from 0
dataneg_80_80 = dataneg_80_80.reset_index(drop=True)
dataneg_80_20 = dataneg_80[dataneg_80.index % 5 == 0]  # Selects every 5th raw starting from 0
dataneg_80_20 = dataneg_80_20.reset_index(drop=True)

data_test = pd.concat([data_20, dataneg_20])
data_validate = pd.concat([data_80_20, dataneg_80_20])
data_train = pd.concat([data_80_80, dataneg_80_80])

data_test.to_csv("Data/Datasets/test.csv")
data_validate.to_csv("Data/Datasets/validate.csv")
data_train.to_csv("Data/Datasets/train.csv")