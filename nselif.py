bs=int(input("Enter the basic salary : "))
if bs<10000:
	da=bs*0.25
	hra=bs*0.3
	pf=bs*0.08
elif bs>=10000 and bs<20000:
	da=bs*0.20
	hra=bs*0.25
	pf=bs*0.06
elif bs>=20000 and bs<30000:
	da=bs*0.15
	hra=bs*0.2
	pf=bs*0.04
else:
	da=bs*0.10
	hra=bs*0.15
	pf=bs*0.02
ns=bs+da+hra-pf
print("Basic Salary : ",bs)
print("DA : ",da)
print("HRA : ",hra)
print("PF : ",pf)
print("Net Salary : ",ns)

	