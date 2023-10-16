# 16/10/2023

# Starter activity

### How many more bytes does 4MiB have than 4MB ? 

(2<sup>20</sup> * 4) - (4 * 10<sup>6</sup>) = 194 304 Bytes

### How many nibbles (i.e a group of 4 bits) are there in 16KiB ?

Number of Nibbles = (Size in KiB) * 1000 (bytes/KiB) * 8 (bits/byte) / 4 (bits per nibble)

Number of Nibbles = 16 * 1000 * 8 / 4 = 32000 nibbles.

---

# Learning Ojectives

- Explain:
    - difference between:
        - unisgned
        - signed
        - fixed-point

- Calculate:
    - minimum and maximum values of all three binary forms

- Compare:
    - decimal to binary arithmetic for:
        - addition
        - multiplication

- Convert:
    - From binary to each binary form, and vice versa


***decimal means from 0 to 9***

***decimal POINTS mean when there is a point = 1.75***

# Binary recap

Bit = either 1 or 0

Byte = 8 bits

# Binary Forms

- AS cover ***3 binary forms***:
    - unisgned
    - signed
    - fixed-point

# Unsigned VS Signed

Unsigned binary = represent ***natural*** numbers

Signed binary = represent ***integers***

- they use different methods for representing the same values

---

# Unsigned Binary

Value of unsigned binary = calculate the sum of each bit, either 1 or 0

## Unsigned Limits

n bits can represent 2<sup>n</sup> different values, therfore the minimum and maximum values of unsigned binary using One's Complement are 0 and 2<sup>n</sup> - 1

# Decimal Arithmetic : Addition

- Recall how to calculte the sum of two decimal numbers:
    - YOU SHOULD BE ABLE TO EXPLAIN TO OTHER

27 + 15 = 42

# Unsigned Binary Arithmetic : Addition

- Recall how to calculte the sum of two decimal numbers:
    - YOU SHOULD BE ABLE TO EXPLAIN TO OTHER

27 + 15 = 42 = 00001111 + 00011011 = 00101010

| x | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| - | - | - | - | - | - | - | - | - |
| x | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |
| carry | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| result | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

| Syntax      | Description | Syntax      | Description |
| - | - | - | - |
| Header      | Title       | tes | test |

