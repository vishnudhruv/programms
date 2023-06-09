bus={
	"Routeno":5,
	"Driver":"kiran",
	"Cleaner":"Manu",
	"points":["karamana","PMG","pattom"]
}

print(bus["Driver"])=>"Kiran"
print(bus.get("Driver")) =>"Kiran"
bus.keys()=>["Routeno","Driver","Cleaner","points"]
bus.values()=>[5,"Kiran","Manu",["karamana","PMG","Pattom"]]
bus.items()=>[{"Routeno":5},]
bus["color"]="Red"
bus.update("Fare")=1500
bus["Driver"]="Mohan"
bus.pop("fare")
bus.popitem()
del bus["Fare"]
del bus
bus.clear()

for x in bus:
	print(x)	=>Routeno Driver Cleaner points 
for x in bus:
	print(bus[x])	=>5 kiran Manu ["karamana","PMG","Pattom"]