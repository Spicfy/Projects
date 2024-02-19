def count_vowels(phrase):
    '''(str) --> int
    returns the number of vowels in a given phrase

    >>> count_vowels("August")
    3
    count_vowels("

    '''
    num_vowels = 0
    for char in phrase:
        if char in 'aeiouAEIOU':
            num_vowels += 1


    return num_vowels

for i in range(10, 0, -1): #not including zero, or not including the element b in for i in ragne(a, b, c)
    print(i)
