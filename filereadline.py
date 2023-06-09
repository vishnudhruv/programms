f=open("content1.txt","r")
a=f.readline()
while a:
	print(a,end="")
	a=f.readline()
f.close()