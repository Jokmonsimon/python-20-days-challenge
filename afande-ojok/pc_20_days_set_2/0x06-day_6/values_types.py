# Values and Types in Python

# String
hello = 'Hello World!'
print('The value: {} is of type: {}'.format(hello, type(hello)))
print('The value 27 is of type: {}'.format(type(27)))
print('The value 3.59 is of type: {}'.format(type(3.59)))
print('The value "27" is of type: {}'.format(type('27')))
print('The value "3.59" is of type: {}'.format(type('3.59')))

# Number separated by commas is not legal in Python
print('This is not what we expected: {}'.format(1,000,000)) # Semantic error