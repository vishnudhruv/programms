def sum(*no):
	print(type(no))
	s=0
	for x in no:
		s=s+x
	return s
def add(p):
	print(p*6)
def avg(s):
	print(s/5)
sm=sum(10,20,30,40)
add(sm)
sm=sum(25,36,45,78,52)
avg(sm)


