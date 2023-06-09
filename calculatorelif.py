print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division ")
print("5. Exponet")
choice=int(input("Enter your choice of operation :"))
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if choice==1:
	res=a+b
elif choice==2:
	res=a-b
elif choice==3:
	res=a*b
elif choice==4:
	res=a/b
elif choice==5:
	res=a**b
else:
	print("Invalid choice!!!")
print("The result is ",res)
