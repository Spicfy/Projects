#Excercise 5
import random
n = int(input('Enter a positive even integer: '))
#1
zerolist = [0]
zerolist = zerolist*n
print(zerolist*n)
for i in range(n - 1):
    zerolist += [0]
print(zerolist)
#2
b = []
for i in range(n):
    randob = random.randint(1, 100)
    b.append(randob)
print(b)
b = []
count = 0
while count < n:
    b += [random.randint(1,100)]
    count += 1
print(b)
#3
c = b.copy()
print("start",c)
print(b)
c = c * 2
print(c)
print(b)
#4
c[0: (len(b)-1 //2)] = [0]*(int(n/2))
c[len(b)//2: len(b)] = b[(len(b)//2): len(b)]
print(c)
#5
d = []
for i in b:
    d.append(i)
print(d)
d = b.copy()
print(d)
#6
e = []
for i in range(1, len(b), 2):
    e.append(b[i])
print(e)