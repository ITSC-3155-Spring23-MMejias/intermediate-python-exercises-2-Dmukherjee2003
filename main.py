import numpy as np
import random as r

list = []
for i in range(0,10):
    a = float(r.random())
    list.append(a)

arr = np.array(list)
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
print(arr)
print("Mean:", mean, "median", median, "Standard Deviaiton:", std )


  