import numpy as np
import os
import pandas as pd
from scipy.io import loadmat
import glob

def read_classes_from_head_files(file):
    my_list = []
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
    my_list.append(my_dict)
    return my_list

def read_classes_from_mat_files(file):
    leads = ['name']
    for i in range(12):
        leads.append('lead' + str(i))
    my_dict = dict.fromkeys(leads)
    my_dict['name'] = file.split('.')[0]
    # for val in
    vals = loadmat(file)['val']
    for i in range(len(vals)):
        my_dict['lead' + str(i)] = vals[i]
    return my_dict

def convert_lead_to_str(lead_array):
    for i in range(10):
        lead_str = ''
        for it in lead_array['lead' + str(i)]:
            lead_str += str(it) + ''
        lead_array['lead' + str(i)] = lead_str
    return lead_array

def get_joined_data(files):
    head_data = read_classes_from_head_files(files[0])
    mat_data = read_classes_from_mat_files(files[1])
    new_dict = dict(head_data[0], **mat_data)
    return new_dict

def get_pandas_dataframe(dicts):

items = [[item.replace('.mat', '.hea'), item] for item in glob.glob('dataset/*.mat')]
get_joined_data(items[0])