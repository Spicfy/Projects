#Lecture  13 
#Topics: 2d lists
#a matrix gets reperesented by multiple lists(lists within lists)
m= []
n = int(input("Give me an int: "))
for i in range(n):
    row = [1]*n
    m.append(row)

for i in range(len(m)):
    #m[i] = row
    for j in range(len(m[i])):
        print(m[i][j], end = " ")
    print()
    
