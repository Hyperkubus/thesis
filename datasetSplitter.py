import numpy as np

data = np.genfromtxt('Data/features.csv',delimiter=',',skip_header=1)
dataneg = np.genfromtxt('Data/features.neg.csv',delimiter=',',skip_header=1)

if(data.shape[0] != dataneg.shape[0]):
    print("Data and DataNeg should have same size")
    exit()


data.sort(0)

ones = np.ones((data.shape[0],1))
data = np.append(data, ones ,axis=1)
dataneg.sort(0)
zeroes = np.zeros((dataneg.shape[0],1))
dataneg = np.append(dataneg, zeroes ,axis=1)

_100 = range(0,data.shape[0])
_20 = range(0,data.shape[0],5)
_80 = np.delete(_100, _20)

data_20 = np.delete(data, list(_80), axis=0)
dataneg_20 = np.delete(dataneg, list(_80), axis=0)
data_validate = np.concatenate((data_20,dataneg_20))
np.savetxt("Data/Datasets/test.csv", data_validate, delimiter=",")

data_80 = np.delete(data, list(_20), axis=0)
dataneg_80 = np.delete(dataneg, list(_20), axis=0)

_100 = range(0,data_80.shape[0])
_20 = range(0,data_80.shape[0],5)
_80 = np.delete(_100, _20)

data_20 = np.delete(data, list(_80), axis=0)
dataneg_20 = np.delete(dataneg, list(_80), axis=0)
data_test = np.concatenate((data_20,dataneg_20))
np.savetxt("Data/Datasets/validation.csv", data_test, delimiter=",")

data_80 = np.delete(data, list(_20), axis=0)
dataneg_80 = np.delete(dataneg, list(_20), axis=0)
data_train = np.concatenate((data_80,dataneg_80))
np.savetxt("Data/Datasets/train.csv", data_train, delimiter=",")