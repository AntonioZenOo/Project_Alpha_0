print('Hello world!')

import numpy as np
import pandas as pd
from colorama import Fore

data_np =  np.genfromtxt('C:/Users/ДиктаторЭ/Desktop/DS_distri/data_sample.csv',delimiter=',')
data_df = pd.read_csv('C:/Users/ДиктаторЭ/Desktop/DS_distrib/data_sample.csv', sep=',')

print(Fore.CYAN)
print(data_np)