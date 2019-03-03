# Palindromes
# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '':
        return True
    else:
        a = len(s)
        if s[0] == s[a-1]:
            return is_palindrome(s[1:a-1])
        else:
            return False

 
print (is_palindrome(''))
#>>> True
print (is_palindrome('abab'))
#>>> False
print (is_palindrome('abba'))
#>>> True