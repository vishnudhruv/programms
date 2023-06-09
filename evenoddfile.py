n=int(input("Enter the count : "))
f=open("master.txt","w")
print("Enter the numbers : ")
for i in range(0,n):
	no=input()
	f.write(no+"\n")
f.close()
f=open("master.txt","r")
p=open("evenfile.txt","w")
q=open("oddfile.txt","w")
for i in range(0,n):
	x=int(f.readline())
	if x%2==0:
		p.write(str(x)+"\n")
	else:
		q.write(str(x)+"\n")
f.close()
p.close()
q.close()