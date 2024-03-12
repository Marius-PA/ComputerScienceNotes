
# internal hardware components

## Processor
- main memory
    - stores data as well as intructions
    - number of memory addresses is constrained by the width of the address bus
        - each address can store a fixed numner of bits
            - determined by the processor


- Inside the CPU
    - all coordinated with the buses
        - data bus
        - address bus
        - control bus

# Others

- I/O controllers
    - external devices
        - USB
    - cannot be directly connected to the processor
    - I/O controller
        - acts as an interface

- Fetch-execute cycle
    - fetch the next instruction
    - decode the instruction and prepare to execute the intruction
    - execute instruction

- Stored program concept

# System buses

- system buses
    - Sending information via buses
    - get coordinated by buses
        - data bus
            - has bits of information
        - address bus
            - carries the adress of a memory location
            - memory allocation
            - tells where the data should go
        - control bus
            - controls data
                - memory:
                    - read
                    - write
                - bus:
                    - request
                    - grant
                - clock
                    - synchronise
                    - faster the clock, the more informations it processes

---

# Words

- memory is divided up in equal units called words
- word length is usually 8,16,32,64 bits
- each word has a separate memory address

# Architecture

### John von Neumann
- most common

- instructions and data are stored in a common main memory

### Harvard

- seperates the data and instructions into separate memories using different buses
- program instructions and data are no longer competing for the same bus