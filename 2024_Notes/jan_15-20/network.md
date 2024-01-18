
# 15/01/24

# Starter activity

logical topology = protocols

physical topology = physical layout

# Types of network hosts

## peer-to-peer networking

Each computer has equal status.


## client-server networking

One or more as servers, most computers are nominated as clients

---

# Presentation

privacy and anonymity—that is, ensuring that the contents of communications are hidden from eavesdroppers, and that the identities/locations of the participants are concealed.

points of failure, if one goes down, others still working : All devices must be switched off for the network to stop working.

direct communication, every divices are connected one another, without physical location limit

cost super low

security = reduce the single point attacks and unauthorized access

everyone contributes for everyone

everyone have equal status, no one has the full control

community-based

disadvantges/advantages : more suitable for small scale applications (gaming, messaging)

dis = performance issues.

no physical attacks point, not in a single room

---

# The enemy (client server)

daniil saying wrong things, he described 

Server are more powerful

email suing client-servers

- advantages:
    - quality connections
    - powerful
    - good for large buisiness
    - good for large data

---

# client-server / P2P

Centralized and decentralized

---

# 16/01/24

# starter

- PAN
    - Personal Area Network
- LAN
    - Local Area Network
- WAN
    - Wide Area Network

# Learning Objectives

- Explain the:
    - purpose of WiFi
    - the wireless protocol Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) with and without request to Send/Clear to Send (RTS/CTS).
- Be familiar with
    - the components required for wireless networking
    - how wirless networks are secured
    - the purpose of Service Set Identifier (SSID)

---

# Wired vs Wireless

- Wired:
    - signals are electrical volatges

- Wireless:
    - signals are radio waves

The type of 'channel'

# Why WiFi ?

- WiFi:
    - international standard for communication
        - wireless local area networks
        - is a protocol for wireless
            - enable devices to connect to a network wirelessly


## Frequency band

Most WLAN devices will be dual-band

- 2.4Ghz
    - general industrual use
    - has a better range
- 5.0Ghz
    - less congested
    - less trafic
    - better performance

### Channels

- In frequencies
    - smaller bands known as "channels"

---

# Networking Devices

- Network Interface Controllers (NICs)
    - has a MAC address

- Hubs and Switches
    - hub = broacasting
    - switches = only give the packets to the destinated device

- Wireless Access Points (WAPs)
    - operating on radio waves
    - allow wireless devices to connect to a local network

- Modulator/Demodulator (Modems)
    - (combination of modulator/demodulator)
    - change the signal so that it can be sent through a cable that uses a different technology.
    - the meeting point
    - receive wireless and converts it as voltages in the cables

- Routeurs
    - Where communication happens between two separate networks, a router is required
    - same as switch
    - distribute ips to MAC addresses
    - routers reroutes data packets towards/closer to their destinations

- Network Access Devices
    - typically contain a wireless access point (WAP), a router, a modem, and a switch.
    - connect home devices to the internet
    
- Gateways
    - a device that is used to allow the transmission of data between dissimilar networks
    - convert the protocols

Switch = DHCP server ?

# Security

- WEP (Wired Equivalent Privacy)
    - same security as a wired network
    - symmetric encryption algorithm

    - WEP keys:
        - too short
        - used for too long
- WPA
    - temporary improvement to WEP
    - introduced key management
    - new ecryption key for each data packet

- WPA2 (WiFi Protected Access)
    - improvement on WPA
    - each message is encrypted several times

- SSID (Service Set Identifier) broascast disabled
    - an alphanumerical string used to identify a network

- MAC (Media Access Control) address allow list

---

# 18/01/24

# Wireless network (advanced)

# CSMA/CS protocol

- makes sure that network collisions are avoided.

## Carrier-sense

- steps:
    - listen to the channel to check for the presence of any other signals
    - decision is made whether to send the message or to try again


## Collision avoidance

- the node — an end device
    - either sending or receiving data across the network
- wait for a period of time before trying again. Typically, this is a random time within a range.

## Transmission

- Once the channel is free, the data is sent.


## Hidden node problem

# Request to Send/Clear to Send (RTS/CTS)

![diagram](https://adacomputerscience.org/images/content/computer_science/computer_networks/networking/figures/ada_cs_network_chart_wireless.svg)

- an optional method
    - alleviates the problem of hidden nodes

- Once the channel is determined to be idle, a signal is sent called Request to Send (RTS).
- The answering device then sends a Clear to Send (CTS) reply