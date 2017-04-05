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
            countPerLabel = [data[np.where(data == label),:] for label in labels[0]]
            countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0]==label),:] for i in range(len(countPerLabel)) for label in labels[1]]
            countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0]==label),:] for i in range(len(countPerLabel)) for label in labels[2]]
        return labels, countPerLabel

    def convertDataPerLabel(self, data):
        if len(data) == 2:
            listLabel = [np.ones(data[i].size)*(i+1) for i in range(len(data))]
        elif len(data) == 4:
            listLabel = [np.ones(data[i].size)*(i+1) for i in range(len(data))]
        return listLabel







                # def arrayPerLabel(self, data):
    #     labels = np.unique(data)

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")