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

---

## __Algorithm definition:__

An algorithm is a procedure used for __**solving a problem**__ or performing a computation.
It acts as an exact __**list of instructions**__ that conduct specified actions step by step.

---

# Learning Objectives:

- differences between cariable and a constant
- explain advantages of using named constans
- be familair with : 

        random number generation

        exception handling

- use exception handling with a familiar programming language

---

# Organisation:

put variables in CAPS to tell the variable is important and for context

## CONTEXT is the most important in a script

---

## Seed:

used to create radom numbers that will follow the same patern:

- the same seed will always display the same numbers

---

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

substring:
starting index, ending index:
step = -number 