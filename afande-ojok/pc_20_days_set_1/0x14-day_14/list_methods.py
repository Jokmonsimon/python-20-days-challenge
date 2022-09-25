from ntpath import join


my_list = [1, 30, 21, 8, 3, 15, 28, 17, 53, 42, 5]
print(sorted(my_list))
print(sorted(my_list, reverse=True))

# Append Item to a list
my_list.append(100)
print(sorted(my_list))
print(sorted(my_list, reverse=True))

# Pop Item from a list
my_list.pop()
print(sorted(my_list))
print(sorted(my_list, reverse=True))

# Join Function in Python
python_variables = ['Burdese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python' ]
print("\n".join(python_variables))
print("; ".join(python_variables))

# Append Item to a list
python_variables.append('Blood Python')
print("\n".join(python_variables))
print("; ".join(python_variables))

# len(), max() & min()
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

# sorted(), join() and Lists
names = ['Carlo', 'Albert', 'Ben', 'Donna']
print(' & '.join(sorted(names)))

# Append
names.append('Eugenia')
print(sorted(names))

