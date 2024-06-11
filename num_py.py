import numpy as np

#1
ans=np.full((3,5),11)
print(ans)
print(np.arange(10,50,5))
print(np.random.randint(10,100,5))
arr=np.array([[1,2],[2,3],[3,4],[4,5]])
print(np.shape(arr))
arr.shape=(2,4)
print(np.shape(arr))
print(arr)

#2
n1=np.array([1,2,3,4])
n2=np.array([1,2,7,8])
print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))
ans=np.intersect1d(n1,n2)
print(ans)

#3
print(np.setdiff1d(n2,n1))
n=np.array([1,2,3,4,5,6,7,8,9])
print(np.mean(n))
print(np.median(n))
print(np.std(n))

#4
m=np.array([[1,2,3],[4,5,6],[7,8,9]])
n=np.array([[1,1,1],[2,2,2],[3,3,3]])
print(m,"\n")
print(m[1])
print(m[:,2])
print("\n")
print(np.transpose(m))

#5
print(m.dot(n))
print("\n")
print(n.dot(m))
print(m[1:3,0:2])

#6
np.save("numpy_array",n)
np.load("numpy_array.npy")