def reverse(n):
	rev=0
	while n!=0:
		d=n%10
		rev=(rev*10)+d
		n=n//10
	return rev
n=int(input("Enter a number : "))
#r=reverse(n)
print("Reverse of ",n," is ",reverse(n))
