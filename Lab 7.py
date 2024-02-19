#Lab 7 
#Q1
def indexes(str, char):
    '''(str, str)--> list of ints
    returns a list of the indexes at which char appears in str
    '''
    inlist = []
    for i in range(len(str)):
        if str[i] == char:
            inlist.append(i)

    return inlist

#print(indexes('mississippi', 'a'))
#Q2
def doubles(list):
    '''(list of ints)--> none
    prints the integers that are twice the previous integer in the list
    returns none datatype
    '''
    for i in range(1, len(list)):
        if list[i] == 2*list[i-1]:
            print(list[i])
#print(doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5]))
#question 3
def four_letter(list):
    '''(list of str)-->(list of str)
    returns a list containing all 4 letter words in list
    '''
    sublist = []
    for i in list:
        if len(i) == 4:
            sublist.append(i)
    return sublist
#print(four_letter(['dog', 'letter', 'stop','door', 'bus', 'dust']))
#Question 4
def inBoth(list1, list2):
    '''(list, list)--> bool
    returns True or False depending on whether or not if there are mutually shared intems in both lists
    '''
    for i in list1:
        for j in list2:
            if i ==j:
                return True 
    return False
#print(inBoth([3, 2, 5, 4, 7], [9, 0, 1, 21]))
#Q5
def intersect(list1, list2):
    '''(list, list)--> list
    preconditions: List does not contain duplicate values
    returns a list of the values that are in both list1 and list2
    '''
    intersect = []
    for i in list1:
        for j in list2:
            if i ==j:
                intersect.append(i)
    return intersect
#print(intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9]))
#Q6
def pair(list1, list2, n):
    '''((listof int), (list of int), int)--> none
    prints the pair of integers between list1 and list2 that sum up to n
    returns none
    '''
    for i in list1:
        for j in list2:
            if i +j == n:
                print(i, j)

#print(pair([2, 3, 4], [5, 7, 9, 12], 9))
#Q7
def pairSum(list, n):
    '''((list of ints), int)--> none
    prints the indexes of the combinations of 2 integers in list that add up to n
    returns none

    '''
    for i in range(len(list) - 1):
        count = 1
        while i + count < len(list):
            if list[i] + list[i + count] == n:
                print(i, (i+count))
            count += 1
print(pairSum([7, 8, 5, 3, 4, 6], 11))
#Q8
def lastfirst(namelist):
    '''(list of strings)-->(list of str), (list of str)
    returns a list containing first names and another for their respective last names
    '''
    firstname = []
    lastname = []
    for i in namelist:
        commapoint = i.find(',')
        last = i[:commapoint]
        first = i[commapoint + 2:]
        firstname.append(first)
        lastname.append(last)
    return firstname, lastname
#print(lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob']))
#Q9
def subsetSum(intlist, target):
    '''((list of nums), num) --> bool
    preconditions: intlist and target should contain only positive numbers
    returns True or False depending on whether there exists 3 numbers in intlist that add up to target
    '''
    for i in range(len(intlist)): #n
        for j in range(len(intlist)):
            for k in range(len(intlist)):
                if intlist[i] + intlist[j] + intlist[k] == target and i != j and i != k and j != k:
                    return True
    return False
#print(subsetSum([5, 4, 10, 20, 15, 19], 10))
#Q10
def mystery(n):
    '''(int)-->int
    preconditions: n must be positive
    returns the number of times n can be halved before reaching 1
    '''
    times = 0
    while n>1:
        n = n/2
        if n < 1:
            pass
        else:
            times += 1
    return times
#print(mystery(25))
#Q11
def inversions(str): #ord: letters from the start of the alphabet are less that the ones later in alphabet
    '''(str)--> int
    Preconditions: Characters are uppercase
    returns the number of inversions that occur in str
    '''
    invcount = 0
    for i in range(len(str)):
        for j in range(1, len(str)):
            if i + j < len(str):
                if str[i] > str[i + j]:
                    invcount += 1
    return invcount
#print(inversions('DCBA'))
#Q12
def sublist(list1, list2):#is list 1 appear in list2? in same order
    '''(list of ints, list of ints)--> bool
    returns True if the elements in list1 appear in the same order as they appear in list2
    '''
    ind = []
    for i in list1:
        f = list2.index(i)
        ind.append(f)
    copyind = ind.copy()
    ind.sort()
    if ind == copyind:
        return True
    else:
        return False
#print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))
#Q13
def mssl(inter):
    '''(list of ints)--> int
    returns the sublist of inter with the highest sum
    '''
    highest = 0
    for i in range(len(inter)):
        for j in range(len(inter)+1):
            sublist = inter[i:j]
            if sum(sublist) > highest:
                highest = sum(sublist)
    return highest
#print(mssl([-2, -3, -5]))



    





        




