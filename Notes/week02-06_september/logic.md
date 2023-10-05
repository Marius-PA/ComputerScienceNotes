# Optimise code:

### returning absolute truth in a 'if' statement

```python

def is_odd(x): # DO NOT REMOVE THIS LINE
    if x % 2 == 0:
        return False
    else:
        return True

def is_even(x): # DO NOT REMOVE THIS LINE
    if x % 2 != 0:
        return False
    else:
        return True

# DO NOT EDIT BELOW THIS LINE

for x in range(0,101,2):
    assert is_even(x) and not is_odd(x)

for x in range(1,100,2):
    assert is_odd(x) and not is_even(x)

```

---

```python

def is_odd(x): # DO NOT REMOVE THIS LINE
    return x % 2 != 0

def is_even(x): # DO NOT REMOVE THIS LINE
    return not is_odd(x)

# DO NOT EDIT BELOW THIS LINE

for x in range(0,101,2):
    assert is_even(x) and not is_odd(x)

for x in range(1,100,2):
    assert is_odd(x) and not is_even(x)

```

***Advantages:*** only needs to change 1 function to make 2 changes = more efficient