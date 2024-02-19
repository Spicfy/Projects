#programming excercise #2
def sumof2(x, y):
     '''(int, int) --> int
         returns the sum of the 2 integers
     '''
     return (x + y)
int1 = int(input('Enter the first integer: '))
int2 = int(input('Enter the second integer: '))
print(sumof2(int1, int2))
while True:
     zz = input('Do you wish to perform the operation again?(Enter yes to repeat operation): ')
     zzsimple = (zz.strip()).lower()
     if zzsimple == 'yes':
          int1 = int(input('Enter the first integer: '))
          int2 = int(input('Enter the second integer: '))
          print(sumof2(int1, int2))
     else:
          break
