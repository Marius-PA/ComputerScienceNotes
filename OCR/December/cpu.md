# objectives

- performance of CPU:
    - clock speed, cores, cache
- pipelining
    - how it improves efficiency

# Assembly

- memory divided in equal units
    - called "words"
- each word
    - separate memory address

- 8 bit address
- 8 bit data
    - 8 * 8 = 64 bit memory capacity

# address bus

- width
    - maximum possible memory addresses

- 8 bit address but
    - memory addresses number = 2⁸ = 256

- BI DIRECTIONAL, DATA CAN BE SENT BOTH WAYS

- if same lenght words and data bus
    - can send in a single operation

# format of instructions

- Assembly is close to the metal

- architecture includes
    - word size
    - width of the address bus

- determine the format used by the proc

# Mchine code instruction

- maximum size of operand
    - depends of the width of data bus

# System clock

- ON/OFF signals
    - to synchronise the operations

- on the rising edge of the clock
- actions take a fixed number of cycles to complete

# Number of cores

- cores linked together in the same of intergrated circut
- software may not be able to take full advantages of the cores

# parallel processing

- several procs
    - working at the same time

- different part of the same task

# cache memory

- small and superfast amount of memory

- cache level 2
    - larger, slower

- both types are held on the processor chip

## level 1 cache

- split
    - instruction cache and data cache
        - can be FETCHED SIMULTANEOUSLY

- more cache
    - will not have to fetch the next intruction into the RAM
        - it will already been loaded in the superfast cache memory
            - can be retrived more quickylw