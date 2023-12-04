
# 28/11/23

- Caesar cipher
    - encrypt a plaintext message
    - decrypt

# Cryptography

## Scytale Cipher 

tool used to perform a transposition cipher

# Security

- authenticity
    - proof that it is someone that sent it
    - not be able to take back what they sent

- confidentiality
    - restrict access unauthorised person
    - ensuring you only give access to the authorised persons

- data integrity
    - did the data was still the same after transmission
        - no interception

---

# Encryption

Encryption = ***the process converting a plaintext-encoded message into ciphertext, using a cipher algorithm with a key***

***obfustation of data*** = making a text not human readable

### Key terminology

- Cipher:
    - a process
    - an algorithm (or a set of multiple algorithms) used to convert between palaintext and cipher text

- plaintext:
    - unencrypted/decrypted message
    - human readable

- Ciphertext:
    - encrypted message
    - obfuscated

# Decryption

Decryption = ***process of converting a ciphertext-encoded message into plaintext using a cipher algorithm with a key to make it human readable***

unencryption = DOESN'T EXIST

## Keys

- keys:
    - public key
        - share between the sender and receiver
    - private key

## Symmetric Vs Asymmetric

Symmetric cipher = the same key is used for both encryption and decryption

Asymmetric cipher = uses different keys for encryption and decryption, public and private key

- public key = encryption
- private key = decryption

---

# Ciphers

Cipher = an algorithm, a set of instructions

- Caesar Cipher
- Vernam Cipher

## Caesar Cipher

shifts the ordinal value of a character codes by the key value

exemple: key = 7

    AN EXAMPLE = TG XQTFIEX

## Vernam Cipher

Vernam Cipher = ***substitution cipher, in theory, perfectly secure, the Caesar and Vernam ciphers are at the extremes opposite in terms of security***

- Caesar uses one key for all of the characters in the plaintext
- Vernam uses a key stream that consists of multtple keys, one per character
    - no dependencies between each keys

- encrypts by applying a bitwise XOR operation on each corresponding character code between the palaintext and key

XOR = Exclusively-OR

to encrypt you perform an XOR with the character code and the plaintext

to decrypt you perform an XOR with the ciphertext and the key

- ***One or the other, but not both, or not neither***

## Perfect Security

- only perfectly secured if:
    - each key must be truly random (i.e not pseudorandom)
    - each key must be used only once
    - there must be only two copies of each key, privately
    - each key must be destroyed after use

# Brute Force

Brute force = attempting each possibility (all possible keys)

Caesar cipher is easily breakable as there are only 25 possible keys, meaning it is susceptible to the 'brute force' approach; attempting each possible key

