# AS

## During holidays

# paper 1

- 1 hour
    - programming
        - learn squeleton code
        - learn the python script

        - name a variable, constant containing a indefinite loop

# paper 2

- 1h30
    - theory

---

# What to revise

- representing float numbers into binary

- difference between the way the Harvard and von Neumann architectures operate.

- laws of Boolean algebra, simplify the following Boolean expression

- steps involved in the Fetch-Execute cycle

    - Fetch: Contents of Program Counter / PC transferred to Memory Address Register / MAR Address bus used to transfer this address to main memory Transfer of content uses the data bus Contents of addressed memory location loaded into the Memory Buffer Register / MBR Increment (contents of) Program Counter / PC  A. at any part of fetch process after transferring PC to MAR Increment Program Counter / PC and fetch simultaneously Contents of MBR copied to CIR

    - Decode: Decode instruction held by the (Current) Instruction Register / (C)IR The control unit decodes the instruction Instruction split into opcode and operand
    
    - Execute: If necessary, data is fetched If necessary, data is stored in memory The opcode identifies the type of operation/instruction to be performed (by the processor) Result (may be) stored in register/accumulator The operation (identified by the opcode) is performed by the processor. A. ALU Status register updated If jump / branch required Program Counter/PC is updated

- assembly

# Coding part

- if a maximum of a value : constant, doesn t change, when reaching constant value

- identifier = the name of a variable

- parameter = if statement, NoOfMoves == 9:
- between a constant and a variable
    - variable can vary(change), constant remains unchanged throughout the program

- Describe the circumstances under which these instructions will stop being repeated
    - when one of the playrs wins, or number of moves reaches 9

- Possible that the game might end in a draw even though there are winning opportunities on the board, explain why this could happen
    - this could happen if the win-checking logic is flowaed or if the game staate is not updated correctly after each move
- identifier for a variable that has an accumulator role
    - find accumulators in loop, number_of_moves, PlayerOne/TwoScore

- identifier for a variable that has a flag role
    - game has been won, has been drawn

- identifier for a user-defined function that returns a value
    - check_win
    - check for functions that returns a value, any of them

- subroutine getwhostart, give an exmaple of a condition statement in this subroutine
    - find, if, elif
    - if (RandomNo % 2) == 0:

- case statement
    - if case 1, do this, if cas 2, do this
    - default case, if none of the cases fit in