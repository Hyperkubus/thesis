import sys
from Utils.DataLoader import loadData
from Algorithms.neuralnet import train, test, load

def runTest():
    print("Running Keras Test...")
    data_train, target_train = loadData('train')
    data_val, target_val = loadData('validate')
    print("training,...")
    keras = train(data_train, target_train, data_val, target_val)
    print("done")
    data_test, target_test = loadData('test')
    print("Test Results:")
    test('Train', keras, data_train, target_train)
    test('Validation', keras, data_val, target_val)
    test('Test', keras, data_test, target_test)

def runPartial(len):
    print("Running Keras Test...")
    keras = load("Algorithms/neuralnet.h5")
    data_test, target_test = loadData('%06d' % len)
    print("Test Results:")
    test('Test', keras, data_test, target_test)

if __name__ == "__main__":
    runTest()
    #runPartial(int(sys.argv[1]))