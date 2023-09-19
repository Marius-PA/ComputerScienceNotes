# weekly note

Week 18-22 september:

# string:

- length
- position
- substring
- concatenation
- character TO character code | (exemple “E” as a string might equal 25 known as ASCII which make our computer known which key we type)
- character code TO character
- string conversation operations.

Word decomposed = “ayo” = ‘a’, ‘y’, ‘o’ = a list of character !

len() counts the number of character in a string : “hello” returns 5 as int:

```python
name = hello
len(hello[1])

returns : h
```

refering to his index: 

last index of a string is len(x) - 1, where x is a string

```python
x = "huh"
last = len(x) - 1

print(last)

returns : 2
```

when putting negative numbers, the index counts backwards.

---

Substring:

Substring is like a range 

```python
name = "test"

print(name[0:3]) # 'tes'
print(name[1:-2]) # 'e'

output:
'tes'
'e'
```

```python
name = "testhello"

print(name[1:-1:2]) # 'etel' = here it skips the first and last index and counts every 2 leters
print(name[::2]) # 'tshlo' = here it doesn't skip anything and just counts every 2 steps

output:
'etel'
'tshlo'
```

Concatenation:

```python
name = "jaj" + "tens" # it needs to be the same datatype ot be added !!

print(name)

output:
"jajtens"
```

---

FROM Character TO Character Code:

```python
ord('A') # 65 / it gives the Ascii number

output:
'65'
```

FROM Character Code TO Character:

```python
chr(65) # A

output:
'A'
```

---

String Conversion Operations:

```python
b = True
i = "2"
f = "3.0"

bool(b) # True
int(i) # 2
str(f) # 3.0
```

Lower and Upper cases:

```python
name = "GoOdTeSt"

name.lower() # goodtest
name.upper() # GOODTEST

output:
"mittens"
"MITTENS"
```

--- 

Const VS Variables:

Reorder logic

```python
name = "marius"
a = True
b = False

if a:
    print("yes")
else:
    if b:
        print("maybe")
    else:
        print("no")

### identical but setenced differently

if a:
    print("yes")
elif b:
    print("Maybe")
else:
    print("no")
```

### “For” Loops VS “While” Loops:

### “While” Loops:

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

### “For” Loops:

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

---

### __Algorithm definition:__

An algorithm is a procedure used for __**solving a problem**__ or performing a computation.
It acts as an exact __**list of instructions**__ that conduct specified actions step by step.
