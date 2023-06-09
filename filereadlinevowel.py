f=open("content1.txt","r")
a=f.readline()
vowel=['a','e','i','o','u','A','E','I','O','U']
while a:
	count=0
	for x in a:
		if x in vowel:
			count+=1
	print(f'{count} vowels in {a} ')
	a=f.readline()
f.close()