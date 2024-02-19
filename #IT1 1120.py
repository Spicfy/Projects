#IT1 1120
#lab 3
#Bruce Wang
#September 2023
#Question 1
def pay(wage, worked):
    '''
    (number, number) -- > number
    preconition( wage and worked must be greater than or equal to 0)
    returns the number of money earned
    '''
    hrs = 40 * wage
    overhours = 20 * (1.5*wage)
    if worked <= 40:
        return (worked * wage)
    elif 40<worked<=60:
      x = (hrs + (worked - 40) * (1.5 * wage))
      return  x
    elif worked > 60:
        x = (hrs + overhours + (worked - 60) *(2 * wage))
        return x
#print(pay(10, 35))
#print(pay(10, 45))
#print(pay(10, 61))
#Question 2
def rps(p1, p2):
    '''(str, str) -- > integer
    precondition (p1 and p2 must be 'R', 'P' or 'S')
    returns a number that determines which player has won
    '''
    x = (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R') or (p1 == 'R' and p2 == 'S')
    if x == True:
        return -1
    elif x == False and p1 != p2:
        return 1
    elif p1 == p2:
        return 0
#print(rps('R', 'P'))
#print(rps('R', 'S'))
#print(rps('S', 'S')) 

def is_divisible(n, m):
    '''(integer, integer) --> booleon value
        precondition(x and y must be integers)
        returns a booleon value based whether or not n is divisible by m
    '''
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
    '''(integer) --> string
        precondition: x is an integer 
        returns a sentence that tells user whether the integer they have inputted is divisible by 2 or 3 but not 8
    '''
    two = is_divisible(x, 2)
    three = is_divisible(x, 3)
    eight = is_divisible(x, 8)
    if (two == True or three == True) and eight == False:
        return(str(x) + ' is divisible by 2 or 3 but not 8')
    else:
        return('It is not true that ' + str(x) + ' is divisible by 2 or 3 but not 8')
var = int(input('Enter an integer: '))
print(is_divisible23n8(var))