def my_function(*formal):
	print(type(formal))
	s=0
	for x in formal:
		s=s+x
	print("Sum is ",s)
my_function(10,20)
my_function(10,20,30,40,50)
my_function(10.2,15.5,26.3)
