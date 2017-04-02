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
        print(labels)
        # lb1Data = data[np.where(data[:, 0] == label1)]
        # lb2Data = data[np.where(data[:, 0] == label2)]
        # return lb1Data, lb2Data

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")