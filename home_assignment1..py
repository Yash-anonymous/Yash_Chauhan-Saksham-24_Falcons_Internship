# You are given a single number. You need to print one of the following outputs according to the number's nature.
# Print 1,if the number is positive
# Print -1,if the number is negative
# Print 0, if the number is equal to zero
num=int(input("Enter the number:"))
if num>0:
    print(1)
elif num<0:
    print(-1)
else:
    print(0)

# You are given two numbers. You need to calculate and print their greatest common divisor(GCD)
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
for i in range(1,100000):
    if a%i==0 and b%i==0:
        ans=i
print(ans,"is the greatest common divisor of",a,"and",b)

    
# Write a program for fibonacci series
num=int(input("Enter the limit of fibonacci series:"))
n1=0
n2=1
i=0
while i<num:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    i+=1

# Write a program to find the prime number
num=int(input("Enter the number:"))
flag=False
if num==1:
    print(num,"is not a prime number.")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
    if flag:
        print(num,"is a not prime number.")
    else:
        print(num,"is a prime number.")

# Write a program to find if the triangle is valid or not
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a+b>c and a+c>b and b+c>a:
    print("It's a valid Triangle")
else:
    print("It's not a valid Triangle")

# Write a program to find the factorial of a number.
num=int(input("Enter the number:"))
f=1
for i in range(1,num+1):
    f=f*i
print("The factorial of",num,"is",f)

# Write a program to find the sum of all even number.
sum1=0
r=int(input("Enter the range:"))
for i in range(0,r+1):
    if i%2==0:
        sum1=sum1+i
print("The sum of all even numbers is :",sum1)

# Write a program to convert faranite to celcius.
far=float(input("Enter the temperature in faranite:"))
cel=(f-32)*5/9
print("Temperature in celcius is:",cel)
