import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#1
df=pd.read_csv("D:\placement.csv")
print(df.shape)
print(df.sample(5))
#2
plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
sns.distplot(df['cgpa'])
plt.subplot(1,2,2)
sns.distplot(df['placement_exam_marks'])
plt.show()
#3
df['placement_exam_marks'].skew()
print("Mean value of cgpa",df['cgpa'].mean())
print("Std value of cgpa",df['cgpa'].std())
print("Min value of cgpa",df['cgpa'].min())
print("Max value of cgpa",df['cgpa'].max())
#4
print("Highest allowed",df['cgpa'].mean()+3*df['cgpa'].std())
print("Lowest allowed",df['cgpa'].mean()-3*df['cgpa'].std())
print(df[(df['cgpa']>8.80)|(df['cgpa']<5.11)])
#5
new_df=df[(df['cgpa']>8.80)&(df['cgpa']<5.11)]
print(new_df)
df['cgpa_zscore'] = (df['cgpa'] - df['cgpa'].mean())/df['cgpa'].std()
print(df.head())
print(df[(df['cgpa_zscore'] > 3)|(df['cgpa_zscore'] < -3)])
print(df[(df['cgpa_zscore'] > 3)&(df['cgpa_zscore'] < -3)])
#6
upper_limit=df['cgpa'].mean()+3*df['cgpa'].std()
lower_limit=df['cgpa'].mean()-3*df['cgpa'].std()
print(upper_limit)
print(lower_limit)
print(df.shape)
print(df['cgpa'].describe())