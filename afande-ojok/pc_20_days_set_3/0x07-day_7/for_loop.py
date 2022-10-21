# Loop through a number
for x in range(10):
    print(x)

print("-------------------------------------")

# Loop through a string
for i in "Python":
    print(i)

print("-------------------------------------")

# Loop through a List
friends = ['Bryan', 'Sharon', 'Arnold', 'David', 'Jaspher']
for friend in friends:
    print("Hi " + friend)

# Calcualte sum and average of a given List
values = [25, 90, 1, 23, 21, 6, 18, 4]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum))
print("Average: " + str(sum/length))