import pandas as pd
import numpy as np


convert_f = lambda x: [int(item) for item in x.split(',') if item != '']
min = 5000
max = 12000
for i in range(104):



    print('batch {} started'.format(i))
    df = pd.read_csv('processed_data/' + str(i*200) + '.csv')
    for j in range(len(df)):
        new_len = len(df['lead0'].apply(convert_f).iloc[j])
        if(new_len > max):
            max = new_len
        if(new_len < min):
            min = new_len
    # print(len(df['lead0'].apply(lambda x: x.split(',')).iloc[0]))
print(min, ' ', max)