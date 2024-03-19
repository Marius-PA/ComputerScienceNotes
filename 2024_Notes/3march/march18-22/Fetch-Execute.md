
# Objectives

- role and operation of a processor and its major components
- stages of the Fetch-Execute cycle and determine the roles of the various processor regiserts in faciliting this
- Factors that affect the performance of a processor

# Fetch-Execute cycle

- Fetch-Execute cycle = 8 - 10 marks
    - extended answer

- describe the 4-steps
    - 8 mark

- 4 steps
    - 3 main stages
        - fetch
            - PC placed into the MAR
            - contents of MAR is placed onto address bus so it accesses the correct location in the main memory
            - placed on the data bus
            - value received on data bys loaded into MBR
                - not all fetches will be for instructions so cannot be loeaded directly into the CIR
            - PC is incremented
                - next instruction in the sequence can be fetched
            - Contents of MBR is copied to the CIR
                - so that data is fetched correctly
        - decode
            - packs the upcode, location of the instructions and the instructions
            - identifies the opcode
            - identifies operands it needs
            - look at the addressing mode
            - indirect
                - using a register to point to a memory location
        - execute
            - identifies what kind of operation if it is and sends it forward

- upcode
    - instructions
- 3 addressing mode
    - 2 bit

# Arithmetic

- x = 2

---

# CPU

- calculates
- executes instructions

- different components:
    - Arithmetic-Logic Unit (ALU)
    - SOC
        - everything built into a CPU
        - all on one chip

    - Control Unit
    - Clock
    - General purpose registers
    - Dedicated registers

# ALU

- does all the logic, arithmetic, shift operation on dataa
- arithmetic
    - add, substract, multiply, divide
- Shift operations
    - move bits to the left or right within a register
    - bitwise switching

# control unit

- coordinates the activity of all other components

# The system clock

- A series of regular ON/OFF
    - syncronises the steps

# general purpose registers

- results from the ALU need to be stored somewhere
    - CPU have several locations of super-fast memory called registers that are used to temporarily store results

- allows for CPU to immediately re-use these results in subsequent calculations

- further redading
    - figure out the different between L1,L2,L3 cache memory (inside the cpu, where the registers resides)

# Executing instructions

- carrying out sequences of programming instructions requires many different snippets of information to be held
    - CPU has to temporarily hold the current instruction being executed
    - hold address of data needed, and data itself
    - keep track of the address of the next instruiction to be executed

# Dedicated registers

- most IMPORTANT REGISTERS TO REMEMBER

- Program Counter (PC)
    - holds the memory address of the next instruction to be executed
- Current Instruction Register (CIR)
    - holds the current instruction
- Memory Address Register (MAR)
    - holds the address in memory where the cpu is required to fetch or store data from or to
- Memory Buffer Register (MBR) or (MDR = Memory Data Register)
    - temporarily holds data moving between the CPU and main memory
- Status register (SR)
    - holds information about the current state of operationss. It is used to set flags (carry or overflow) or to detect error conditions

---
