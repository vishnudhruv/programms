a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if a>b:
	if a>c:
		big=a
	else:
		big=c
else:
	if b>c:
		big=b
	else:
		big=c
print("Biggest is : ",big)