# Javier Vazquez
# Todo: Add your names
# Adult Classifier
# Date: March 29 ,2017
# Description: Predict whether income exceeds $50K/yr based on census data.
# Also known as "Census Income" dataset.
# Source: http://archive.ics.uci.edu/ml/datasets/Adult


import os
import linearClassifierClass, dataWranglerClass
import pandas as pd
import numpy as np


def main():

    #url for the training data for the linear classifier
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

    lc = linearClassifierClass.linearClassifier()
    dw = dataWranglerClass.dataWrangler()

    # Get the data from internet without manual download
    # data is a pandas dataframe
    data = dw.getData(url)

    # Pandas data frame to numpy ndarray
    data = data.values

    age, workclass, fnlwgt, education, educationYrs, marital, occupation, relationship, race, \
    sex, capitalGain, capitalLoss, hoursWK, country, income = dw.dataPerVariable(data)

    # Releasing space
    index = [1,3,5,6,7,8,9,13,14]
    keslerList = []
    np.set_printoptions(edgeitems=9)
    for i in index:
        print(np.unique(data[:,i]))
        print(lc.kesler(data[:,i]))
    # workclassKesler = lc.kesler(workclass)
    # educationKesler = lc.kesler(education)










if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()