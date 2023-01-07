## Transmission Control Protocol

This is a transport layer protocol that was designed primarily for the *reliable* exchange of information over a network between two machines. <br />
There are examples of a TCP server and a client written in Python in this directory.


## Pros

- **Ackowledgement**: Part of what makes TCP reliable is the fact that every response is acknowledged. In the world of data exchange, anything might happen to the data. To be sure of the fact that data has, in fact, reached the destination, we have a mechanism in place for acknowledging services.
- **Retransmission**: If the acknowledgement is not recieved by the sender, it would send the data again, until it reaches the acknowledgement. So there indeed is guaranteed delivery.
- **Connection Based**: For this protocol to work, there needs to be establishment of connection first. The TCP 3-Way Handshake happens here.
- **Congestion Control**: In networks, congestion happens when there are too many packets floating around and being routed everywhere. TCP connections ensure that whenever the packets can smoothly reach the destination, they are let go. They aren't let go all at once, because that would create a ruckus and lead to congestion.
- **Ordered Packets**: Sometimes during transfer of packets, due to data being transferred to so many places via a network, packets might get jumbled up. TCP will always order them by labelling.


## Cons

- **Larger Packets**: We can see so many good things about TCP like connection maintainability, ordering of packets, congestion conrol, etc. But all of these add on to the packets, along with the data that is being transferred. That is a con. The packet sise bloats up with overhead. And sometimes, it might not be needed.
- **More bandwidth**: To ship larger packets, more bandwidth is needed. So, 2G or 3G would perform insufficiently.
- **Slower than UDP**: We are establishing a connection. That obviously adds a lot of wait to the transfer (for larger packets, acknowledgements, etc.). 
- **Stateful**: Statefulness means that when the connection between client and server were to falter and then remade to continue the work that is being done, if the process *cannot* continue right where it left off without interruptions. It *will* get interrupted. This is because the state of the connection is stored and carried around by both the parties. In other words, the connection is lost if it breaks. It cannot be *reconnected*, so to speak.
- **Server Memory**: TCP is very much server-first in its approach. That means, every TCP connection being handled by the server causes some overhead to it. It uses up memory to create and maintain that TCP connection. So, there is a limit to the number of TCP connections a server can make.


## TCP 3-Way Handshake

- This is the method that happens for the establishment of a TCP connection:
    - Client asks for the server's permission to connect. It sends a segment with a SYN.
    - If server allows, it acknowledges the request with a response SYN ACK.
    - Client, after recieving the server's approval, finally ackeledges the response by sending an ACK. This marks the start of a reliable connection that gets established here.
- **SYN**: Synchronize Sequence Number is an ID that informs the server that it is likely to start communication with that ID or sequence number that is sent.
- **SYN ACK**: Synchronize Sequence Number Acknowledgement that the server sends back.
- **ACK**: Acknowledgement of the client upon server's approval.