"""if the deposit>=200000 or years>=5	
		rate of interest =12%
otherwise
	rate of interest =9%
i=p*r*t/100"""

p=int(input("Enter the principal amount :"))
n=int(input("Enter the period :"))
if p>=200000 or n>=5:
	r=0.12
else:
	r=0.09
i=p*r*t/100
print("Interest is ",i," for ",t," years at a rate of ",r )








