import os
import pandas as pd
import numpy as np
import linearClassifierClass
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
        # for datum in data:
        #     xticks.append(datum[0])
        #     ax.annotate(str(datum.size), xy=(datum[0], datum.size))
        i = 1.5
        for datum in data:
            if datum.size == 0:
                plt.text(i, 0, 0, fontsize=14, horizontalalignment='center', verticalalignment='center')
            else:
                plt.text(datum[0], datum.size + 100, datum.size, fontsize=14, horizontalalignment='center',
                         verticalalignment='center')
            i += 1
        maxY = max([len(datum) for datum in data])
        ax.set_ylim(0, maxY + 500)
        ax.set_xticks([1.15, 1.85])
        ax.set_xticklabels(labels[0])
        p = mpatches.Rectangle((0, 0), (len(data) / 2) + .5, maxY + 500, facecolor="y", alpha=.2)
        q = mpatches.Rectangle(((len(data) / 2) + .5, 0), len(data) / 2, maxY + 500, facecolor="g", alpha=.2)
        plt.text(.75, maxY + 100, labels[0][0], fontsize=15, horizontalalignment='center',
                 verticalalignment='center', bbox=dict(facecolor='y'))
        plt.text(2, maxY + 100, labels[0][1], fontsize=15, horizontalalignment='center',
                 verticalalignment='center', bbox=dict(facecolor='g'))

        ax.add_patch(p)
        ax.add_patch(q)
        plt.show()

    def plotHistLevel2(self, data, labels):
        # fig = plt.figure()
        colors = patches = []
        ax = plt.subplot()
        if len(labels[1]) == 2:
            colors = ["r", "b"]
            colors *= 2
            patches = [mpatches.Patch(color=colors[i], label=labels[1][i]) for i in range(len(labels[1]))]
        elif len(labels[1]) == 5:
            colors = ["r", "b", "k", "y", "g"]
            colors *= 2
            patches = [mpatches.Patch(color=colors[i], label=labels[1][i]) for i in range(len(labels[1]))]
        elif len(labels[1]) == 6:
            colors = ["r", "b", "k", "y", "g", "c"]
            colors *= 2
            patches = [mpatches.Patch(color=colors[i], label=labels[1][i]) for i in range(len(labels[1]))]
        elif len(labels[1]) == 7:
            colors = ["r", "b", "k", "y", "g", "c", "m"]
            colors *= 2
            patches = [mpatches.Patch(color=colors[i], label=labels[1][i]) for i in range(len(labels[1]))]
        elif len(labels[1]) >= 9:
            lc = linearClassifierClass.linearClassifier()
            file = "ColorsHTML.xlsx"
            sheet = "Colors"
            cols = "B"
            skip = 0
            colorHTML = lc.loadData(file, sheet, cols, skip)
            colors = [colorHTML[i][0] for i in range(len(labels[1]))]
            colors *= 2
            patches = [mpatches.Patch(color=colors[i], label=labels[1][i]) for i in range(len(labels[1]))]
        plt.legend(handles=patches)
        ax.hist(data, color=colors, rwidth=1, align="mid", bins=len(data))
        maxY = max([len(datum) for datum in data])
        i = 1
        for datum in data:
            if datum.size == 0:
                plt.text(i, 0, 0, fontsize=14, horizontalalignment='center',verticalalignment='center')
            else:
                plt.text(datum[0], datum.size+100, datum.size, fontsize=14, horizontalalignment='center',verticalalignment='center')
            i += 1
        p = mpatches.Rectangle((0, 0), (len(data)/2)+.5, maxY+500, facecolor="y", alpha=.2)
        q = mpatches.Rectangle(((len(data)/2)+.5, 0), len(data)/2, maxY+500, facecolor="g", alpha=.2)
        ax.add_patch(p)
        ax.add_patch(q)
        plt.text(len(data)/4+.5, maxY+100, labels[0][0], fontsize=15, horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='y'))
        plt.text(len(data)*.75+.25, maxY+100, labels[0][1], fontsize=15, horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='g'))
        ax.set_xticks([i for i in range(1, len(data)+1)])
        ax.set_ylim(0, maxY+500)
        xticks = [label for label in labels[1]]
        xticks *= 2
        ax.set_xticklabels(xticks, rotation='vertical')
        plt.show()

    def plotHistLevel3(self, data, labels):
        ax = plt.subplot()
        r = ["r"]
        b = ["b"]
        colors = (r*16 + b*16) * 2
        plt.hist(data, color=colors, bins=len(data))
        red_patch = mpatches.Patch(color='r', label=labels[1][0])
        blue_patch = mpatches.Patch(color='b', label=labels[1][1])
        plt.legend(handles=[red_patch, blue_patch])

        p = mpatches.Rectangle((0, 0), 32.5, 3400, facecolor="y", alpha=.2)
        q = mpatches.Rectangle((32.5, 0), 32, 3400, facecolor="g", alpha=.2)
        ax.add_patch(p)
        ax.add_patch(q)

        datums = []
        for datum in data:
            if len(datum) > 0:
                datums.append(datum[0])
            else:
                datums.append(0)
        for i in range(len(data)):
            ax.annotate(str(data[i].size), xy=(datums[i], len(data[i])))
        ax.set_xlim(0.5, len(data) + .5)
        ax.set_ylim(0, 3400)
        ax.set_xticks([i for i in range(1, 65)])
        xticks = [label for label in labels[2]]
        xticks *= 4
        ax.set_xticklabels(xticks, rotation='vertical')
        plt.text(16, 3300, labels[0][0], fontsize=15, horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='y'))
        plt.text(48, 3300, labels[0][1], fontsize=15, horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='g'))
        plt.savefig("histISE.png")
        plt.show()



if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")