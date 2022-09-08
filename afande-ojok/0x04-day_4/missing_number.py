# Find the missing number in an array of 0 to n

def missing_numbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 19, 20, 22, 23]
print("The Missing Numbers are: {}".format(missing_numbers(list_of_numbers)))