import pandas as pd
import os
import numpy as np
folder_path = '/Users/user/Desktop/200/saved_files/Grouping Patients/'
save_path = '/Users/user/Desktop/200/saved_files/Grouping Patients/'


for i in range(1,6):
  data = np.zeros((18, 14))
  if i==4:
    continue
  group_path = folder_path + 'DG' + str(i) + '/'
  data_dirlist = os.listdir(group_path)
  for index in data_dirlist:
    read_file = pd.read_csv(group_path + index, header = None).iloc[1:, 1:]
    data += read_file
  data /= len(data_dirlist)
  output_data = pd.DataFrame(data)
  output_data.to_csv(save_path + 'DG' + str(i) + ' Matrix.csv')
