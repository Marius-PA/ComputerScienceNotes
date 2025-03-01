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