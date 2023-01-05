# The TCP/IP Model

- This is a more concise and handier version of the OSI model, which is widely being used today. The OSI Model was a bit too overlapping and extensive in its definition. Hence, something more succinct was desired.
- It has 4/5 layers (depending on the source).


## The Four Layers

We consider four layers here.
- **Application Layer** 
    - This layer performs the functions of top three layers of the OSI model: Application, Presentation and Session Layer.
    - Some of the protocols present in this layer are: HTTP, HTTPS, FTP, TFTP, Telnet, SSH, SMTP, SNMP, NTP, DNS, DHCP, NFS, X Window, LPD.
- **Transport Layer**
    - This layer is analogous to the transport layer of the OSI model. It is responsible for end-to-end communication and error-free delivery of data.
    - TCP and UDP would be the examples.
- **Internet Layer**
    - This layer parallels the functions of OSI’s Network layer. It defines the protocols which are responsible for logical transmission of data over the entire network.
    - ARP, ICMP and IP are some examples.
- **Network Access/ Physical Layer**
    - This layer corresponds to the combination of Data Link Layer and Physical Layer of the OSI model. It looks out for hardware addressing and the protocols present in this layer allows for the physical transmission of data.
    - One important thing to note is that there is conflict as to whether we should address ARP as a part of the internet layer or physical layer.