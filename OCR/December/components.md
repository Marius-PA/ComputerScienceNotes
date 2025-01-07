# ALU
- arethemtic logic unit

- logic gates
    - solving part of the processor
    - logical and shift operations on data
    - operations: add, subract, multiply, divide
        - AND, OR, NOT, XOR
    - shift operations: move bits to right or left

- registers 
    - speed things up

# CPU
- central processing unit

# Control Unit
- coordinates the activity of all components

# Bus
- data tranfers along
- 8,16,32 lines = more bits

# System Bus
- Data
- Control
    - read : Ram places on the data bus
    -  write :
    - request : a device request use of data bus
    - grant : indicates CPU has granted access
- Address

# dedicated registers

- PC , Program Counter
    - holds memory address of the next intruction
- CIR
    - holds the current instruction
        - opcode and operand
- MAR
    - holds the address in memory
        - processor is required to fetch or store data
- MDR
    - temporarily holds data
        - moving between the processor and main memory
- accumulator
    - hold intermidiate results of an instruction


# Fetch step 1-4

1. next instruction copied from PC to MAR
2. instruction copied to MDR
3. contents of PC incremented
4. content of MDR , copied to the CIR

# Decode 5-7

5. instruction in CIR = decoded
6. operand or opcode = determine what type of instruction it is, fectes additional data from the memory 
7. passed to the accumulator

- opcode
    - specifies the operation  = carried out
- operand either
    - address of the data to be used, copied to the MDR
    - the acutal data, passed to the MDR

# Plenary

- mains components of proc:
    - ALU
    - Control Unit
    - Registers
    - System bus

- Data
- Control
- Address

- MDR
- PC
- CIR
- MAR
- accumulator