type=input("Enter the type of connection : ")
u=int(input("Enter the units consumed : "))
charge=0
if type=="domestic":
	if u<=100:
		charge=u*1
	elif u<150:
		charge=(100*1)+(u-100)*1.5
	elif u<=200:
		charge=(100*1)+(50*1.5)+(u-150)*2
	else:
		charge=(100*1)+(50*1.5)+(50*2)+(u-200)*3
elif type=="commercial":
	if u<=100:
		charge=u*3
	elif u<150:
		charge=(100*3)+(u-100)*4
	elif u<=200:
		charge=(100*3)+(50*4)+(u-150)*6
	else:
		charge=(100*3)+(50*4)+(50*6)+(u-200)*10
else:
	print("Invalid connection type ")
print("Tarriff	: ",charge)




