import math
def repeater(s1, s2, n):
    return ('_' + (s1 + s2)*n + '_')
print(repeater("AAA", "x", 3))
print(repeater("+", "--", 30))

def roots(a, b, c):
    print("the quadratic equation with coefficients a =", a, "b =", b, "c =", c, "\nhas the following solutions (i.e. roots): ")
    root1 = (-1 * b + math.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return (str(root1)+" and "+str(root2))
print(roots(-1, 4, 1.5))
print(roots(1, 2, 1))
def real_roots(a, b, c):
    return b**2-4*a*c >= 0
print(real_roots(-1, 4, 1.5))
print(real_roots(1, 2, 1.))
print(real_roots(1, 1, 1))
def reverse(x):
    digit1 = int(x%10)
    a = x - digit1
    digit2 = int((a / 10))
    return (str(digit1) + str(digit2))
print(reverse(27))
print(reverse(44))
print(reverse(19))