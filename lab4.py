#Question 1
def is_eligible(age, citizenship, prison):
    '''(int, str, str) -- > booleon value
    precondition: age == int, citizenship and prison are string values
    returns a booleon variable determining whether you are allowed to vote or not
    '''
    ageverify = age >= 18
    citizencheck = (citizenship.strip()).lower()
    prisoncheck = (prison.strip()).lower()
    return ageverify == True and (citizencheck == 'canadian' or citizencheck == 'canada') and prisoncheck == 'no'
        

age = int(input('How old are you?: '))
citizenship = input('What citizenship are you?: ')
prison = input('Are you currently a convicted criminal? ')
x = is_eligible(age, citizenship, prison)

if x == True:
    print('You are eligible to vote in canada')  
else:
    print('You are not eligible to vote in canada')
#Question 2
def mess(string):
    '''(string) --> string
    precondition: none
    returns a new string which has the last 8 consonant characters and whitespaces altered
    '''
    newstr = ''
    for i in string:
        if i in 'rstvwxyz':
            newstr += i.upper()
        elif i == ' ':
            newstr += '-'
        else:
            newstr += i
    return newstr
def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0
#Question 3
def is_divisible23n8(n):
     '''(int)->bool
     returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not(is_divisible(n,8))):
          return True
     else:
          return False
def print_all_23n8(num):
     '''(int) --> none
     parameter: num must be an non negative integer
     returns none
     '''
     for i in range(num):
          x = is_divisible23n8(i)
          if x == True:
               print(i)
call = int(input('Enter a non-negative number: '))
#print(print_all_23n8(call))
#Question 4
def halfpyr(num, char):
    '''(int, str) -->none
        parameters: num must be non negative
    '''
    for i in range(num):
        print(char * (i + 1))
int = int(input('Enter a non negative integer: '))
g = input('Enter a character: ')
#print(halfpyr(int, g))
#Question 5
num = int(input('Enter a positive integer: '))
for i in range(1, num + 1):
    if num%i == 0:
        print(i)
def prime(n):
    '''(int) --> booleon value
    parameter: n must be a positive integer
    returns a booleon value (True or False) based off whether n is a prime number or not
    '''
    primecount = 0
    for i in range(1, n + 1):
        if n%i == 0:
            primecount +=1
        else:
            pass
    if primecount == 2:
        return True 
    else:
        return False
print(prime(num))