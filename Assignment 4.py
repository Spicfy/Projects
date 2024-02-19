#ITI1120 
#Assignment 4 part 1
#Bruce Wang
#October 2023
def number_divisible(list, n):
    '''(list[int], int)--> int
    returns the number of integers in list that are divisible by n
    '''
    Goofy = 0
    for i in list:
        if i%n == 0:
            Goofy += 1
    return Goofy
#trasher = (input('Please input a list of numbers seperated by space: '))
#trasher_list = (trasher.strip()).split()

#trasher_list = [int(x) for x in trasher_list]
#print(number_divisible(trasher_list, 3))

#############################
#Question 2
#############################
def two_length_run(list):
    for i in range(len(list)- 1):
        if list[i] == list[i +1]:
            return True
        
    return False
