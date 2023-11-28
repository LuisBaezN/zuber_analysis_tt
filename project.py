import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

try:
    path = 'datasets/moved_project_sql_result_01.csv'
    data_1 = pd.read_csv(path)
    path = 'datasets/moved_project_sql_result_04.csv'
    data_2 = pd.read_csv(path)
except:
    path = '../datasets/moved_project_sql_result_01.csv'
    data_1 = pd.read_csv(path)
    path = '../datasets/moved_project_sql_result_04.csv'
    data_2 = pd.read_csv(path)

data_1.info()
print(data_1.head(3))

data_2.info()
print(data_2.tail(3))

print('> Duplicated data: ', data_1.duplicated().sum())
print('> Duplicated data: ', data_2.duplicated().sum())

print(data_2.sort_values('average_trips', ascending=False).head(10))

print(len(data_1['company_name'].unique()))
data_1.plot(kind='bar', x='company_name')
plt.show()