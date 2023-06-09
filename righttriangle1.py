a=int(input("Enter the measurement of first side :"))
b=int(input("Enter the measurement of second side :"))
c=int(input("Enter the measurement of third side :"))
if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
	print("Right triangle")
else:
	print("Not a right traingle")


