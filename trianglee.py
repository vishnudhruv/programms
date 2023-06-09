def triangle(rows):
    for i in range(rows):
        for j in range(7-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
i=7
while i<=7:
    triangle(i)
    if i==2:
        break 
    i-=1      
    
