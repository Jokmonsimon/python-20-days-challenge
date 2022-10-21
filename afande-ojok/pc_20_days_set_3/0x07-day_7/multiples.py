# Write a script that prints the multiples of 7 between 0 and 100. 
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
# Remember that 0 is also a multiple of 7.

def multiples(x):
    for n in range(100):
        n = (n*x)
        if n <= 100:
            print(n)
print(multiples(7))
print("==================================")

# Another method
for x in range(0, 100, 7):
    print(x)
print("==================================")

# Using Lambda 
for i in range(0, 100, 7): print(i)