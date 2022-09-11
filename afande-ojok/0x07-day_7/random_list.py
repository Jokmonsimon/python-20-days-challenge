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