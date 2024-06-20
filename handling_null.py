import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#1
print(sns.get_dataset_names())
data=sns.load_dataset('attention')
print(data.head())
print(data.isnull().value_counts())
#2
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
pl=sns.load_dataset('planets')
print(pl.isnull().value_counts())
print(pl.shape)
pl1=pl.dropna()
print(pl1.shape)
print(pl.fillna('Null Value'))
print(pl.sample(10))
#3
value1=pl['orbital_period'].mean().round(5)
print(value1)
pl.fillna(value1,inplace=True)
print(pl)