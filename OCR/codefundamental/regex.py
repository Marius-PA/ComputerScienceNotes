import re

name = input("Name")

valid = re.match("[A-Z]+[0-9]+[a-zA-Z]+[@][gmail.com]", name)
print(valid)

if valid:
    print("Ok")
else:
    print("invalid")