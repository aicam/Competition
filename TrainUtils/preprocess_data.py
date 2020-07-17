import numpy as np
from .config import *
def convert_df(df):
    arr = df
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = arr[i][j].split(',')
            arr[i][j] = np.genfromtxt(np.array(arr[i][j]))

    return arr

def padding(arr):
    x = np.zeros([arr.shape[0], CNNInputShape[1], CNNInputShape[0]])
    x_in = np.zeros([arr.shape[0], CNNInputShape[0], CNNInputShape[1]])
    for i in range(len(arr)):
        for j in range(12):
            x[i][j][:len(arr[i][j])] = arr[i][j]
    for i in range(len(x)):
        x_in[i] = np.transpose(x[i])
    return x_in

def get_labels_array(labels, Dx):
    Y = []
    for item in Dx:
        new_y = labels.copy()
        lbls = [int(it) for it in item.split(',')]
        for lb in lbls:
            new_y[lb] = 1
        Y.append(new_y.values())
    return Y