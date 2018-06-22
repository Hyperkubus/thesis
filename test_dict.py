from Utils.DataLoader import loadData
from Algorithms.dictionary import train, test
import pandas as pd

def runTest():
    print("Running Dictionary Test...")
    dictionary = train()
    data_train, target_train = loadData('train')
    data_val, target_val = loadData('validate')
    data_test, target_test = loadData('test')
    print("Test Results:")
    test('Train', dictionary, data_train, target_train)
    test('Validation', dictionary, data_val, target_val)
    test('Test', dictionary, data_test, target_test)

if __name__ == "__main__":
    runTest()