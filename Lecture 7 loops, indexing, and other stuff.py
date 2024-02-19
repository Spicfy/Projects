print(ord('B'))
ord("a")
print('\u2660')
s = "It is a nice day."
s[1]
#therefore B is less than a a ord is 97 while ord B is 66
#for indexing the first element(access the first character) do  s[0] which prints I
#if we do the len(s) we will get 17 (whitespaces count as a character)
#To get the 17'th character of s we index the 16th position [16]

print(s[len(s) - 1]) #will print . always remember the -1 when changing from the length to the index 
print(s[-1]) #Will print from the very end of the string 
print(- len(s))
s = "123456789"
print(s[2:7]) #from the second element(3rd value in string) and goes up to the 7th position
print(s[:7]) #all elements up to the 7th position are stored and printed
print(s[7:]) #prints everything from the 7th position but not including the 7th position to the end
print(s[:])#prints everthing in the string


#strings are immutable
