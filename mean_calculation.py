# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 16:54:00 2025

@author: samar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Project_Data_Values.csv")
df_meta = pd.read_csv("Project_Data.csv")
data = df.iloc[0:, 1:].astype(float).values
wavelengths = df.iloc[0:, 0].astype(float).values

sample_code = df_meta.iloc[0:, 0].astype(str).values
replicate = df_meta.iloc[0:, 16].astype(int).values

data_sample_codes = []
new_data = []
data_mean = 0
num_replicates = 0



for i in range(2150):
    if sample_code[i] != "White_reference " and sample_code[i] != "Water_16_sediment":
        if(replicate[i] == 1):
            data_mean = data[:, i]

            num_replicates = 1
            if(replicate[i+1] ==1):
                data_mean = data_mean/num_replicates
                new_data.append(data_mean)
        else:
            data_mean += data[:, i]
            num_replicates += 1
            if(replicate[i+1] != replicate[i] +1):
                data_mean = data_mean/num_replicates
                new_data.append(data_mean)
                data_sample_codes.append(sample_code[i])


data_sample_codes.append("Vazio")
#Prints de Verificação
print(new_data[0])      #do 1 ao 5
print(new_data[1])      #do 6 ao 10
print(new_data[5])      #do 26 ao 35
print(new_data[416])    #do 5546 ao 5550
print(len(new_data))
print(len(data_sample_codes))


new_data_array = np.array(new_data)
new_data_array = new_data_array.T

new_data = new_data_array.tolist()


df_export = pd.DataFrame(new_data, columns=data_sample_codes)

df_export.to_csv("New_data.csv", index=False)