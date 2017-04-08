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
    # print(data.shape)
    # labels, income = dw.sortDataPerLabels(data, 14)
    # incomeToPlot = dw.convertDataPerLabel(income)
    # hc.plotHist1d(incomeToPlot, labels)

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

    # labels, sex = dw.sortDataPerLabels(data, 9, 14)
    # sexToPlot = dw.convertDataPerLabel(sex)
    # print(sexToPlot)
    # hc.plotHistLevel2(sexToPlot, labels)

    labels, education = dw.sortDataPerLabels(data, 14, 9, 3)
    print(labels[0])
    print(len(education))
    i = 1
    for grade in education:
        print(i)
        i += 1
        print(grade[0].shape)
        print(np.unique(grade[0][:,[14, 9, 3]]))


    # np.set_printoptions(edgeitems=14)
    # print("education[0][0]")
    # print(len(education[0][0]))
    # print(np.unique(education[0][0][:,[3,9,14]]))
    # print("education[1][0]")
    # print(len(education[1][0]))
    # print(np.unique(education[1][0][:, [3, 9, 14]]))
    # print("education[2][0]")
    # print(len(education[2][0]))
    # print(np.unique(education[2][0][:, [3, 9, 14]]))
    # print("education[3][0]")
    # print(len(education[3][0]))
    # print(np.unique(education[3][0][:, [3, 9, 14]]))
    # educationToPlot = dw.convertDataPerLabel(education)
    # print(len(educationToPlot))
    # print(np.unique(educationToPlot[0]))
    # print(len(educationToPlot[0]))
    # print(np.unique(educationToPlot[1]))
    # print(len(educationToPlot[1]))
    # print(np.unique(educationToPlot[2]))
    # print(len(educationToPlot[2]))
    # print(np.unique(educationToPlot[3]))
    # print(len(educationToPlot[3]))
    #
    # toPlot = []
    # for i in range(len(educationToPlot)):
    #     toPlot.append(educationToPlot[i])
    # print(toPlot[0][0])
    # hc.plotHistLevel3(toPlot)


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