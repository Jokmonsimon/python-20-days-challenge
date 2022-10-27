def first_and_last(message):
    for char in message:
        if char[0] == char[-1]:
            return True
        elif char == "":
            return True
        else: 
            return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))