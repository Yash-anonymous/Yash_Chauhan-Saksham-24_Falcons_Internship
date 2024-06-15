import seaborn as sns
from matplotlib import pyplot as plt
print(sns.get_dataset_names())
data=sns.load_dataset("tips")
print(data)
#line graph
sns.lineplot(x='day',y='total_bill',data=data,hue='time',style='time',markers=True)
plt.show()
#bar graph
sns.barplot(x='day',y='size',data=data,palette='rocket')
plt.show()
#scatter graph
sns.scatterplot(x='total_bill',y='tip',data=data,hue='size',style='size')
plt.show()
#histograph
sns.distplot(data['total_bill'],color='green') #sns.distplot(data['total_bill'],hist=False,color='green')
plt.show()
#jointplot graph
sns.jointplot(x='size',y='tip',data=data,kind='reg')
plt.show()
#boxplot graph
sns.boxplot(x='day',y='total_bill',data=data)
plt.show()