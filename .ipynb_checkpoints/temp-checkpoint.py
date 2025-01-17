#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read data
path = 'E:\\AI\\course\\02\\data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
#show data details
print('data = \n' ,data.head(10) )
print('**************************************')
print('data.describe = \n',data.describe())
print('**************************************')
#draw data
data.plot(kind='scatter', x='Population', y='Profit', figsize=(5,5))

#=========================================================================
