import sys
from Utils.DataLoader import loadData
from Algorithms.bayes import train, test, load

def runTest():
    print("Running Bayes Test...")
    data_train, target_train = loadData('train')
    print("training,...")
    gnb = train(data_train, target_train)
    print("done")
    data_val, target_val = loadData('validate')
    data_test, target_test = loadData('test')
    print("Test Results:")
    test('Train', gnb, data_train, target_train)
    test('Validation', gnb, data_val, target_val)
    test('Test', gnb, data_test, target_test)

def runPartial(len):
    print("Running Bayes Test...")
    gnb = load("Algorithms/bayes.pkl")
    data_test, target_test = loadData('%06d' % len)
    print("Test Results:")
    test('Test', gnb, data_test, target_test)

if __name__ == "__main__":
    runPartial(int(sys.argv[1]))