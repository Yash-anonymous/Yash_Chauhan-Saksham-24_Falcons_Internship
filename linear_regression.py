import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#1
sns.get_dataset_names
df=sns.load_dataset('iris')
print(df.head())
print(df[df['sepal_width']>4])
print(df[df['petal_width']>2])
sns.scatterplot(x='sepal_length',y='petal_length',hue='species')
plt.show()
print(df.value_counts())
print(df['petal_length'].isnull().value_counts())
print(df['petal_width'].isnull().value_counts())
print(df['sepal_length'].isnull().value_counts())
print(df['petal_width'].isnull().value_counts())
#2
x=df[['sepal_length']]
y=df[['sepal_width']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
#3
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
print(y_pred[0:5])
print(y_test.head())
print(mean_squared_error(y_test,y_pred))
sns.regplot(x=x,y=y,data=df)
plt.show()
#4
q=df[['sepal_length']]  
p=df[['sepal_width','petal_length','petal_width']]
p_train,p_test,q_train,q_test=train_test_split(p,q,test_size=0.2)
lr.fit(p_train,q_train)
q_pred=lr.predict(p_test)
print(q_test.head())
print(q_pred[:5])
#5
mean_squared_error(q_test,q_pred)
sns.regplot(x='sepal_length',y='petal_width',data=df)
plt.show()
sns.scatterplot(x='sepal_length',y='petal_width',data=df)
plt.show()