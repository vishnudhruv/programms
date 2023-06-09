def reverse(n):
	rev=0
	while n!=0:
		d=n%10
		rev=(rev*10)+d
		n=n//10
	return rev
no=int(input("Enter a number : "))
r=reverse(no)
if no==r:
	print("Palindrome")
else:
	print("Not a palindrome")