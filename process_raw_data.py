import numpy as np
import os
import pandas as pd
from scipy.io import loadmat
import glob

def read_classes_from_head_files(head_files):
    my_list = []
    passed_file = 0
    for file in head_files:
        if passed_file % 100 == 0:
            print('number of passed files: ', passed_file)
        my_dict = dict.fromkeys(['name', 'Hx', 'Rx', 'Dx', 'Sex', 'Age'])
        my_dict['name'] = file.split('.')[0]
        with open(file, 'r') as f:
            for line in f:
                if line.startswith('#Sx'):
                    my_dict['Sx'] = line.split(': ')[1].rstrip()
                if line.startswith('#Hx'):
                    my_dict['Hx'] = line.split(': ')[1].rstrip()
                if line.startswith('#Rx'):
                    my_dict['Rx'] = line.split(': ')[1].rstrip()
                if line.startswith('#Dx'):
                    my_dict['Dx'] = line.split(': ')[1].rstrip()
                if line.startswith('#Sex'):
                    my_dict['Sex'] = line.split(': ')[1].rstrip()
                if line.startswith('#Age'):
                    my_dict['Age'] = line.split(': ')[1].rstrip()
        passed_file = passed_file + 1
        my_list.append(my_dict)
    return my_list

def read_classes_from_mat_files(mat_files):
    my_list = []
    passed_file = 0
    for file in mat_files:
        if passed_file % 100 == 0:
            print('number of passed files: ', passed_file)
        leads = ['name']
        for i in range(12):
            leads.append('lead' + str(i))
        # print(i for i in [str(x for x in list(range(12
        # ))])
        my_dict = dict.fromkeys(leads)
        my_dict['name'] = file.split('.')[0]
        # for val in
        vals = loadmat(file)['val']
        for i in range(len(vals)):
            my_dict['lead' + str(i)] = vals[i]
        passed_file = passed_file + 1
        my_list.append(my_dict)
    return my_list


print(read_classes_from_head_files(['dataset/E01763.hea']))