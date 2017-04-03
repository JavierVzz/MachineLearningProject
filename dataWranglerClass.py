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


    def Out_sortDataPer2Labels(self, data, label1, label2):
        labels = []
        labels.append(np.unique(data[:,label1]))
        labels.append(np.unique(data[:,label2]))
        print(labels)
        countPerLabel = [data[np.where(data == label),:] for label in labels[0]]
        print(countPerLabel[0][0])
        print(countPerLabel[0][0][np.where(countPerLabel[0][0]== labels[1][0])].size)
        print(countPerLabel[0][0][np.where(countPerLabel[0][0]== labels[1][1])].size)


    def sortDataPer2Labels(self, data, *args):
        labels = [np.unique(data[:,arg]) for arg in args]
        print(labels)
        countPerLabel = [data[np.where(data == label),:] for label in labels[0]]
        print(countPerLabel[0][0])
        print(countPerLabel[0][0][np.where(countPerLabel[0][0]== labels[1][0])].size)
        print(countPerLabel[0][0][np.where(countPerLabel[0][0]== labels[1][1])].size)


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