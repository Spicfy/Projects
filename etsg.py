import math
import random
#IT1 1200
#Assignment 2 part 1
#Student number 300359298
#year 2023
###########
#Question 1
###########
    
def elementary_school_quiz(flag, n):
    '''(int, int) --> int
        preconditions: flag == 1 or flag ==0
        n ==1 or n ==2
        returns the number of answers in total that were answered correctly 
    '''
    count = 0
    if flag == 0:
        val1 = random.randint(1, 9)
        val2 = random.randint(1, 9)
        print('What is ' + str(val1) + '-' + str(val2))
        sub = val1 - val2
        stu = int(input('Enter your answer here: '))
        if sub == stu:
            count += 1
    elif flag == 1:
        val1 = random.randint(1, 9)
        val2 = random.randint(1, 9)
        print('What is ' + str(val1) + ' to the power of ' + str(val2))
        exp = val1**val2
        stu = int(input('Enter your answer here: '))
        if exp == stu:
            count += 1
    else:
        print('Invalid choice, you are only aloud to choose 0 for subtraction and 1 for exponential')
    if n == 1:
        pass
    elif n == 2:
        if flag == 0:
            val1 = random.randint(1, 9)
            val2 = random.randint(1, 9)
            print('What is ' + str(val1) + '-' + str(val2))
            sub = val1 - val2
            stu = int(input('Enter your answer here: '))
            if sub == stu:
                count += 1
        elif flag == 1:
            val1 = random.randint(1, 9)
            val2 = random.randint(1, 9)
            print('What is ' + str(val1) + ' to the power of ' + str(val2))
            exp = val1**val2
            stu = int(input('Enter your answer here: '))
            if exp == stu:
                count += 1
    return count






    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
 
def high_school_quiz(a,b,c):
    '''(number, number, number) --> strings
        precondition: a, b, c are elements of real numbers
        function returns the roots from the quadratic equation containing coefficients a, b, c or a sentence if no roots exist

    '''
    if b**2 - 4*a*c <0:
        root1 = str((-1*b)/(2*a)) + ' + i ' + str(math.sqrt((b**2 - 4*a*c) * -1)/(2*a))
        root2 = str(-1*b/(2*a)) + ' - i ' + str((math.sqrt((b**2 - 4*a*c)* -1)/(2*a)))
        return('The quadratic equation ' + str(a) + '*x^2 + ' + str(b) + '*x + ' + str(c) + '= 0\nhas the following complex roots: ' + str(root1) + ', ' + str(root2))
    elif b**2 - 4*a*c == 0 and a != 0:
        root1 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)
        return('The quadratic equation ' + str(a) + '*x^2 + ' + str(b) + '*x + ' + str(c) + '= 0\nhas the single root of ' + str(root1))
    elif a == 0 and b == 0 and c != 0:
        return('the quadratic equation ' + str(a) + '*x^2 + ' + str(b) + '*x + ' + str(c) + '= 0 Is satisfied for no numbers x')
    elif a == 0 and b!= 0 and c != 0:
        root =  -c/b  
        return('The linear equation ' + str(b) + 'x + ' + str(c) + '= 0 has the root of ' + str(root))
    elif a == 0 and b == 0 and c == 0:
        return('the quadratic equation ' + str(a) + '*x^2 + ' + str(b) + '*x + ' + str(c) + '= 0\nis satisfied for all values x')
    else:
        root1 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)
        root2 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)
        return('The quadratic equation ' + str(a) + '*x^2 + ' + str(b) + '*x + ' + str(c) + '= 0\nhas the following real roots: ' + str(root1) + ', ' + str(root2))

# main

# your code for the welcome tmessage goes here
a = 40
b = a -2
print('*'*a +'\n*' + ' '*b + '*'+ '\n* __' + ' welcome to my quiz generator.__   *' + '\n*' + ' '*b + '*' + '\n' + '*'*a )
name= input("What is your name?: ")

status=input("Hi "+name+". what education level are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    n = 75
    x = n-2
    print('*'*n +'\n*' + ' '*x + '*'+ '\n* __' + name + ' welcome to my quiz generator for elementary school students.__  *' + '\n*' + ' '*x + '*' + '\n' + '*'*n )
    type = int(input(' What would you like 0 for subtraction, 1 for exponentials: '))
    if type == 0 or type == 1:
        question = int(input('Enter the number of questions you would like to practice,  you can do 0, 1, or 2: '))
        if question == 1 or question == 2:
            print(name + ' Here are are your ' + str(question) + ' questions')
            lol = elementary_school_quiz(type, question)
            if lol == question: 
                    print('Congratulations! ' + name + ' You will probably get an A tommorow')
            elif lol == (question/2):
                    print('you did okay ' + name + ' but I know you can do better ')
            else:
                print('I think you need some practice ' + name + ' ')
        elif question > 2 or question <0:
            print('Only 0, 1, or 2 are valid choices for number of question')
            
        else:
            print('Zero questions okay')
    else:
        print('Invalid choice only enter 0 or 1')
elif status=='2':
    n = 75
    x = n-2
    print('*'*n +'\n*' + ' '*x + '*'+ '\n* __quadratic equation a*x^2 + b*x + c = 0 solver for ' + name + '__               *' + '\n*' + ' '*x + '*' + '\n' + '*'*n )
    Ask = input(name + ' Would you like a quadratic equation solver?: ')
    lower = Ask.lower()
    if 'yes' in lower:
        a = float(input('Enter the number for coefficient a: '))
        b = float(input('Enter the number for coefficient b: '))
        c = float(input('Enter the number for coefficient c: '))
        print(high_school_quiz(a, b, c))


    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        lower = question.lower()
        # your code to handle varous form of "yes" goes here

        if 'yes' not in lower:
            flag=False
        else:
            print("Good choice!")
            a = float(input('Enter the number for coefficient a: '))
            b = float(input('Enter the number for coefficient b: '))
            c = float(input('Enter the number for coefficient c: '))
            print(high_school_quiz(a, b, c))
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
else:
    print(name + ' You are not the target audience for this software')

print("Good bye "+name+"!")
