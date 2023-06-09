a=int(input("Enter the first side : "))
b=int(input("Enter the second side : "))
c=int(input("Enter the third side : "))
p=a+b+c
s=p/2
ar=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area is ",ar)
print("Perimeter is ",p)
