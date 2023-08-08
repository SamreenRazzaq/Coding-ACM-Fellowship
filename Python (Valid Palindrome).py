#Valid Palindrome

def is_valid_palindrome(s):
# Remove non-alphanumeric characters and convert to lowercase
    alphanumeric_s = ''.join(c.lower() for c in s if c.isalnum())
# Compare the alphanumeric string with its reverse
    return alphanumeric_s == alphanumeric_s[::-1]
#Examples:
print(is_valid_palindrome("A man, a plan, a canal, Panama")) # Output: True
print(is_valid_palindrome("race a car"))                     # Output: False
print(is_valid_palindrome(" "))                              # Output: True
