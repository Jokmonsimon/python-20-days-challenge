# The is_palindrome function checks if a string is a palindrome. 
# A palindrome is a string that can be equally read from left to right or right to left, 
# omitting blank spaces, and ignoring capitalization. 
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for string in input_string.lower():
        # Add any non-blank letters to the end of the string,
        # and to the front of the other string.
        if string.strip():
            new_string = string + new_string
            reverse_string = string + reverse_string
    # Compare thr strings
    if new_string[::-1] == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True