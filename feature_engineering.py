import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
print(sns.get_dataset_names)
#1
df=sns.load_dataset('titanic')
print(df.head())
#2
df2=df[['survived','pclass','age','parch']]
print(df2.head())
#3
df3=df2.fillna(df2.mean())
print(df3.head())
#4
x=df3[['pclass','age','parch']]
y=df2[['survived',]].fillna(df2.mean())
print(x)
print(y)
#5
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=51)
print(x_train)
print(x_train.shape)
print(x_test)
print(x_test.shape)
#6
sc=StandardScaler()
print(sc.fit(x_train))
print(sc.mean_)
print(sc.scale_)
print(x_train.describe())
#7
x1_scalled=sc.transform(x_train)
x2_scalled=sc.transform(x_test)
print(x1_scalled)
print(x1_scalled.head())
print(x2_scalled)
print(x2_scalled.head())
#8
x_test_sclval=pd.DataFrame(x_test)
print(x_test_sclval)
#9
mnc=MinMaxScaler()
print(mnc.fit(x_train))
x_train_min=mnc.transform(x_train)
x_test_min=mnc.transform(x_test)
print(x_train_min)
print(x_test_min)
data1=pd.DataFrame(x_test_min)
data2=pd.DataFrame(x_train_min)
print(data1.describe())
print(data2.describe().round(5))