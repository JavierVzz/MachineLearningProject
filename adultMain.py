# Javier Vazquez
# Todo: Add your names
# Adult Classifier
# Date: March 29 ,2017
# Description: Predict whether income exceeds $50K/yr based on census data.
# Also known as "Census Income" dataset.
# Source: http://archive.ics.uci.edu/ml/datasets/Adult


import os
import linearClassifierClass, dataWranglerClass, histogramClass
import pandas as pd
import numpy as np


def main():

    #url for the training data for the linear classifier
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

    lc = linearClassifierClass.linearClassifier()
    dw = dataWranglerClass.dataWrangler()
    hc = histogramClass.histogramAdult()

    # Get the data from internet without manual download
    # data is a pandas dataframe
    data = dw.getData(url)

    # Pandas data frame to numpy ndarray
    data = data.values

    sex = dw.sortDataPerLabel(data[:,9])
    sexToPlot = dw.convertDataPerLabel(sex)
    # sexToPlot = dw.convertDataPerLabel(data[:,9])
    # print(sex[1].size)
    hc.plotHist1d(sexToPlot)

    # Index of columns to Keslerize
    # 1: workclass
    # 3: education
    # 5: marital
    # 6: occupation
    # 7: relationship
    # 8: race
    # 9: sex
    # 13: country
    # 14: income
    # index = [1,3,5,6,7,8,9,13,14]



    # List of Keslers
    # 0: workclass
    # 1: education
    # 2: marital
    # 3: occupation
    # 4: relationship
    # 5: race
    # 6: sex
    # 7: country
    # 8: income
    # keslerList = []
    # np.set_printoptions(edgeitems=9)
    # for i in index:
    #     keslerList.append(lc.kesler(data[:,i]))
    #
    # workclassKesler = lc.kesler(workclass)
    # educationKesler = lc.kesler(education)

    # Validating Keslers
    # print(keslerList[0] == workclassKesler)
    # print(keslerList[1] == educationKesler)
    # print(len(keslerList))

    #TODO: Modify kesler to handle binary labels








if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()