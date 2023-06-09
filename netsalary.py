bs=int(input("Enter the basic salary"))
da=bs*0.15
hra=bs*0.25
pf=bs*0.03
ns=bs+da+hra-pf
print("Basic Salary : ",bs)
print("DA	 : ",da)
print("HRA : ",hra)
print("PF  : ",pf)
print("Net salary :",ns)