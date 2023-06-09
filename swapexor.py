a=int(input("Enter first  number"))
b=int(input("Enter second number"))
print("Value of a before swapping: ",a)
print("value of b before swapping: ",b)
a=a^b
b=a^b
a=a^b
print("Value of a after swapping: ",a)
print("value of b after swapping: ",b)