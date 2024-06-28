import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
#1
poke=pd.read_csv('D:\pokemon.csv')
print(poke.head())
poke.rename(columns={'Type 1':'Primary_Type','Type 2':'Secondary_Type'}, inplace=True)
print(poke.head())
print(poke['Primary_Type']=='Grass')
#2
grass_pokemon=poke[poke['Primary_Type']=='Grass']
print(grass_pokemon.head())
water_pokemon=poke[poke['Primary_Type']=='Water']
print(water_pokemon.head())
fire_pokemon=poke[poke['Primary_Type']=='Fire']
print(fire_pokemon.head())
#3
print(poke.shape)
print(grass_pokemon.shape)
print(water_pokemon.shape)
print(fire_pokemon.shape)
#4
sns.histplot(grass_pokemon['Speed'])
plt.show()
sns.histplot(grass_pokemon['Sp. Atk'])
plt.show()
sns.histplot(grass_pokemon['Sp. Def'])
plt.show()
print(grass_pokemon.describe())
#5
sns.histplot(water_pokemon['Speed']) 
plt.show()
sns.histplot(water_pokemon['Sp. Atk'])
plt.show()
sns.histplot(water_pokemon['Sp. Def'])
plt.show()
print(water_pokemon.describe())
#6
sns.histplot(fire_pokemon['Speed'])
plt.show()
sns.histplot(fire_pokemon['Sp. Atk'])
plt.show()
sns.histplot(fire_pokemon['Sp. Def'])
plt.show()
print(fire_pokemon.describe())
#7
print(poke['Legendary'].value_counts())
x=poke[['Speed']] 
y=poke[['Legendary']]
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.3)
dtc=DecisionTreeClassifier()
dtc.fit(x_train,y_train)
y_pred=dtc.predict(x_test)
print(y_pred[0:5])
print(y_test.head())
#8
confusion_matrix(y_test,y_pred)
x=poke[['Defense']] 
print(x.head())
y=poke[['Attack']]
print(y.head())
#9
dtr=DecisionTreeRegressor()
dtr.fit(x_train,y_train)
y_pred=dtr.predict(x_test)
print(y_pred[0:5])
y_test.head()
#10
print(mean_squared_error(y_test,y_pred))