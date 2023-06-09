a=int(input("Enter the coefficient of x^2 term : "))
b=int(input("Enter the coefficient of x term : "))
c=int(input("Enter the constant term : "))
x=b**2-(4*a*c)
roots="Imaginary"
if x>=0:
	roots="Real"
print("Roots are ",roots)
