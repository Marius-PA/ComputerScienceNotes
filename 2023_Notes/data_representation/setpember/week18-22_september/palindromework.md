substring:

starting index, ending index:

step = -number 

```python

# check if the user inputs is palindrome
# put in uppercase

# steps:
# check if the first and last number = same
# check of the second and last-second = same
# ignore middle letter

# Check if a word is a palindrome

word = input("Enter a word: ")
word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

# Check if the word has at least 2 characters
if len(word) <= 2:
    print("/!\ Your word must be at least 2 characters long. /!\ ")
    exit()
else:
    # Check if the word is a palindrome
    if word == word[::-1]: # looking at the last index of the word to see if it is similar
        print("'",word,"'",": is a palindrome")
    else:
        print("'",word,"'","is not a palindrome")

```

---

Using a function:

```python

    
word = input("Enter a word: ")
word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

# Check if the word has at least 2 characters

def palindrome():

    if len(word) <= 2:
        print("/!\ Your word must be at least 2 characters long. /!\ ")
        exit()

    elif word == word[::-1]: # looking at the last index of the word to see if it is similar
        print("'",word,"'",": is a palindrome")
    else:
        print("'",word,"'","is not a palindrome")

palindrome()

```