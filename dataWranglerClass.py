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
            print(labels)
            income = [data[np.where(data == label), :] for label in labels[0]]

            # sex = []
            # sex.append(income[0][0][np.where(income[0][0] == labels[1][0]),:])
            # sex.append(income[0][0][np.where(income[0][0] == labels[1][1]),:])
            # sex.append(income[1][0][np.where(income[1][0] == labels[1][0]),:])
            # sex.append(income[1][0][np.where(income[1][0] == labels[1][1]),:])

            # for i in range(len(labels[0])):
            #     for j in range(len(labels[1])):
            #         sex.append(income[i][0][np.where(income[i][0] == labels[1][j]), :])

            sex = [income[i][0][np.where(income[i][0] == labels[1][j]), :] for i in range(len(labels[0])) for j in range(len(labels[1]))]

            print(len(labels[2]))

            education = []
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][0]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][1]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][2]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][3]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][4]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][5]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][6]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][7]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][8]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][9]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][10]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][11]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][12]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][13]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][14]),:])
            education.append(sex[0][0][np.where(sex[0][0] == labels[2][15]),:])

            education.append(sex[1][0][np.where(sex[1][0] == labels[2][0]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][1]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][2]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][3]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][4]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][5]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][6]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][7]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][8]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][9]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][10]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][11]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][12]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][13]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][14]),:])
            education.append(sex[1][0][np.where(sex[1][0] == labels[2][15]),:])

            education.append(sex[2][0][np.where(sex[2][0] == labels[2][0]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][1]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][2]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][3]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][4]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][5]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][6]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][7]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][8]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][9]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][10]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][11]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][12]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][13]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][14]),:])
            education.append(sex[2][0][np.where(sex[2][0] == labels[2][15]),:])

            education.append(sex[3][0][np.where(sex[3][0] == labels[2][0]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][1]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][2]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][3]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][4]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][5]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][6]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][7]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][8]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][9]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][10]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][11]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][12]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][13]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][14]),:])
            education.append(sex[3][0][np.where(sex[3][0] == labels[2][15]),:])


            return labels, education
            # countPerLabel = [data[np.where(data == label),:] for label in labels[0]]
            # print("countPerLabel")
            # print(countPerLabel)
            # countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0]==label),:] for i in range(len(countPerLabel)) for label in labels[1]]
            # countPerLabel = [countPerLabel[i][0][np.where(countPerLabel[i][0]==label),:] for i in range(len(countPerLabel)) for label in labels[2]]
        return labels, countPerLabel

    def convertDataPerLabel(self, data):
        if len(data) == 2:
            listLabel = [np.ones(len(data[i][0]))*(i+1) for i in range(len(data))]
            return listLabel
        elif len(data) == 4:
            listLabel = [np.ones(len(data[i]))*(i+1) if i==0 or i==3 else np.ones(len(data[i]))*(i+2) if i==1 else np.ones(len(data[i]))*i if i==2 else 0 for i in range(len(data))]
            return listLabel
        elif len(data) == 64:
            # listLabel = []
            # for i in range(len(data)):
            #     listLabel.append(np.ones(len(data[i][0])) * (i + 1))
            listLabel = [np.ones(len(data[i][0])) * (i + 1) for i in range(len(data))]

            return listLabel







                # def arrayPerLabel(self, data):
    #     labels = np.unique(data)

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")