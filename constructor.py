class student:
	def __init__(self):
		self.name="Kiran"
		self.age=25
		self.height=181.25
	def __init__(self,n,a,h):
		self.name=n
		self.age=a
		self.height=h
	def display(self):
		print("Name : ",self.name)
		print("Age : ",self.age)
		print("Height : ",self.height)
S=student()
P=student("Manu",29,174.56)
S.display()
P.display()
		