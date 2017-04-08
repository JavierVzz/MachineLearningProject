import os
import pandas as pd
import numpy as np


class dataWrangler():

    def __init__(self):
        pass

    def getData(self, url):
        """Gets the data from the specified URL"""
        data = pd.read_csv(url, header=None)
        return data
    
    def sortDataPerLabels(self, data, *args):
        if len(args) == 1:
            labels = [np.unique(data[:, arg]) for arg in args]
            countPerLabel = [data[np.where(data == label), :] for label in labels[0]]
        elif len(args) == 2:
            labels = [np.unique(data[:,arg]) for arg in args]
            countPerLabel = [data[np.where(data == label),:] for label in labels[0]]
            countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0] == labels[1][j])] for i in range(len(countPerLabel)) for j in range(len(labels[1])) ]
        elif len(args) == 3:
            labels = [np.unique(data[:,arg]) for arg in args]
            print(labels)
            # income = []
            #
            # for label in labels[0]:
            #     income.append(data[np.where(data == label), :])

            income = [data[np.where(data == label), :] for label in labels[0]]

            sex = []
            # sex.append(income[0][0][np.where(income[0][0] == labels[1][0]),:])
            # sex.append(income[0][0][np.where(income[0][0] == labels[1][1]),:])
            # sex.append(income[1][0][np.where(income[1][0] == labels[1][0]),:])
            # sex.append(income[1][0][np.where(income[1][0] == labels[1][1]),:])


            for i in range(len(labels[0])):
                for j in range(len(labels[1])):
                    sex.append(income[i][0][np.where(income[i][0] == labels[1][j]), :])



            return labels, sex
            # countPerLabel = [data[np.where(data == label),:] for label in labels[0]]
            # print("countPerLabel")
            # print(countPerLabel)
            # countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0]==label),:] for i in range(len(countPerLabel)) for label in labels[1]]
            # countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0]==label),:] for i in range(len(countPerLabel)) for label in labels[2]]
        return labels, countPerLabel

    def convertDataPerLabel(self, data):
        if len(data) == 2:
            listLabel = [np.ones(len(data[i][0]))*(i+1) for i in range(len(data))]
            return listLabel
        elif len(data) == 4:
            listLabel = [np.ones(len(data[i]))*(i+1) if i==0 or i==3 else np.ones(len(data[i]))*(i+2) if i==1 else np.ones(len(data[i]))*i if i==2 else 0 for i in range(len(data))]
            return listLabel
        elif len(data) == 64:
            # listLabel = []
            # for i in range(len(data)):
            #     listLabel.append(np.ones(len(data[i][0])) * (i + 1))
            listLabel = [np.ones(len(data[i][0])) * (i + 1) for i in range(len(data))]

            return listLabel







                # def arrayPerLabel(self, data):
    #     labels = np.unique(data)

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")