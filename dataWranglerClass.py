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

    def dataPerLabel(self, data):
        age = data[:,0]
        workclass = data[:,1]
        fnlwgt = data[:,2]
        education = data[:,3]
        educationYrs = data[:,4]
        marital = data[:,5]
        occupation = data[:,6]
        relationship = data[:,7]
        race = data[:,8]
        sex = data[:,9]
        capitalGain = data[:,10]
        capitalLoss = data[:,11]
        hoursWK = data[:,12]
        country = data[:,13]
        income = data [:,14]
        return age, workclass, fnlwgt, education, educationYrs, marital, occupation, relationship, race,\
               sex, capitalGain, capitalLoss, hoursWK, country, income




if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")