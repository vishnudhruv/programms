def interest(x,y,z):
	i=x*y*z/100
	return i
p=int(input("Enter the principle amount : "))
r=int(input("Enter the rate of interest : "))
t=int(input("Enter the period : "))
i=interest(p,r,t)
print("Simple Interest is : ",i)