#pattern 1
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
#pattern 2
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()
#pattern 3
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
#pattern 4
n=3
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j,end="")
    print()
#pattern 5
n=3
k=0
for i in range(1,n+1):
    for j in range(1,n+1):
        k+=1
        print(k,end="")
    print()
#pattern 6
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
