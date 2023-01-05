# The OSI Model

- The Open Systems Interconnection (OSI) model describes seven layers that computer systems use to communicate over a network. It was the first standard model for network communications, adopted by all major computer and telecommunication companies in the early 1980s.
- It describes network communication in 7 layers.
- Layer 1 is the physical layer, layer 2 is the data link layer, ... the application layer is the 7th layer. 


## The Seven Layers

- **Application Layer**
    - Application accesses network services. This is the interface from which data that is to be sent or recieved is actually put in or recieved by the people communicating.
    - Used by the client softwares to send and recieve end to end information.
    - Tangible.
    - Examples: HTTP, DNS, SMTP, FTP, POP, etc.
- **Presentation Layer**
    - The presentation layer takes any data transmitted by the application layer and prepares it for transmission over the session layer.
    - It is associated with *encoding*, *encrypting* as well as *compressing*.
    - Examples: LPP, AFP, ICA, etc.
- **Session Layer**
    - A communication channel is established between the communicating devices, which is called as the *session*. This layer is responsible for starting, closing and maintaining a connection.
    - It can also set checkpoints during data transfer. In case connection breaks, it can rework it and start it from the checkpoint.
    - Examples: PPTP, RPC, etc.
- **Transport Layer**
    - This takes the data from the session layer and breaks it down into *segments* (and does the assembling from the segments as well).
    - It carries out *error correction* of the segments, which is checking if the data arriving is in its expected format.
    - It carries *flow control*, which is sending data at a rate that matched the connection speed of the requesting device.
    - Examples: TCP, UDP, etc.
- **Network Layer**
    - Breaks down the *segments* into *packets* (or assembles it back).
    - Routes the packets through the network by discovering the best path using various algorithms. To rote packets, we need the IPs of the devices.
    - Example: IP.
- **Data Link Layer**
    - Establishes and terminates connection between two physically connected nodes.
    - Breaks up *packets* into *frames* (or assembles it back).
    - It carries out *error checking* of the frames, which is checking if the data arriving is in its expected format. **This is done on the Logical Link Control**.
    - It uses **MAC** addresses to connect devices and define permissions for transmission.
    - Examples: PPP, LAP, SDLC, HDLC, etc.
- **Physical Layer**
    - The physical layer is responsible for the physical cable or wireless connection between network nodes. 
    - It defines the connector, the electrical cable, etc. and is responsible for transmission of the raw data, which is simply a series of 0s and 1s, while taking care of bit rate control.
    - Examples: IEEE, Bluetooth, etc.


## Cons

- This model is way too extensive and almost every layer described is overlapping.
- A better and more standard TCP/IP model was adopted later.