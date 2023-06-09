print("1.Add a contact ")
print("2.Delete a contact")
print("3.Edit a contact ")
print("4.Search a contact")
print("5.List all contacts")
print("6.Exit")
contactbook={}
choice=int(input("Enter your choice "))
while choice!=6:
	if choice==1:
		name=input("Enter the name : ")
		phno=int(input("Enter the phone number : "))
		contactbook[name]=phno
		print("1 contact added successfully")
	elif choice==2:
		name=input("enter the name of contact to delete :")
		contactbook.pop(name)
		print("1 contact deleted succefully")
	elif choice==3:
		name=input("enter the name of contact to edit :")
		phno=int(input("Enter the phone number : "))
		contactbook[name]=phno
		print("contact edited successfully")
	elif choice==4:
		name=input("enter the name :")
		print("Phone Number of ",name," : ",contactbook[name])
	elif choice==5:
		print("Name\t\t Phone Number")
		for x,y in contactbook.items():
			print(x,"\t\t",y)
	else:
		print("Invalid choice !!!")
	choice=int(input("Enter your choice "))


		



