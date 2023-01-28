# Bandwidth

- Bandwidth is measured by how many bits a device is allowed to send or recieve in a given second. Higher it is, more is the "speed" (apparently, although many other factors are at play here). This depends on a number of different things such as the network card being used or the ISP.
- Download also means incoming traffic and upload means outgoing traffic.


## Upper Bandwidth

- This term is used by ISPs to limit their services that they provide. More the upper bandwidth to be purchased, higher the cost. 
- For example, if we have an upper bandwidth of 80 mb/s download given by our ISP, that means we can only recieve 80 megabits per second. No more than that in any circumstance.
- The same ISP may prescribe us an amount of 1 mb/s for upload. We cannot send more traffic than that.
- We may have very expensive cabling and wiring that would support a higher bandwidth but the ISP would throttle the whole traffic to serve us just that much amount. So, getting a higher bandwidth mostly depends on cost.
- Obviously, centralized servers are quite fast and expensive. They would send content easily at 6 seconds or so. But the ISPs would stop it and throttle the whole thing down. If this happens, the ISPs would get clogged. But we have a solution.
- We use TCP over the internet in most cases and this is the reason. It comes with congestion control that signals the server to stop transmitting if network is getting clogged. So, everything is safe.
- Things are different with UDP, though. The scenario described above can actually happen if we use UDP since that has no congestion control. This is why many companies (ISPs) even block UDP off completely.


## Units

- Here, 'mb' means mega bits.
- Another unit is 'mB', which means megabytes. It is frequently miscalculated or misunderstood by everyone.
- As usual, 1 byte = 8 bits.


## Usage Patterns

- **Web Browsing**: When we are normally browsing the web, visiting websites to scourge through data, we send simple GET requests that are of a few bytes. We in turn recieve some text, images, etc. It seems like a lot but it isn't just because a lot of compression is done on the recieving data. So overall, the download bandwidth is somewhat greater than the upload bandwidth. But both aren't too great. 
- **Gaming**: There is a lot of data to be exchanged between the clients and the server. These data generally are of the state of the players in the game. The result state to the input states gets calculated by the server and then sent down. So, download here is a little bit more than upload. But both are huge as compared to simple web browsing.
- **Streaming**: A simple request goes forth detailing what is to be streamed. A little bit of upload. A huge stream of stuff as download. Still the upload is larger than the web browsing equivalent just because the client has to keep the servers pinging for more content.
- **Media Production**: Some content uploads to the internet cannot really wait. Famous huge YouTube channels are some examples. They really need a lot of upload capacity.
- **Servers**: Servers are what we use to distribute and make other streams. The output traffic is huge. Download is quite small, actually, because these services don't really have a lot of stuff to get.

