import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class histogramAdult():

    def __init__(self):
        pass

    def plotHist1d(self, data):
        print(data[0].size)
        print(data[1][0])
        fig = plt.figure()
        ax = plt.subplot()
        ax.set_xlim(0.5, 2.5)
        ax.set_xticks([0.5, 1, 2, 2.5])
        ax.set_xticklabels(['', 'Female', 'Male', ''])
        colors = ["red", "blue"]
        ax.hist(data, color=colors, rwidth=1)
        for datum in data:
            ax.annotate(str(datum.size), xy=(datum[0], datum.size))
        plt.show()


if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")