### VALUE ITERATION ALGORITHM ###

import numpy as np
import pandas as pd
import os


imm_reward = 1 #daily
lam = (0.97 ** (1/365))
epsilon = 1e-3
delta = epsilon * ((1-lam)/(2*lam))


v = np.zeros((19,14))
v_new = v

reward_path = '/Users/user/Desktop/200/rewards/'
patient_path = '/Users/user/Desktop/200/patient_state/'
save_path = '/Users/user/Desktop/200/saved_files/'

reward_dirlist = os.listdir(reward_path)

# iters among the list of the names of the csv files in the folder 
for index in reward_dirlist:
    patient_state_full_path = patient_path + index
    reward_full_path = reward_path + index

    state_patient = pd.read_csv(patient_state_full_path, header=None).iloc[1:,1:]  # loads TPM, 19x19 matrix
    reward_data = pd.read_csv(reward_full_path).iloc[:, 1:]  # loads rewards 18x14

    v = np.zeros((19, 14))  # empty 19x14 matrix to fill in with values
    v_new = v

    diverged = [False for i in range(14)]
    difference = 1

    for iter in range(30000):
        for liver_cond in range(14):
            if diverged[liver_cond] == True:  
                continue
            pt_reward = reward_data.iloc[:, liver_cond].values

            for i in range(19):   #iterating over states of the patient
                q = np.dot(v.iloc[i].values, v[:, liver_cond].T)

                if i < 18:            #conditioning on the fact that death has no immediate reward 
                    v_new[i, liver_cond] = max(q * lam + imm_reward, pt_reward[i])
                else:   
                    v_new[i] = q * lam

            if iter > 10:
                difference = (np.abs(v[:, liver_cond] - v_new[:, liver_cond])).max()

            if difference <= delta: 
                diverged[liver_cond] = True
            v = np.copy(v_new)

    test = pd.DataFrame(v) 
    test = test.drop(test.index[18])
    test.set_index(np.arange(1, 19), drop=True, inplace=True)
    test.columns = np.arange(1, 15)
    test.to_csv(save_path + index + '.csv')