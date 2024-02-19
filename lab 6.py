#Programming excercise 1
def sum_odd_while_v2(n):
     '''(int) --> int
     returns the sum of all odd integer between 5 and n inclusively
     '''
     sum = 0
     looper = 5
     while looper <= n:
          sum += looper
          looper += 2
     
     return sum
     
          
#print(sum_odd_while_v2(10))
#Excerice 2 completed on seperate python file
#excercise 3
def first_neg(list):
     '''(list[nums]) --> int
         returns the index of the first negative number in list. If no negative numbers appear return none
     '''
     i = 0
     while i < len(list):
          if list[i] <0:
               return i
          else:
               i += 1
#print(first_neg([2, 3, 1, 4, 2]))    
#Question 4
def sum_5_consecutive(list):
     x = False
     if len(list)>=5:
          for i in range((len(list)//5) + (len(list) -5)):
               sum = list[i]
               for j in range(1, 5):
                    sum += list[i + j] 
               if sum == 0:
                    x = True
                    return x
          
     return x

#print(sum_5_consecutive ([-10, 1, 1, 4, 2, 10, 13]))
#excercise 5 on seperate file

#excercise 6

def fib(n):
     '''(int) --> (list[int])
        preconditions: n must be a positive integer
        returns a list of the first n numbers in the fibbonacci sequence
     '''
     fibb = [] 
     for i in range(n):
          if i == 0:
               fibb.append(1) 
          elif i == 1:
               fibb.append(1) 
          else:
               fibb.append(fibb[i-1] + fibb[i - 2])
     return fibb
        
        

#print(fib(7))

#Excercise 7
def inner_product(list1, list2):
    '''(list[int], list[int])-->int
       preconditions: len(list1) == len(list2)
       returns the inner product of list1 and list2
    '''
    sum = 0
    for i in range(len(list1)):
        sum += (list1[i])*(list2[i])
    return sum


               
 

