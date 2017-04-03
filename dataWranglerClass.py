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
        return countPerLabel, labels


    def sortDataPer2Labels(self, data, label1, label2):
        labels = np.unique(data[:,label1])
        print(labels)
        countPerLabel = [np.where(data == label) for label in labels]
        print(countPerLabel[0][0])
        print(len(countPerLabel))
        print(data[countPerLabel[0][0],:])
        # return countPerLabel, labels

    def convertDataPerLabel(self, data):
        listLabel =[]
        for i in range(len(data)):
            listLabel.append(np.ones(data[i].size)*(i+1))
        return listLabel








                # def arrayPerLabel(self, data):
    #     labels = np.unique(data)

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")