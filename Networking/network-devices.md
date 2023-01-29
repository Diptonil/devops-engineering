# Network Devices

There are many hardware devices in a network architecture. Some are often misunderstood. There are four primary devices that vastly differ from one another.


## Hub

- MAC Addresses are used in this case. So, everything in layer 2 is concerned with this device.
- Hub is a device used primarily in network topologies to act as a broadcast device.
- Assuming machine with MAC address A has to send a frame to a machine with MAC address D, A sends the frame to the hub. But the hub doesn't send it directly to D. It broadcasts it to everyone in that network. D would just accept it because the frame would have a destination address attached to it. The others just drop it.
- These are almost never used these days since they broadcast, making networks inefficient.


## Switch

- It is connected in an exact same way as the hub. However, it is a little bit smarter.
- It actually parses through the content and looks at the destination, then sends the frame to the destination machine.
- There is no bulk spamming of frames across a network leading to unnecessary congestion.
- The switch also records the MAC addresses of the senders in a table. That also increases efficiency.


## Bridge

- It is a device used to connect two distinct and separate networks. It also has information about which machine is in which network.
- Its functionality is almost rendered useless if we consider switches, hence we'd talk about the two networks having a centralized hub.
- Consider we have two networks - A and B in one and C and D in another. Each network has its hub and is connected by a bridge.
- If A is to send traffic to B, the hub would broadcast but the bridge would block the traffic there itself since it knows that B is in A's network.
- Switches are more efficient since apart from knowing where a machine is, it also knows all the ports that it is connected to, which the bridge doesn't.
- Wireless bridges are quite powerful.


## Router

Routers are used when traffic is meant for external subnets. If two hosts are communicating within the same subnet, the 3 devices above are enough to handle it. When connection is to be made with another subnet, we would need a device that is capable of servicing those requests appropriately.
- For example, a host needs to send a frame to a machine. It checks with the local subnet's switch and is unable to find that host. Then, it would appeal to the gateway to dish it the responsibility of sending the fraem to the required destination.
- So, the host would have a destination as the gateway router (whose job s to take that incoming frame and send it to the correct place). There is a lot of mechanisms that occur after this step to actually route the whole thing, but that is another discussion.
- Routers are stateful and they remember what host is sending what request since the public IP gets swapped out. This is done using the NAT table.