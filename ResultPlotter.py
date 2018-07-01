import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("time.log",delimiter=" ",header=0)

data_none = data[data['Runner'] == 'test_none.py']
data_dict = data[data['Runner'] == 'test_dict.py']
data_bayes = data[data['Runner'] == 'test_bayes.py']
data_markov = data[data['Runner'] == 'test_markov.py']
data_keras = data[data['Runner'] == 'test_keras.py']

plt.figure()
plt.title("Memory")
plt.plot(data_none['Size'],data_none['memory'],label='Ground Truth')
plt.plot(data_dict['Size'],data_dict['memory'],label='Dictionary')
plt.plot(data_bayes['Size'],data_bayes['memory'],label='Bayes')
plt.plot(data_markov['Size'],data_markov['memory'],label='Markov')
plt.plot(data_keras['Size'],data_keras['memory'],label='NeuralNet')
plt.legend(loc='best')
plt.xlabel('Anzahl Eingaben')
plt.ylabel('Speicherverbrauch in mb')
plt.savefig('Graphs/Results/Memory.png')
plt.close()
plt.clf()

plt.figure()
plt.title("Time")
plt.plot(data_none['Size'],data_none['time'],label='Ground Truth')
plt.plot(data_dict['Size'],data_dict['time'],label='Dictionary')
plt.plot(data_bayes['Size'],data_bayes['time'],label='Bayes')
plt.plot(data_markov['Size'],data_markov['time'],label='Markov')
plt.plot(data_keras['Size'],data_keras['time'],label='NeuralNet')
plt.legend(loc='best')
plt.xlabel('Anzahl Eingaben')
plt.ylabel('Laufzeit in s')
plt.savefig('Graphs/Results/CPUtime.png')
plt.close()
plt.clf()