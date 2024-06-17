import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
#1
sns.get_dataset_names()
tit=sns.load_dataset('titanic')
print(tit.shape)
print(tit.head())
print(tit.sample(5))
print(tit.info())
print(tit.describe())
#2
print(tit.duplicated())
print(tit[886:887])
#3
sns.histplot(tit['survived'])
plt.show()
print(tit['survived'].value_counts())
#4
print(tit['who'].value_counts())
sns.countplot(tit['who'])
plt.show()
#5
plt.hist(tit['age'])
plt.show()
#6
sns.boxplot(x='fare',data=tit)
plt.show()
#7
sns.boxplot(tit['age'])
plt.show()
#8
tips=sns.load_dataset('tips')
print(tips.head())
flight=sns.load_dataset('flights')
print(flight.head())
iris=sns.load_dataset('iris')
print(iris.head())
sns.scatterplot(x='total_bill',y='tip',data=tips)
plt.show()
#9
sns.scatterplot(x='total_bill',y='tip',hue='sex',data=tips)
plt.show()
#10
sns.scatterplot(x='total_bill',y='tip',hue='sex',style='smoker',data=tips)
plt.show()
#11
sns.scatterplot(x='total_bill',y='tip',hue='sex',style='smoker',size='size',data=tips)
plt.show()
#12
sns.barplot(x='pclass',y='age',data=tit)
plt.show()
#13
sns.barplot(x='pclass',y='fare',hue='sex',data=tit)
plt.show()
#14
sns.boxplot(x='sex',y='age',hue='sex',data=tit)
plt.show()
#15
print(pd.crosstab(tit['pclass'],tit['survived']))
sns.heatmap(pd.crosstab(tit['pclass'],tit['survived']))
plt.show()