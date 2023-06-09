class employee:
	def __init__(self,name,ecode):
		self.emp_name=name
		self.emp_code=ecode
	def print_details(self):
		print("Employee Name : ",self.emp_name)
		print("Employee Code : ",self.emp_code)
class manager(employee):
	def __init__(self,nme,code,bs):
		employee.__init__(self,nme,code)
		self.basic_salary=bs
	def calculate(self):
		self.net_salary=self.basic_salary+self.basic_salary*0.2
		print("Basic Salary : ",self.basic_salary)
		print("Net salary : ",self.net_salary)
m=manager("Manu",101,25000)
m.print_details()
m.calculate()
n=manager("Kiran",102,35000)
n.print_details()
n.calculate()
