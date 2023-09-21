# Try and Execpt

Telling python to try his best to figure out a instructions without error.

```python


try:
    number = int(input("Enter a number : ")) # if the number the user input is a int then print :)

    print(":)")
except:
    print(":(") # if the user inputs not a integer (string), then print :( 


```

Using with a loop:

```python

isLooping = True # loop around it until the user gives a correct input

while isLooping:
    try:
        number = int(input("Enter a number : "))
        print(":)")
        isLooping = False
    except:
        print(":(")


```