def triplicates(l):
    n = len(l) #1
    for i in range(n): # 1 * n 
        for j in range(n): # n^2 operation in time
            #n^2
            for k in range(n): #1 operation n^2 * n = 1n^3
                if l[i]== l[j] and l[j] == l[k] and i != j and j!= k and i != k: #5 operations because there are 5 conditions
                    return True # <=1
    return False #<=1 can either happen or not happen
#1 + n + n^2 + 6n^3 + 1 = 2 + n + n^2 + 6*n^3
# O(n^3) keep fastest growing term and approximates how many operations is being done in this code 
# <= 2*n^3 + n^3 + n^3 + 6*n^3  = 10*n^3 = O(n^3)
def triplicates_via_count(l): #O(n^2) quadratic time
    for item in l: #1 * n (size of list)
        if l.count(item)>=3: # n * n = n^2 (goes through every element in the list) every method that goes through the list such as sum, max, count all check every item in the list so it is linear time
            return True # <=1
    return False #<= 1
#n + n^2 + 1 = O(n^2)
#O(n^3) is worst
#O(n^2) is better

def triplicates_via_sort(l): 
    l.sort() #O(n*log n) #best solutions are n*logn
    n = len(l)#1
    for i in range(n-2):#1* n-2
        if l[i] == l[i +2]:#1*n-2
            return True #<= 1
    return False #<= 1  
#1+ 2 *(n-2) + 1 == 2 + 2n -4 = 2n - 2       
# n + n*log n         
#n + n^2 + 1 = O(n^2)
#O(n^3) is worst
#O(n^2) is better
#O(n*log n) is best
def aha(l, x):
    l[0] = 999
    x = 888
num = 100
t = [1, 1, 1]
aha(t, num)

print(num)
print(t)