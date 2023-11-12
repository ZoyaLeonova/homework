import numpy as np
import pandas as pd
import seaborn as sns

from arch.bootstrap import IIDBootstrap, IndependentSamplesBootstrap

filename_excel = 'Для выполнения домашнего задания.xlsx'

filename_col_a = pd.read_excel(filename_excel, header=0, usecols='A')
filename_col_b = pd.read_excel(filename_excel, header=0, usecols='B')
filename_col_c = pd.read_excel(filename_excel, header=0, usecols='C')

#rng = np.random.default_rng(111111)
#x = rng.normal(loc=5, scale=4, size=20)

#sred = np.mean(x)

x = np.array(filename_col_a)


print(x)
# print(filename_opened.head())
