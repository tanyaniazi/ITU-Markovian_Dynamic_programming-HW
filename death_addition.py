import os
from turtle import title
path = "/Users/user/Desktop/200/patient_state/"
# Get the list of all files and directories
dir_list = os.listdir(path)

import pandas as pd
import numpy as np

for index in dir_list:
    path = "/Users/user/Desktop/200/patient_state/"
    save_path = '/Users/user/Desktop/200/patient_state/modified/'
    path += index
    save_path += index
    df = pd.read_csv(path, index_col=0)
    # df.drop(df.columns[0], axis=1, inplace=True)
    new_column = np.zeros(18)

    df['19'] = new_column
    new_row = np.zeros(18)
    new_row = np.append(new_row, 1)
    df.loc[19] = new_row


    df_sum = df.sum(axis = 1)

    for i in range(len(df)):
        if df_sum.iloc[i] == round(1.0, 4):
            continue
        elif df_sum.iloc[i] > 1.0:
            max_value = round(df.iloc[i].max(), 4)
            max_position = df.iloc[i].idxmax()

            row_sum = round(df_sum.iloc[i], 4)
            new_max_value = round(max_value - (row_sum - 1), 4)
            df.iloc[i][max_position] =  new_max_value
        else:
            row_sum = round(df_sum.iloc[i], 4)
            death_value = round(1 - row_sum, 4)
            df.iloc[i][18] =  death_value

    df.to_csv(save_path)
    