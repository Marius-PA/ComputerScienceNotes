# Local variables in subroutines

- Subroutines may declare their own variables, called local variables, and that local variables:
    - exist only while the subroutine is executing
    - are accessible only within the subroutine

Good practice = use local variables

---

# Local variables:

Variables in a function are DIFFERENT from the variables OUTSIDE a function.

```python

x = 1

def f(): # the x = 2 in the function f() is DIFFERENT from the x = 1
    x = 2 

f()

print(x)

```

# Global variables:

```python

x = 1 # this x will refer to x = 2 as global x make the 

def f():
    global x # state that you already declared a variable
    x = 2

f()

print()

```