
[Adacomputer Logic Gate](https://adacomputerscience.org/concepts/boolean_logic_gates?examBoard=all&stage=all)

[Logic Gate Simulator](https://academo.org/demos/logic-gate-simulator/)

# Logic Gate

---

## 0 = False
## 1 = True

---

- What is a logic gate
    - UNARY
        - 1 input
    - BINARY
        - 2 inputs
    - high and low voltage

- A buffer
    - produce the same output as his input
    - if input is 1, output is 1

- If circle at the end of a logic gate
    - then = a NOT gate

---

- NOT gate
    - produce the opposite output

![NOT gate](img/image-2.png)

- AND gate
    - if both inputs are 1, produces input of 1

![AND gate](img/image-3.png)

- OR gate
    - if either of their inputs are 1, produces an input of 1

![OR gate](img/image-4.png)

---

- NAND gate
    - like AND gate
        - the NOT variant

![NAND gate](img/image-5.png)

- NOR gate
    - like OR gate
        - the NOT variant

![NOR gate](img/image-6.png)

- XOR gate
    - exclusive
        - one or the other but not both
        - can be created with an OR, NOR, AND gate

![XOR gate](img/image-7.png)

---

# Construct a truth table

[Ada compter science | Truth table](https://adacomputerscience.org/concepts/boolean_construct_truth_table?examBoard=all&stage=all)

- Dott = AND
    - Exemple:
        - A . B (A and B)

- inversion
    - a straight line on the letter

- (plus) + = OR
    - A + B (A or B)

---

# Smallest Computer Using boolean

![2 bits calculation](img/image21.png)

---

# Boolean algebra

- 3 different forms of writting boolean algebra
    - USE AQA ONE !

- 3 primary operations
    - Negation = NOT
        - REPRESENTED BY A BAR AT THE TOP OF A LETTER
            - returns the opposite truth
                - if 2 over bars, IT CANCELS OUT
                    - cancel the opposite
                    - have to match the EXACT SAME PART TO CANCEL OUT

    - Conjunction = AND
        - "." dotts
            - akin to multiplication
                - true if and only if both operands are true, otherwise false

    - Disjunction = OR
        - "+"
            - akin to binary addition
                - returns true of at least one operand is true, otherwise false

    - Exclusive Disjunction = XOR
        - "+" inside a circle
            - one or the other but not both
            - A but not B, or not A but B

    A +circle B = A . B- + A- . B

- order of operation
    - brackets happen first
        - negation
        - conjunction

    A . B + C = (A.B) + C

- Associative Laws
    - order of operations doesn't matter IF AND ONLY IF they are the same logic gates

    A . (B . C) = (A . B) . C

- Simplifying
    - reduces the number of logic gates without changing the functionality

    A . (A + B)
    A . A + A . B
    A + A . B = A