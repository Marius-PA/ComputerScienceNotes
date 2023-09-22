# subroutines (procedures/functions)

Objectives:
- being familiar with subroutines and uses
- subroutine is a 'out of line' block of code
- explain advantages of using fuctions
- reducing down the code, less spaghetti code

---

# Subroutines(procedures, functions):

- subroutines = a portion of a programm which can be called again
- procedures = a bit of code/ doesn't return anything
- functions = return values

- wether or not it gives you back a value:
    - if yes : functions
    - else : procedure

---

Example of a procedure:

```python

def hello():
    print("Hello guys !")

hello() # (hello) function being called, avoid repetition
hello()

output:

Hello guys !
Hello guys !

```
Functions give us the ability to reduce redundancy of the code and being able to re-use it:
### **it's like a big variable** which can be called

---

# Parameters of subroutines:

- Being able to:
    - Describe the use of parameters to pass data within programs
    - Use subroutines with interfaces

### well definied interface is import !

# Functions VS Procedures:

Examples of a procedure (doesn't return anything):

```python

def sq(x): # sq() everything in bracket is the parameter of tge sq function

    # the function make x^2 and then print the result
    print(x ** 2) 

sq(1) # 1^1 = 1
sq(2) # 2^2 = 4
sq(3) # 3^2 = 9

# not returning value so = procedure

```

example of funtcion (returns a value):

```python

def sq(x):
    return x ** 2

print(sq(1)) # 1
print(sq(2)) # 4
print(sq(3)) # 9

# returning value so = function

```

---

