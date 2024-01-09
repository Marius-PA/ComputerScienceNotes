# 09/01/2024

## data transmission:

the tranference from one device to another

Q2. Issue that might be caused by electromagnetic interference/noise

bits being flipped

# Learning objectives

- define:
    - serial
        - advantages of serial over parallel transmission
    - parallel
    - compare
        - synchronous and asynchronous

# Serial Transmission

serial : one at the time, sent in sequence

USB = Universal Serial Bus

# Parallel Transmission

Bits sent along multiple wires: at the same time, simultaneously

# How devices communicate

data is represented as a series of electrical voltages: a high voltage =1

low voltage (e.g. 0 V) = 0. 

These 1s and 0s are the binary digits (i.e. bits) that represent all of the information that a computer can store and transmit.

- In wired communication between devices, the signal would be a sequence of voltages or light pulses that travel through a cable.

- In wireless communication, the signal would consist of radio waves. In both cases, what is transmitted is a sequence (or stream) of bits.

# Serial Better than parallel

- Crosstalk :
    - where wires in proximity interfering within another, electromagnetic interference

- Skew :
    - data falling out of sync with the clock signal, data not arriving at the exact same time and not in order

- 1.8 meter :
    - parallel has a short wire range, only 1.8 meters, beyond that the more skew occurs.

Wire = a naked bit of cable, without protection

Cable = often coutains multiple wires whitin the cable, has protection

---

# Synchronous and asynchronous transmission

- Synchronous:
    - stream of bits transferred at a constant rate
    - The transmitter and the receiver are synchronised using a common clock signal.

- asynchronous:
    - there is no clock signal
    - so additional data is used to control the communication
    - start and stop bits
        - a start bit is sent at the beginning of the transmission = receiver can prepare for the incoming data
        - idle = dormant
        - The START signal should be the OPPOSITE of the STOP signal



write a function wether a number is a prime or not