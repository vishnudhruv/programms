a=int(input("Enter the coefficient of x^2 term : "))
b=int(input("Enter the coefficient of x term : "))
c=int(input("Enter the constant term : "))
x=b**2-(4*a*c)
if x>=0:
	print("Roots are real")
else:
	print("Roots are Imaginary")


