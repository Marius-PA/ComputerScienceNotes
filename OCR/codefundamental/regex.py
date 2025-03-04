import re

def is_valid_username(username: str) -> bool:
    """Check if the username contains only English letters and can contain numbers."""
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    return bool(pattern.match(username))

# Example usage
username = "T323hisIsanExampleUser123"
if is_valid_username(username):
    print("Valid username")
else:
    print("Invalid username")


def is_valid_password(password: str) -> bool:
    """Check if the password is at least 10 characters long, contains at least 1 special character, 1 capital letter, and 2 numbers."""
    pattern = re.compile(
        r'^(?=.*[A-Z])(?=.*\d.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{10,}$'
    )
    return bool(pattern.match(password))

# Example usage
password = "AnExample35!"
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")