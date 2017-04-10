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

    file = "project_data.xlsx"
    sheet = "data"
    cols = "A:O"
    skip = 0
    data = lc.loadData(file, sheet, cols, skip)

    # Get the data from internet without manual download
    # data is a pandas dataframe
    # data = dw.getData(url)

    # Pandas data frame to numpy ndarray
    # data = data.values
    # print(data)
    # print(data.shape)
    # print(np.unique(data[:,13]))
    # print(np.unique(data[:,13]).size)


    # Index of columns to Keslerize
    # 1: workclass 9
    # 3: education 16
    # 5: marital 7
    # 6: occupation 15
    # 7: relationship 6
    # 8: race 5
    # 9: sex 2
    # 13: country 42
    # 14: income
    # index = [1,3,5,6,7,8,9,13,14]


    labels, income = dw.sortDataPerLabels(data, 14)
    incomeToPlot = dw.convertDataPerLabel(income)
    hc.plotHist1d(incomeToPlot, labels)
    #
    # #Workclass
    # labels, sex = dw.sortDataPerLabels(data, 14, 1)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # #SEX
    # labels, sex = dw.sortDataPerLabels(data, 14, 9)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # #RACE
    # labels, sex = dw.sortDataPerLabels(data, 14, 8)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # #RELATIONSHIP
    # labels, sex = dw.sortDataPerLabels(data, 14, 7)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # # MARITAL
    # labels, sex = dw.sortDataPerLabels(data, 14, 5)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # # OCCUPATION
    # labels, sex = dw.sortDataPerLabels(data, 14, 6)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # # EDUCATION
    # labels, sex = dw.sortDataPerLabels(data, 14, 3)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # # COUNTRY
    # labels, sex = dw.sortDataPerLabels(data, 14, 13)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # hc.plotHistLevel2(sexToPlot, labels)
    #
    # labels, education = dw.sortDataPerLabels(data, 14, 9, 3)
    # educationToPlot = dw.convertDataPerLabel(education)
    # hc.plotHistLevel3(educationToPlot, labels)
    #

    #TODO 3rd level histogram


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