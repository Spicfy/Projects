#Exception handling 
try: #Used for when risky inputs can be entered 
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
 #errors can occur such as if denominator were to be 0, then a 0 division error would occur
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 dumbass")
except ValueError as e: #Except block is executed if user attempts to enter non integer values 
    print(e)
    print('Only enter numbers please')

except Exception:
    print("Something went wrong dumbass")
else:
    print(result)