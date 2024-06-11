import math
print(math.pow(2,3))
print(math.log(10))
print(math.ceil(6.87))
print(math.floor(6.87))
print(math.fabs(-34.78))
print(math.sin(45))
print(math.tan(90))

from random import *
print(random())
print(randrange(5,10))
print(randint(10,20))
s="Iamstring"
print(choice(s))
l=[1,2,3,4,5,6,7,"name"]
print(choice(l))
t=(90,78,56)
print(choice(t))
shuffle(l)
print(l)

import statistics as S
l=[1,2,3,4,5,6]
print(S.mean(l))
print(S.median(l))
print(S.mode(l))
