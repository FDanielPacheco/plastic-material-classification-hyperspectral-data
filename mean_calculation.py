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

sample_ranges = []

calibrationSamples = [ "White_reference ", "Water_16_sediment", "Wood_d_NA_NA_PoA_field", "Clear water" , "Water_1500_algae", "Water_3000_algae", "Water_4_sediment", "Black_cloth_calibrationFacility"]

for i in range(len(sample_code)):
    if sample_code[i] not in calibrationSamples:
        if(replicate[i] == 1):
            data_mean = data[:, i]
            sample_range_init = i
            num_replicates = 1
        else:
            data_mean += data[:, i]
            num_replicates += 1
        if(replicate[i+1] != replicate[i] +1):
            sample_range = str(sample_range_init) + "-" + str(i)
            data_mean = data_mean/num_replicates
            new_data.append(data_mean)
            data_sample_codes.append(sample_code[i])
            sample_ranges.append((sample_range))






#Prints de Verificação
print(len(sample_ranges))
print(new_data[0])      #do 1 ao 5
print(new_data[1])      #do 6 ao 10
print(new_data[5])      #do 26 ao 35
print(new_data[416])    
print(len(new_data))
print(len(data_sample_codes))


new_data_array = np.array(new_data)



df_export = pd.DataFrame(
    new_data_array,
    index=data_sample_codes,
    columns=wavelengths
)

# Insert sample ranges as first column
df_export.insert(0, "Sample_Range", sample_ranges)

df_export.to_csv("New_data.csv")

