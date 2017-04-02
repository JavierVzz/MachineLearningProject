import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class histogramAdult():

    def __init__(self):
        pass

    def plotHist1d(self, data):
        plt.hist(data)
        plt.show()


if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")