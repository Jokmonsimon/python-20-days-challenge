# Checking Equaality Vs Identity

from re import A


a = [1, 2, 3]
b = a 
c = [1, 2, 3]

print(a == b)
print(b == a)
print(a is b)
print(b is a)
print(a == c)
print(c == a)
print(a is c)
print(c is a)