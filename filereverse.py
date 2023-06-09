f=open("content.txt","r")
p=open("reversewords.txt","w")
a=f.readline()
while a:
	x=a[::-1]
	print(x)
	p.write(x)
	a=f.readline()
f.close()
p.close()