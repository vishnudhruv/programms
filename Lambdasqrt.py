import math
def myfunc(n):
  return lambda a : math.pow(a,n)

squareroot = myfunc(1/2) #lambda a : math.pow(a,1/2)

cubicroot = myfunc(1/3)  #lambda a : math.pow(a,1/3)

print(squareroot(25)) 
print(cubicroot(27))