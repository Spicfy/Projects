def is_up_monotone(X, d):
    '''(str, int) --> bool
        preconditions: X should be a string containing positive integers, d should also be a positive integer, d should be able to split X into even parts of itself 
        returns True or false depending whther or not X can be up monotone when it's characters are split into groups of d
    '''
    if len(str(X))%int(d) == 0:
        strX = str(X)
        t = strX[0:int(d)]
        a = int(t)

        flag = True
        for i in range ((len(strX))//int(d)):
            if i != (int(len(strX)/int(d))-1):
                print(t, end = ', ')
                b = strX[(i + 1)*int(d): (i + 2)*int(d)]
                c = int(b)
                if a < c:
                    pass
                else:
                    flag = False
                t = str(c)
                a = c
            else:
                print(t)
        return (flag)
