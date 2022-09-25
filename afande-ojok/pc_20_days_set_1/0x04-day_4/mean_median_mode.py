# Calculate Mean of a given List
from statistics import median


list_items = [42, 33, 70, 70, 42, 30, 25, 23, 24, 70, 80, 187, 35, 35]
mean = sum(list_items)/len(list_items)
print("The mean of a given list is: {}".format(mean))

# Calculate the Median of given list

# The Median is the middle value among all the values in sorted order.

# When the total number of values is even: 
# Median = [(n/2)th term + {(n/2) + 1}th]/2

# When the total number of values is odd:
# Median = {(n+1)/2}th term

list_items = [42, 33, 70, 70, 42, 30, 25, 23, 24, 70, 80, 187, 35, 35]

list_items.sort()
# print(list_items)

if len(list_items) % 2 == 0:
    mid_value_1 = list_items[len(list_items) // 2]
    mid_value_2 = list_items[len(list_items) // 2 - 1]
    median =  (mid_value_1 + mid_value_2)/2
else:
    median = list_items[len(list_items) // 2]
print("The Median of the given list is: {}".format(median))

# Mode is the most frequently occurring value among all the values.
list_items = [42, 33, 33, 33, 33, 33, 70, 70, 42, 30, 25, 23, 24, 70, 80, 187, 35, 35]

frequency = {}
for i in list_items:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("The Mode of a given list is: {}".format(mode))
