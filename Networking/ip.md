# IP Address

- IP addresses are quite important because they are the reason why the internet even works.
- IP Addresses are basically identifiers that are used to recognize a system uniquely.
- We can use `ipconfig` in Windows and `ifconfig` in Linux to access the machine's IP. We may have different IPs for LAN1, LAN2, Wi-Fi, etc. We generally get one for anything that we are connected to.
- The router or the wifi decides the IP address for us.
- In an address, every section separated by a dot is called an *octet*.
- If we use `ipconfig` in Windows, we are greeted by 4 things:
    - Link-local IPv6 address.
    - The IPv4 address - this is what we care about.
    - The Subnet Mask or Netmask
    - The Default Gateway or Router.


## Why are IP Addesses Made Up of "192.168..."

- We see that most IPs have the first 3 sets of numbers the same, even though it could have taken anything from 0 to 255.
- It has a technically complex reason that has to do with RFC1918.
- It is due to the subnet mask. If the subnet mask has an octet as 255, we can be confident of the fact that the corresponding octets of the IP would always be the same for the connected network.
- The octet for which the subnet is 0, we can have any varying value for the IP in that case.
- The part of the IPv4 that always stays the same is the *network portion* of the IP and the other varying one is the *host* portion of the IP.


## Network Portion and Host Portion

- When a router or a wifi allocates IP addresses, we get the network portion of it the same. The host portion changes for every allocated address.
- Communication happening between machines with the same network portion can be done using the subnet.
- Communication happening between machines with different network portion can be done using the router gateway. Because they have completely different addresses.


## Why a Router Can Give Only 253 Addresses?

- So if we have the network portion as '192.169.1', that is fixed. Hence, every router, in theory, should be able to give out addresses from '192.169.1.0' to '192.169.1.255' (256). That would be practically wrong.
- The '192.169.1.0' is known as the network address and is never meant to get assigned to any device. It is the network address and it acts as the leader.
- The '192.169.1.0' is known as the broadcast address and is never meant to get assigned to any device. It is the address to which, if anything is sent, would broadcast that information to everyone.
- The router of the network that itself allots IPs itself shall have an IP address.
- So, we can allot 3 addresses less than what we had figured out originally.


## IPv4

- Initially, when internet began, we had the capability to have 4.3 billion addresses. We had not figured out that it would extinguish so soon because the use of digital machinery had increased enormously in a few years.
- The makers organized the IP Addresses in classes of A, B, C, D and E.
    - A: 1.0.0.0 - 126.255.255.255
    - B: 128.0.0.0 - 191.255.0.0
    - C: 192.0.0.0 - 223.255.255.0
    - D: 224.0.0.0 - 239.255.255.255
    - E: 240.0.0.0 - 255.255.255.255
- Each class also has its own subnet mask (like we saw before).
- The A class is used mostly by larger companies.
- The lower we go down the chart, the fewer nodes can exist for a given network but the number of networks that can be formed per class also increases.
- There is a whole class of addresses that are missing '127...'.These are known as loop-back addresses. They can be used to check our networks and they exist on our devices.