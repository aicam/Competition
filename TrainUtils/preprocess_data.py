import numpy as np

def convert_df(df):
    learning_cols = [it for it in df.columns if it.__contains__('lead')]
    arr = df[learning_cols].to_numpy()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = arr[i][j].split(',')
            arr[i][j] = np.genfromtxt(np.array(arr[i][j]))

    return arr

def padding(arr):
    x = np.zeros([arr.shape[0], 12, 94000])
    for i in range(len(arr)):
        for j in range(12):
            x[i][j][:len(arr[i][j])] = arr[i][j]
    return x

def get_labels_array(labels, Dx):
    Y = []
    for item in Dx:
        new_y = labels.copy()
        lbls = [int(it) for it in item.split(',')]
        for lb in lbls:
            new_y[lb] = 1
        Y.append(new_y.values())