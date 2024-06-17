import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
data=pd.read_excel("D:\data.xlsx")
print(data)
#line graph
sns.lineplot(x='pizza_size',y='total_price',data=data,hue='pizza_category',style='pizza_category',markers=True)
plt.show()
#bar graph
sns.barplot(x='pizza_category',y='total_price',data=data,palette='rocket')
plt.show()
#scatter graph
sns.scatterplot(x='quantity',y='pizza_name',data=data,hue='pizza_size',style='pizza_size')
plt.show()
#histograph
sns.distplot(data['order_date'],color='green') #sns.distplot(data['pizza_size'],hist=False,color='green')
plt.show()
#jointplot graph
sns.jointplot(x='pizza_category',y='pizza_size',data=data)
plt.show()
#boxplot graph
sns.boxplot(x='order_date',y='pizza_category',data=data)
plt.show()