import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix 
#1
data=pd.read_excel('D:\car_price_prediction.xlsx')
print(data.head())
print(data.shape)
print(data.describe())
#2
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
sns.boxplot(y=data['Price'])
plt.ylim(-2000,300000)
plt.subplot(1,2,2)
sns.boxplot(y=data['Prod. year'])
plt.show()
#3
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(data['Leather interior'])
plt.subplot(1,2,2)
sns.countplot(data['Fuel type'])
plt.show()
#4
print(data['Leather interior'].value_counts())
print(data['Fuel type'].value_counts())
print(data['Leather interior'].value_counts(normalize=True))
print(data['Fuel type'].value_counts(normalize=True))
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.boxplot(x=data['Leather interior'], y=data['Price'] , data=data)
plt.ylim(-2000,300000)
plt.subplot(1,2,2)
sns.boxplot(x=data['Leather interior'],y=data['Prod. year'], data=data)
plt.show()
#5
print(pd.crosstab(data['Fuel type'], data['Gear box type'],normalize='index').round(2))
sns.heatmap(data[['Price','Cylinders']].corr() , annot=True)
plt.show()
print(data.isnull().sum())
q1,q3=data['Cylinders'].quantile([.25,.75])
print(q1,q3)
IQR=(q3-q1)
lower=q1-1.5*(IQR)
upper=q3+1.5*(IQR)
print(lower)
print(upper)
df=data[data['Cylinders']>lower]
print(df)
#6
data['Cylinders']=np.where(data['Cylinders']>upper,upper, data['Cylinders']) 
sns.boxplot(y=data['Cylinders'])
plt.ylim(-1,10)
plt.show()
#7
data=pd.get_dummies(data,drop_first=True)
print(data.head())
x=data.drop('Airbags',axis=1)
y=data['Airbags']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=21)
print(x_train.shape) 
print(x_test.shape)
print(y_train.value_counts(normalize=True).round(2))
print(y_test.value_counts(normalize=True).round(2))
#8
lr=LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
print(y_pred[0:5])
#9
print(confusion_matrix(y_test,y_pred))
