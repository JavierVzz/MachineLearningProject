import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class histogramAdult():

    def __init__(self):
        pass

    def plotHist1d(self, data, labels):

        fig = plt.figure()
        ax = plt.subplot()

        colors = ["red", "blue"]
        ax.hist(data, color=colors, rwidth=1, align="mid", bins=2)
        ax.set_xlim(0.5, 2.5)

        ax.set_xticklabels(labels)
        xticks = []
        for datum in data:
            xticks.append(datum[0])
            ax.annotate(str(datum.size), xy=(datum[0], datum.size))
        # ax.set_xticks([1, 2])
        ax.set_xticks(xticks)
        plt.show()


if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")