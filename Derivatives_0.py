print('Hello world!')

import numpy as np
import pandas as pd
from colorama import Fore

data_np =  np.genfromtxt('C:/files/DS_distrib/data_sample.csv',delimiter=',')
data_df = pd.read_csv('C:/files/DS_distrib/data_sample.csv', sep=',')
data_np2 = np.recfromcsv('C:/files/DS_distrib/data_sample.csv', delimiter=',', filling_values=np.nan, case_sensitive=True, deletechars='', replace_space=' ')

#print(Fore.CYAN)
#print(data_np)

print(Fore.LIGHTYELLOW_EX)
print(data_df)

print(Fore.LIGHTGREEN_EX)
print(data_np2)


data_np2_3 = data_np2[:,[5,6,7]]
print(data_np2_3)
print(Fore.CYAN)
data_df_3 = data_df['FACTOR1','FACTOR2','FACTOR3']
print(data_df_3)