# Working with Conditional Flow in Python

n = 11
# n = 26

if n % 2 == 0:
    print("Number {} is even!".format(str(n)))
else:
    print("Number {} is odd!".format(str(n)))

# if, elif, else

season = 'Winter'

if season == 'Spring':
    print('Pland the garden!')
elif season == 'Summer':
    print('Water the gardern!')
elif season == 'Fall':
    print('Harvest the garden!')
elif season == 'Winter':
    print('Stay indoors!')
else:
    print('Unrecognized season!')
