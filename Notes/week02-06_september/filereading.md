# Objectives

- define:
    - fields
    - records
    - files

short term memory:
rams

long term memory:
hard drives

# File, records, fields

File = consists of a number of **records**

Records = number of **fields**, each holding an item of data

---

# Records

Record = data strucutre consisting of a number of fields which cana all be of different data types

### A record in pascal:

```pascal

Type
    studentRec = Record
    surname, first name: string[20]
    mark : integer
    End;
Var
    student : studentRec

```

Here a user-defined data type **studentRec** is defined, and a variable of this type is declared