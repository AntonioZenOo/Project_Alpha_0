import numpy as np
import pandas as pd
from colorama import Fore
from IPython.display import display
from IPython.display import Image

data_df = pd.read_csv('C:/files/DS_distrib/data_sample.csv', sep=',')

print(Fore.LIGHTYELLOW_EX)
print(data_df)

Q123 = np.array([0.1, 0.2, 0.3])

data_df_upd = data_df
data_df_upd['Vjh'] = data_df_upd['FACTOR1']*0.1+data_df_upd['FACTOR2']*0.2+data_df_upd['FACTOR3']*0.3
data_df_upd['exp_Vjh'] = np.exp(data_df_upd['Vjh'])

print(Fore.LIGHTRED_EX)
print(data_df_upd)

EVENTS_SUM = data_df_upd.groupby(['EVENT_ID'])['exp_Vjh'].sum()
EVENTS_SUM_DF = EVENTS_SUM.to_frame().reset_index()

EVENTS_SUM_DF.columns = ['EVENT_ID', 'Vjh_E_SUM']

print(Fore.LIGHTMAGENTA_EX)
print(EVENTS_SUM_DF)
print(type(EVENTS_SUM_DF))

print(Fore.LIGHTRED_EX)
#data_df_upd.set_index('EVENT_ID').join(EVENTS_SUM_DF.set_index('EVENT_ID'))
data_df_upd2 = pd.merge(data_df_upd, EVENTS_SUM_DF, on='EVENT_ID',suffixes=('_left', '_right'))
print(data_df_upd2)

data_df_upd2['Pjh'] = data_df_upd2['exp_Vjh'] /  data_df_upd2['Vjh_E_SUM']
data_df_upd2['log_Pjh'] =  np.log(data_df_upd2['Pjh'])

print(Fore.LIGHTYELLOW_EX)
print(data_df_upd2)

L = data_df_upd2[data_df_upd2['WIN'] == 1]['log_Pjh'].sum()
print(Fore.LIGHTGREEN_EX)
print(L)
#df['exp'] = np.exp(df['b'])