import numpy as np
import pandas as pd
import os

value_path = '/Users/user/Desktop/200/saved_files/value_results '
reward_path = '/Users/user/Desktop/200/patient_state'
save_path = '/Users/user/Desktop/200/saved_files/'

reward_dirlist = os.listdir(value_path)

for index in reward_dirlist:
    value_full_path = value_path + index
    reward_full_path = reward_path + index
    reward_full_path = reward_full_path[:-4]

    policy_matrix = [['' for i in range(14)] for j in range(18)]
    value_data = pd.read_csv(value_full_path, header = None).iloc[1:, 1:]
    reward_data = pd.read_csv(reward_full_path).iloc[:, 1:]

    for i in range(18):
      for j in range(14):
        if value_data.iloc[i, j] > reward_data.iloc[i, j]:
          policy_matrix[i][j] = 'Reject'
        else:
          policy_matrix[i][j] = 'Accept'

    test = pd.DataFrame(policy_matrix)
    test.to_csv(save_path + index)