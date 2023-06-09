def  digitsum(n):
	if n==0:
		return 0
	d=n%10
	s=d+digitsum(n//10)
	return s
no=int(input("Enter the number : "))
sum=digitsum(no)
print("sum of digits : ",sum)
	