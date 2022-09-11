# Random List

random_list = [1, 3.4, 'Yearn AI', True]

print(random_list[0])
print(random_list[1:])
print(random_list[:-1])
print("==============================================================================================================")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

third_quarter = months[6:9]
print("Months in third quarter of a year are: {}".format(third_quarter))

# Slicing List
first_half = months[:6]
print("Months in first half of a year are: {}".format(first_half))

second_half = months[6:]
print("Months in second half of a year are: {}".format(second_half))
print("==============================================================================================================")

# Length of List and String

print("The length of the list variable 'months' is: {}".format(len(months)))

greeting = "Welcome to Yearn AI"
print("The length of the string variable 'greeting' is: {}".format(len(greeting)))
print("==============================================================================================================")

# 'in' or 'not in' - String

greeting = "Welcome to Yearn AI"

print('ai' in greeting)
print('ai' not in greeting)
print('AI' in greeting)
print('AI' not in greeting)
print("==============================================================================================================")


# 'in' or 'not in' - List
num = [1, 2, 3, 4, 6, 8, 12]

print(5 in num)
print(5 not in num)
print("==============================================================================================================")

# Mutable and Ordered
# List is Mutable and Order
# String is Immutable and Order

my_list = [1, 3, 5, 7, 9, 11]
print(my_list)
my_list[2] = 4
print(my_list)
my_list[3:] = 4, 6, 8
print(my_list)
print("==============================================================================================================")

my_string = 'Hello Afande Ojok'
print(my_string[:5])
print(my_string[5:])
print(my_string[-1])
print(my_string[5]) # Prints the space separating Hello and Afande
print("==============================================================================================================")

# List Indexing
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[7]
num_days_1 = days_in_month[month - 1]

print(num_days)
print(num_days_1)
print("==============================================================================================================")

# Slicing Lists
# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# List and String
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

sentence2[6] = '!'
print(sentence2)

sentence2[0] = "Our Majesty"
print(sentence2)

# sentence1[30] = '!'
# print(sentence1) - Returns an error: TypeError: 'str' object does not support item assignment

sentence2[0:2] = ['We', 'want']
print(sentence2)