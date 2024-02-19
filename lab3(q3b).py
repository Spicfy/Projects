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
