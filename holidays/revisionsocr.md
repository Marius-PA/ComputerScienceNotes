# abstraction

- representation of reality
    - solving a problem by separating parts

subroutines / libraries
- easier to understand and quicker to debug
- focus on what is important

- concentrate on 1 part at a time

---

cache = data that has been used and that is stored temporarly in case it is needed again

- reusable components :
    - libraries
    - subroutines
    - classes

# recursion

- overflow if no terminating condition

# variables

local = declared in a function
global = declared outside of a function

# subroutines

Subprograms = subroutine, functions, procedures

- functions : subprograms 
    - usally but not ALWAYS return a VALUE
- procedures
    - performs operations but DO NOT return a VALUE

# parameters

IF NOT SPECIFIED, VALUE

- by value
    - only changes value WITHIN the subroutine
- by reference
    - changed in BOTH the subroutine and outisde

# IDE

- comprehensive set of tools to develop programs

Integrated Development Environment

- an editor
- error diagnostics
- a run time environment
- step by step progression though a program


# OOP

- class and constructor
- methods

```
## create class and constructor

class Pet 
    private name

    public procedure new(givenName)
        name = givenName

---

## methods

public procedure setName(givenName)
    name = givenName
endprocedure

public function getName()
    return name
endfunction

## instantiating an new object from another class

Pet myPet = new Pet("Fido")

# calling methods from another class

myPet.setName("Spike")
print(myPet.getName())


```