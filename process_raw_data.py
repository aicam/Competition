import numpy as np
import os
import pandas as pd
from scipy.io import loadmat
import glob

BATCH_SIZE = 200

def read_classes_from_head_files(file):
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
    return my_dict


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
            lead_str += str(it) + ','
        lead_array['lead' + str(i)] = lead_str
    return lead_array


def get_joined_data(files):
    head_data = read_classes_from_head_files(files[0])
    mat_data = read_classes_from_mat_files(files[1])
    mat_data = convert_lead_to_str(mat_data)
    new_dict = {'name': mat_data['name'], 'lead1': mat_data['lead1'], 'lead2': mat_data['lead1'],
                'lead3': mat_data['lead3'], 'lead4': mat_data['lead4'], 'lead5': mat_data['lead5'],
                'lead6': mat_data['lead6'], 'lead7': mat_data['lead7'], 'lead8': mat_data['lead8'],
                'lead9': mat_data['lead9'], 'lead10': mat_data['lead10'], 'lead11': mat_data['lead11'],
                'lead0': mat_data['lead0'], 'Dx': head_data['Dx'], 'Hx': head_data['Hx'], 'Sx': head_data['Sx'],
                'Rx': head_data['Rx'], 'Sex': head_data['Sex'], 'Age': head_data['Age']}
    return new_dict


def get_pandas_dataframe(batch_files):
    datas = []
    for file in batch_files:
        datas.append(get_joined_data(file))
    return pd.DataFrame(datas)


items = [[item.replace('.mat', '.hea'), item] for item in glob.glob('dataset/*.mat')]
try:
    os.mkdir('processed_data')
except FileExistsError:
    pass

print(len(items))
for i in range(0, len(items), BATCH_SIZE):
    get_pandas_dataframe(items[i: i + BATCH_SIZE]).to_csv('processed_data/' + str(i) + '.csv')
    print('Batch ', str(i/BATCH_SIZE), ' finished')
# get_pandas_dataframe(items[:20]).to_csv('processed_data/1.csv')
# df = pd.read_csv('processed_data/1.csv')
# print(df['lead0'].apply(lambda x: x.split(',')))
# df = pd.read_hdf('processed_data/1.h5')
# print(df)
# for r in range(0, len(items), BATCH_SIZE):
#