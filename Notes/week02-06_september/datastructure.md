
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

---

# List

a list of dynamic = contain ANY data

    append() = add to the end of a list
    pop() = remove a the end of a list

# Set

Set are unordered = can only contain instance of a value

exemple :

```python

set = {"2", "3", "4", "2"}
print(set)

#output

# 2,3,4
#(the last 2 doesn't appeaer)

```

```python

fruits = {"apple", "banana", "cherry"}

print(fruits)

# {'banana', 'cherry', 'apple'}

```


# Tuple

a tuple is static = a fixed size = can't change the order = imutable

exemple :

```python

fruits = ("apple", "banana", "cherry")

print(fruits)

```

swap variables using tupple

```python

x = 1
y = 2

x, y = y,x

```

---

# 1D arrays

## Objectives

- Be familiar with the concept of a data structure
- Use 1D and 2D arrays in the design of solutions to simple problems

bytes = smallest addressable memory

---

# why index start from 0 and not 1

## 0 is the black hole of nothing, it disovles

0 is having the concept of nothing = formula to make sens

### ***without nothing we can't have something***

---

# 2D arrays

|0,0|1,0|2,0|
|:-:|:-:|:-:|
|0,1|1,1|x|
|0,2|x|1,1|

```python

grid = [[1] * 3] * 10

grid[0] = 1
grid[5] = 7

print(grid)


```

---

```python

MAGIC = 3
grid = [[0] * MAGIC] * MAGIC

for row in range(MAGIC):
    print(grid[row])

#output
#[0, 0, 0]
#[0, 0, 0]
#[0, 0, 0]

```

---

naming different = CAN BE ANYTHING AS LONG AS YOU HAVE THE SAME LOGIC CONSITENTLY

```python

MAGIC = 3
grid = [[0] * MAGIC] * MAGIC

for row in range(MAGIC):
    for col in range(MAGIC):
        print(col, row)

#output:

#0 0
#1 0
#2 0
#0 1
#1 1
#2 1
#0 2
#1 2
#2 2

```

---

```python

MAGIC = 3
grid = [[0] * MAGIC] * MAGIC

grid[1][1] = 7

print(grid)

for row in range(MAGIC):
    for col in range(MAGIC):
        print(grid[col][row])

#output:

#[[0, 7, 0], [0, 7, 0], [0, 7, 0]]
#0
#0
#0
#7
#7
#7
#0
#0
#0

```

## to understand 2D arrays, you need to understand 1D arrays

---

```python

numbers = [ x for x in range(1,101, 2) if x > 50]

print(numbers)

```