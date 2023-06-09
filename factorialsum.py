def sum(n):
	if n==1:
		return 1
	s=n+sum(n-1)
	return s
no=int(input("Enter the number : "))
total=sum(no)
print("Sum  is : ",total)
