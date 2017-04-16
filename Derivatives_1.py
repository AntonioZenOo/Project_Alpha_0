import numpy as np
import pandas as pd
from colorama import Fore

data_np =  np.genfromtxt('C:/files/DS_distrib/data_sample.csv',delimiter=',', skip_header = 1)

print(Fore.LIGHTGREEN_EX)
print(data_np)

data_np_3 = data_np[:,4:7]
print(Fore.CYAN)
print(data_np_3)

Q123 = np.array([0.1, 0.2, 0.3])

df = pd.DataFrame(Q123)

data_Q123 = data_np_3*Q123
print(Fore.GREEN)
print(df)
exit()

print(Fore.GREEN)
print(data_Q123)

V = data_Q123.sum(axis=1)
print(Fore.BLUE)
print(V)
