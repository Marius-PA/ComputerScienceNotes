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

|+| 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| - | - | - | - | - | - | - | - | - |
|+| 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |
| carry | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| result | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

---

# 17/10/23

# Starter activity

Q1.

(base 2)

    0 + 0 = 0
    0 + 1 = 1
    1 + 0 = 1
    1 + 1 = 10

Q2. 

0011 + 0001 = 0100

0101 + 0110 = 1011

0011 + 0101 = 1000

---

One's and Two's complement are **techniques**

## States

different combinations of the **bits**

---

# Signed Binary

Signed binary = calculated the same way as unsigned binary, HOWEVER **the last bit is negative**, meaning -2<sup>n-1</sup>.

|-2^7|2^6|2^5|2^4|2^3|2^2|2^1|2^0|
|-|-|-|-|-|-|-|-|
|-128|64|32|16|8|4|2|1|

last bit as a sign = a minus sign

- 11111111 = 
    - 255 (1's Complement (Unsigned Binary))
    - -1 (2's Complement(Signed Binary))

# Importance of bits order
### First bit = least significant bit
### last bit = most significant bit

Overflow can occurs every everywhere

# Signed Limits

Minimum and maximul values of signed binary = -2<sup>n-1</sup> and 2<sup>n-1</sup> - 1

# Signed Binary Arithmetic: Subtraction

To substarct one signed binary number from another = must use Two's Complement; **flip the bits** (i.e dwitch from 0 to 1, and vice versa) and add 1, then perform addition.

7 - 5 = 7 + -5 = 00000111 - 00000101 = 00000111 + 11111011

|5|00000101|
|-|-|
|-6|11111010|
|+|00000001|
|-5|11111011|

# Fixed-Point Binary

Both signed and unsigned binary = powers increase from left to right

fixed-point = decreases from left to right after the fixed point

|2^4|2^3|2^1|2^0|-|2^-1|2^-2|2^-3|2^-4|
|-|-|-|-|-|-|-|-|-|
|8|4|2|1|-|0.5|0.25|0.125|0.0625|

### Fixed-Point Binary (Unsigned)

Example:

1001.0110

|2^3|2^2|2^1|2^0|-|2^-1|2^-2|2^-3|2^-4|
|-|-|-|-|-|-|-|-|-|
|1|0|0|1|.|0|1|1|0|
|8|0|0|1|.|0|0.25|0.125|0|

8 + 1 + 0.25 + 0.125 = **9.375**

### Fixed-Point Binary (Signed)

exemple = 1001.0110

|-2^3|2^2|2^1|2^0|-|2^-1|2^-2|2^-3|2^-4|
|-|-|-|-|-|-|-|-|-|
|1|0|0|1|.|0|1|1|0|
|-8|0|0|1|.|0|0.25|0.125|0|

-8 + 1 + 0.25 + 0.125 = **-7.375**

---

# 19/10/2023

# Learning Objectives

- Differentiate between:
    - character code representation of a decimal digit and its pure binary representation

- Describe:
    - ASCII
    - Unicode
        - coding systems for coding character data and explain how it works

# ASCII

ASCII stands for the American Standard Code for Information Interchange, which is a character encoding standard from 1963

### Why was unicode introduced

- we needed international communication
- increase in international communication
- needed to accept more than English

## UTF

- UTF-8 = ASCII
- UTF-16 = Unicode