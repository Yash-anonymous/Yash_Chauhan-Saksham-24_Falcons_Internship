import numpy as np
from matplotlib import pyplot as plt
#1
x=np.array([1,2,3,4,5])
y=2*x
plt.plot(x,y,color="yellow",linewidth="2",linestyle=":")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("line chart")
plt.show()
#2
x=np.arange(11,20)
