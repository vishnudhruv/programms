def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #mydoubler=lambda a : a * 2
mytripler = myfunc(3) #mytripler=lambda a: a*3

print(mydoubler(11))
print(mytripler(11))

