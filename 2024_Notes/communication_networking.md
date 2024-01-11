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

# Serial and Paralell ARE INTERFACES

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
    - streaming data

- asynchronous:
    - there is no clock signal
    - so additional data is used to control the communication
    - start and stop bits
        - a start bit is sent at the beginning of the transmission = receiver can prepare for the incoming data
        - idle = dormant
        - The START signal should be the OPPOSITE of the STOP signal



write a function wether a number is a prime or not

# 11/01/24

# Starter activity

Q1. serial is stable and data will always be transferred in the right order, it cannot be used for simultaneous data transfers, however serial is much slower than paralell.

Q2. a common clock signal

---

# Bit rate

The bits transmitted per second (bps)

if 2 Kb (KiloBYTES) is tranferred in 5 second, then the bit rate is 3.2Kbps (kiloBITS)

    2Kb/5 = 3.2 Kbps

# Baud Rate

Baud rate = the quantify of ***signal changes per second***

each signal = MAY consits of one-or-more bits

- amount of time the signal changes

- changes of the signal per second

## Bit Rate vs. Baud Rate

Bit rate = MAY be higher than the baud rate if signal change CONSISTS of more than one bit

    bit rate = baud rate * bits per signal

# Baseband

Baseband = signals = one of two levels (high or low voltage), each representing a binary value

# Broadband

Supports more than two different signal levels (there are multiple frequency bands or voltage levels), so every signal change can represent more than one bit. In this case, a symbol can encode 2, 4, or 8 (etc.) bits.

# Bandwidth

- the maximum rate/range of frequencies
    - that can be transmitted across a network connection
    - bit rate may be less due to electromagnetic interference

- Maximum "lanes"/"states" the network support

## Bit rate and Bandwidth

- bit rate is directly proportionate to bandwidth
- the greater the bandwidth, the greater the bit rate

# Latency

- delay
    - between the time a signal is sent and received
    - may cause various issues for real-time communication

    - exemple of issue = videogames

# Protocol

- A set of rules between devices within or via a network
    - such as :
        - data format (packet data)
        - wired or wireless
        - serial or parallel
        - synchronous or asynchronous
        - bit rate and/or baud rate
        - error checking (e.g parity bits or majority voting)