student={"name":"Kiran",
		"age":25,
		"mark1":76,
		"mark2":85}
student["name"] =>Kiran
student.get("name") =>kiran
student.keys() =>[name,age,mark1,mark2]
student.values() =>["Kiran",25,76,85]
student.items()=[(name:"Kiran"),(age:25),(mark1:76),(mark2:85)]

student["name"]="Manu"
student["phone"]=958744123
student.update({"name":"Mohan"})
student.update({"Address":"Kottayam"})

student.pop("name")
student.popitems()
del student["name"]
del student
student.clear()
candidate=student.copy()
candidate=dict(student)
print(student) =>{name:kiran,age:25....}
