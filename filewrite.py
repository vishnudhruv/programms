f = open("content.txt", "w")
n=int(input("Enter the count"))
for x in range(n):
	name=input("Enter a text : ")
	name=name+"\n"
	f.write(name)
f.close()