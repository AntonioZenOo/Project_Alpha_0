print('Hello world!')

import numpy as np
import pandas as pd
from colorama import Fore

data_np =  np.genfromtxt('C:/files/DS_distrib/data_sample.csv',delimiter=',', skip_header = 1)
#data_df = pd.read_csv('C:/files/DS_distrib/data_sample.csv', sep=',')
#data_np2 = np.recfromcsv('C:/files/DS_distrib/data_sample.csv', delimiter=',', filling_values=np.nan, case_sensitive=True, deletechars='', replace_space=' ')

#print(Fore.CYAN)
#print(data_np)

#print(Fore.LIGHTYELLOW_EX)
#print(data_df)

print(Fore.LIGHTGREEN_EX)
print(data_np)

#factor_list = ['FACTOR1','FACTOR2','FACTOR3']
#data_df_3 = data_df[factor_list]
#print(data_df_3)

#div1 = data_df_3.diff()
print(type(data_np))
#exit()
data_np_3 = data_np[:,4:7]
print(Fore.CYAN)
print(data_np_3)

#print(Fore.CYAN)
#print(div1)
