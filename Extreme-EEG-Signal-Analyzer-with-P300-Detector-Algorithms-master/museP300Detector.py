import numpy as np

import extremeEEGSignalAnalyzer
import csv
import matplotlib.pyplot as plt


# csv_reader = csv.reader(csv_file, delimiter=',')
# p300Signals = []
# line_count = 0
# for row in csv_reader:
#     p300Signals.append(row)
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     else:
#         line_count += 1
# print(f'Processed {line_count} lines.')

eegData = np.genfromtxt('testData\\alpha_tp9tp10.csv', delimiter=',').T

windowMilliSecond = 600
stimulusAmount = len(eegData)
windowSize = int(windowMilliSecond / 2)
p300Signals = np.zeros((stimulusAmount, windowSize))

for i in range(stimulusAmount):
    p300Signals[i] = np.mean(eegData[i], axis=0)

stimulusStd = extremeEEGSignalAnalyzer.P300FinderAlgorithmSTD(p300Signals)
stimulusPeak = extremeEEGSignalAnalyzer.P300FinderAlgorithmPeak(p300Signals)
stimulusTotEn = extremeEEGSignalAnalyzer.P300FinderAlgorithmTotEnergy(p300Signals)
stimulusTraveller = extremeEEGSignalAnalyzer.P300TravellerFinder(p300Signals, 50)
#  ===Plotting Realtime P300 ============
string = 'Fz'
xAxis = np.arange(0, 599, 2)
plt.cla()
for i in range(stimulusAmount):
    plt.plot(xAxis, p300Signals[i], label=[i])
    plt.ylabel('Amplitude [uV]', fontsize=20)
    plt.xlabel('Time [Ms]', fontsize=20)
    plt.legend(loc='upper right', fontsize=10)
    plt.title(string + ' Location, Found Stimulus :' + str('stimulus'))
    plt.show()
plt.pause(.005)
