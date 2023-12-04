# 27/11/2023

# Compression

- know why:
    - images
    - text
    - sounds files
        - are compressed

- understand the difference between:
    - lossy
    - lossless
        - advantages
        - disadvantages

---

## Compression technique

reduces the storage requirements of files

- compression
    - reduced the file size of an uncompressed file

- decompression
    - was once compressed

- uncompressed
    - synonyme of "original"
    - the original file

## Compression Ratios

- Compression ratios
    - used to compare the difference between the uncompressed and compressed storage requirements

    uncompressed/compressed = uncompressed : compressed

45MB uncompressed

15MB compressed

= 3:1 ratio

---

Exercices:

Q1. uncompressed should be the higher ratio

Q2. 80/5 = 16 

16x2 = 32KB

# Lossless vs. Lossy

Terms to describe wether or not a compression technique results in ***loss of data***

Lossless = no loss of data during Decompression

Lossy = loss of data during Decompression

- Lossless format
    - PNG
    - GIF
    - ZIP: file/folders

- Lossy format
    - MP3: audio
    - JPEG: images
    - MP4: video
        - grouping together similar patterns
        - always results in loss of data

---

# Compression Techniques

- BOTH TECHNIQUE ARE LOSSLESS

## Run Length Encoding (RLE)

RLE is lossless

***run-repeating patterns are replaced with a single instance alongside its frequency (i.e, count)***

Exemple:

    BOOKKEEPER = B1,O2,K2,E2,P1,E1,R1

## Dictionary-Based

Lossless technique

***patterns are replaced with a corresponding key (i.e unique identifier) for a dictionary***

    TO BE OR NOT TO BE = 00,01,10,11,00,01

    4 difference words, so 2 bits

- TO = 00
- BE = 01
- OR = 10
- NOT = 11

---

## Exercice:

Q1. reduce the ( file size) storage capacity of a file (or folder)