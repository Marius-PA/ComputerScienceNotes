
# Organisation:

put variables in CAPS to tell the variable is important and for context

## CONTEXT is the most important thing in a script

---

# Reorder logic

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
