# 14/11/23

# Bitmap

bitmap = ***a representation*** in which each item corresponds to one or more bits of information, especially the information used to control the display of a computer screen.

# Pixel

### pixel is the smallest addressable unit of an image

a pixel is a representative of a bit coresponding a colour or level of brightness

# Colour Depth

***the number of bits used to store each pixel*** NOT the number of COLOURS

- colour depth = 8

- different colour = 256 

- BECAUSE 2<sup>8</sup> = 256

---

colour depht = 2

only 2 colours can be represented

colour depth = 2<sup>n

i.g = 2 bits can represent 4 colours

# Resolution

***Dots per inch/cm/unit*** where a dot is a pixel

Resolution most of a time REFERS OF ITS ***width by height*** in pixels

doesn't only mean width and height, BUT ALSO ppi

### For exams

Resolution = ***Dots per inch/cm/unit***,  ***width by height*** in pixels

# Calculating bitmap file size

image file size (in bits) = width (in pixels) × height (in pixels) × colour depth

When an image has a width of 8 pixels and a height of 8 pixels, with a colour depth of 4 bits, the calculation is:

    Calculate total bits: 8 × 8 × 4 = 256 bits

# Metadata

Data about the data

- Image dimensions (e.g. width in pixels, height in pixels)
- File format
- Date and time of creation
- Geographical location of creation
- Details about the device used to create the - image
- Camera settings

# Image formats

- comparing file formats:
    - bitmaps (.bmp)
    - Graphic Interchange Format (.gif)
    - Portable Network Graphics (.png)
    - Scalable Vector Graphics (.svg)

# Storage Requirements

metadata + width * height * depth = bits

---

# Learning objectives

- Explain:
    - how bitmaps are represented
        - resolution
        - colour depth
        - size in pixels

- calculate:
    - storage requirement for bitmapped images
    - bitmap image may also contain metadata

- Being familiar with typical metadata

---

exercice:

Q1. smallest addressable unit of an image

Q2. the resolution is (dots/inch) pixel/inch or per centimeters, it can also be the width and height in term of pixels

Q3. 5 state

colour depth = 3

Ex2:

Q1. 320 * 240 * 2/1000 = n

153.6 kilobits

156.6/8 = 19.2 kilobytes

Q2. 

500000*8 = 4 000 000

n2 * 4 = 4 000 000
n = sqrt(4 000 000/4)

1000 width and height pixels

Q3. 

360000*8 = 2 880 000

800 * 600 * n = 2 880 000

2 880 000 / 800 * 600 = n

n = 6

---

# Test topic 

- Number Systems
- Number Bases
- Units of information
- binary number system *
- informaton coding systems 
- analogue vs Digital
- bitmap graphics