# “For” Loops VS “While” Loops:

## “While” Loops:

```python
name = "marius"

for i in name:
    print(i)

output:

m
a
r
i
u

```

## “For” Loops:

```python
name = "marius"
index = 0 

while index < len(name):
    print(name[index])
    index += 1

Output:

m
a
r
i
u
s

```

“For” loops are used for Loops with a defined range.

```python

name = "marius"

for x in [ 1,2,3,4,5 ]: # standard list counting, counts up to 5
    print(x)

for x in range(1, 8): # Range : counts up to 7 as the last number is out of the list
    print(x)

for x in reversed(range(1, 8)): # Range : counts from 7 to 1
    print(x)

```