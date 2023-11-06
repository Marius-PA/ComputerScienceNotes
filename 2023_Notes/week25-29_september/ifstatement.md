
# Objectives

- be able to use relational operators
- be able to use boolean operations AND, OR (AND happens first and then OR)

---

# IF ... THEN

- program flows is controlled by evaluating a Boolean condition
- A Boolean condition evaluates to True or False

Relational operators

- < Greater then
- > less than
- =< greater than or equal to
- => less than or equal
- = equal to 
- <> not equal to

---

# Boolean

AND  : returns TRUE of both conditions are true
OR   : returns TRUE if either of the condition is true
NOT  : A TRUE expression become FALSE and vise versa

--- 

```python

x = 1
y = 2

if x > y and x < 10: # relational and boolean
    print (":)")
else:
    print(":(")

```

# Breaking loops

```python

count = 0

while True:
    while True: # even if there is another loop, break breaks both loop, it breaks all loop the break statement is in, breaks whatever loops it's part of
        count += 1
        if count > 10: # if the count is more than 10, then the loop breaks
            break

        print(":)") # will stops after 10 ":)"

```

# Continue

```python

count = 0

while count < 10:
    count += 1
    if count > 5:
        continue  # means "go to the top", stop sthe execution of the loop and then goes to the loop WHEREAS "break" will stop completely the loop 
    print(count)


# output:
#1
#2
#3
#4
#5

```

---

## Break exemple

```python

number = 0

while True:
    try:
        number = int(input("Enter a number : ")) # if the answer is right then break the loop
        break
    except:
        print("you did it wrong !")

print(number)


```

---

## Continue exemples

```python

number = -1

while True:
    try:
        number = int(input("Enter a number : "))
    except:
        print("you did it wrong !") # if the data is not correct, continue until it is and ONLY AFTER THE DATA IS CORRECT check if the number is between 0 and 10
        continue
    
    if number < 0 or number > 10:
        print("needs to be between 0 and 10")
        continue

print(number)


```