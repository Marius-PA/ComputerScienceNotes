
# Data structure

- Structure of Data (of a specific context)
    - organizing
    - processing
    - retrieving
    - storing data

# Dynamic VS static structures

***static*** = does not change size at run time

***dynamic*** = size and shape can change during runtime

### Memory allocation

---

# Abstract data structure

definition = a kind of a data type whose behavior is defined with the help of some attributes and some functions

the idear of a list

---

# Introduction to data structures

|Category|Word|
|-|-|
|Elementary data type|intergers, char, real, Boolean|
|Composite data type|string, array|
|Abstract data type|list, stack, queue|

array are always same size = static

list = static or dynamic = more generalised idea of arrays

a list uses arrays to implement list but 

    list != array

---

# List

```python


stuff = []

stuff.append("a")
stuff.append(2)
stuff.append(True)

print(stuff)

#output
#['a', 2, True]

```
multitple data type can be in one list

---

underflow: going to the negative value

```python

stuff = []

stuff.append("a")
stuff.append(2)
stuff.append(True)

print(stuff)

while True:
    print(stuff.pop())

#output
#IndexError: pop from empty list

```