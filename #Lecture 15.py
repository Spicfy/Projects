#Lecture 15
import random

l = list(range(1, 1000001))#creates a list from 1 to 1 million

l =random.sample(range(1, 1000001), 1000)
print(l[:100])
def linear_search(L, v):
    '''(list, object)-->
    '''
    n = len(L)#1
    for i in range(n):#n
        if L[i] == v:#n
            return i #<=1
    return False#<= 1
#<= 2n + 2 = 2n = O(n) therefore the solution is in linear time 
print(linear_search(l, 575))
def binary_search(L, v):
    while b <= e:
        b = 0
        e = len(L)-1
        mid = (b+e)//2
        if v < L[mid]:
            e = mid - 1
        elif v > L[mid]:
            b = mid + 1
        else:
            return mid
    return False
    
