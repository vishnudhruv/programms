def add(*n):
	s=0
	for x in n:
		s=s+x
	return s

p=add(10,20,30)
print("Sum is ",p)
q=add(10,20,30,40,50)
print("Sum is ",q)
r=add(25.5,36.6,42.7,52.8)
print("Sum is ",r)


