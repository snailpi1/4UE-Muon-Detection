import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

header_size = 6 #number of leading lines to ignore
footer_size = 4500 #number of trailing lines to ingnore

data_raw = np.genfromtxt("test.txt", delimiter=";", dtype=None, skip_header=header_size,
                     skip_footer=footer_size, encoding=None) #generating a numpy array using ; as a delimiter

data = np.array((len(data_raw), 2))
data = data_raw[:,:2] #removing an empty column resulting from a trailing ; in each line

for i in range(len(data)):
    if data[i,0] == "Coincidence":
        data[i,0] = True
    else:
        print("oops")

time_array = np.zeros((len(data), 5))
for i in range(len(data)): #seperating out values with : as delimiter, resulting in an array reading [hh, mm, ss, us, ns]
    time_array[i,:] = np.array( ((data[i,1]).split(":"))[:-2], dtype=float)

time_in_seconds = time_array * [3600, 60, 1, 1e-6, 1e-9] #converting to nanoseconds for ease of conversion an precision
total_nanoseconds = time_in_seconds.sum(axis=1) * 10 ** 9

time_values = total_nanoseconds.astype("datetime64[ns]") #converting to datetime64 dtype

#fixing our frame of reference from the day of data acquisition instead of UNIX reference, in Paris we started on
# 29/03/2024
start = np.datetime64("2024-03-29")
ref = np.datetime64("1970-01-01")
delta = start - ref
for i in range(len(time_values)):
    time_values[i] = time_values[i] + delta


