# User Datagram Protocol

This is a transport layer protocol that was designed primarily for the *unreliable* exchange of information over a network between two machines. <br />
There are examples of a UDP server and a client written in Python in this directory.


## Pros

- **Smaller Packets**: Due to all the less information that UDP packets are associated with, packet size is small.
- **Less Bandwidth**: Lesser bandwisth is needed to ship them all.
- **Faster than TCP**: Less overhead in everything makes it much faster than TCP.
- **Stateless**: Due to there being no need for active connection maintenance, the server can just start back up after it being offline and the transaction between the devices would still continue.


## Cons

- **No Acknowledgement**: No hassle of acknowledgement by the client. This makes things a little bit faster and more expensive.
- **No Guaranteed Delivery**: The data either reaches or it doesn't. No guarantee at all. No retransmission. The only important thing that UDP adds on top of the packet is the checksum. Packet missing its destination is a very common thing here.
- **Connectionless**: There is no maintained connection that remains established.
- **No Congestion Control**: UDP doesn't wait or care, it just sends data. That's it. No controlling or ordering of packets.
- **Security**: If the port is open, anyone can jump in and transmit data. That is really bad. A lot of firewalls just disable UDP for this reason.


## Reliable UDP

Some applications over networks use a slightly altered version of the UDP in which the protocol is made a bit more reliable so that at least loss of data is not that frequent. This form sees many applications when the best of both UDP and reliable protocols are to be seen. <br />
Video games and video call applications use that all the time.