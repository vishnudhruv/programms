num=int(input("Enter the number : "))
print("Menu")
print("1.Automorphic")
print("2.Trimorphic")
choice=int(input("Enter your choice : "))
l=len(str(num))
if choice==1:
	sq=num**2
	if sq%(10**l)==num:
		print(num," is automorphic")
	else:
		print(num," is not automorphic")
elif choice==2:
	cb=num**3
	if cb%(10**l)==num:
		print(num," is trimorphic")
	else:
		print(num," is not trimorphic")
else:
	print("Invalid choice!!!")

