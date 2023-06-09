class student:
	def __init__(self,nm,ag,ht):
		self.name=nm
		self.age=ag
		self.height=ht
	def display(self):
		print("Name : ",self.name)
		print("Age : ",self.age)
		print("Height : ",self.height)
S=student("Midhun",29,185.4)
S.display()
n=input("Enter a name : ")
a=int(input("Enter the age : "))
h=float(input("Enter the height : "))
P=student(n,a,h)
P.display()
		