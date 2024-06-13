import numpy as np
from matplotlib import pyplot as plt
#1
x=np.array([1,2,3,4,5])
y=2*x
plt.plot(x,y,color="green",linewidth="2",linestyle="-")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("line chart")
plt.show()
#2
x=np.arange(11,20)
y1=2*x
y2=3*x
plt.plot(x,y1,color="red",linewidth="2",linestyle=":")
plt.plot(x,y2,color="blue",linewidth="2",linestyle="-")
plt.grid(True)
plt.show()
#3
plt.subplot(1,2,1)
plt.plot(x,y1,color="red",linewidth="2",linestyle=":")
plt.subplot(1,2,2)
plt.plot(x,y2,color="blue",linewidth="2",linestyle="-")
plt.show()
#4
student={"Parnav":60,"Manvi":80,"Marnal":50}
name=list(student.keys())
marks=list(student.values())
print(name)
print(marks)
plt.bar(name,marks)  #for horizontal plt.barh(name,marks)
plt.title("Bar Chart")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
#5
a=np.random.randint(20,31,10)
b=np.random.randint(1,11,10)
plt.scatter(a,b)
plt.show()
#6
p=np.random.randint(40,51,10)
q1=np.random.randint(10,31,10)
q2=np.random.randint(20,31,10)
plt.scatter(p,q1,color="black")
plt.scatter(p,q2,color="yellow",s=100)
plt.show()
#7
x=[1,2,2,3,3,3,2,6,6,6,6,6,7,8,8,9,9]
plt.hist(x)
print("\n\n")
plt.hist(x,color="blue",bins=4)
plt.show()
#8
one=[10,20,30,40,50]
two=[51,55,57,59,70,80]
three=[40,32,20,45,75,95]
data=list([one,two,three])
plt.boxplot(data)
plt.show()
#9
plt.violinplot(data)
plt.show()
#10
fruits=["Mango","Lichi","Watermelon","Pineapple"]
percentage=[70,50,90,60]
plt.pie(percentage,labels=fruits,autopct='0.1f%%')
plt.show()