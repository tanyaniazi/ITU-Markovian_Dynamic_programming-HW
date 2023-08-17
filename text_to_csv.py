import os

# path = "/Users/user/Desktop/Ad Topics in IE/A2-supp/instances/IWLM_instances/H1-18_L14"
# save_path = '/Users/user/Desktop/Ad Topics in IE/A2-suppinstances/IWLM_instances/csv-csv'
path = "/Users/user/Desktop/my_attempt/textfiles/"
save_path = "/Users/user/Desktop/my_attempt/csvfiles/"

# os.listdir prints a list of names of all the files present in the specified path.
dir_list = os.listdir(path) 
 
import pandas as pd
import numpy as np

# we create an empty list that we will fill it with the converted data 
corrupted_files = []

# we list the names of the columns of each matrix in one file
columns_patient = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
columns_patient_liver = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
columns_reward = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

# since some of the files are not in the standard format of the matrices (dimensions might be different etc we use the try/except code)
for index in dir_list:
    try:
        # path = "/Users/user/Desktop/Ad Topics in IE/A2-supp/instances/IWLM_instances/H1-18_L14/"
        # save_path = '/Users/user/Desktop/Ad Topics in IE/A2-supp/instances/IWLM_instances/csv-csv/'
        path += index

        # .removesuffix is supported in the plus 3.9 versions of python
        # in the case of lower versions use the below code:
        # save_path = save_path[:-4]
        save_path += index.removesuffix('.txt')

        # print(index)
        # pd.read_csv reads not only csv files but also txt files
        # header = None is for our data files consist of the columns names already and we do not want our DF to read the column names as the data
        read_file = pd.read_csv (path, header=None) 

        # empty dataframes to be filled with only the column names
        patient_df = pd.DataFrame(columns = columns_patient)
        patient_liver_df = pd.DataFrame(columns=columns_patient_liver)
        reward_df = pd.DataFrame(columns=columns_reward)

        for i in range(2,20): # to iterate over rows of the first matrix (patient health)
            data = read_file.iloc[i].values # reads the values of each row in each iter
            splitted_data = data[0].split()  # to seperate the data from each other 
                                             #however, list cannot be split, split is for strings. we add the index of 0 as [0] to fix this
            splitted_data = splitted_data[1:]  # not to include the first column of the row since it is the name of the row 
            patient_df.loc[len(patient_df)] = splitted_data  # filling the empty DF row by row with the splitted data

        patient_df.index = np.arange(1, len(patient_df) + 1)  # to give names (indexes) to the rows
        patient_df.to_csv(save_path+' patient.csv')  # converting the processed data to csv

        for i in range(22,40):
            data = read_file.iloc[i].values
            splitted_data = data[0].split()
            splitted_data = splitted_data[1:]
            patient_liver_df.loc[len(patient_liver_df)] = splitted_data

        patient_liver_df.index = np.arange(1, len(patient_liver_df) + 1)
        patient_liver_df.to_csv(save_path+' patient_liver.csv')


        for i in range(42, 60):
            data = read_file.iloc[i].values
            splitted_data = data[0].split()
            splitted_data = splitted_data[1:]
            reward_df.loc[len(reward_df)] = splitted_data

        reward_df.index = np.arange(1, len(reward_df) + 1)
        reward_df.to_csv(save_path+' reward.csv')
    
    except:
        corrupted_files.append(index)
        continue



print(corrupted_files)

