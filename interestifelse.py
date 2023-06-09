p=int(input("Enter principle amount"))
n=int(input("Enter the duration in years"))
if n>=10:
	r=12
else:
	r=8
i=p*r*n/100
print("Interest : ",i)