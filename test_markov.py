import sys
from Utils.DataLoader import loadData
from Algorithms.markov import train, test, load

def runTest():
    print("Running Markov Test...")
    data_train, target_train = loadData('train')
    model = train(data_train,target_train)
    data_val, target_val = loadData('validate')
    data_test, target_test = loadData('test')
    print("Test Results:")
    test('Train', model, data_train, target_train)
    test('Validation', model, data_val, target_val)
    test('Test', model, data_test, target_test)

def runPartial(len):
    print("Running Markov Test...")
    model = load('Algorithms/markov.pkl')
    data_test, target_test = loadData('%06d' % len)
    print("Test Results:")
    test('Test', model, data_test, target_test)

if __name__ == "__main__":
    runTest()
    #runPartial(int(sys.argv[1]))