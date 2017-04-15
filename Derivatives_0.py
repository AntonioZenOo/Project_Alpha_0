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

def hessian(x):
    """
    Calculate the hessian matrix with finite differences
    Parameters:
       - x : ndarray
    Returns:
       an array of shape (x.dim, x.ndim) + x.shape
       where the array[i, j, ...] corresponds to the second derivative x_ij
    """
    x_grad = np.gradient(x)
    hessian = np.empty((x.ndim, x.ndim) + x.shape, dtype=x.dtype)
    for k, grad_k in enumerate(x_grad):
        # iterate over dimensions
        # apply gradient again to every component of the first derivative.
        tmp_grad = np.gradient(grad_k)
        for l, grad_kl in enumerate(tmp_grad):
            hessian[k, l, :, :] = grad_kl
    return hessian

x = np.random.randn(100, 100, 100)
h = hessian(data_np_3)
x_grad = np.gradient(data_np_3)
print(Fore.LIGHTYELLOW_EX)
print(h)

print(Fore.CYAN)
print(x_grad)