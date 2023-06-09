bs=int(input("Enter the basic salary : "))
da=bs*0.2
hra=bs*0.25
pf=bs*0.06
if bs>=10000:
	da=bs*0.1
	hra=bs*0.15
	pf=bs*0.04
ns=bs+da+hra-pf
print("Basic Salary : ",bs)
print("DA : ",da)
print("HRA : ",hra)
print("PF : ",pf)
print("Net Salary : ",ns)

	