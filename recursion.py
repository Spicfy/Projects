def countdown(n):
    while n >=0:
        if n <= 0:
            print('Blast off')
        else:
            print(n)
        countdown(n-1)
        
