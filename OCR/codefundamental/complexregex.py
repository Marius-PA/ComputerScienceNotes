import re

pattern = r'^(?=(?:\D*\d){4})(?=(?:\d*\D){4})[A-Za-z0-9]{8}$'

def is_valid_string(s):
    return bool(re.fullmatch(pattern, s))

# Test cases
print(is_valid_string("a1b2C3d4"))  # True
print(is_valid_string("abcd1234"))  # True
print(is_valid_string("12345678"))  # False (only numbers)
print(is_valid_string("abcdefgh"))  # False (only letters)
print(is_valid_string("ab12CD34"))  # True
