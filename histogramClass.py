import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class histogramAdult():

    def __init__(self):
        pass

    #Updating
    def plotHist1d(self, data, labels):
        # fig = plt.figure()
        ax = plt.subplot()
        colors = ["r", "b"]
        ax.hist(data, color=colors, rwidth=1, align="mid", bins=2)
        ax.set_xlim(0.5, len(data)+.5)
        xticks = []
        for datum in data:
            xticks.append(datum[0])
            ax.annotate(str(datum.size), xy=(datum[0], datum.size))
        ax.set_xticks(xticks)
        ax.set_xticklabels(labels[0])
        plt.show()

    def plotHistLevel2(self, data, labels):
        # fig = plt.figure()
        ax = plt.subplot()
        colors = ["r", "b", "r", "b"]
        ax.hist(data, color=colors, rwidth=1, align="mid", bins=len(data))
        red_patch = mpatches.Patch(color='r', label='Female')
        blue_patch = mpatches.Patch(color='b', label='Male')
        plt.legend(handles=[red_patch, blue_patch])
        ax.set_xlim(0.5, len(data)+.5)
        for datum in data:
            ax.annotate(str(datum.size), xy=(datum[0], datum.size))
        ax.set_xticks([1.5,3.5])
        ax.set_xticklabels(labels[1])
        plt.show()


if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")