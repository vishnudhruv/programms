a=int(input("Enter the coefficient of x^2 term : "))
b=int(input("Enter the coefficient of x term : "))
c=int(input("Enter the constant term : "))
x=b**2-(4*a*c)
if x>0:
	x1=(-b+x**0.5)/(2*a)
	x2=(-b-x**0.5)/(2*a)
	print("Roots are ",x1,x2)
elif x==0:
	x1=-b/(2*a)
	print("Root is ",x1)
else:
	print("Imaginary roots")


