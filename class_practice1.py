#calculator
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
print("------------CALCULATOR-------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
ch=input("Enter your choice:")
if ch=="1":
    add(a,b)
elif ch=="2":
    sub(a,b)
elif ch=="3":
    mul(a,b)
elif ch=="4":
    div(a,b)
else:
    print("Invalid Input")
# Even or Odd
z=int(input("Enter the number:"))
if z%2==0:
    print(z,"is an Even number")
else:
    print(z,"is an Odd nummber")

# Table for number
n=int(input("Enter a number"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)

# Even from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i)

#Greater among three numbers
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1>=n2 and n1>=n3:
    print(n1,"is greater")
elif n2>=n1 and n2>=n3:
    print(n2,"is greater")
else:
    print(n3,"is greater")