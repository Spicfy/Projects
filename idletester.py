#IT1 1120
#Assignment 3 part 2
#Bruce Wang
#October 2023
import math
###############
#Question 1
###############
def sum_odd_divisors(n):
    '''(integer) --> integer
    parameters: n must be a positive integer
    returns the sum of all the divisors of n
    example: sum_odd_divisor(9)
    13 
    '''
    n = abs(n)
    sum = 0
    if n == 0:
        return None
    else:
        for i in range(1, n + 1):
             if n%i == 0 and i%2 == 1:
                sum += i
    return sum
#print(sum_odd_divisors(-9))
###############
#Question 2
###############
def series_sum():
    '''(none) --> number
    parameters: none
    returns the sum of the series (1000 + 1/1^2 + ... 1/n^2)
    '''
    integer = int(input('Enter a non negative integer n: '))
    x = 1000
    if integer < 0:
        return 
    elif integer == 0:
        return 1000
    else:
        for i in range(integer, 0, -1):
            x += (1/i**2)
        return x
#print(series_sum())

#####################
#Question 3
#####################
def pell(n):
    '''(int)--> int
    parameters: n should be a positive inegers
    retunrs the nth pell number of the pell sequence
    '''
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n0 = 0
        n1 = 1
        for i in range(n - 1):
            Pn = (2 * n1) + n0
            n0 = n1
            n1 = Pn
    return Pn
#print(pell(0)) 
#print(pell(2))
#print(pell(6))
#print(pell(1743))
################
#Question 4
################
def countMembers(s):
    '''(string)--> int
    parameters: none
    returns the number of times a extraordinary character appears in the 
    '''
    counter = 0
    for i in s:
        if i in "efghijFGHIJKLMNOPQRSTUVWX23456!,":
            counter +=1
    return counter
#print(countMembers("2aAb3?eE'_13"))
#print(countMembers("one, Two"))
######################
#Question 5
######################
def casual_number(s):
    '''(string)--> int
    parameters: s should contain numerical digits with commas(,) being allowed 
    returns the user a integer value of the string they have entered 
    '''
    num = ''
    for i in s: 
        if i in '1234567890':
            num += i
        elif i == ',' or ((s[0] == '-' and len(s)>1) and '-' not in s[1:]):
            pass
        else:
              num += 'stop'           
    if 'stop' in num :
        return None
    elif len(s) == 0:
        return None
    elif s[0] == '-':
        return int('-' + num)
    else: return int(num)
#print(casual_number("-97,251"))
#print(casual_number('--,,,,'))
#############################
#Question 6
#############################
def alienNumbers(s):
    '''(str)--> int
    preconditions: s should contain only the characters ('T', 'y', '!', 'a', 'N' or 'U)
    returns the sum of the value of the characters called into the function
    '''
    T = s.count('T')
    y = s.count('y')
    exclamation = s.count('!')
    a = s.count('a')
    N = s.count('N')
    U = s.count('U')
    Ttotal = T * 1024
    ytotal = y * 598
    exctotal = exclamation*121
    acount = a *42
    Ncount = N*6
    sum = Ttotal + ytotal + exctotal + acount + Ncount + U
    return sum
#print(alienNumbers("aaaUUU"))
    
#print(alienNumbers(''))
####################
#Questionn 7
####################
def alienNumbersAgain(s):
    '''(str)--> int
    preconditions: s should contain only the characters ('T', 'y', '!', 'a', 'N' or 'U)
    returns the sum of the value of the characters called into the function
    '''
    T = 1024
    y = 598
    exclamation = 121
    a = 42
    N = 6
    U = 1
    Tcount = 0
    ycount = 0
    exclamationcount = 0
    acount = 0
    Ncount = 0
    Ucount = 0
    sum = 0
    for i in s:
        if i == 'T':
            Tcount +=1
        elif i == 'y':
            ycount +=1
        elif i == '!':
            exclamationcount += 1
        elif i == 'a':
            acount +=1
        elif i == 'N':
            Ncount +=1
        elif i == 'U':
            Ucount +=1
    T = T*Tcount
    y = y *ycount
    exclamation = exclamation * exclamationcount
    a = a*acount
    N = N *Ncount
    U = U*Ucount
    print(T, y, exclamation, a, N, U)
    sum = T + y + exclamation + a + N + U
    return sum
#######################
#Question 8
#######################
def encrypt(s):
    '''
    '''
    reverse = s[::-1]
    newmsg = ''
    for i in range(len(reverse)):
        if i == 0:
            newmsg += reverse[i]
        elif i == 1:
            newmsg += reverse[-i]
        elif i%2 == 0:
            newmsg += reverse[i - int(i/2)]
        elif i%2 == 1:
            newmsg += reverse[-(i - int((i-1)/2))]
    return newmsg

#print(encrypt("12345"))
################
#Question 9
################
def weaveop(s):
    new_string = ''
    newchar = s[0]
    for i in range(len(s)):
        new_string += newchar
        if s[i].isalpha():
            if len(s) >1:
                if i != (len(s) - 1):
                    if newchar == s[i].upper() and s[i + 1] == s[i + 1].upper() and s[i + 1].isalpha():
                        new_string += 'O' + 'P'
                    elif newchar != s[i].upper() and s[i + 1] == s[i + 1].upper() and s[i + 1].isalpha():  
                        new_string += 'o' + 'P'
                    elif  newchar == s[i].upper() and s[i + 1] != s[i + 1].upper() and s[i + 1].isalpha():
                        new_string += 'O' + 'p'
                    elif newchar != s[i].upper() and s[i + 1] != s[i + 1].upper() and s[i +1].isalpha():
                        new_string += 'o' + 'p'
                    newchar = s[i + 1]
                else:
                    pass
            else:
                new_string += s[i]
        else:
            if i != len(s) - 1:
                newchar = s[i + 1]
            else:
                pass


    return new_string
#print(weaveop("abcdef22x"))
###############
#Queston 10
###############

def squarefree(s):
    '''(str)--> bool
    
    '''
    flag = True
    for i in range(len(s)):
        count = 0
        for x in range(len(s)):
            if i >= count:
                pass
            else:
                char = s[i:count]
                if char == s[count: ((count) + len(char))]:
                    flag = False
            count += 1

            

    return flag
