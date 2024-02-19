#given a string s, need to return a new string where
#1. if a character x is non-digit skip it
#2. if x is prime replace it by "pr"
#3 if x is not a prime, add that digit x x times
def messify(s):
    '''s(str) --> str
    >>>messify('12')
    '1pr'
    >>> messify('x-y')
    ''
    >>> messify('01234a')
    '1prpr4444'
    '''
    #\' tells python this is not the end of the string
