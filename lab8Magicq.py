def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # YOUR CODE GOES HERE
     else:
          diagsum1 = 0
          rowsum = []
          columnsum = []
          for i in range(len(m)):
               for j in range(len(m)):
                    if i == j:
                         diagsum1 += m[i][j]
          for i in range(len(m)):
               rowsum.append(sum(m[i]))
          rowsum.sort()
          if rowsum[0] != rowsum[-1]:
               print('rows they not the same')
               return False
          for rows in range(len(m)):
               sumcolumn = 0
               for j in range(len(m)):
                    sumcolumn += m[rows][j]
               columnsum.append(sumcolumn)
          columnsum.sort()
          if columnsum[0] != columnsum[-1]:
               print(columnsum)
               print('columns they not the same')
               return False
          diag2 = 0
          for i in range(len(m)):
               diag2 += m[i][(len(m)- 1) - i]
          rowget = rowsum[0]
          columnget = columnsum[0]
          if diagsum1 == rowget == columnget == diag2:
               return True
          else:
               return False
     
          
                    
          
               
               
     # TEST CONDITION 1

     # TEST CONDITION 2




# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3 
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
