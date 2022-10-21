# In math, the factorial of a number is defined as the product of an integer and all the integers below it. 
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. 
# Fill in the blanks to make the factorial function return the right number.

import re
from unittest import result


def factorial(n):
    result = 1
    for i in range(result, n+1):
        result = result * i
    return result

print(factorial(4))
print(factorial(5))
print(factorial(12))

# Fill in the blanks to make the factorial function return the factorial of n. 
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer and all integers before it. 
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. 
# Also recall that the factorial of zero (0!) is equal to 1.

def new_factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result
print("=====================================\n")
for n in range(0, 10):
    print(n, new_factorial(n))