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
    
    def sortDataPerLabel(self, data):
        labels = np.unique(data)
        countPerLabel = [data[np.where(data == label)] for label in labels]
        return countPerLabel

    def convertDataPerLabel(self, data):
        labels = np.unique(data)
        m = data.size
        toPlot = np.zeros(m)
        for i in range(len(labels)):
            toPlot[np.where(data == labels[i])] = i+1
        return toPlot







                # def arrayPerLabel(self, data):
    #     labels = np.unique(data)

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")