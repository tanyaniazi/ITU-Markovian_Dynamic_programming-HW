import pandas as pd
import os
import numpy as np

folder_path = '/Users/user/Desktop/200/saved_files/Grouping Patients/'
save_path = '/Users/user/Desktop/200/saved_files/Grouping Patients/'

for i in range(1, 6):
    if i == 4:
        continue
    group_path = folder_path + 'DG' + str(i) + '/'
    data_dirlist = os.listdir(group_path)

    data = np.zeros((len(data_dirlist), 14))

    for index in range(len(data_dirlist)):
        read_file = pd.read_csv(group_path + data_dirlist[index], header=None).iloc[1:, 1:]
        for j in range(14):
            each_column = read_file.iloc[:, j].values
            for item in each_column:
                if item % 1 == 0:
                    data[index, j] = item
                    break
    df = pd.DataFrame(np.mean(data, axis=0))
    df.to_csv(save_path + 'DG' + str(i) + ' Average Control Limit Within a disease group.csv')

