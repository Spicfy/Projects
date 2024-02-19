def is_divisible(n, m):
    if n % m == 0:
        return True
    else:
        return False
x = int(input('Enter the 1st integer: '))
y = int(input('Enter the 2nd integer: '))
verify = is_divisible(x, y)
if verify == True:
    print(str(x) + ' is divisible by ' + str(y))
else:
    print(str(x) + ' is not divisible by ' + str(y))
def is_divisible23n8(x):
    two = is_divisible(x, 2)
    three = is_divisible(x, 3)
    eight = is_divisible(x, 8)
    if (two == True or three == True) and eight == False:
        return(str(x) + ' is divisible by 2 or 3 but not 8')
    else:
        return('It is not true that ' + str(x) + ' is divisible by 2 or 3 but not 8')
var = int(input('Enter an integer: '))
print(is_divisible23n8(var))
