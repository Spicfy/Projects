def m(i):
    '''(int) --> float
    preconditions: i is a non negative integer
    returns a float value that computes the series i/(2i + 1)
    '''
    if i == 0:
        return 0
    else:
        return i/(2*i + 1) + m(i-1)
#print(m(10))
def count_digits(n):
    '''(int) --> int
    preconditions: n is a non negative integer
    returns the number of digits in int n
    '''
    if len(str(n)) == 1:
        return 1
    else:
        return 1 + count_digits(n//10)
#print(count_digits(13079797))
def is_palindrome(word):
    '''(str) --> bool
    returns true if word is palindrome and false otherwise
    '''
    lowerword = word.lower()
    if len(word) == 2 and lowerword[0] == lowerword[-1]:
        return True
    elif lowerword[0] != lowerword[-1]:
        return False
    if len(word) == 1:
        return True
    else:
        return is_palindrome(word[1: -1])
#print(is_palindrome('bazblab'))
def makealpha(word):
    '''(str) --> str
    returns modified version of word removing whitespaces, and punctuation
    '''
    newword = ''
    for i in word:
        if i.isalpha():
            newword += i
    return newword

def is_palindrome_v2(word):
    '''(str)--str
    returns true if word is palindrome and false otherwise, ignores punctuation and whitespaces
    '''
    if not word.isalpha():
        word = makealpha(word)
    lowerword = word.lower()
    if len(word) == 2 and lowerword[0] == lowerword[-1]:
        return True
    elif lowerword[0] != lowerword[-1]:
        return False
    if len(word) == 1:
        return True
    else:
        return is_palindrome(word[1: -1])
#print(is_palindrome_v2("Mqwfdqewrwwvfjewfkjcnqwejbdewi"))

    
def GCD(a, b):
    '''(int, int) --> int
    preconditions: a >= b
    returns the greatest common divisor between a and b
    '''
    if b == 0:
        return a    
    else:
        return GCD(b, a%b)
#print(GCD(36, 36))    
#Maximum depth of recursion for GCD(36, 20) is 4 recursions   
# GCD(36, 20) is 4 