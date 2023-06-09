m1=int(input("Enter the marks for physics"))
m2=int(input("Enter the marks for chemistry"))
m3=int(input("Enter the marks for maths"))
if m1>=50 and m2>=50 and m3>=50:
	p=(m1+m2+m3)*100/300
	if p>=90:
		grade="A+"
	elif p<90 and p>=80:
		grade="A"
	elif p<80 and p>=70:
		grade="B+"
	elif p<70 and p>=60:
		grade="B"
	else:
		grade="C"
else:
	grade="Failed"
print("His grade is ",grade)

